# Project: Movie Recommender System Using Machine Learning

![mrs](https://github.com/user-attachments/assets/96f58373-15c9-47f2-a63e-d5f8b96545f7)

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, the recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

# Types of Recommendation System :

### 1 ) Content Based :
* Content-based systems, which use characteristic information and takes item attriubutes into consideration .

* Twitter , Youtube .

* Which music you are listening , what singer are you watching . Form embeddings for the features .

* User specific actions or similar items reccomendation .

* It will create a vector of it .

* These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future

* One issue that arises is making obvious recommendations because of excessive specialization (user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).

### 2 ) Collaborative Based :
* Collaborative filtering systems, which are based on user-item interactions.

* Clusters of users with same ratings , similar users .

* Book recommendation , so use cluster mechanism .

* We take only one parameter , ratings or comments .

* In short, collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item, item B, the first user could also be interested in the second item .

* Issues are :

  * User-Item nXn matrix , so computationally expensive .

  * Only famous items will get reccomended .

  * New items might not get reccomended at all .

 ### 3 ) Hybrid Based :
* Hybrid systems, which combine both types of information with the aim of avoiding problems that are generated when working with just one kind.

* Combination of both and used now a days .

* Uses : word2vec , embedding .


# About this project:
This is a streamlit web application that can recommend similar movies based on user interest.

For more details, visit the [Movie Recommender System]( https://movies-recommendation-system-39e01fea8f97.herokuapp.com/).

# Demo:

<img width="1580" alt="Screenshot 2024-11-19 at 1 15 05 AM" src="https://github.com/user-attachments/assets/d5dff040-8abe-44e1-ad92-13ceef23c64c">
<img width="1580" alt="Screenshot 2024-11-19 at 1 20 35 AM" src="https://github.com/user-attachments/assets/d2269902-8244-4678-8b81-d6bbac702e0e">
<img width="1580" alt="Screenshot 2024-11-19 at 1 22 57 AM" src="https://github.com/user-attachments/assets/54d67538-8b8d-4da7-971b-3be83e821634">
<img width="1580" alt="Screenshot 2024-11-19 at 1 27 02 AM" src="https://github.com/user-attachments/assets/6a1ed246-0859-4929-ad8d-a9a49b61360d">


# Dataset been used:
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

# Concept used to build the similarity.pkl file : cosine_similarity
1 . Cosine Similarity is a metric that allows you to measure the similarity of the documents.

2 . In order to demonstrate cosine similarity function we need vectors. Here vectors are numpy array.

3 . Finally, Once we have vectors, We can call cosine_similarity() by passing both vectors. It will calculate the cosine similarity between these two.

4 . It will be a value between [0,1]. If it is 0 then both vectors are complete different. But in the place of that if it is 1, It will be completely similar.

5 . For more details , check URL : https://www.learndatasci.com/glossary/cosine-similarity/
