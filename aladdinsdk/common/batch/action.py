import time
import uuid
import threading
from enum import Enum
import logging
import concurrent.futures
from aladdinsdk.config import user_settings

logger = logging.getLogger(__name__)


class SDKActionStatus(Enum):
    ENQUEUED = 'ENQUEUED'
    RUNNING = 'RUNNING'
    COMPLETE = 'COMPLETE'
    FAILED = 'FAILED'


class SDKAction:
    """
    A class to represent a generic action to be executed in a batch.
    """
    def __init__(self, method, *args, **kwargs):
        if not callable(method):
            raise ValueError(f"method: '{method}' must be a callable function")
        # store run parameters
        self.method = method
        self.args = args
        self.kwargs = kwargs
        # setup action for execution
        self.run_status = SDKActionStatus.ENQUEUED
        self.result = None
        self.error = None
        # setup action for tracking
        self.uid = f'{method.__name__}-{uuid.uuid4().hex}'
        self.lock = threading.Lock()
        self.thread = None

    def perform(self):
        """
        Perform the action and return the result or error.

        Returns:
            _type_: The result of the action or an error if the action failed.
        """
        logger.debug(f"Action {self.uid} started")
        try:
            self.run_status = SDKActionStatus.RUNNING
            self.lock.acquire()
            self.result = self.method(*self.args, **self.kwargs)
            self.lock.release()
            self.run_status = SDKActionStatus.COMPLETE
            logger.debug(f"Action {self.uid} success")
            return self.result
        except Exception as e:
            self.error = e
            self.run_status = SDKActionStatus.FAILED
            logger.debug(f"Action {self.uid} failed")
            return e


class SDKActionBuffer:
    """
    A class to represent a buffer of SDKAction objects to be executed in a batch.
    """
    def __init__(self, max_size=None):
        self.max_size = max_size if max_size is not None else user_settings.get_batch_buffer_max_size()
        self.actions = []

    def append_action(self, action):
        """
        Append an action to the buffer.

        Args:
            action (_type_): An SDKAction to append to the buffer.

        Raises:
            ValueError: If the buffer is full. Max size is configured during initialization or via config file.
        """
        if self.max_size is not None and len(self.actions) >= self.max_size:
            raise ValueError(f"SDKActionBuffer is full. Max size is configured to {self.max_size}")
        self.actions.append(action)

    def remove_action(self, action):
        """
        Remove an action from the buffer.

        Args:
            action (_type_): An SDKAction to remove from the buffer.
        """
        self.actions.remove(action)

    def clear_actions(self):
        """
        Clear all actions from the buffer.
        """
        self.actions.clear()

    def get_action_map(self):
        """
        Get a map of actions keyed by action uid.

        Returns:
            _type_: A map of actions keyed by action uid.
        """
        action_map = {}
        for action in self.actions:
            action_map[action.uid] = action
        return action_map

    def get_response_map(self):
        """
        Get a map of results or errors keyed by action uid.

        Returns:
            _type_: A map of results or errors keyed by action uid.
        """
        response_map = {}
        for action in self.actions:
            if action.run_status == SDKActionStatus.COMPLETE:
                response_map[action.uid] = action.result
            elif action.run_status == SDKActionStatus.FAILED:
                response_map[action.uid] = action.error
            else:
                response_map[action.uid] = None
        return response_map

    def run_sequential(self, interval=None):
        """
        Run all actions in the buffer sequentially. If an interval is provided, wait that many seconds between each action.

        Args:
            interval (_type_, optional): Interval in seconds to wait between each action. Defaults to None i.e. no interval between actions.
        """
        if interval is None:
            interval = user_settings.get_batch_sequential_interval()
        counter = 0
        for action in self.actions:
            if interval is not None and counter > 0:
                logger.debug(f"Action {action.uid} to begin in {interval} seconds per configured interval.")
                time.sleep(interval)
            action.perform()
            counter += 1

    def run_parallel(self, max_workers=None):
        """
        Run all actions in the buffer in parallel using a ThreadPoolExecutor.
        Max workers can be configured during initialization or via config file.

        Args:
            max_workers (_type_, optional): Maximum number of workers to use in the ThreadPoolExecutor. Defaults to ThreadPoolExecutor worker count.
        """
        max_workers = max_workers if max_workers is not None else user_settings.get_batch_parallel_max_workers()
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            action_future_map = {}
            for action in self.actions:
                action_future_map[action] = executor.submit(action.perform)

            for action in action_future_map:
                future = action_future_map[action]
                future.result()
