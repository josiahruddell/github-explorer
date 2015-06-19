import unittest
import server
import json


class CommitApiResultTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_commit_route_returns_json(self):
        res = self.app.get('/api/commits/netflix/astyanax')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers['Content-Type'], 'application/json')


    def test_commits_route_is_sorted_by_author_date_descending(self):
        res = self.app.get('/api/commits/netflix/astyanax')
        commits = json.loads(res.get_data())
        self.assertGreaterEqual(len(commits), 2)

        first_commit = commits[0]
        second_commit = commits[1]

        self.assertTrue('author' in first_commit)
        self.assertTrue('author' in second_commit)
        self.assertTrue('date' in first_commit['author'])
        self.assertTrue('date' in second_commit['author'])

        self.assertGreaterEqual(first_commit['author']['date'], second_commit['author']['date'])