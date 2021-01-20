# Download the helper library from https://www.twilio.com/docs/python/install
'''
from twilio.rest import Client



# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACee901e403172574f7329636417f3866c"
auth_token = "fcd324362e47d930584894d0314dfb91"
client = Client(account_sid, auth_token)
def send(body,to):
        message = client.messages.create(
                                    body=body,
                                    from_='whatsapp:+14155238886',
                                    to=f'whatsapp:{to}'
                                )

'''
'''
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACee901e403172574f7329636417f3866c"
auth_token = "fcd324362e47d930584894d0314dfb91"
client = Client(account_sid, auth_token)
def send(body,to):
    message = client.messages \
        .create(
            body=body,
            from_='+15017122661',
            to={to}
        )

#print(message.sid)
'''
'''
from twilio.rest import Client 
 
account_sid = 'ACee901e403172574f7329636417f3866c' 
auth_token = 'fcd324362e47d930584894d0314dfb91'
client = Client(account_sid, auth_token) 
def send(body,to):
    message = client.messages.create( 
                                from_='+18705379206',  
                                body=body,     
                                to='+919047791133'
                            ) 
    
#print(message.sid)
'''
'''
import http.client

conn = http.client.HTTPSConnection("api.msg91.com")

payload = ""

headers = {

    'authkey': "EnterYourAuthKey",

    'content-type': "application/json"

    }

​

conn.request("POST", "/api/v5/flow/", payload, headers)

​
res = conn.getresponse()
data = res.read()
​
print(data.decode("utf-8")
'''




import requests
import os

url = "https://www.fast2sms.com/dev/bulk"
def send(body,to):
    num=f"{to}"
    num=num[3:]

    querystring = {
    "authorization":"giOcNyft0GP96p4LKU5XqFkAa1E3JnMxWBwvV2DmC7ezj8oHTugL1xf3MzTUyiZQRaNcEOVP5uS7pFlC",
    "sender_id":"FSTSMS",
    "message":f"{body}",
    "language":"english",
    "route":"p",
    "numbers":num
    }
    

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    print(num,type(num))
