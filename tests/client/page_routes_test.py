import unittest
import server


class PageRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_index_route_exists(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], 'text/html; charset=utf-8')