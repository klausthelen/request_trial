import aiohttp
import asyncio
import json

httpbinurl = "http://httpbin.org"
payloadget = {'key1': 'value1', 'key2': 'value2'}
httpbinuser = "hola"
httpbinpass = "mundo"

HEADERSA = {
    "accept": "application/json"
}

async def as_requests(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERSA) as resp:
            print("--------------- Begin -----------")
            print(resp.status)
            respuesta = await resp.json(content_type=None)
            print(resp)
            print (json.dumps(respuesta, indent=4))
            print("--------------- End -----------")

async def main():
    responseb = loop.create_task(as_requests(httpbinurl + "/basic-auth/" + str(httpbinuser) + "/" + str(httpbinpass)))
    responsec = loop.create_task(as_requests(httpbinurl + "/uuid"))
    responsed = loop.create_task(as_requests(httpbinurl + "/delay/5"))
    responsea = loop.create_task(as_requests(httpbinurl + "/get"))
    await asyncio.wait([responsea,responseb,responsec,responsed])

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except Exception as e:
    pass
    print("Error")
    print(e)
finally:
    print("Se va a cerrar")
    loop.close()