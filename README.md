# Top Charts
Aggregator of music charts of different radio stations\.
**Django 3.1** + **sqlite3** + **PostgreSQL** + **Docker** + **DjangoRestFramework** + **BeautifulSoup** + **custom html+css**.

Implemented data collection (parsing radio station chats) 
by running run_scraping.py file in the root of the project.
The script collects charts on the added stations and puts 
into the database through Django models.\
Configured admin panel and rewrote its design (css).
Implemented **DjangoRestFramework** API with basic features.

Added docker-compose and Dockerfile. 
You can build a container with this project and use postgresql as a database.\
Create a django superuser with the default name and password `Admin` {\.
Build an image and run it:\
`docker-compose up -d --build`.

It's possible to work with an internal sqlite database without docker: \
`python manage.py runserver

The home page is a card with the name of the station. 
If you hover over it - the card unfolds and on the back side 
fresh chart in abbreviated form (top 5) and a caption how many days ago 
it was updated. When you click on the card you are redirected to a page 
with a choice of chart for previous weeks of the given station.

![](top_charts.gif)

##TODO:
  * add user registration,
  * automate start of data collection,
  * write errors in the log,
  * implement subscription to updated charts,
  * implement a form for adding a chart of the desired station,
  * write tests,
  * add stations and chart parsers (record, hitfm, ...),
  * expand the database
    * expand models (e.g. url of a radio station),
    * add models (e.g. countries and genres),
    * add a ParseError model and record parsing errors,
  * work on the front end,
  * expand API capabilities (add permissions and queries).
