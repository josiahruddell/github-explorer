import unittest
import server
import json


class RepositoryApiResultTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_repos_route_returns_json(self):
        res = self.app.get('/api/repositories/netflix')
        # success
        self.assertEqual(res.status_code, 200)
        # json
        self.assertEqual(res.headers['Content-Type'], 'application/json')

    def test_not_found_github_repo_returns_json(self):
        res = self.app.get('/api/repositories/foobarfoobarfoobarfoobar-dne')
        # success
        self.assertEqual(res.status_code, 200)
        # json
        self.assertEqual(res.headers['Content-Type'], 'application/json')

    def test_repos_route_is_sorted_by_pushed_at_descending(self):
        res = self.app.get('/api/repositories/netflix')
        # success
        repos = json.loads(res.get_data())
        self.assertGreaterEqual(len(repos), 2)

        first_repo = repos[0]
        second_repo = repos[1]

        self.assertTrue('pushed_at' in first_repo)
        self.assertTrue('pushed_at' in second_repo)

        self.assertGreaterEqual(first_repo['pushed_at'], second_repo['pushed_at'])
