import os
from unittest import TestCase, mock
from test.resources.testutils import utils


class TestCommonBatchProcessing(TestCase):
    @classmethod
    def setUpClass(self):
        self.env_patcher = mock.patch.dict(os.environ, {
            "defaultWebServer": "http://dummy.dws.com",
            })
        self.env_patcher.start()
        utils.reload_modules()
        super().setUpClass()

    @classmethod
    def tearDownClass(self):
        super().tearDownClass()
        self.env_patcher.stop()

    def setUp(self) -> None:
        return super().setUp()

    def test_batch_action_perform(self):
        from aladdinsdk.common.batch.action import SDKAction, SDKActionStatus
        action = SDKAction(lambda x: x, 1)
        self.assertEqual(action.run_status, SDKActionStatus.ENQUEUED)
        self.assertEqual(action.perform(), 1)
        self.assertEqual(action.run_status, SDKActionStatus.COMPLETE)

    def test_batch_action_perform_error(self):
        from aladdinsdk.common.batch.action import SDKAction, SDKActionStatus

        def failed_action(x):
            raise ValueError(f"Test error {x}")

        action = SDKAction(failed_action, 1)
        self.assertEqual(action.run_status, SDKActionStatus.ENQUEUED)
        action.perform()
        self.assertEqual(action.run_status, SDKActionStatus.FAILED)

    def test_batch_action_error_on_init(self):
        from aladdinsdk.common.batch.action import SDKAction
        with self.assertRaises(ValueError) as context:
            SDKAction('not a function', 1)
            context.assertEqual(str(context.exception), "method: 'not a function' must be a callable function")

    def test_batch_remove_actions(self):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer()
        self.assertEqual(buffer.actions, [])
        buffer.append_action(SDKAction(lambda x: x, 1))
        self.assertEqual(len(buffer.get_action_map()), 1)
        buffer.append_action(SDKAction(lambda x: x, 2))
        self.assertEqual(len(buffer.get_action_map()), 2)
        buffer.append_action(SDKAction(lambda x: x, 3))
        self.assertEqual(len(buffer.get_action_map()), 3)
        buffer.remove_action(buffer.actions[2])
        self.assertEqual(len(buffer.get_action_map()), 2)
        buffer.append_action(SDKAction(lambda x: x, 3))

    def test_batch_action_buffer_sequential(self):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer()
        self.assertEqual(buffer.actions, [])
        buffer.append_action(SDKAction(lambda x: x, 1))
        self.assertEqual(len(buffer.actions), 1)
        buffer.append_action(SDKAction(lambda x: x, 2))
        self.assertEqual(len(buffer.actions), 2)
        buffer.append_action(SDKAction(lambda x: x, 3))
        self.assertEqual(len(buffer.actions), 3)

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [None, None, None])

        buffer.run_sequential()

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [1, 2, 3])

        buffer.clear_actions()
        self.assertEqual(buffer.actions, [])

    @mock.patch('logging.Logger.debug')
    def test_batch_action_buffer_sequential_intervals(self, mock_logger_debug):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer()
        buffer.append_action(SDKAction(lambda x: x, 1))
        buffer.append_action(SDKAction(lambda x: x, 2))
        buffer.append_action(SDKAction(lambda x: x, 3))

        buffer.run_sequential(interval=0.1)

        mock_logger_debug.assert_any_call(f"Action {buffer.actions[0].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[0].uid} success")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} to begin in 0.1 seconds per configured interval.")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} success")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} to begin in 0.1 seconds per configured interval.")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} success")

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [1, 2, 3])

        buffer.clear_actions()
        self.assertEqual(buffer.actions, [])

    @mock.patch('logging.Logger.debug')
    def test_batch_action_buffer_sequential_one_failed_action(self, mock_logger_debug):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer()

        def failed_action(x):
            raise ValueError(f"Test error {x}")

        buffer.append_action(SDKAction(lambda x: x, 1))
        buffer.append_action(SDKAction(failed_action, 2))
        buffer.append_action(SDKAction(lambda x: x, 3))

        buffer.run_sequential(interval=0.1)

        mock_logger_debug.assert_any_call(f"Action {buffer.actions[0].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[0].uid} success")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} to begin in 0.1 seconds per configured interval.")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} failed")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} to begin in 0.1 seconds per configured interval.")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} success")

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [1, response_values[1], 3])

        buffer.clear_actions()
        self.assertEqual(buffer.actions, [])

    def test_batch_action_buffer_parallel(self):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer()
        buffer.append_action(SDKAction(lambda x: x, 1))
        buffer.append_action(SDKAction(lambda x: x, 2))
        buffer.append_action(SDKAction(lambda x: x, 3))

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [None, None, None])

        buffer.run_parallel()

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [1, 2, 3])

        buffer.clear_actions()
        self.assertEqual(buffer.actions, [])

    @mock.patch('logging.Logger.debug')
    def test_batch_action_buffer_parallel_one_failed_action(self, mock_logger_debug):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer()

        def failed_action(x):
            raise ValueError(f"Test error {x}")

        buffer.append_action(SDKAction(lambda x: x, 1))
        buffer.append_action(SDKAction(failed_action, 2))
        buffer.append_action(SDKAction(lambda x: x, 3))

        buffer.run_parallel()

        mock_logger_debug.assert_any_call(f"Action {buffer.actions[0].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[0].uid} success")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[1].uid} failed")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} started")
        mock_logger_debug.assert_any_call(f"Action {buffer.actions[2].uid} success")

        response_values = list(buffer.get_response_map().values())
        self.assertEqual(response_values, [1, response_values[1], 3])

        buffer.clear_actions()
        self.assertEqual(buffer.actions, [])

    def test_batch_action_buffer_init_error_on_full(self):
        from aladdinsdk.common.batch.action import SDKActionBuffer, SDKAction
        buffer = SDKActionBuffer(max_size=2)
        buffer.append_action(SDKAction(lambda x: x, 1))
        buffer.append_action(SDKAction(lambda x: x, 2))
        with self.assertRaises(ValueError) as context:
            buffer.append_action(SDKAction(lambda x: x, 3))
            context.assertEqual(str(context.exception), "SDKActionBuffer is full. Max size is configured to 2")
