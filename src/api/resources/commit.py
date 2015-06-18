from . import RequestResource
from flask.ext.restful import fields, marshal_with

class SubField(fields.Raw):
    sub_field_name = None

    def __init__(self, sub_field_name, **kwargs):
        self.sub_field_name = sub_field_name
        super(SubField, self).__init__(**kwargs)

    def format(self, value):
        k = self.sub_field_name
        return value[k] if k in value else None


commit_fields = {
    'author': SubField('author', attribute='commit'),
    'message': SubField('message', attribute='commit'),
    'html_url': fields.String,
    'sha': fields.String
}

class CommitResourceList(RequestResource):
    _url = '/repos/{owner}/{repo}/commits'

    @marshal_with(commit_fields)
    def get(self, owner, repo):
        res = self.request(route_keys={'owner': owner, 'repo': repo})
        return res.json()