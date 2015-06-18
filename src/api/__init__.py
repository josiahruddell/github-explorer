from collections import namedtuple

from src.api.resources.commit import CommitResourceList
from src.api.resources.repository import RepoResourceList


# simple endpoint-to-class mapping structure
Route = namedtuple('Route', ['endpoint', 'cls'])

# define application routes
route_map = [
    Route(cls=CommitResourceList, endpoint='/commits/<string:owner>/<string:repo>'),
    Route(cls=RepoResourceList, endpoint='/repositories/<string:org>')
]

# activate routes
def init(api_app):
    for r in route_map:
        api_app.add_resource(r.cls, '/api' + r.endpoint)