from pathlib import Path

import jinja2
from aiohttp import web
from aiohttp import ClientSession

import aiohttp_jinja2

from .views import index
from .views import json_example


THIS_DIR = Path(__file__).parent
BASE_DIR = THIS_DIR.parent


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/json', json_example)


async def create_app():
    app = web.Application()
    session = ClientSession()
    app.update(
        name='mars alert',
        http_client=session
    )

    jinja2_loader = jinja2.FileSystemLoader(str(THIS_DIR / 'templates'))
    aiohttp_jinja2.setup(app, loader=jinja2_loader)

    setup_routes(app)
    return app
