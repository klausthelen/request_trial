import requests
import json
from req_data import (ping_data, payment_metods_data, submit_transaction_data)

payu_host = "sandbox.api.payulatam.com"

payments_api_url = "https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi"
reports_api_url = "https://sandbox.api.payulatam.com/reports-api/4.0/service.cgi"

PAYU_HEADERS = {
    "Host": payu_host,
    "Content-Type": "application/json; charset=utf-8",
    "Accept": "application/json"
}



def post_request(url, data, headers):
    print("--------- REQUESTS TO " + str(url) + " ---------")
    post_req = requests.post(url,data=json.dumps(data), headers=headers).json()
    print(json.dumps(post_req, indent=4))
    print("------------------------------------ ")


post_request(reports_api_url, ping_data, PAYU_HEADERS)
# post_request(payments_api_url, payment_metods_data, PAYU_HEADERS)
post_request(payments_api_url, submit_transaction_data, PAYU_HEADERS)