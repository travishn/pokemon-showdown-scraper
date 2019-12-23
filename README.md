# Pokemon Showdown Webscraper

## Overview
A simple script that grants direct access to basic data on Generation 1 to 7 Pokemon through Selenium web scraping. Data is generated and organized into CSV files, which can be then used in various ways such as creation of a database for use on a personal project.

![](https://res.cloudinary.com/emanon/image/upload/c_scale,h_600,w_1000/v1533412224/todos-21-iniciais-shiny-6-ivs-pokemon-sun-moon-ou-ultra-D_NQ_NP_629320-MLB26464649284_112017-F.jpg)

## Getting Started
First install the necessary packages in your terminal:
```
$ pip install -r req.txt
```
Simply run the script via "python scraper.py" and watch Selenium scrape data from Pokemon Showdown for you!
```
$ python scraper.py
```
![](./scrape-example.gif)

## Note
You can dictate which generation of pokemon data you are scraping by altering the numbers on line 15 of the scraper script. This simply slices out the names of the pokemon_names data array.

```python
for name in pokemon_names[721:807]:
```
```python
Generation 1: [0:151]
Generation 2: [151:251]
Generation 3: [251:386]
Generation 4: [386:493]
Generation 5: [493:649]
Generation 6: [649:721]
Generation 7: [721:807]
```
If you decide to separate the data by Pokemon Generation, be sure to change the path that the file is opening on line 9 accordingly. For instance, if you are scraping for Generation 4:

```python
file = open("./pokemon-data/pokemon-gen4-data.csv", 'w')
```
