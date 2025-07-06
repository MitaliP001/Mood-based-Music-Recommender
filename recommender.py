import random
from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # -1 to 1

def recommend_music(mood_score):
    if mood_score > 0.5:
        mood = "😊 Happy"
        playlist = [
            "Happy Hits – Spotify",
            "Feel Good Friday – YouTube",
            "Uplifting Pop"
        ]
    elif mood_score > 0:
        mood = "🙂 Slightly Positive"
        playlist = [
            "Chill Vibes – Spotify",
            "Lo-fi Beats",
            "Acoustic Coffeehouse"
        ]
    elif mood_score < -0.5:
        mood = "😢 Sad"
        playlist = [
            "Sad Songs – Spotify",
            "Rainy Mood Jazz",
            "Melancholy Piano"
        ]
    else:
        mood = "😐 Neutral/Unclear"
        playlist = [
            "Focus Flow – Spotify",
            "Instrumental Chill",
            "Coding Mix"
        ]

    return mood, random.choice(playlist)

if __name__ == "__main__":
    print("🎧 Mood-based Music Recommender")
    user_input = input("How are you feeling today?\n> ")
    score = get_sentiment(user_input)
    mood, suggestion = recommend_music(score)

    print(f"\nDetected Mood: {mood}")
    print(f"🎶 Recommended Playlist: {suggestion}")
