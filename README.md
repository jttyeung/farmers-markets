Farmer's Markets
======

Farmer's Markets is a simple API built with data from: [https://catalog.data.gov/dataset/farmers-markets-geographic-data](https://catalog.data.gov/dataset/farmers-markets-geographic-data).



Table of Contents
------
* [Technologies Used](#technology)
* [How Run Farmer's Markets Locally](#run)
* [How To Use The App](#use)
* [Author](#author)
* [License](#license)


## <a name="technology"></a>Tech Stack

<b>Backend:</b> Python, Flask, Flask-RESTful PostgreSQL, PostGIS, SQLAlchemy, GeoAlchemy2<br/>
<b>Frontend:</b> JSON<br/>


## <a name="run"></a>How to Run Farmer's Markets Locally

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.



### Prerequisites

1. Python 2.7.0
2. PostgreSQL



### Installation Instructions
1. Clone this repository:
  ```
  $ git clone https://github.com/jttyeung/farmers-markets.git
  ```

2. Set up a Python virtualenv and activate it.
  ```
  $ virtualenv env
  $ source env/bin/activate
  ```

3. Install all app dependencies listed in requirements.txt.
  ```
  $ pip install -r requirements.txt
  ```

4. Make sure you have PostgreSQL running (psql).
5. Create a database named farmers-markets.
  ```
  $ createdb farmers-markets
  ```

6. Open the database, add the PostGIS database extension, and exit out of the database.
  ```
  $ psql farmers-markets
  ```

  ```
  CREATE EXTENSION postgis;
  \quit
  ```

7. Create tables in your database.
  ```
  $ python model.py
  ```

8. Go into the <kbd>/static/data/</kbd> directory and seed the database using the <kbd>dump.sql</kbd> file.
  ```
  $ cd static/data
  $ psql farmers-markets < dump.sql
  ```

9. Start the Flask server.
  ```
  $ python server.py
  ```

10. Go to localhost:5000 to view the application.


## <a name="use"></a>Usage
To use the app, simply visit one of the REST API endpoints to retrieve data:
* /markets - This will give you data for all the markets in the U.S.
* /markets/<fm_id> - Search data by farmer's market ID.
* /markets/<state_id> - Search data by state ID. -- coming soon!


## <a name="author"></a>Author

Joanne Yeung is a full-stack engineer in San Francisco, CA.
Learn more on LinkedIn: [https://linkedin.com/in/jttyeung](https://linkedin.com/in/jttyeung)



## <a name="license"></a>License

This project is licensed under the [MIT License](LICENSE.md).

