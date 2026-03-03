import pandas as pd

def get_recommendations(cart_items, time_of_day):
    try:
        df = pd.read_csv("data/orders.csv")
    except:
        return ["CSV Not Found"]

    if not cart_items:
        return []

    # Make everything lowercase for comparison
    df["cart_item"] = df["cart_item"].str.lower()
    df["add_on"] = df["add_on"]

    cart_list = cart_items.lower().split(",")

    recommendations = []

    for item in cart_list:
        related = df[df["cart_item"] == item.strip()]
        recommendations += related["add_on"].tolist()

    recommendations = list(set(recommendations))

    return recommendations[:8]