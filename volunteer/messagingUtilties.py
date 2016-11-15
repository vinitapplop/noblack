import requests
from threading import Thread
payload = {
    'EmailID': 'applopOTP',
    'Password': 'rahul123',
    'SenderID': 'Applop',
    'ServiceName': 'TEMPLATE_BASED'}

def buildPayload(number, message):
    p = payload.copy()
    p['MobileNo'] = number
    p['Message'] = message
    return p

def buildOTPMessage(userName,otp):
    m = "Dear " + userName + ": Welcome ! Your verification code is  " + otp + '.'
    return m

def newMessage(payload):
    url = 'http://sms.applop.com/api_1.0/SendSMS.aspx'
    r = requests.get(url, params=payload)
    print(r.text)
def sendMessage(phoneNo,otp):
    message = buildOTPMessage(phoneNo,otp)
    pl = buildPayload(phoneNo,message)
    print(pl)
    t = Thread(target=newMessage,args=(pl,))
    t.start()

def sendPullReply(payload):
    url = 'http://smsapi.24x7sms.com/api_2.0/SendSMS.aspx'
    r = requests.get(url,params=payload)
    print(r.text)

def messageReplyBuilder(number,message):
    s = "Dear " +number +": "+message
    return s
def sendUserReply(number,message):
    message =messageReplyBuilder(number, message)
    pl = buildPayload(number,message)
    print(pl)
    t = Thread(target=newMessage, args=(pl,))
    t.start()

def replyPullSMS(number,message):
    datax = {
        'APIKEY':'syzJ8242Xlc',
        'MobileNo':number,
        'SenderID':'Numbrr',
        'Message':message,
        'ServiceName':'OPTIN_OPTOUT',
    }
    t = Thread(target=sendPullReply, args=(datax,))
    t.start()

# 'http://smsapi.24x7sms.com/api_2.0/SendSMS.aspx?APIKEY=syzJ8242Xlc&MobileNo=919111199991&SenderID=Numbrr&Message=Test%20SMS&ServiceName=OPTIN_OPTOUT'
promotionalPayLoad = {

}