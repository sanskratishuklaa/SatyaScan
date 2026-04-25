import random

def analyze_profile(username):
    # Dummy AI logic (later replace with ML model)
    activity_score = random.randint(1, 100)

    if activity_score > 70:
        return {
            "risk_score": activity_score,
            "is_fake": True
        }
    else:
        return {
            "risk_score": activity_score,
            "is_fake": False
        }