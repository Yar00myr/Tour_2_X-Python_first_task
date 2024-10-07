def check_temperature(temperature):
    if temperature <= 0:
        return "A cold, isn’t it?"
    elif 0 < temperature < 10:
        return "Cool."
    return "Nice weather we're having."
