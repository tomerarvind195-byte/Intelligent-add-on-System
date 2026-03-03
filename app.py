from flask import Flask, render_template, request
from model.recommender import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = []
    if request.method == "POST":
        cart_items = request.form.get("cart")
        time_of_day = request.form.get("time")
        recommendations = get_recommendations(cart_items, time_of_day)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)