from aiohttp_jinja2 import template
from aiohttp import web

@template('index.jinja')
async def index(request):
    return {
        'title': request.app['name'],
        'message': "Success!",
    }

async def json_example(request):
    async with request.app['http_client'].get('https://mars-storm.herokuapp.com/data') as response:
        something = await response.json()
    return web.json_response({'rawData': something})
