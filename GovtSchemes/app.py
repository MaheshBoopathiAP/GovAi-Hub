from flask import Flask, request, jsonify, render_template
import pandas as pd
import spacy

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('CenterSectorScheme2021-22.csv')

# Load spaCy NLP model
nlp = spacy.load('en_core_web_sm')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()

    if not query:
        return jsonify({"error": "Please provide a query parameter."})

    # Use spaCy NLP to process the query
    doc = nlp(query)

    # Extract keywords (nouns, proper nouns, and adjectives) from the query
    keywords = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN', 'ADJ']]

    if not keywords:
        return jsonify({"error": "No relevant keywords found in the query."})

    # Perform filtering based on extracted keywords
    search_mask = pd.Series([True] * len(df))  # Default True for all rows
    for keyword in keywords:
        search_mask &= df['Scheme'].str.lower().str.contains(keyword, na=False)

    # Get the filtered results
    results = df[search_mask]

    if results.empty:
        return jsonify({"message": "No schemes found matching the query."})

    # Convert the filtered results to JSON format
    response = results[['Category', 'Ministry/Department', 'Scheme']].to_dict(orient='records')

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
