# from flask import Flask, request, redirect
# from twilio.rest import TwilioRestClient
 
# # Your Account Sid and Auth Token from twilio.com/user/account
# account_sid = "ACda44a370a99ff80870641e53fff0b602"
# auth_token  = "aa8cde211ccaa453f60435713e17af6c"
# client = TwilioRestClient(account_sid, auth_token)
 
# loc = "Dabo"
# curLoc = "Today's location: " + loc

# message = client.messages.create(body="Today's location: Dabo",
#     to="+12069097512",
#     from_="+14158308671") #,
#     #media_url="http://www.example.com/hearts.png")
# #print message.sid


from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+12069097512": "Chef",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)