
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load your pickled models
user_final_rating = pickle.load(open('pickle_file/user_final_rating.pkl', 'rb'))
item_final_rating = pickle.load(open('pickle_file/item_final_rating.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the user input
    user_input = request.form['user_input']
    
    # Perform recommendation logic (for both user and item-based systems)
    user_recommendations = user_final_rating.loc[user_input].sort_values(ascending=False).head(5).index
    item_recommendations = item_final_rating.loc[user_input].sort_values(ascending=False).head(5).index
    
    return render_template('index.html', user_recommendations=user_recommendations, item_recommendations=item_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
