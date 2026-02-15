from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("kmeans_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route('/')
def home():
    # Default values when page loads first time
    return render_template(
        "index.html",
        age="",
        income="",
        spending=0
    )

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        income = float(request.form['income'])
        spending = float(request.form['spending'])

        data = np.array([[age, income, spending]])
        data_scaled = scaler.transform(data)

        prediction = model.predict(data_scaled)[0]

        cluster_names = {
            0: "High Spending Customers",
            1: "Careful High-Income Customers",
            2: "Average Customers",
            3: "High Spending – Low Income Customers",
            4: "Low Budget Customers"
        }

        cluster_descriptions = {
            0: "Customers with high income and high spending behavior.",
            1: "Customers with high income but controlled spending habits.",
            2: "Customers with balanced income and spending patterns.",
            3: "Customers with lower income but relatively high spending activity.",
            4: "Customers with lower income and low spending behavior."
        }

        segment = cluster_names.get(prediction)
        description = cluster_descriptions.get(prediction)

        return render_template(
            "index.html",
            result=segment,
            description=description,
            age=age,
            income=income,
            spending=spending
        )

    except:
        return render_template(
            "index.html",
            result="Invalid Input",
            description="Please enter valid numeric values.",
            age="",
            income="",
            spending=0
        )

if __name__ == "__main__":
    app.run(debug=True)



