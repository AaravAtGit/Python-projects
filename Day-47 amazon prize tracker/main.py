import requests
import bs4
import lxml
import smtplib




key = "hglqqxyiojlzrlrr"
email = "aaravshishodia5029@gmail.com"
send = "aarav54897@gmail.com"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

link = "https://www.amazon.in/Intel-i7-3770-Processor-Turbo-3-90GHz/dp/B09PMLW3ZZ/ref=sr_1_4?crid=3V6HR7LRK0PMY&keywords=i7&qid=1654321729&s=computers&sprefix=i7%2Ccomputers%2C1499&sr=1-4"
r = requests.get(link, headers=header)
html = r.text
# print(html)

soup = bs4.BeautifulSoup(html,"lxml")

price_span = soup.find(name="span",class_="a-price-whole")

price = price_span.getText()

price = price.replace(",","")
price = price.replace(".","")
price = int(price)


title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 4500

if price < BUY_PRICE:
    message = f"{title} is now {price}"
    message.encode("utf-8")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(email, key)
        connection.sendmail(
            from_addr=email,
            to_addrs=send,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{link}".encode("utf-8")
        )
