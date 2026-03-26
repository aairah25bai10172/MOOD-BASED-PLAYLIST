import sys

def get_mood_score(text):
    """
    A simple Keyword-Based Sentiment Analysis.
    It counts 'weighted' words to decide the mood.
    """
    text = text.lower()
    
    # Simple word lists for our 'AI' to look for
    happy_keywords = ['happy', 'great', 'awesome', 'good', 'excited', 'love', 'masti', 'party', 'fun']
    sad_keywords = ['sad', 'bad', 'tired', 'broken', 'heart', 'alone', 'lonely', 'cry', 'stress']
    calm_keywords = ['peace', 'relax', 'chill', 'soft', 'quiet', 'sleepy', 'study', 'sukoon']

    score = 0
    words = text.split()

    # Logic: Check each word in user input
    for word in words:
        if word in happy_keywords:
            score += 1
        elif word in sad_keywords:
            score -= 1
            
    # Final Mood Selection
    if score > 0:
        return "Happy"
    elif score < 0:
        return "Sad"
    elif any(cw in text for cw in calm_keywords):
        return "Calm"
    else:
        return "Neutral"

def main():
    print("--- 🎵 Mood Music Finder 🎵 ---")
    print("How is your heart today? Describe your day in a sentence:")
    
    user_input = input("> ")
    
    if len(user_input.strip()) < 3:
        print("Bhai, please write a bit more so I can understand!")
        return

    mood = get_mood_score(user_input)
    
    # Song Database
    playlists = {
        "Happy": [
            "1. Kar Gayi Chull - Kapoor & Sons",
            "2. Mauja Hi Mauja - Jab We Met",
            "3. Dil Chori - Sonu Ke Titu Ki Sweety",
            "4. Makhna - Drive",
            "5. Zingaat - Dhadak"
        ],
        "Sad": [
            "1. Channa Mereya - Ae Dil Hai Mushkil",
            "2. Agar Tum Saath Ho - Tamasha",
            "3. Hamari Adhuri Kahani - Title Track",
            "4. Kabira (Encore) - Yeh Jawaani Hai Deewani",
            "5. Pachtaoge - Jaani Ve"
        ],
        "Calm": [
            "1. Kun Faya Kun - Rockstar",
            "2. Iktara - Wake Up Sid",
            "3. Raatan Lambiyan (Lofi) - Shershaah",
            "4. Moh Moh Ke Dhaage - Dum Laga Ke Haisha",
            "5. Tum Ho - Rockstar"
        ],
        "Neutral": [
            "1. Phir Se Ud Chala - Rockstar",
            "2. Ilahi - Yeh Jawaani Hai Deewani",
            "3. Safarnama - Tamasha",
            "4. Matargashti - Tamasha",
            "5. Sham - Aisha"
        ]
    }

    print(f"\n[AI Analysis Result]")
    print(f"Detected Mood: {mood}")
    print(f"Here is your curated playlist:")
    print("-" * 40)
    
    for song in playlists[mood]:
        print(song)
    print("-" * 40)
    print("Hope this makes your day better!")
    print("\nधन्यवाद!")
    print("\nشکریہ!")

if __name__ == "__main__":
    main()
