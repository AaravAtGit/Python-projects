import bs4
import requests

r = requests.get("https://www.timeout.com/film/the-100-best-bollywood-movies-the-list")
Html = r.text

scrape = bs4.BeautifulSoup(Html, "html.parser")
movies = scrape.find_all(name="h3", class_="_h3_cuogz_1")

with open("moves.txt","a") as f:
    for movie in movies:
        text = movie.getText()
        text = text.replace("$nbsp","")
        f.write(f"{text}\n")
