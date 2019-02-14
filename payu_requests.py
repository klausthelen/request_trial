import requests
import json
import aiohttp
import asyncio
from req_data import (ping_data, payment_metods_data, submit_transaction_data)

payu_host = "sandbox.api.payulatam.com"

payments_api_url = "https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi"
reports_api_url = "https://sandbox.api.payulatam.com/reports-api/4.0/service.cgi"

PAYU_HEADERS = {
    "Host": payu_host,
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json"
}
async def as_get_requests(url, headers, params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERSA) as resp:
            print("--------------- Begin -----------")
            print(resp.status)
            respuesta = await resp.json(content_type=None)
            print(resp)
            print (json.dumps(respuesta, indent=4))
            print("--------------- End -----------")

async def as_post_requests(url, data, headers):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(data)) as resp:
            print("--------------- Begin -----------")
            print(resp.status)
            respuesta = await resp.json(content_type=None)
            print(resp)
            print (json.dumps(respuesta, indent=4))
            print("--------------- End -----------")

async def trans():
    submit_trans_req = loop.create_task(as_post_requests(payments_api_url, submit_transaction_data, PAYU_HEADERS))
    payment_metods = loop.create_task(as_post_requests(payments_api_url, payment_metods_data, PAYU_HEADERS))
    await asyncio.wait([submit_trans_req, payment_metods])


def post_request(url, data, headers):
    print("--------- REQUESTS TO " + str(url) + " ---------")
    post_req = requests.post(url,data=json.dumps(data), headers=headers).json()
    print(json.dumps(post_req, indent=4))
    print("------------------------------------ ")


# post_request(reports_api_url, ping_data, PAYU_HEADERS)
# post_request(payments_api_url, payment_metods_data, PAYU_HEADERS)
# post_request(payments_api_url, submit_transaction_data, PAYU_HEADERS)

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(trans())
except Exception as e:
    pass
    print("Error")
    print(e)
finally:
    print("Se va a cerrar")
    loop.close()