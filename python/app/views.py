from aiohttp_jinja2 import template
from aiohttp import web

@template('index.jinja')
async def index(request):
    return {
        'title': request.app['name'],
        'message': "Success!",
    }

@template('alerting.jinja')
async def alerting(request):
    # Stationsdaten als Objekt holen
    async with request.app['http_client'].get('https://mars-storm.herokuapp.com/data') as response:
        stationsData = await response.json()

    for station in stationsData:
        if station["windVelocity"] > 50:
            station["isStormy"] = True
        else:
            station["isStormy"] = False
    # Stationsdaten in eine HTML Tabelle schreiben
    # Rot einfärben, falls station starken Wind anzeigt
    return { "stations": stationsData, "showResults": False }

async def json_example(request):
    async with request.app['http_client'].get('https://mars-storm.herokuapp.com/data') as response:
        something = await response.json()
    return web.json_response({'rawData': something})
