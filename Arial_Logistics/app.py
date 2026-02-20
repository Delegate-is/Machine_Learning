from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total = None

    if request.method == "POST":
        base_fee = float(request.form["base_fee"])
        distance = float(request.form["distance"])
        per_km = float(request.form["per_km"])
        zone_multiplier = float(request.form["zone_multiplier"])
        seasonal = float(request.form["seasonal"])

        subtotal = base_fee + (distance * per_km * zone_multiplier)
        total = subtotal + (subtotal * seasonal / 100)

    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(debug=True)