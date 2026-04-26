
    
import random
def analyze_profile(username):

    score = 0
    reasons = []

    username_lower = username.lower()

    # 🔹 Rule 1: length check
    if len(username) < 5:
        score += 25
        reasons.append("Username too short")

    # 🔹 Rule 2: numeric only
    if username.isdigit():
        score += 40
        reasons.append("Only numbers username")

    # 🔹 Rule 3: suspicious keywords
    suspicious_words = ["bot", "fake", "spam", "test", "user123"]
    if any(word in username_lower for word in suspicious_words):
        score += 35
        reasons.append("Suspicious keyword detected")

    # 🔹 Rule 4: repetitive pattern
    if len(set(username)) < 3:
        score += 30
        reasons.append("Repetitive characters detected")

    # 🔹 Final decision
    is_fake = score > 60

    return {
        "risk_score": min(score, 100),
        "is_fake": is_fake,
        "reasons": reasons,
        "recommendation": "🚨 High Risk - Avoid Interaction" if is_fake else "✅ Looks Safe",
        "confidence": f"{min(score, 100)}%"
    }