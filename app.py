from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open("xgboost_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    """Display the form and handle predictions."""
    form_data = {}  # Empty inputs initially
    prediction = None
    error = None

    if request.method == "POST":
        # If "Reset" is clicked, return empty form
        if "reset" in request.form:
            return render_template("index.html", prediction=None, form_data={})

        try:
            # Store entered values
            form_data = {
                "Energy_lag_1h": request.form.get("Energy_lag_1h", ""),
                "GHI": request.form.get("GHI", ""),
                "Energy_rolling_6h": request.form.get("Energy_rolling_6h", ""),
                "SunlightTime_daylength": request.form.get("SunlightTime_daylength", ""),               
                "humidity": request.form.get("humidity", ""),
                "temp": request.form.get("temp", "")
            }

            # Convert inputs to float for prediction
            features = np.array([[float(form_data[key]) for key in form_data]])
            features[0][1] = np.log1p(features[0][1])  # Apply log transformation

            # Predict
            prediction = np.expm1(model.predict(features)[0])


        except ValueError:
            error = "Invalid input. Please enter numeric values."

    return render_template("index.html", prediction=prediction, form_data=form_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
