<h1 align="center">Hi, I'm Aairah Parvaiz 👋</h1>

---

# 🎵 **MOOD BASED PLAYLIST (CLI AI Project)**

> A lightweight AI-powered command-line application that detects user mood from text and recommends a personalized playlist

**Student reg no :** 25BAI10172
**Student Name:** Aairah Parvaiz
**Institution:** VIT Bhopal

---

## 🎯 Project Objective

To build a simple yet effective system that:

* Accepts user input describing their feelings
* Uses **keyword-based sentiment analysis** to detect mood
* Classifies mood into categories (Happy, Sad, Calm, Neutral)
* Recommends a curated playlist accordingly

---

## 🎨 Project Overview

### What is This Project?

This project is a **CLI-based mood detection and music recommendation system** that:

* Simulates basic AI using keyword scoring
* Processes natural language input
* Maps emotions to curated Bollywood playlists
* Provides an engaging and interactive user experience

### Why This Project?

✅ Demonstrates **core AI/NLP concepts (sentiment analysis)**
✅ Beginner-friendly **rule-based recommendation system**
✅ Combines **logic + creativity (music + emotion)**
✅ Runs entirely in terminal (no heavy setup)

---

## 🌟 Features

### Core Features:

* 🎭 Mood detection from user text input
* 🧠 Keyword-based sentiment scoring algorithm
* 🎵 Curated playlists for each mood
* 💻 Simple CLI interaction
* 🌐 Multilingual touch (Hindi + Urdu messages)

### Supported Moods:

* 😊 Happy
* 😢 Sad
* 😌 Calm
* 😐 Neutral

---

## 🔧 Technology Stack

| Technology          | Purpose          |
| ------------------- | ---------------- |
| **Python**          | Core programming |
| **Basic NLP Logic** | Mood detection   |
| **CLI (Terminal)**  | User interface   |

---

## 📦 Installation

### Step 1: Save the Code

Save the file as:

```bash
mood_music_finder.py
```

### Step 2: Run the Program

```bash
python mood_music_finder.py
```

---

## 🚀 Usage Guide

### Example Interaction:

```
--- 🎵 Mood Music Finder 🎵 ---
How is your heart today? Describe your day in a sentence:

> I feel awesome and excited today!

[AI Analysis Result]
Detected Mood: Happy
Here is your curated playlist:
----------------------------------------
1. Kar Gayi Chull - Kapoor & Sons
2. Mauja Hi Mauja - Jab We Met
...
----------------------------------------
```

---

## 🧠 Algorithm & Pseudocode

### Mood Detection Algorithm

```
ALGORITHM GetMoodScore(text)

INPUT: user text

OUTPUT: mood category

BEGIN
    CONVERT text to lowercase

    DEFINE happy_keywords
    DEFINE sad_keywords
    DEFINE calm_keywords

    score ← 0

    FOR each word IN text DO
        IF word IN happy_keywords THEN
            score ← score + 1
        ELSE IF word IN sad_keywords THEN
            score ← score - 1
        END IF
    END FOR

    IF score > 0 THEN
        RETURN "Happy"
    ELSE IF score < 0 THEN
        RETURN "Sad"
    ELSE IF calm_keywords found in text THEN
        RETURN "Calm"
    ELSE
        RETURN "Neutral"
END
```

---

## 📊 Data Flow

```
User Input (Text)
        ↓
Text Preprocessing (Lowercase)
        ↓
Keyword Matching
        ↓
Score Calculation
        ↓
Mood Classification
        ↓
Playlist Recommendation 🎵
```

---

## 🔧 Key Functions

### 1. Mood Detection Function

```python
def get_mood_score(text):
    """
    Detects mood based on keyword scoring
    Returns: Happy / Sad / Calm / Neutral
    """
```

### 2. Main Execution Function

```python
def main():
    """
    Handles user interaction and displays playlist
    """
```

---

## 📈 Results & Output

* ⚡ Instant mood detection
* 🎵 Personalized playlist recommendations
* 🧠 Logical classification using simple AI rules
* 😊 Engaging user experience

---

## 🎓 Learning Outcomes

### 1. AI & NLP Basics

* Keyword-based sentiment analysis
* Text preprocessing
* Rule-based classification

### 2. Python Programming

* Functions & control flow
* Dictionaries & lists
* Input/output handling

### 3. Problem Solving

* Mapping emotions to actions
* Designing simple recommendation logic

### 4. Software Development

* Clean code structure
* User interaction design

---

## 🚀 Future Enhancements

* 🤖 Upgrade to ML-based sentiment analysis (Naive Bayes / NLP models)
* 🎧 Spotify / YouTube API integration
* 🌐 Web version using Flask or Streamlit
* 🎙️ Voice input for mood detection
* 🧠 Emotion intensity scoring

---

## 👨‍💻 Contributors

* **Aairah Parvaiz** – Developer
* **Mentor:** Pramod Kumar Bhat Sir

---

## 🙏 Acknowledgments

* Open-source Python community
* Inspiration from real-world music apps
* VIT Bhopal faculty support

---

## 📄 License

This project is for educational purposes.

---

## 📞 Contact

**Aairah Parvaiz**
CSE Student, VIT Bhopal

---

<div align="center">

### 🎶 Let your mood choose your music 🎶

**"Sometimes, the right song understands you better than words."**

</div>

