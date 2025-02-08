sudo apt -y update
sudo apt -y upgrade
python -m venv call
source call/bin/activate
pip3 install -r requirements.txt
export TWILIO_ACCOUNT_SID="Your Twilio Account SID"
export TWILIO_AUTH_TOKEN="Your Twilio Account Token"
export TWILIO_NUMBER="Your Twilio Buyed Number"
export TARGET_NUMBER="Target Number" #only for verified number
python call.py
