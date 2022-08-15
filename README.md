# wsb_nltk
Scrape the world's most intelligent subreddit!


# Setup
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/elgizabbasov/wsb_nltk.git
$ cd wsb_nltk
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv myenv
$ source myenv/bin/activate
```

Then install the dependencies:

```sh
(myenv)$ pip install -r requirements.txt
```

Note the `(myenv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Then run the following to view the top 10 mentioned tickers in a graph and the most mentioned ticker according to the last 500 HOT posts in WSB:

```sh
(myenv)$ python ticker_scraper_wsb.py
```
