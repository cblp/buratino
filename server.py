import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def webcomponent():
    connection = sqlite3.connect('rates.db')
    cursor = connection.execute('SELECT currency, base, rate FROM rates')
    result = cursor.fetchall()
    return (
        """
            <table border=1>
                <tr>
                    <td>currency</td>
                    <td>  base  </td>
                    <td>  rate  </td>
                </tr>
        """ 
        +
        ''.join([
            f"<tr> <td>{currency}</td> <td>{base}</td> <td>{rate}</td> </tr>" 
            for currency, base, rate in result
        ]) 
        + 
        """
            </table>
        """
    )

if __name__ == "__main__":
    app.run(debug=True)
