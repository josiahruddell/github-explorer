from . import RequestResource
from flask.ext.restful import fields, marshal_with

class Owner(fields.Raw):
    def format(self, value):
        return value['login'] if 'login' in value else None

repo_fields = {
    'owner_login': Owner(attribute='owner'),
    'full_name': fields.String,
    'name': fields.String,
    'description': fields.String,
    'html_url': fields.String,
    'language': fields.String,
    'watchers_count': fields.Integer,
    'forks_count': fields.Integer,
    'open_issues_count': fields.Integer
}

class RepoResourceList(RequestResource):
    _url = '/orgs/{org}/repos'

    # marshal to reduce client overhead
    @marshal_with(repo_fields)
    def get(self, org):
        res = self.request(route_keys={'org': org })
        return res.json()