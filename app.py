
from flask import Flask, request, render_template
import os
from model import get_user_recommendations, get_item_recommendations  # Import functions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '')

    user_recommendations = []
    item_recommendations = []

    if user_input:
        user_recommendations = get_user_recommendations(user_input)
        item_recommendations = get_item_recommendations(user_input)

    return render_template('index.html', user_recommendations=user_recommendations, item_recommendations=item_recommendations)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
