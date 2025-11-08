# Lightweight sentiment/emotion analyzer and simple reply generator
# This is intentionally lightweight for easy deployment in MVP.
POSITIVE_WORDS = {"good","great","happy","awesome","love","like","enjoy","excited","positive","confident","motivated","productive"}
NEGATIVE_WORDS = {"sad","bad","angry","hate","tired","unmotivated","stressed","anxious","depressed","down","frustrated"}

def analyze_emotion(text):
    if not text or not isinstance(text, str):
        return "NEUTRAL", 0.0
    t = text.lower()
    pos = sum(t.count(w) for w in POSITIVE_WORDS)
    neg = sum(t.count(w) for w in NEGATIVE_WORDS)
    if pos > neg:
        score = min(0.99, pos / (pos + neg + 0.1))
        return "POSITIVE", round(score, 2)
    if neg > pos:
        score = min(0.99, neg / (pos + neg + 0.1))
        return "NEGATIVE", round(score, 2)
    # fallback neutral
    return "NEUTRAL", 0.6

def generate_reply(user_text):
    emotion, confidence = analyze_emotion(user_text)
    # rule-based replies for MVP; later integrate GPT
    if not user_text.strip():
        return ("Please type something so I can help — your goals, worries, or plans.", emotion, confidence)
    if emotion == "POSITIVE":
        reply = (
            "I can feel your positive energy — that's excellent! "
            "Let's channel it: what skill would you like to strengthen next?"
        )
    elif emotion == "NEGATIVE":
        reply = (
            "I sense some negativity — it's okay to have rough days. "
            "Tell me one small, manageable step you can take today toward your goal."
        )
    else:
        reply = (
            "Thanks for sharing. Would you like a step-by-step plan for a career goal "
            "or a short productivity routine to boost motivation?"
        )
    return reply, emotion, confidence