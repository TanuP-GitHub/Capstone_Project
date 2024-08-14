
import pickle
import numpy as np

# Load your pickled models
user_final_rating = pickle.load(open('pickle_file/user_final_rating.pkl', 'rb'))
item_final_rating = pickle.load(open('pickle_file/item_final_rating.pkl', 'rb'))

def get_user_recommendations(user_input):
    """
    Given a user ID, return the top 5 product recommendations based on user-based collaborative filtering.
    """
    try:
        recommendations = user_final_rating.loc[user_input].sort_values(ascending=False).head(5).index
        return recommendations.tolist()
    except KeyError:
        return ["No user found"]

def get_item_recommendations(item_input):
    """
    Given a product ID, return the top 5 product recommendations based on item-based collaborative filtering.
    """
    try:
        recommendations = item_final_rating.loc[item_input].sort_values(ascending=False).head(5).index
        return recommendations.tolist()
    except KeyError:
        return ["No items found"]
