# Movie Recommendation System

## Description
This project focuses on building a robust movie recommendation system for a mobile app. The system suggests movies similar to the user's input movie using various NLP and machine learning techniques. A flask backend is used to facilitate communication between the model and the front end using REST APIs. Similar movies along with their posters, release dates, names, cast etc can be displayed on the screen in a second from user selection

## Table of Contents

1. [Movie Recommendation System](#movie-recommendation-system)
2. [Technologies Used](#technologies-used)
3. [System Architecture](#system-architecture)
4. [Recommendation System](#recommendation-system)
5. [Integration with Mobile App](#integration-with-mobile-app)
6. [Contributors](#contributors)


## Technologies Used
- Python
- Pandas: For data manipulation and preprocessing, especially for handling movie datasets.
- Natural Language Processing (NLP)
- scikit-learn: Besides CountVectorizer, other modules from scikit-learn might have been utilized for data preprocessing or modeling tasks.
- nltk (Natural Language Toolkit): used for text preprocessing tasks such as tokenization and stemming.
- Flask-Restful: For backend and Rest APIs
- JSON: Used for data interchange between the backend and frontend, especially for sending movie recommendations in JSON format.
- Requests: Likely used to make HTTP requests to interact with the IMDb API for fetching movie details.
- IMDb API
- Flutter for Mobile App Development

## System Architecture
The system architecture consists of the following components:
- **Mobile App**: Developed using Flutter, the mobile app serves as the user's gateway to the movie recommendation system. Users can easily browse through a vast collection of movies and select or search for any one of them. When a user chooses a movie, its unique identifier (ID) is sent to the backend server via an API request.
  
- **Recommendation System**: Leveraging NLP techniques and machine learning models, the recommendation system processes the incoming movie ID to generate a list of 7 similar movies, based on attributes of the selected movie such as its genre, description, cast, and crew.

- **Backend Server**: Developed using Flask. When the mobile app sends the movie ID, the backend server transmits the movie ID to the recommendation system, which then processes the request and generates a curated list of similar movies. Subsequently, the backend server retrieves this list of similar movies from the recommendation system and sends movies data back to the mobile app. This bidirectional communication ensures a smooth and efficient flow of data between the various components of the system.

- **IMDb API Integration**: To enrich the recommended movies with additional information, such as poster images, plot summaries, cast details, and release dates, the system integrates with the IMDb API. Once the recommendation system provides a list of similar movies, the backend server calls the IMDb API to fetch the relevant details for each movie. This information is then bundled into a JSON format and sent back to the mobile app for display.
  
- The entire process, from the user clicking on a movie within the app, generating and then displaying similar movies on the screen, occurs in less than a second due to optimised and efficient integration between the frontend and the backend


## Recommendation System

The recommendation system employs various processes to generate movie recommendations efficiently:

1. **Data Preprocessing**:
   - **Tokenization**: Movie descriptions and metadata of over 5000 movies are tokenized, breaking down the text into individual words or tokens. This includes Movie names, descriptions, genres, keywords, cast, and crew information.
   - **Stemming**: Words are reduced to their root form using stemming, eliminating variations and reducing vocabulary size.
   **CountVectorizer**: CountVectorizer is utilized to transform tokenized text into numerical vectors, representing the frequency of words in the corpus. It converts the text data into a matrix of token counts using techniques like bag of words.

2. **Feature Engineering**:
   - **Combining Features**: Movie descriptions, genres, keywords, cast, and crew information are combined into a single feature set or tags, allowing the system to consider multiple aspects of a movie when computing similarity.

3. **Model Selection**:
   - **Cosine Similarity**: Similarity between movies is measured using cosine similarity, which calculates the cosine of the angle between vectors representing movies in the feature space. It's chosen for its effectiveness in comparing documents and suitability for high-dimensional data like text.

4. **Recommendation Process**:
   - **Input Movie Selection**: The user selects a movie within the app, providing the system with an input movie.
   - **Similarity Calculation**: The system computes cosine similarity between the input movie and all other movies in the dataset.
   - **Top Similar Movies**: Movies with the highest similarity scores are selected as recommendations.
   - **IMDb API Integration**: Detailed information about recommended movies, including poster URLs, descriptions, cast, release dates, etc., is fetched using the IMDb API.
   - **JSON Response**: Relevant information about recommended movies is bundled into a JSON format and sent back to the frontend for display.

5. **Rationale**:
   - **Optimization for User Experience**: Techniques like tokenization and stemming enhance computational efficiency, ensuring swift recommendation generation for a seamless user experience.
   - **Comprehensive Recommendations**: By considering various movie features such as descriptions, genres, and cast, the system offers diverse and comprehensive movie suggestions tailored to user preferences.

6. **Why Cosine Similarity?**:
   - **Effective for Text Data**: Cosine similarity is well-suited for comparing text data, making it an ideal choice for analyzing movie descriptions and metadata.
   - **Sparse Data Handling**: It effectively handles sparse data, accommodating scenarios where not all movies share the same features or metadata.


## Integration with Mobile App
The mobile app provides a user-friendly interface for accessing movie recommendations and exploring movie details. It communicates with the backend server via RESTful APIs to fetch recommended movies and display their information. Users can also search for specific movies within the app and receive recommendations based on their search queries from our movies database.


## Contributors
- [Myself](https://github.com/dp1500) - Recommendation System and Backend
- [Contributor 1](https://github.com/Programmer9211) - Mobile App Developer
- [Contributor 2](https://github.com/Nitin-Singh18) - Mobile App Developer

