import app
import unittest

class TestHelloWrold(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        req = self.app.get('/')

        assert req.status_code == 200
        assert req.get_data(as_text=True) == 'Hello, world!'


if __name__ == '__main__':
    unittest.main()

