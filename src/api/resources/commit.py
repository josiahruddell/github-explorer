from . import RequestResource
from flask.ext.restful import fields, marshal_with

class NestedField(fields.Raw):
    sub_field_name = None

    def __init__(self, sub_field_name, **kwargs):
        self.sub_field_name = sub_field_name
        super(NestedField, self).__init__(**kwargs)

    def format(self, value):
        k = self.sub_field_name
        return value[k] if k in value else None

commit_fields = {
    'author': NestedField('author', attribute='commit'),
    'message': NestedField('message', attribute='commit'),
    'html_url': fields.String,
    'sha': fields.String
}

class CommitResourceList(RequestResource):
    _url = '/repos/{owner}/{repo}/commits'

    @marshal_with(commit_fields)
    def get(self, owner, repo):

        data = self.request(route_keys={'owner': owner, 'repo': repo}).json()

        return data