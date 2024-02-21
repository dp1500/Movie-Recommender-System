# Movie Recommendation System and App

This project entails the development of a movie recommendation system integrated with a mobile app. The system suggests movies similar to the user's preferences and provides detailed information about each movie. It leverages the IMDb API for movie details and implements various Natural Language Processing (NLP) techniques to process and analyze movie descriptions and metadata.

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [System Architecture](#system-architecture)
4. [Recommendation System](#recommendation-system)
5. [Integration with Mobile App](#integration-with-mobile-app)
6. [NLP Techniques](#nlp-techniques)
7. [Usage](#usage)
8. [Contributors](#contributors)
9. [License](#license)

## Introduction
The movie recommendation system provides users with personalized movie recommendations based on their preferences. It employs machine learning models to analyze movie metadata and user preferences, enabling accurate recommendations. The system also features integration with a mobile app, allowing users to explore recommended movies and search for specific titles.

## Technologies Used
- Python
- IMDb API
- Flask (for backend)
- Natural Language Processing (NLP)
- CountVectorizer (from scikit-learn)
- Cosine Similarity
- Mobile App Development (Flutter)

## System Architecture
The system architecture consists of the following components:
- **Mobile App**: Developed using Flutter, the mobile app serves as the user's gateway to the movie recommendation system. Users can easily browse through a vast collection of movies and select or search for any one of them. When a user chooses a movie, its unique identifier (ID) is sent to the backend server via an API request.
  
- **Recommendation System**: Leveraging NLP techniques and machine learning models, the recommendation system processes the incoming movie ID to generate a list of 7 similar movies, based on attributes of the selected movie such as its genre, description, cast, and crew.
- 
- **Backend Server**: Developed using Flask. When the mobile app sends the movie ID, the backend server transmits the movie ID to the recommendation system, which then processes the request and generates a curated list of similar movies. Subsequently, the backend server retrieves this list of similar movies from the recommendation system and sends movies data back to the mobile app. This bidirectional communication ensures a smooth and efficient flow of data between the various components of the system.
- 
- **IMDb API Integration**: To enrich the recommended movies with additional information, such as poster images, plot summaries, cast details, and release dates, the system integrates with the IMDb API. Once the recommendation system provides a list of similar movies, the backend server calls the IMDb API to fetch the relevant details for each movie. This information is then bundled into a JSON format and sent back to the mobile app for display.
- The entire process, from the user clicking on a movie within the app, generating and then displaying similar movies on the screen, occurs in less than a second due to optimised and efficient integration between the frontend and the backend


## Recommendation System
The recommendation system employs NLP techniques and machine learning models to generate movie recommendations. It preprocesses movie descriptions and metadata using techniques such as tokenization, stemming, and vectorization. Cosine similarity is then used to measure the similarity between movies, and the system recommends movies with the highest similarity scores to the user.

## Integration with Mobile App
The mobile app provides a user-friendly interface for accessing movie recommendations and exploring movie details. It communicates with the backend server via RESTful APIs to fetch recommended movies and display their information. Users can also search for specific movies within the app and receive recommendations based on their search queries.

## NLP Techniques
The project utilizes various NLP techniques to process and analyze movie descriptions and metadata:
- **Tokenization**: Breaking down movie descriptions into individual words or tokens.
- **Stemming**: Reducing words to their root forms to improve processing efficiency.
- **Vectorization**: Converting text data into numerical vectors for machine learning model input.
- **Cosine Similarity**: Measuring the similarity between movies based on their feature vectors.

## Usage
To use the movie recommendation system and app:
1. Start the backend server using Flask.
2. Access the mobile app and interact with the user interface to receive movie recommendations and explore movie details.

## Contributors
- [Your Name](link-to-your-github-profile) - Project Lead and Backend Developer
- [Contributor 1](link-to-contributor1-github-profile) - Mobile App Developer

## License
This project is licensed under the [MIT License](link-to-license-file).
