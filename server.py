import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def webcomponent():
    connection = sqlite3.connect('rates.db')
    cursor = connection.execute('SELECT rate FROM rates WHERE currency = "USD" AND base = "EUR";')
    result = cursor.fetchone()
    if result is not None:
        (rate,) = result
        return rate
    else:
        return 'no such currency pair'

if __name__ == "__main__":
    app.run(debug=True)
