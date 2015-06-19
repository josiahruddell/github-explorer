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
    'pushed_at': fields.String
}

class RepoResourceList(RequestResource):
    _url = '/orgs/{org}/repos'

    # marshal to reduce client overhead
    @marshal_with(repo_fields)
    def get(self, org):

        data = self.request(route_keys={'org': org }).json()

        if data and 'pushed_at' in data:
            data = sorted(data, key=lambda x: x['pushed_at'], reverse=True)

        return data