import requests
from sgqlc.operation import Operation
import logging

try:
    import aiohttp
    _can_async = True
except:
    _can_async = False


from .model import model, Query

__version__ = '0.1.0'

logger = logging.getLogger()

api = 'https://api.graphql.imdb.com/'
_cookies = {"session-id": "145-9061510-1804852"}

def Query() -> Query:
    return Operation(model.Query)

def fetch(op: Operation):
    r = requests.post(api, cookies=_cookies, json={'query':str(op)}).json()
    if r.get('errors', {}):
        logger.warning(r['errors'].get('message', ''))
    return op + r

async def async_fetch(op: Operation):
    if not _can_async:
        raise ImportError("Couldn't import 'aiohttp' module")
    async with aiohttp.ClientSession() as session:
        async with session.post(api, json=str(op), cookies=_cookies) as response:
            ans = await response.json()
            if ans.get('errors', {}):
                logger.warning(ans['errors'].get('message', ''))
            return op + ans
