from twilio.rest import Client

while True:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/classic.mp3',
                            to='PUT NUMBER HERE',
                            from_='PUT TWILLO NUMBER HERE'
                        )
    
    print(call.sid)
