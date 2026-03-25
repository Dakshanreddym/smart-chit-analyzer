async function calculateInvestment(){

    const monthly = document.getElementById("monthly").value;
    const years = document.getElementById("years").value;
    const members = document.getElementById("members").value;
    const month_number = document.getElementById("month_number").value;
    const defaults = document.getElementById("defaults").value;

    const need_money = document.getElementById("need_money").checked;
    const registered = document.getElementById("registered").checked;
    const known_members = document.getElementById("known_members").checked;

    const res = await fetch("/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            monthly, years, members, month_number,
            defaults, need_money, registered, known_members
        })
    });

    const data = await res.json();

    document.getElementById("results").classList.remove("hidden");

    document.getElementById("sipResult").innerText =
        "SIP Final Value: ₹ " + data.sip_value;

    document.getElementById("chitResult").innerText =
        "Chit Fund Final Value: ₹ " + data.chit_value;

    document.getElementById("riskResult").innerText =
        "Chit Risk Score: " + data.risk_score + "/100";

    document.getElementById("bidPrediction").innerText =
        "Predicted Winning Bid: " + data.predicted_bid + "% discount";

    document.getElementById("recommendation").innerText =
        "Recommendation: " + data.recommendation;

    createChart(data.sip_value, data.chit_value);
}

function createChart(sip, chit){
    new Chart(document.getElementById("chart"), {
        type: "bar",
        data: {
            labels: ["SIP", "Chit Fund"],
            datasets: [{
                label: "Final Amount ₹",
                data: [sip, chit]
            }]
        }
    });
}
