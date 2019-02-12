import hashlib

apiLogin = "pRRXKOl8ikMmt9u"
apiKey = "4Vj8eK4rloUd272L48hsrarnUA"

merchantid =  508029
referenceCode= "TestPayUs"
tx_value = 20000
currency  = "COP"

signature = str(apiKey)+"~"+str(merchantid)+"~"+str(referenceCode)+"~"+str(tx_value)+"~"+str(currency)
signature_md5 = hashlib.md5(signature).hexdigest()

ping_data = {
   "test": False,
   "language": "en",
   "command": "PING",
   "merchant": {
      "apiLogin": apiLogin,
      "apiKey": apiKey
   }
}

payment_metods_data = {
   "test": False,
   "language": "en",
   "command": "GET_PAYMENT_METHODS",
   "merchant": {
      "apiLogin": apiLogin,
      "apiKey": apiKey
   }
}

submit_transaction_data = {
   "language": "es",
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
         "language": "es",
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
      "deviceSessionId": "vghs6tvkcle931686k1900o6e1",
      "ipAddress": "127.0.0.1",
      "cookie": "pt1t38347bs6jc9ruv2ecpv7o2",
      "userAgent": "Mozilla/5.0 (Windows NT 5.1; rv:18.0) Gecko/20100101 Firefox/18.0"
   },
   "test": False
} 