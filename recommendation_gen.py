from datetime import datetime, timezone
import pandas as pd
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# User data
users = [
    {"user_id": 1, "birth_year": 1990, "country": "Italy", "currency": "EUR", "registration_date": "2022-03-01T00:00:00"},
    {"user_id": 2, "birth_year": 1985, "country": "Germany", "currency": "EUR", "registration_date": "2022-03-01T00:00:00"},
    {"user_id": 3, "birth_year": 1995, "country": "Spain", "currency": "EUR", "registration_date": "2022-03-01T00:00:00"}
]

# Event data
events = [
    {"event_id": "E001", "league": "Premier League", "sport": "Football", "country": "England", "begin_timestamp": "2022-04-10 15:00:00+00:00", "end_timestamp": "2022-04-10 17:00:00+00:00", "participants": ["Liverpool", "Chelsea"]},
    {"event_id": "E002", "league": "La Liga", "sport": "Football", "country": "Spain", "begin_timestamp": "2022-04-10 20:00:00+02:00", "end_timestamp": "2022-04-10 22:00:00+02:00", "participants": ["Real Madrid", "Barcelona"]},
    {"event_id": "E003", "league": "Serie A", "sport": "Football", "country": "Italy", "begin_timestamp": "2022-04-12 21:00:00+02:00", "end_timestamp": "2022-04-12 23:00:00+02:00", "participants": ["Juventus", "AC Milan"]}
]

# Coupon data
coupons = [
{"coupon_id": "C001", "selections": [{"event_id": "E001", "odds": 2.0}], "stake": 10.0, "timestamp": "2022-04-08T09:30:00", "user_id": 1},
{"coupon_id": "C002", "selections": [{"event_id": "E002", "odds": 1.5}, {"event_id": "E003", "odds": 2.0}], "stake": 5.0, "timestamp": "2022-04-08T10:30:00", "user_id": 2},
{"coupon_id": "C003", "selections": [{"event_id": "E003", "odds": 2.5}], "stake": 20.0, "timestamp": "2022-04-08T11:30:00", "user_id": 3},
]



# Load the data into pandas dataframes
users_df = pd.DataFrame(users)
events_df = pd.DataFrame(events)
coupons_df = pd.DataFrame(coupons)

# Convert the timestamp strings to datetime objects
events_df['begin_timestamp'] = events_df['begin_timestamp'].apply(lambda x: datetime.fromisoformat(x[:-6]))
events_df['end_timestamp'] = events_df['end_timestamp'].apply(lambda x: datetime.fromisoformat(x[:-6]))
coupons_df['timestamp'] = coupons_df['timestamp'].apply(lambda x: datetime.fromisoformat(x))

# Join the dataframes to create a single table
data = pd.merge(coupons_df, events_df, on='event_id', how='left')
data = pd.merge(data, users_df, on='user_id', how='left')

# Group the data by user_id and create a list of events they have bet on
user_events = data.groupby('user_id')['league'].apply(list).reset_index(name='events')

# Create a CountVectorizer object to convert the events list into a matrix of word frequencies
cv = CountVectorizer()
event_matrix = cv.fit_transform(user_events['events'].apply(lambda x: ' '.join(x)))

# Calculate the cosine similarity between event vectors
similarity_matrix = cosine_similarity(event_matrix)

# Define a function to recommend events to a user based on the similarity matrix
def recommend_events(user_id, num_recommendations=3):
    # Get the index of the user in the similarity matrix
    user_index = user_events[user_events['user_id'] == user_id].index[0]
    # Get the similarity scores between the user and all other users
    user_similarities = similarity_matrix[user_index]
    # Get the indices of the most similar users
    most_similar_users = user_similarities.argsort()[::-1][1:num_recommendations+1]
    # Get the events that the most similar users have bet on
    recommended_events = data[data['user_id'].isin(most_similar_users)]['event_id'].unique().tolist()
    # Return the recommended events
    return recommended_events
