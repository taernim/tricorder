from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
SYSTEM_PHONE_NUMBER = "+15005550006"
DEBUG = True

cType = ["Engineer", "Designer", "QA", "Other"]
id = 0
candidateDict = {
    #1: "John",
    #4: "Margaret",
}
class Candidate:
    """Each new candidate added to the system creates a new instance of the Candidate class"""
    name = ""
    field = ""
    votes = { } #Holds the votes & who voted for them
    def __init__(self, cField, cName_First, cName_Last):
        print "CANDIDATE __INIT__"
        self.name = cName_First
        print "name: " + self.name
        self.name += ' '
        self.name += cName_Last
        print "name: " + self.name
        self.field = cField
        print "field: " + self.field
        # Add our candidate to the candidateDict
        candidateDict[name] = id
        print candidateDict
        #Increment id
        id = id + 1

        # Announce our new candidate
        self.Announce()
    def Announce(self):
        print "Annoucing a new Candidate!"
        print "Name: " + self.name
        print "Field: " + self.field

def listAllCandidates():
    for id, person in candidateDict:
        print "id: " + id
        print "candidate: " + id

# All of our possible users
callers = {
    "+12069097512": "Chef",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}

#REAL CREDENTIALS
ACCOUNT_SID = "ACda44a370a99ff80870641e53fff0b602"
AUTH_TOKEN  = "aa8cde211ccaa453f60435713e17af6c"

#TEST CREDS~!!
#ACCOUNT_SID = "ACa081e28c446625fb2bccfcc53f2a1476"
#AUTH_TOKEN = "ae20b33c4bb179292fbf89bdf1601431"


app = Flask(__name__)

def _twilio_client():
    return TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# Handle all of our SMS sending via Twilio, since we use this a lot
def send_sms(sms_to, sms_body):
    # Don't send an SMS if they are on our blacklist
    print "DEBUG: sending sms to: {}".format(sms_to)
    client = _twilio_client()
    client.messages.create(to=sms_to,
                               from_=SYSTEM_PHONE_NUMBER,
                               body=sms_body)

def create_candidate():
    '''Creates a new candidate entry '''


    return
def delete_candidate():
    return


# Splits up words for parsing

## PROTOCOL: Candidate <Job Type> <FirstName> <LastName>
def parse_message(message):
    parse = message.split(' ')

    word_one = ''
    word_two = ''
    word_three = ''
    word_four = ''

    if len(parse) >= 1:
        word_one = str(parse[0])
    if len(parse) >= 2:
        word_two = parse[1]
    if len(parse) >= 3:
        word_three = parse[2]
    if len(parse) >= 4:
        word_four = parse[3]

    print "word_one: " + word_one
    print "word_one.lower: "
    print word_one.lower()

    return word_one.lower(), word_two.lower(), word_three.lower(), word_four.lower()

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    body = request.values.get('Body')
    if (DEBUG == True):
        print "******************DEBUG INFO ******************"
        print "values:"
        print request.values
        print "body: " + body

    # Parse to see if we have a new candidate
    print "About to parse_message()"
    word_one, word_two, word_three, word_four = parse_message(body)

    print "Preparing to test word_one/two/three values"
    if ((word_one == 'yes') or (word_one == 'no')):
        print "YES/NO DECIDER"
        print "&&&&& TODO: Handle Yes/No"

    elif (word_one == 'candidate'):
        #Ok we are adding a new candidate entry
        print "////////////////////////Candidate elif ///////////////////////////"

        # Find out if we're listing candidates or adding a new one
        if ((word_two == 'list') or (word_two == 'List')):
            listAllCandidates()
        else:
            Candidate(word_two, word_three, word_four)

    elif (word_one == 'list'):
        listAllCandidates()
    else:
        print "Unknown word: " + word_one
        resp = twilio.twiml.Response()
        resp.message("Unknown commands, please try again or contact Chef for help.")
        return str(resp)

    # Get name from the directory
    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Monkey"
    print "from: " + from_number
    resp = twilio.twiml.Response()
    resp.message("Hello, " + name)
    return str(resp)
 
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)