# web
a simple currency exchange rate web


## DATA STRUCTURE

### Table currency
| *Field Name*  | *Type*     |
| ------------  |------------|
| id            | Primary Key|
| Name          | Varchar    |
| Description   | Varchar    |


### Table currency_exchange

| *Field Name*      | *Type*                 |
| --------------    | ----------             |
| id                | Primary Key            |
| source_currency   | Foreign Key (currency) |
| target_currency   | Foreign Key (currency) |


### Table currency_exchange_rate_history

| *Field Name*      | *Type*                             |
| ------------------| -----------------------------------|
| id                | Primary Key                        |
| currency_exchange | Foreign Key (currency_exchange)    |
| rate              | Float                              |
| date              | date                               |


# API DOCUMENTATION

### API GET CURRENCY LIST
URL: /api/mvp/currencies

METHOD: GET

Response Example:

    HTTP/1.1 200 OK

    [
        {
            "id": 1,
            "name": "AFN"
        },
        {
            "id": 2,
            "name": "EUR"
        },
    ]

### API GET CURRENCY EXCHANGE LIST
URL: /api/mvp/currency-exchange

METHOD: GET

Response Example:

    HTTP/1.1 200 OK

    [
        {
            "id": 5,
            "source_currency": {
                "id": 2,
                "name": "EUR"
            },
            "target_currency": {
                "id": 1,
                "name": "AFN"
            }
        }
    ]

### API ADD CURRENCY EXCHANGE TO THE LIST TRACK
URL: /api/mvp/currency-exchange/

METHOD: POST

Request Example:

    {
        "source_currency": 1, required (id from API GET CURRENCY LIST)
        "target_currency": 2  required (id from API GET CURRENCY LIST)

    }

Response Example:

    HTTP/1.1 201 CREATED 

    'success add currency exchange to track'

### API REMOVE CURRENCY EXCHANGE FROM LIST TRACK
URL: /api/mvp/currency-exchange/

METHOD: DELETE

Request Example:

    {
        "source_currency": 1, required (id from API GET CURRENCY LIST)
        "target_currency": 2  required (id from API GET CURRENCY LIST)

    }

Response Example:

    HTTP/1.1 202 ACCEPTED

    'success remove currency exchange from track'


### API GET CURRENCY EXCHANGE RATE DAILY
URL: /api/mvp/exchange-track/?date=<YYYY-MM-DD>

METHOD: GET

Response Example:

    HTTP/1.1 200 OK

    [
        {
            "source_currency": "EUR",
            "rate": 1.23456,
            "date": "2018-07-23",
            "target_currency": "AFN",
            "seven_days_average": "insuficient data"
        }
    ]



### API ADD CURRENCY EXCHANGE RATE DAILY
URL: /api/mvp/exchange-track/

METHOD: POST

Request Example:

    {
        "source_currency": 1, #### required (id from API GET CURRENCY LIST)
        "target_currency": 2  #### required (id from API GET CURRENCY LIST),
        "date": "2018-07-18",
        "rate": 1.3456 

    }

Response Example:

    HTTP/1.1 201 CREATED

    'success remove currency exchange from track'
