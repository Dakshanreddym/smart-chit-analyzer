from flask import Flask, render_template, request, jsonify
from ml_model import predict_bid   # ML integration

app = Flask(__name__)

# ---------------- HOME ROUTE ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- SIP CALCULATOR ----------------
def sip_future_value(monthly, rate, months):
    r = rate / 12
    fv = monthly * (((1 + r) ** months - 1) / r) * (1 + r)
    return fv

# ---------------- CHIT CALCULATOR ----------------
def chit_return(monthly, months, discount=25):
    chit_value = monthly * months
    dividend_per_month = (chit_value * discount / 100) / months
    maturity = chit_value + dividend_per_month * months
    return maturity

# ---------------- RISK SCORE ENGINE ----------------
def risk_score(registered, known_members, defaults):
    score = 100
    if not registered:
        score -= 40
    if not known_members:
        score -= 20
    if defaults > 5:
        score -= 20
    return score

# ---------------- RECOMMENDATION ENGINE ----------------
def recommend(years, need_money):
    if need_money:
        return "Join Chit Fund"
    if years >= 5:
        return "Invest in SIP"
    return "FD / RD is safer"

# ---------------- MAIN CALCULATION API ----------------
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json

    # User inputs
    monthly = int(data["monthly"])
    years = int(data["years"])
    need_money = data["need_money"]
    registered = data["registered"]
    known_members = data["known_members"]
    defaults = int(data["defaults"])
    members = int(data["members"])
    month_number = int(data["month_number"])

    months = years * 12

    # Financial calculations
    sip_value = sip_future_value(monthly, 0.12, months)
    chit_value = chit_return(monthly, months)

    # Risk + Recommendation
    risk = risk_score(registered, known_members, defaults)
    suggestion = recommend(years, need_money)

    # 🤖 ML Prediction
    predicted_bid = predict_bid(members, month_number)

    # Response to frontend
    return jsonify({
        "sip_value": round(sip_value, 2),
        "chit_value": round(chit_value, 2),
        "risk_score": risk,
        "recommendation": suggestion,
        "predicted_bid": predicted_bid
    })

# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
