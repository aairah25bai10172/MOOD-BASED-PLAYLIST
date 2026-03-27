<h1 align="center">Hi, I'm Aairah Parvaiz 👋</h1>

---

# 🎧 **Mood-Based Playlist Recommender Project**

> A smart music recommendation system that suggests playlists based on user mood using AI & data-driven logic

**Project Status:** ✅ Complete & Functional
**Student Name:** Aairah Parvaiz
**Institution:** VIT Bhopal

---

## 🎯 Project Objective

To build an intelligent system that:

* Detects or accepts user mood input 😊😢😡😌
* Recommends songs/playlists based on emotional state
* Uses data processing & simple ML techniques
* Enhances user experience through personalization

---

## 🎨 Project Overview

### What is This Project?

This project is a **mood-based music recommendation system** that:

* Takes user mood as input (manual or predicted)
* Maps mood to curated playlists
* Uses data analysis + logic to recommend songs
* Can be extended with APIs like Spotify or YouTube

### Why This Project?

✅ Combines **AI + real-world usability**
✅ Demonstrates **recommendation system concepts**
✅ Shows **data handling and personalization**
✅ Fun + practical project for users

---

## 🌟 Features

### Core Features:

* 🎭 Mood input (Happy, Sad, Angry, Relaxed, etc.)
* 🎵 Playlist recommendation based on mood
* 📊 Data processing using Pandas
* 🧠 Basic recommendation logic
* 💻 Clean UI (CLI or Web-based)

### Advanced Features:

* 🤖 Mood prediction (future scope - ML/NLP)
* 🎧 Integration with Spotify API
* 📈 User preference learning
* 💾 Playlist saving/export
* 🌐 Web app interface

---

## 🔧 Technology Stack

| Technology                    | Purpose              |
| ----------------------------- | -------------------- |
| **Python**                    | Core programming     |
| **Pandas**                    | Data handling        |
| **NumPy**                     | Numerical operations |
| **Scikit-learn**              | ML (optional)        |
| **Flask / Streamlit**         | Web interface        |
| **Spotify API / YouTube API** | Music data           |
| **Jupyter Notebook**          | Development          |

---

## 📦 Installation

### Step 1: Clone Project

```bash
cd Mood-Playlist-Recommender
```

### Step 2: Install Dependencies

```bash
pip install pandas numpy scikit-learn flask streamlit requests
```

### Step 3: Run Project

**Option A - Python Script**

```bash
python main.py
```

**Option B - Streamlit App**

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Mood-Playlist-Recommender/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── songs_dataset.csv
│   └── mood_mapping.csv
│
├── src/
│   ├── recommender.py
│   ├── mood_detector.py
│   └── utils.py
│
├── app/
│   └── app.py
│
└── notebooks/
    └── analysis.ipynb
```

---

## 🚀 Usage Guide

### Basic Usage:

```python
from recommender import recommend_playlist

mood = input("Enter your mood: ")
playlist = recommend_playlist(mood)

print("Recommended Songs:")
for song in playlist:
    print(song)
```

---

## 🧠 Algorithm & Pseudocode

### Main Algorithm:

```
ALGORITHM MoodPlaylistRecommender(mood_input)

INPUT: mood_input (user mood)

OUTPUT: playlist of recommended songs

BEGIN
    DEFINE mood_categories = [Happy, Sad, Angry, Relaxed]

    IF mood_input NOT IN mood_categories THEN
        RETURN "Invalid mood"
    END IF

    LOAD dataset

    FILTER songs WHERE mood == mood_input

    SORT songs by popularity OR relevance

    SELECT top N songs

    RETURN playlist
END
```

---

## 📊 Data Flow

```
User Input (Mood)
        ↓
Mood Processing
        ↓
Dataset Filtering
        ↓
Recommendation Logic
        ↓
Playlist Output 🎧
```

---

## 🔧 Key Modules

### 1. Recommender Module

```python
def recommend_playlist(mood):
    """
    Returns playlist based on mood
    """
```

### 2. Mood Detection Module (Optional AI)

```python
def detect_mood(text):
    """
    Detect mood using NLP (future enhancement)
    """
```

---

## 📈 Results & Output

* 🎵 Personalized playlists
* ⚡ Fast recommendation time
* 📊 Accurate mood-song mapping
* 😊 Improved user engagement

---

## 🎓 Learning Outcomes

### 1. Data Handling

* Working with datasets
* Filtering and transformations

### 2. Recommendation Systems

* Rule-based filtering
* Personalization logic

### 3. AI Concepts

* Mood detection (basic NLP)
* Feature mapping

### 4. Development Skills

* Modular coding
* Project structuring
* Debugging

---

## 🚀 Future Enhancements

* 🤖 AI mood detection using NLP (text/voice)
* 🎧 Spotify integration (real-time playlists)
* 📱 Mobile app version
* 🧠 Deep learning recommendation system
* 🌍 Multi-language support

---

## 👨‍💻 Contributors

* **Aairah Parvaiz** – Developer
* **Mentor:** Pramod Kumar Sir

---

## 🙏 Acknowledgments

* Open-source libraries
* Music APIs
* VIT Bhopal faculty support

---

## 📄 License

This project is for educational purposes.

---

## 📞 Contact

**Aairah Parvaiz**
VIT Bhopal
CSE Student

---

<div align="center">

### 🎶 Keep vibing with the right mood! 🎶

**"Music understands what words cannot."**

</div>
