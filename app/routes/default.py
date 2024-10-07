from flask import render_template, request
from ..helpers import check_temperature
from .. import app


@app.get("/")
def get_temperature_form():
    return render_template("temperature.html")


@app.post("/")
def post_temperature():
    user_input = request.form.get("temperature", "").replace(",", ".")
    message = "Please enter a temperature."

    if user_input:
        try:
            temperature = float(user_input)
            message = check_temperature(temperature)
        except ValueError:
            message = "Please enter a valid number (use '.' for decimal)."

    return render_template("temperature.html", message=message)
