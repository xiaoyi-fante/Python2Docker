import unittest
from ager import Python2docker
import warnings


class CheckPython2Docker(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CheckPython2Docker, self).__init__(*args, **kwargs)
        self.test_docker = Python2docker()

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)

    def test_exec_docker(self):
        print('test_exec_docker')
        self.assertEqual("Hi DevOps, age 1\n",
                         self.test_docker.get_logs("DevOps", 5))


if __name__ == "__main__":
    unittest.main()
