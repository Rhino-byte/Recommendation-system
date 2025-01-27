# Recommendation-system
Recommendation system
Authors:

[Noel Christopher](https://github.com/NOE0464) 

[Savins Nanyaemuny](https://github.com/Rhino-byte)

[Anthony Ekeno](https://github.com/sananthonio)

[Linet Lydia](https://github.com/LinetLydia)

[Imran Mahfoudh](https://github.com/malvadaox)

![Cinema - 30x40cm _ No frame](https://github.com/user-attachments/assets/4d9dcbd8-8e2e-49ff-baa2-fef524bb5bc4)

# Business Understanding
In a data-driven world, businesses aim to personalize user experiences to boost engagement, satisfaction, and revenue. For a movie streaming platform, a recommendation system can provide tailored suggestions based on user preferences and behavior. This project focuses on building a movie recommender system using collaborative filtering, matrix factorization, and a hybrid model to enhance recommendation quality and precision, ultimately improving user experience and platform engagement.

Business Question:
How can we build a recommendation system to provide personalized movie suggestions to users, improving engagement and satisfaction?
# Problem Statement
The movie streaming platform needs a recommendation system to:

- Develop a robust recommendation system that utilizes user and item interactions (ratings) and metadata (genres) to predict user preferences and generate personalized movie recommendations.

- Enhance customer satisfaction and retention by providing personalized movie suggestions.

- Increase user engagement, conversion rates, and platform revenue.

- Address the "cold start problem" for new users and movies with limited interaction data.

- Overcome the limitations of current recommendation methods in capturing the dynamics between users and movies, ensuring recommendations are relevant and diverse. The system must balance accuracy, scalability, and real-time processing to deliver seamless recommendations
# Objectives
Collaborative Filtering: Develop a model that recommends movies based on user-item interactions, such as ratings and viewing history.

- **Matrix Factorization:** Apply techniques like Singular Value Decomposition (SVD) to uncover latent factors in user-movie relationships, improving predictions.

- **Hybrid Model:** Combine collaborative filtering and matrix factorization to leverage the strengths of both approaches, improving recommendation accuracy and coverage.

- **Cold Start Problem:** Address challenges of recommending movies to new users and suggesting newly added movies with limited data. -Performance Optimization: Ensure the system is scalable and capable of providing real-time, personalized recommendations.

- **Model Evaluation:** Measure and compare model effectiveness using precision, recall, Accuracy and NDCG to evaluate the accuracy of the recommendations
# Success Criteria
1. Improved Accuracy: The hybrid model should outperform collaborative filtering and matrix factorization methods in terms of precision, recall, and user satisfaction.

2. Cold Start Handling: The system should offer meaningful recommendations for new users and movies with minimal performance drop.

3. Scalability: The recommendation system must scale efficiently as the platform grows, ensuring responsiveness even as the number of users and movies increases.

4. Increased Engagement: There should be a measurable increase in user interactions with recommended movies (e.g., views, ratings, or watch time).

5. Business Impact: The system should contribute to key business metrics such as increased subscriptions, user retention, and overall revenue.

# Reasons and Importance of Models
## Collaborative Filtering:
**Reason:** Collaborative filtering leverages historical user-item interactions (e.g., ratings, watch history) to make personalized recommendations.

**Importance:** It helps identify similar users and suggests movies based on what others with similar tastes have liked, improving user satisfaction and engagement.

### Matrix Factorization:
**Reason:** Matrix factorization techniques like Singular Value Decomposition (SVD) decompose the user-movie interaction matrix into latent factors, revealing hidden relationships between users and movies.

**Importance:** It enables the system to make better predictions, especially in sparse datasets (where many user-movie interactions are missing), enhancing recommendation accuracy.`

####  Hybrid Model:
**Reason:** A hybrid model combines the strengths of both collaborative filtering and matrix factorization to overcome their individual weaknesses, such as the cold start problem in collaborative filtering.

**Importance:** Hybrid models improve recommendation robustness by integrating multiple techniques, ensuring more diverse and accurate movie recommendations across different user profiles.

By utilizing these models, the movie recommender system will be more effective, engaging, and scalable, ultimately leading to a better user experience and helping the platform achieve its key business goals
# Data understanding

## MOVIE-dataset
- Data Overview: The dataset contains 9,742 rows and 3 columns: movieId (integer), title (string), and genres (string). All columns have non-null values, with movieId being unique for each entry.

- Summary Statistics: The movieId values range from 1 to 193,609, with a mean value of 42,200, and the most frequent genre is "Drama" (appearing 1,053 times). The dataset has minimal missing data, and the most common movie title is "Confessions of a Dangerous Mind (2002)" which appears twice.

- Shape and Uniqueness: The dataset has a shape of (9742, 3), with movieId containing 9742 unique values, title having 9737 unique values (indicating some duplicate titles), and genres having 951 unique genre types.

- No Duplicates: There are no duplicate movieId values in the dataset, but some movie titles are repeated, suggesting potential cases where the same movie appears with slightly different versions or formats.

# RATINGS-dataset
- Data Overview: The ratings dataset contains 100,836 rows and 4 columns: userId (integer), movieId (integer), rating (float), and timestamp (integer). All columns have non-null values, and the data is structured to track movie ratings by users.

- Summary Statistics: The userId ranges from 1 to 610, with a mean value of 326, and the movieId spans from 1 to 193,609, covering a wide range of movies. The average rating is 3.5 (on a 1-5 scale), and the most frequent timestamp corresponds to the period around 1.2 billion seconds since January 1970.

- Shape and Uniqueness: The dataset has a shape of (100836, 4), with userId containing 610 unique values, movieId containing 9,724 unique movie identifiers, and rating having 10 possible unique rating values. The timestamp column has 85,043 unique values, showing a diverse set of rating times.

- No Duplicates: There are no duplicate rows in the dataset, ensuring that each rating is unique for a given userId and movieId combination, although there may be multiple ratings by the same user for different movies.
# Data Cleaning
Missing values and duplicated rows are handled. Also, columns irrelevant to the project are dropped. Formatting of columns and their contents for smooth analysis.
# Data Merging

- ratings and movies, is merged on the movieId column using an inner join.

- An inner join was used to merge the two DataFrames based on movieId, ensuring only movies that have both ratings and metadata (title/genres) are included, excluding entries with missing data in either DataFrame.

- Shape: The resulting DataFrame has 100,836 entries and 6 columns.

- Columns: contains columns: userId, movieId, rating, timestamp, title, and genres.

- Data Types: The columns contain data types: int64 for identifiers, float64 for ratings, and object for movie title and genres.

- Summary Statistics: Basic descriptive statistics show mean ratings of 3.5, with a rating range from 0.5 to 5.

- Value Counts: 100,836 entries, each representing a unique rating event, with a mix of ratings across various movies and genres.

- Unique Entries: The data includes various combinations of userId, movieId, rating, and timestamp for different movies, showing no duplicates or repeated entries.

- Duplicated Entries: no duplicated rows
# DataSAnalysis; visaualisations
a)General Top-rated genres are Action, comedy and drama
![alt text](image1.png)

b)Top-rated movies that is at least 50 rated is Shawshank redemption, the (1994)
![alt text](image2.png)

c)Avarage ratings per genres: film-noir and war are recommended
![alt text](image3.png)


# Data Preparation
Split data TRAIN & TEST:Splitting the data ensures that the model is trained on one part of the data and evaluated on unseen data to measure its generalization performance.
Importance:Prevents overfitting. Provides an unbiased evaluation of the model.
Splitting the data into train and test sets (80-20 split)
Training data size: 80668
Testing data size: 20168

# Feature Engineering
Enhance the dataset by extracting meaningful features, such as genres, and normalizing ratings to improve matrix factorization performance.

Content-based filtering relies on genres. Normalization reduces biases caused by individual user rating scales

# User-Based Collaborative Filtering (UBCF)
Performance Metrics:

RMSE: 0.8808
MAE: 0.6753
Precision at 10: 0.6551
Recall at 10: 0.6787
Accuracy: 0.6584
Advantages:
Advantages:

Simple to implement and interpret.
Effective when there is a large amount of user data available.
Can provide personalized recommendations based on similar users.
Disadvantages:

Suffers from the "cold start" problem for new users.
Performance can degrade with sparse data.

# Item-Based Collaborative Filtering (IBCF)
Performance Metrics:

RMSE: 0.8911
MAE: 0.6866
Precision at 10: 0.6650
Recall at 10: 0.6767
Accuracy: 0.6345
Advantages:
More stable than UBCF as it relies on item similarities rather than user similarities.
Can be effective in systems with high user turnover.
Disadvantages:

Requires a good amount of item data to be effective.
May not capture user preferences as effectively as UBCF

# Model-Based Collaborative Filtering (Matrix Factorization using SVD)
Performance Metrics:

RMSE: 0.8712
MAE: 0.6693
Precision at 10: 0.6682
Recall at 10: 0.6758
Accuracy: 0.6405
Advantages:

Handles sparsity well and scales efficiently for large datasets.
Can uncover latent features that represent user preferences and item characteristics.
Generally provides better accuracy than memory-based methods.
Disadvantages:

More complex to implement and requires more computational resources.
May require tuning of hyperparameters for optimal performance

## Hybrid Recommendation System
Performance Metrics:

RMSE: 4.2135 (notably high, indicating poor performance)
Precision at 5: 1.0
Recall at 5: 0.1282
F1 Score: 0.2273
Advantages:

Combines the strengths of both collaborative and content-based filtering.
Can provide more diverse recommendations by leveraging multiple data sources.
Disadvantages:

Complexity in implementation and tuning.
The performance can vary significantly based on the weighting of collaborative vs. content-based scores.
Recommendations
Based on the analysis of the performance metrics, the following recommendations can be made:

## Best Model: Matrix Factorization (SVD)

Reason: It has the lowest RMSE and MAE among the models, indicating better predictive accuracy. It also has a higher precision compared to UBCF and IBCF, suggesting that it provides more relevant recommendations.
Advantages: It effectively handles sparsity and scales well with large datasets, making it suitable for real-world applications.
Consider UBCF for Specific Use Cases: If user data is abundant and the system can afford to handle the cold start problem, UBCF can be a good choice due to its simplicity and effectiveness in personalized recommendations.

# Hybrid Movie Recommendations
The hybrid recommendation system effectively combines collaborative and content-based filtering to deliver personalized movie recommendations by leveraging user preferences and movie attributes. Observations reveal that the system performs well in predicting ratings, with reasonable RMSE values indicating accurate estimations of user preferences. Metrics like precision, recall, and F1 score demonstrate the model's ability to recommend relevant movies, while the confusion matrix highlights its effectiveness in distinguishing between relevant and non-relevant films. The balanced hybrid approach ensures that both user behavior and movie content contribute to predictions, resulting in a system that provides diverse and tailored recommendations. These findings suggest that hybrid models can outperform standalone methods, offering a practical solution for personalized recommendation systems.


# Recommendation

1. **General Top-Rated Genres**

**Insights:** Users with similar preferences highly rated genres such as Action, Comedy, and Drama, making them the most likely to engage users. Conversely, genres like Film Noir, Western, and Documentary received low ratings, suggesting limited appeal.

**Action:** Focus on recommending movies within top-rated genres for better user satisfaction and retention.

2. **Top-Rated Movies**

**Insight:** "The Shawshank Redemption (1994)" is a consistently top-rated movie with at least 50 user ratings, making it an excellent candidate for personalized recommendations to a broad audience.

**Action:** Include highly rated movies in recommendations to address user satisfaction and platform engagement goals.

3. **Average Ratings Per Genre**

**Insight:** Although Action, Comedy, and Drama dominate in popularity, genres like Film Noir and War are highly rated on average despite lower engagement.

**Action:** Promote movies in highly rated niche genres to diversify recommendations and provide tailored suggestions for users who prefer less mainstream content, increasing retention.

4. **Average Movie Ratings Over Time**

**Insight:** The average movie rating has increased steadily, from ~34 in 1995 to ~39 in 2015. This indicates a positive trend in user ratings over time, likely due to improved movie quality or changing user expectations.

**Action:** Highlight trending or newer movies with strong ratings to drive engagement, particularly among users seeking contemporary content.

5. **Best Model for Recommendations**

**Insight:** Matrix Factorization (SVD) outperforms other models like UBCF (User-Based Collaborative Filtering) and IBCF (Item-Based Collaborative Filtering) with the lowest RMSE and MAE, indicating better predictive accuracy. Its higher precision ensures relevant and accurate recommendations.

**Action:** Use SVD as the core algorithm for generating personalized movie recommendations to achieve accuracy, scalability, and improved user satisfaction.

6. **Cold Start Problem**

For New Users: Recommend popular and highly rated movies across genres like Action and Drama, ensuring engagement from the first interaction.
For New Movies: Leverage metadata (genres, release year) to suggest new movies to users with preferences aligned to those genres.


# Conclusion
Action, comedy and drama where highly rated genres by general users. while film noir, western and documentary are lowly rated in genres.Top-rated movies that is at least 50 rated is Shawshank redemption, the (1994) and avarage ratings per genres: film-noir and war are recommended The Matrix Factorization (SVD) model stands out as the most effective recommendation system based on the provided metrics, particularly for its accuracy and ability to handle large datasets. User-Based Collaborative Filtering can be effective in certain scenarios but may not perform as well in sparse data situations. The Hybrid Recommendation System has potential but requires further development to enhance its predictive capabilities. Continuous evaluation and tuning of these models are essential to adapt to changing user preferences and improve overall recommendation quality









