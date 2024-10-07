from flask import Flask, render_template, request, redirect, url_for
import csv
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

# Route for the complaint submission page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        complaint = request.form['complaint']
        sector = request.form['sector']

        # Perform sentiment analysis and get both score and label
        sentiment_score, sentiment = analyze_sentiment(complaint)

        # Store complaint, sector, sentiment score, and sentiment label in CSV file
        with open('complaints.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([complaint, sector, sentiment_score, sentiment])

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    # Create the CSV file with headers if it doesn't exist
    try:
        with open('complaints.csv', mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Complaint', 'Sector', 'Sentiment Score', 'Sentiment'])
    except FileExistsError:
        pass

    app.run(debug=True, port=5050)
