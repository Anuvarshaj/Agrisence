def get_recommendation(plant, moisture, ph, n, p, k, temp, hum):

    # Crop ideal conditions
    plants = {
        "Tomato": {
            "ph": (5.5, 7.5),
            "moisture": (60, 80),
            "temp": (18, 30),
            "humidity": (60, 80),
            "npk": (50, 40, 40)
        },
        "Rose": {
            "ph": (6.0, 7.0),
            "moisture": (50, 70),
            "temp": (16, 28),
            "humidity": (50, 70),
            "npk": (30, 30, 30)
        },
        "Cucumber": {
            "ph": (5.8, 7.0),
            "moisture": (70, 85),
            "temp": (20, 32),
            "humidity": (70, 90),
            "npk": (40, 50, 50)
        },
        "Brinjal": {
            "ph": (5.5, 6.8),
            "moisture": (60, 75),
            "temp": (22, 35),
            "humidity": (60, 80),
            "npk": (40, 40, 40)
        },
        "Chilli": {
            "ph": (6.0, 6.8),
            "moisture": (50, 70),
            "temp": (20, 30),
            "humidity": (50, 70),
            "npk": (30, 30, 30)
        },
        "Beans": {
            "ph": (6.0, 7.0),
            "moisture": (60, 75),
            "temp": (18, 30),
            "humidity": (55, 75),
            "npk": (20, 30, 30)
        },
        "Chickoo": {
            "ph": (6.0, 8.0),
            "moisture": (55, 70),
            "temp": (22, 35),
            "humidity": (60, 80),
            "npk": (40, 40, 50)
        },
        "Snake Plant": {
            "ph": (5.5, 7.5),
            "moisture": (20, 40),
            "temp": (15, 30),
            "humidity": (30, 50),
            "npk": (10, 10, 10)
        }
    }

    # Organic remedies knowledge base
    organic_remedies = {
        "ph_low": "Add lime water (1 part lime : 3 parts water) near the roots once every 15 days.",
        "ph_high": "Mix compost, cow dung, neem cake, or leaf compost to reduce alkalinity naturally.",

        "moisture_low": "Water slowly in the morning (1–2 liters). Use drip irrigation and apply dry leaf or straw mulching.",
        "moisture_high": "Reduce watering. Improve drainage using sand or raised beds.",

        "nitrogen_low": "Apply vermicompost, cow dung slurry, or groundnut cake once a week.",
        "phosphorus_low": "Add bone meal, rock phosphate, or banana peel compost.",
        "potassium_low": "Apply wood ash, banana peel water, or compost tea.",

        "temp_low": "Use organic mulching and expose plants to sunlight.",
        "temp_high": "Provide shade net and spray water during noon to cool plants.",

        "humidity_low": "Spray water on leaves early morning or keep water trays nearby.",
        "humidity_high": "Improve air circulation and avoid excess watering."
    }

    p_data = plants[plant]
    suggestions = []

    # Soil Moisture Check
    if moisture < p_data["moisture"][0]:
        suggestions.append(
            f"Soil moisture is low ({moisture}%). {organic_remedies['moisture_low']}"
        )
    elif moisture > p_data["moisture"][1]:
        suggestions.append(
            f"Soil moisture is high ({moisture}%). {organic_remedies['moisture_high']}"
        )

    # pH Check
    if ph < p_data["ph"][0]:
        suggestions.append(
            f"Soil pH is low ({ph}). {organic_remedies['ph_low']}"
        )
    elif ph > p_data["ph"][1]:
        suggestions.append(
            f"Soil pH is high ({ph}). {organic_remedies['ph_high']}"
        )

    # NPK Check
    if n < p_data["npk"][0]:
        suggestions.append(
            f"Nitrogen deficiency detected. {organic_remedies['nitrogen_low']}"
        )
    if p < p_data["npk"][1]:
        suggestions.append(
            f"Phosphorus deficiency detected. {organic_remedies['phosphorus_low']}"
        )
    if k < p_data["npk"][2]:
        suggestions.append(
            f"Potassium deficiency detected. {organic_remedies['potassium_low']}"
        )

    # Temperature Check
    if temp < p_data["temp"][0]:
        suggestions.append(
            f"Temperature is low ({temp}°C). {organic_remedies['temp_low']}"
        )
    elif temp > p_data["temp"][1]:
        suggestions.append(
            f"Temperature is high ({temp}°C). {organic_remedies['temp_high']}"
        )

    # Humidity Check
    if hum < p_data["humidity"][0]:
        suggestions.append(
            f"Humidity is low ({hum}%). {organic_remedies['humidity_low']}"
        )
    elif hum > p_data["humidity"][1]:
        suggestions.append(
            f"Humidity is high ({hum}%). {organic_remedies['humidity_high']}"
        )

    # Final Output
    if not suggestions:
        return f"🌱 {plant} is healthy. Continue current organic farming practices."

    return f"🌿 Smart Organic Suggestions for {plant}:\n\n• " + "\n• ".join(suggestions)
