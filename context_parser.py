import datetime

def extract_context(user_input):
    text = user_input.lower()

    context = {
        "time": "day",
        "goal": "normal",
        "last_meal": "unknown"
    }

    # time detection
    hour = datetime.datetime.now().hour
    if hour < 11:
        context["time"] = "morning"
    elif hour < 17:
        context["time"] = "afternoon"
    elif hour < 22:
        context["time"] = "evening"
    else:
        context["time"] = "late night"

    # goal detection
    if "light" in text:
        context["goal"] = "light"
    elif "protein" in text or "gym" in text:
        context["goal"] = "high protein"
    elif "weight loss" in text:
        context["goal"] = "low calorie"

    # last meal detection
    if "oily" in text or "heavy" in text:
        context["last_meal"] = "heavy"

    return context