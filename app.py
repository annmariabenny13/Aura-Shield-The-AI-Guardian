from flask import Flask, request, jsonify, render_template
import joblib
from twilio.rest import Client

app = Flask(__name__)
model = joblib.load('model/model.pkl')

# ==========================================
# TWILIO CONFIGURATION
# ==========================================
TWILIO_ACCOUNT_SID = "your_twilio_sid_here"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token_here"      
TWILIO_PHONE = '+16205915037'                     
EMERGENCY_CONTACT = '+915678987656'              

def dispatch_twilio_sms(message_body):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE,
            to=EMERGENCY_CONTACT
        )
        print(f"✅ SUCCESS! SMS Sent. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"❌ TWILIO ERROR: {str(e)}")
        return False

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/check_anomaly', methods=['POST'])
def check_anomaly():
    data = request.json
    prediction = model.predict([[
        float(data['route_dev']), 
        float(data['time_stopped']), 
        float(data['traffic']), 
        float(data['noise'])
    ]])[0]
    return jsonify({"anomaly": int(prediction)})

@app.route('/send_sms', methods=['POST'])
def send_sms():
    body = "🚨 AURASHIELD URGENT: Ann Maria is not responding. Cab deviated and stopped. Live Location: http://maps.google.com/?q=9.9816,76.5750"
    if dispatch_twilio_sms(body):
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 500

@app.route('/battery_alert', methods=['POST'])
def battery_alert():
    body = "🔋 AURASHIELD CRITICAL: Ann Maria's battery is at 5%. Last Location: http://maps.google.com/?q=9.9816,76.5750"
    if dispatch_twilio_sms(body):
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 500

# --- NEW: ONLY ADDED THIS SAFE ARRIVAL SMS ---
@app.route('/safe_sms', methods=['POST'])
def safe_sms():
    body = "🟢 AURASHIELD UPDATE: Safe trip completed. No threats detected. Ann Maria has reached home safely."
    if dispatch_twilio_sms(body):
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 500
# ---------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)