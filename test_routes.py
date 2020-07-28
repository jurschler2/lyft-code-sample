from unittest import TestCase

from app import app

# The different request test cases:
good_request_long = {'string_to_cut': 'abcdefg'}
good_request_short = {'string_to_cut': 'ab'}
bad_request_key = {'bad_key': 'abcdefg'}
bad_request_not_string = {'string_to_cut': 100}

# The different responses to the request test cases:
good_response_long = {'return_string': 'cf'}
good_response_short = {'return_string': ''}
bad_response_key = {'error': 'Please use the key: string_to_cut.'}
bad_response_not_string = {'error': 'Please submit a string as the value.'}


class RouteViewTestCase(TestCase):
    """ """

    def setUp(self):
        """ """

        self.client = app.test_client()


    def test_good_request_long(self):
        """
        Test case for a good string long enough to be cut:
        req: {'string_to_cut': 'abcdefg'}
        res: {'return_string': 'cf'}
        """

        with self.client as c:
            resp = c.post("/test", json=good_request_long)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json, good_response_long)


    def test_good_request_short(self):
        """
        Test case for a good string too short to be cut:
        req: {'string_to_cut': 'ab'}
        res: {'return_string': ''}
        """

        with self.client as c:
            resp = c.post("/test", json=good_request_short)

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json, good_response_short)


    def test_bad_request_key(self):
        """
        Test case for with the wrong key sent:
        req: {'bad_key': 'abcdefg'}
        res: {'error': 'Please use the key: string_to_cut.'}
        """

        with self.client as c:
            resp = c.post("/test", json=bad_request_key)

            self.assertEqual(resp.status_code, 400)
            self.assertEqual(resp.json, bad_response_key)


    def test_bad_request_not_string(self):
        """
        Test case for a non-string sent as the value:
        req: {'string_to_cut': 100}
        res: {'error': 'Please submit a string as the value.'}
        """

        with self.client as c:
            resp = c.post("/test", json=bad_request_not_string)

            self.assertEqual(resp.status_code, 400)
            self.assertEqual(resp.json, bad_response_not_string)