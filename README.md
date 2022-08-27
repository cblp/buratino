# Project buratino

## Create database

```sh
$ sqlite3 rates.db '.read schema.sql'
```

## Add currency pair to database

```sql
INSERT INTO rates
    (currency, base, rate) VALUES ("USD", "EUR", 0.99)
    ON CONFLICT DO UPDATE SET rate = 0.99;
```

## Get all rates from the database

```sql
SELECT * FROM rates;
```

## Get currency pair from the database

```sql
SELECT rate FROM rates WHERE currency = 'USD' AND base = "EUR";
```

```py
import sqlite3

connection = sqlite3.connect('db.sqlite')
cursor = connection.execute('SELECT rate FROM rates WHERE currency = "USD" AND base = "EUR";')
result = cursor.fetchone()
if result is not None:
    (rate,) = result
else:
    # no such currency pair
```
