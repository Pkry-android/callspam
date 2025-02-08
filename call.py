from twilio.rest import Client
import os

# Fetch Twilio credentials from environment variables
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Check if credentials are available
if not account_sid or not auth_token:
    print("Error: Twilio Account SID and Auth Token are not set.")
    exit(1)

client = Client(account_sid, auth_token)

# Define phone numbers and TwiML URL
from_number = os.environ.get("TWILIO_NUMBER")
to_number = os.environ.get("TARGET_NUMBER")
twiml_url = "http://demo.twilio.com/docs/voice.xml"


    # Create the call
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        url=twiml_url
    )

try:# Output call SID
    print(f"Call SID: {call.sid}")

except Exception as e:
    # Capture and print error message
    print(f"Error occurred: {e}")

    # Print full error object to see all available details
    print("Full error details:")
    print("Error type:", type(e))
    print("Error args:", e.args)

    # If the exception contains additional information (e.g., Twilio's error detail>    if hasattr(e, 'status'):
        print(f"Error status: {e.status}")
    if hasattr(e, 'message'):
        print(f"Error message: {e.message}")
    if hasattr(e, 'info'):
        print(f"Error info: {e.info}")
