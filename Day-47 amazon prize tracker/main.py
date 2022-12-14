import requests
import bs4
import lxml
import smtplib




key = "your app pass"
email = "email"
send = "email to send on "

header = {
    "User-Agent": "device headers",
    "Accept-Language": "device headers"
}

link = "link of the thing you want to keep an eye on"
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

BUY_PRICE = "your buy price"

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
