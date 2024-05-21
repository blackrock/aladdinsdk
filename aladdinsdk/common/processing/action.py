import threading


class SDKAction:
    def __init__(self, method, *args, **kwargs):
        self.method = method
        self.args = args
        self.kwargs = kwargs
        self.result = None
        self.error = None
        self.lock = threading.Lock()
        self._thread = None

    def perform(self):
        try:
            self.lock.acquire()
            self.result = self.method(*self.args, **self.kwargs)
            self.lock.release()
            return self.result
        except Exception as e:
            self.error = e
            return e


class SDKActionBuffer:
    def __init__(self):
        self.actions = []
        self.result_list = []
        self.lock = threading.Lock()

    def append_action(self, action):
        self.actions.append(action)

    def remove_action(self, action):
        self.actions.remove(action)

    def clear_result_list(self):
        self.lock.acquire()
        self.result_list.clear()
        self.lock.release()

    def clear_actions(self):
        self.lock.acquire()
        self.actions.clear()
        self.lock.release()

    def run_sequential(self, clear_buffer=True):
        for action in self.actions:
            self.result_list.append(action.perform())
        if clear_buffer:
            self.clear_actions()

    def run_parallel(self, clear_buffer=True):
        threads = []
        for action in self.actions:
            thread = threading.Thread(target=action.perform)
            action._thread = thread
            threads.append(thread)
            thread.start()
        for action in self.actions:
            action._thread.join()
            self.result_list.append(action.result)
        if clear_buffer:
            self.clear_actions()
