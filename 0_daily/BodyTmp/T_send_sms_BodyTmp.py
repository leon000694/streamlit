from twilio.rest import Client
from datetime import datetime

def send_sms(name='leon', phone='972919686'):
    account_sid = "AC2fe88218b89f20d27763ff10113e8753"
    auth_token  = "187b1f17ccf287c8713966fb5279e30d"
    client = Client(account_sid, auth_token)
    now_ = datetime.now().strftime('%m/%d, %H:%M')

    message = client.messages.create(
        to=f"+886{phone}", 
        from_="+14438154163",
        body=f"{name}，提醒您，記得於10:30前完成今日體溫登錄哦!\n From M13 許煇昇{now_}")
    
    #print(message.sid)

#send_sms()

