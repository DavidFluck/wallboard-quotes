import csv
import random

from flask import render_template
from app import app

quote_list = []

@app.route('/quotes')
def index():
    quote_dict = random_quote()
    return render_template('index.html', quote = quote_dict['quote'], author = quote_dict['author'])

def random_quote():
    with open('quotes.csv', mode = 'r') as quote_file:
        quote_list = []
        reader = csv.reader(quote_file, delimiter=",", quotechar='"')
        for row in reader:
            quote_list.append({'quote': row[0],
                               'author': row[1]})
        return random.choice(quote_list)
