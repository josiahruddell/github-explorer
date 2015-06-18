from flask.ext.restful import Resource
from src.util import FormatUtil
from requests import request
from src.config import current as config


class RequestResource(Resource):
    """ Inherit flask-restful resource with additional functionality
        for wrapping proxy requests to another API """

    _url = None

    @property
    def url(self):
        return config.GITHUB_API_URL + self._url


    def request(self, method='get', **kwargs):
        url = self.url

        # enable formatting the url on the resource sub-class
        # with route_keys kwarg
        if 'route_keys' in kwargs and '{' in url:
            url = FormatUtil.try_format_str(url, **kwargs.get('route_keys'))
            del kwargs['route_keys']

        print ' ** making request: ', url, method, kwargs
        return request(method, url, **kwargs)