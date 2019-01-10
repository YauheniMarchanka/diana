from aiohttp import web
import aiohttp_jinja2
import jinja2
import logging
import pathlib
from datetime import datetime


TEMPLATES_ROOT = pathlib.Path(__file__).parent / 'templates'
STATIC_ROOT = pathlib.Path(__file__).parent / 'static'


def setup_jinja(app):
    loader = jinja2.FileSystemLoader(str(TEMPLATES_ROOT))
    jinja_env = aiohttp_jinja2.setup(app, loader=loader)
    return jinja_env


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=STATIC_ROOT,
                          name='static')


async def server_time(request):
    return web.json_response(data={'data': datetime.now().isoformat(' ')})

async def hello(request):
    return web.Response(content_type="text/html", text="<h1>Hello, world</h1>")


@aiohttp_jinja2.template('index.html')
async def hello_w_name(request):
    name = 'name' in request.match_info and request.match_info['name'] or "неизвестный"
    return {'name': name}

logging.basicConfig(level=logging.DEBUG)
app = web.Application()
setup_jinja(app)
setup_static_routes(app)

app.add_routes([web.get('/', hello_w_name)])
app.add_routes([web.post('/server_time', server_time)])
app.add_routes([web.get('/{name}', hello_w_name)])

web.run_app(app)
