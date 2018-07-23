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