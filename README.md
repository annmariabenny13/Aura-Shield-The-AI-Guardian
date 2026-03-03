# 🛡️ AuraShield: AI Transit Guardian

**AuraShield** is an AI-powered safety application designed to protect women during cab journeys by proactively detecting danger. Developed by **Ann Maria Benny**, a second-year Integrated MSc Computer Science student at **Nirmala College, Muvattupuzha**, specializing in **AI & Data Science**.

---

## 🚀 Key Features

* **AI Anomaly Detection**: Uses a **Decision Tree Classifier** to analyze route deviations, unusual stops, and traffic density to predict safety risks.
* **Dead Zone Protocol**: Triggers a **Fake Video Call** deterrent (a simulated "Guardian" call) when the internet is unavailable.
* **Dead Battery Protocol**: Automatically sends a final GPS trajectory via **Twilio SMS** when the phone battery drops to 5%.
* **Trip Setup**: Allows users to log driver details and vehicle numbers before a journey begins for accountability.
* **Soft Alert Logic**: Implements a 30-second user-response timer to confirm safety before escalating to emergency contacts.

---

## 🛠️ Technical Stack

* **Backend**: Python & Flask
* **Machine Learning**: Scikit-Learn (Decision Tree Model)
* **Mapping**: Leaflet.js & OpenStreetMap
* **Communications**: Twilio SMS API
* **Frontend**: HTML5, CSS3, JavaScript

---

## 📂 Project Structure

* `app.py`: The Flask backend handling AI logic and Twilio integration.
* `templates/dashboard.html`: The interactive user dashboard and map.
* `model/model.pkl`: The trained AI model for anomaly detection.
* `static/`: Contains assets like the safety siren and fake call video.

---

## 🌟 Recognition
* Secured **4th Position** at **TinkHer Hack 4.0** (March 2026).
* Built as part of an 18-hour hackathon to address real-world safety challenges for women.