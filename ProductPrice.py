import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Beats-Wireless-Noise-Cancelling-Headphones-Bluetooth/dp/B07YVZ15SG?ref_=Oct_DLandingS_D_ec41923b_61&smid=ATVPDKIKX0DER'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()

    dealprice = 0
    dealprice = soup.find(id="priceblock_dealprice").get_text().strip()
    if dealprice:
        converted_price = float(dealprice[1:])

    orig_price = 0
    if converted_price:
        orig_price = converted_price
    originalprice = soup.find("span", {"class": "priceBlockStrikePriceString a-text-strike"}).get_text().strip()
    if(originalprice):
        orig_price = float(originalprice[1:])

    if(converted_price < (orig_price * 0.75)):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pulusu.avinash26@gmail.com', 'iuqtvpfqitiowtes')

    subject = 'Price dropped to less than 75%! Wanna buy now?'
    body = 'Check the Amazon link : https://www.amazon.com/Beats-Wireless-Noise-Cancelling-Headphones-Bluetooth/dp/B07YVZ15SG?ref_=Oct_DLandingS_D_ec41923b_61&smid=ATVPDKIKX0DER'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'pulusu.avinash26@gmail.com',
        'pulusu123456@gmail.com',
        msg
    )
    server.quit()


check_price()
