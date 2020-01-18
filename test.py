import app
import unittest
import json

class TestHelloWrold(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        req = self.app.get('/')

        assert req.status_code == 200
        assert req.get_data(as_text=True) == 'Hello, world!'

class TestSubmission(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_contact_submission(self):

        payload = {
                "first_name": "Test",
                "last_name": "Person",
                "email": "me@example.com",
                "message": "Test message"
                }

        req = self.app.post(
                'submissions',
                data=json.dumps(payload),
                content_type="application/json")

        assert req.status_code == 201

        resp = json.loads(req.get_data())

        for item in [ 'id', 'first_name', 'last_name', 'email', 'message']:
            assert item in resp['submission']

    def test_missing_params(self):
        payload = {
                "first_name": "Test",
                "last_name": "Person",
                "email": "person@example.com"
                }

        req = self.app.post(
                '/submissions',
                data=json.dumps(payload),
                content_type="application/json"
                )

        assert req.status_code == 400

        resp = json.loads(req.get_data())

        assert 'status' in resp
        assert 'message' in resp

        assert resp['message'] == 'Missing required message parameter'

if __name__ == '__main__':
    unittest.main()

