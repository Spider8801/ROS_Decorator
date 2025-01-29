import unittest
from ros2_action_decorator.decorator import ros2_action_decorator

class TestROS2ActionDecorator(unittest.TestCase):
    def test_message_generation(self):
        @ros2_action_decorator
        def test_func(a: int, b: float) -> str:
            return "test"

        self.assertTrue(os.path.exists("ros2_action_decorator_msgs/msg/test_funcInput.msg"))
        self.assertTrue(os.path.exists("ros2_action_decorator_msgs/msg/test_funcOutput.msg"))
        self.assertTrue(os.path.exists("ros2_action_decorator_msgs/action/test_func.action"))

if __name__ == '__main__':
    unittest.main()
