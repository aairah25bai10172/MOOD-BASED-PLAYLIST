# MOOD-BASED-PLAYLIST
A simple Python tool that asks how your day was and suggests Bollywood songs based on your mood. It uses a basic word-counting method to figure out if you're happy, sad, or just chilling.
# Bollywood Mood-to-Playlist Recommender (AI/ML)

## 📌 Project Overview
This project is a Command Line Interface (CLI) tool that uses **Lexicon-based Sentiment Analysis** to understand a user's emotional state from a text entry. Based on the detected mood (Happy, Sad, Calm, or Neutral), the system recommends a curated list of Bollywood songs.

The goal of this project is to demonstrate an end-to-end pipeline: 
`Text Input` -> `Sentiment Scoring` -> `Mood Classification` -> `Content Recommendation`.

---

## 🚀 How to Set Up and Run

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system. You can check this by running:
```bash
python --version

Example Usage:
The program will ask: "How is your heart today? Describe your day in a sentence:"

Input: "I had a very long day and I just want to relax and find some sukoon."

Output: Detected Mood: Calm (Followed by the Calm playlist).

🧠 How it Works
The project utilizes a get_mood_score function that:

Tokenizes user input into individual lowercase words.

Scans for matches against predefined dictionaries for Happy, Sad, and Calm moods.

Calculates a Score:

Positive words increase the score.

Negative words decrease the score.

Logic Branching: If the score is balanced or zero, it searches for "Calm" identifiers before defaulting to "Neutral."

📂 Project Structure
main.py: The primary script containing the sentiment logic and song database.

README.md: Project documentation and setup instructions.
