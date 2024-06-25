# Myntra Fashion Recommendations System

This project aims to build a fashion recommendations system similar to the functionality provided by Myntra. The system utilizes Natural Language Processing (NLP) techniques, TF-IDF vectorization, and cosine similarity to recommend fashion items based on user input. It also includes a FastAPI backend for serving recommendations and a frontend interface for user interaction.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Files and Directories](#files-and-directories)
- [Acknowledgements](#acknowledgements)

## Project Overview

The project consists of several components:

1. **Data Cleaning and Preprocessing**: A Python file (`text_preprocessing.py`) is used to clean and pre-process the fashion dataset. This includes handling missing values, removing duplicates, formatting text data, and creating tags for each fashion item.

2. **Recommendation System**: The recommendation logic is implemented in a Jupyter Notebook (`recommendation_system.ipynb`). It uses cosine similarity scores to recommend similar fashion items based on user input.

3. **FastAPI Backend**: A FastAPI backend (`main.py`) is created to serve the recommendations. It exposes RESTful endpoints for retrieving top dresses and recommendations based on user input.

4. **Frontend Interface**: The frontend interface (`index.html`) provides a user-friendly interface for users to interact with the system. It communicates with the FastAPI backend to fetch and display recommendations.

5. **Model Persistence**: The final trained model, along with the preprocessed data, is serialized and saved using the pickle library (`df.pkl`, `similarity.pkl`, `tfidf.pkl`) for future use in the FastAPI backend.

## Technologies Used

- Python
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- pickle
- FastAPI
- HTML
- CSS
- JavaScript

## Project Structure

The project structure is organized as follows:

```
Myntra-Fashion-Recommendations-System/
│
├── recommendation_system.ipynb
├── main.py
├── df.pkl
├── Fashion Dataset.csv
├── index.html
├── text_preprocessing.py
├── tfidf.pkl
├── Myntra-Logo.png
├── similarity.pkl
├── README.md
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/VatsAmanJha/Myntra-Fashion-Recommendations-System.git
   ```

2. Start the FastAPI backend:

   ```bash
   uvicorn main:app --reload
   ```

3. Open the frontend interface:

   - Open `index.html` in a web browser to access the frontend interface.

## Usage

- Follow the steps in the Jupyter Notebooks (`text_preprocessing.py`, `recommendation_system.ipynb`) to preprocess data, create word embeddings, and build the recommendation system.
- Start the FastAPI backend (`main.py`) to serve recommendations.
- Open the frontend interface (`index.html`) and interact with the system to get fashion recommendations.

## Files and Directories

- `recommendation_system.ipynb`: Jupyter Notebook for building the recommendation system.
- `main.py`: FastAPI backend for serving recommendations.
- `df.pkl`: Pickle file containing serialized DataFrame with preprocessed data.
- `Fashion Dataset.csv`: The raw dataset containing fashion items.
- `index.html`: Frontend interface for user interaction.
- `text_preprocessing.py`: Python script for text preprocessing.
- `tfidf.pkl`: Pickle file containing serialized TF-IDF vectorizer.
- `Myntra-Logo.png`: Logo image for the frontend.
- `similarity.pkl`: Pickle file containing serialized similarity matrix.
- `README.md`: Project documentation.

## Acknowledgements

This project is inspired by the Myntra fashion platform and utilizes concepts from natural language processing, recommendation systems, FastAPI, and frontend development.
