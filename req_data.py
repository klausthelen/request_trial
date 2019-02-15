import hashlib
import requests
import string
import time
import random
import json
from http import cookies

ts = time.time()

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

headers = requests.utils.default_headers()

cookie = cookies.SimpleCookie()
storedcookie = id_generator()
cookie["storedcookie"] = hashlib.md5(storedcookie.encode('utf-8')).hexdigest()
deviceSessionId = str(cookie.output()) + str(ts)
deviceSessionId = hashlib.md5(deviceSessionId.encode('utf-8')).hexdigest()

ip = requests.get('https://api.ipify.org').text

apiLogin = "pRRXKOl8ikMmt9u"
apiKey = "4Vj8eK4rloUd272L48hsrarnUA"

merchantid =  508029
referenceCode= "TestPayUs"
tx_value = 20000
currency  = "COP"

signature = str(apiKey)+"~"+str(merchantid)+"~"+str(referenceCode)+"~"+str(tx_value)+"~"+str(currency)
signature_md5 = hashlib.md5(signature.encode('utf-8')).hexdigest()



def get_ping_data():
   ping_data = {
      "test": False,
      "language": "en",
      "command": "PING",
      "merchant": {
         "apiLogin": apiLogin,
         "apiKey": apiKey
      }
   }
   return ping_data

def get_payment_metods_data():
   payment_metods_data = {
      "test": False,
      "language": "en",
      "command": "GET_PAYMENT_METHODS",
      "merchant": {
         "apiLogin": apiLogin,
         "apiKey": apiKey
      }
   }
   return payment_metods_data


def get_submit_transaction_data(paymentMethod):
   submit_transaction_data = {}
   if paymentMethod is "CARD":
      submit_transaction_data = {
         "language": "en",
         "command": "SUBMIT_TRANSACTION",
         "merchant": {
            "apiKey": apiKey,
            "apiLogin": apiLogin
         },
         "transaction": {
            "order": {
               "accountId": "512321",
               "referenceCode": str(referenceCode),
               "description": "payment test",
               "language": "en",
               "signature": str(signature_md5),
               "additionalValues": {
                  "TX_VALUE": {
                     "value": int(tx_value),
                     "currency": "COP"
               },
                  "TX_TAX": {
                     "value": int(tx_value * 0.19),
                     "currency": "COP"
               },
                  "TX_TAX_RETURN_BASE": {
                     "value": int(tx_value * 0.81),
                     "currency": "COP"
               }
               },
               "buyer": {
                  "fullName": "First name and second buyer  name",
                  "emailAddress": "buyer_test@test.com",
                  "contactPhone": "7563126",
                  "dniNumber": "5415668464654",
                  "shippingAddress": {
                     "street1": "calle 100",
                     "street2": "5555487",
                     "city": "Bogota",
                     "state": "Cundinamarca",
                     "country": "CO",
                     "postalCode": "000000",
                     "phone": "7563126"
                  }
               }
            },
            "payer": {
               "fullName": "First name and second payer name",
               "emailAddress": "payer_test@test.com",
               "contactPhone": "7563126",
               "dniNumber": "5415668464654",
               "billingAddress": {
                  "street1": "calle 93",
                  "street2": "125544",
                  "city": "Bogota",
                  "state": "Bogota DC",
                  "country": "CO",
                  "postalCode": "000000",
                  "phone": "7563126"
               }
            },
            "creditCard": {
               "number": "4097440000000004",
               "securityCode": "321",
               "expirationDate": "2019/12",
               "name": "REJECTED"
            },
            "extraParameters": {
               "INSTALLMENTS_NUMBER": 1
            },
            "type": "AUTHORIZATION_AND_CAPTURE",
            "paymentMethod": "VISA",
            "paymentCountry": "CO",
            "deviceSessionId": str(deviceSessionId),
            "ipAddress": str(ip),
            "cookie": str(cookie.output()),
            "userAgent": str(headers["User-Agent"])
         },
         "test": False
      }
   if paymentMethod is "EFECTY":
      submit_transaction_data = {
         "language": "en",
         "command": "SUBMIT_TRANSACTION",
         "merchant": {
            "apiKey": apiKey,
            "apiLogin": apiLogin
         },
         "transaction": {
            "order": {
               "accountId": "512321",
               "referenceCode": str(referenceCode),
               "description": "payment test",
               "language": "en",
               "signature": str(signature_md5),
               "additionalValues": {
                  "TX_VALUE": {
                     "value": int(tx_value),
                     "currency": "COP"
               },
                  "TX_TAX": {
                     "value": int(tx_value * 0.19),
                     "currency": "COP"
               },
                  "TX_TAX_RETURN_BASE": {
                     "value": int(tx_value * 0.81),
                     "currency": "COP"
               }
               },
               "buyer": {
                  "fullName": "Hermelindo Perez",
                  "emailAddress": "buyer_test@test.com"
               }
            },
            "type": "AUTHORIZATION_AND_CAPTURE",
            "paymentMethod": "EFECTY",
            "expirationDate": "2019-03-02T00:00:00",
            "paymentCountry": "CO",
            "ipAddress": str(ip)
         },
         "test": False
      }
   return submit_transaction_data