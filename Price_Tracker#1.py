import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL_1 = 'https://www.amazon.in/Microsoft-Touchscreen-Integrated-Graphics-1769/dp/B07N16C7QT/ref=lp_21345040031_1_20?s=computers&ie=UTF8&qid=1589612430&sr=1-20'
URL_2 = 'https://www.amazon.in/dp/B083PFZXC4/ref=psdc_1375424031_t1_B07N16C7QT'
URL_3 = 'https://www.amazon.in/dp/B073Q5R6VR/ref=psdc_1375424031_t2_B07N16C7QT'
URL_4 = 'https://www.amazon.in/dp/B07V6SHBJP/ref=psdc_1375424031_t3_B07N16C7QT'

headers = {
	"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

lastknown_price_1 = 93999.0
lastknown_price_2 = 79990.0
lastknown_price_3 = 65990.0
lastknown_price_4 = 109900.0
def check_price():
	page_1 = requests.get(URL_1, headers=headers)
	soup_1 = BeautifulSoup(page_1.content,'html.parser')
	title_1 = soup_1.find(id="productTitle").get_text()
	price_1 = soup_1.find(id="priceblock_ourprice").get_text()
	string_price_1 = price_1[2:]
	string_price_1 = string_price_1.replace(',', '')
	converted_price_1 = float(string_price_1)
	difference_price_1 = lastknown_price_1 - converted_price_1

	if(difference_price_1>0):
		send_mail_1()
	elif(difference_price_1<0):
		send_mail_2()

	print(title_1.strip())
	print(converted_price_1)

	page_2 = requests.get(URL_2, headers=headers)
	soup_2 = BeautifulSoup(page_2.content,'html.parser')
	title_2 = soup_2.find(id="productTitle").get_text()
	price_2 = soup_2.find(id="priceblock_ourprice").get_text()
	string_price_2 = price_2[2:]
	string_price_2 = string_price_2.replace(',', '')
	converted_price_2 = float(string_price_2)
	difference_price_2 = lastknown_price_2 - converted_price_2

	if(difference_price_2>0):
		send_mail_3()
	elif(difference_price_2<0):
		send_mail_4()

	print(title_2.strip())
	print(converted_price_2)

	page_3 = requests.get(URL_3, headers=headers)
	soup_3 = BeautifulSoup(page_3.content,'html.parser')
	title_3 = soup_3.find(id="productTitle").get_text()
	price_3 = soup_3.find(id="priceblock_ourprice").get_text()
	string_price_3 = price_3[2:]
	string_price_3 = string_price_3.replace(',', '')
	converted_price_3 = float(string_price_3)
	difference_price_3 = lastknown_price_3 - converted_price_3

	if(difference_price_3>0):
		send_mail_5()
	elif(difference_price_3<0):
		send_mail_6()

	print(title_3.strip())
	print(converted_price_3)

	page_4 = requests.get(URL_4, headers=headers)
	soup_4 = BeautifulSoup(page_4.content,'html.parser')
	title_4 = soup_4.find(id="productTitle").get_text()
	price_4 = soup_4.find(id="priceblock_ourprice").get_text()
	string_price_4 = price_4[2:]
	string_price_4 = string_price_4.replace(',', '')
	converted_price_4 = float(string_price_4)
	difference_price_4 = lastknown_price_4 - converted_price_4

	if(difference_price_4>0):
		send_mail_7()
	elif(difference_price_4<0):
		send_mail_8()

	print(title_4.strip())
	print(converted_price_4)

def send_mail_1():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Fell Down'
	body = 'https://www.amazon.in/Microsoft-Touchscreen-Integrated-Graphics-1769/dp/B07N16C7QT/ref=lp_21345040031_1_20?s=computers&ie=UTF8&qid=1589612430&sr=1-20'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()

def send_mail_2():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Rised Up'
	body = 'https://www.amazon.in/Microsoft-Touchscreen-Integrated-Graphics-1769/dp/B07N16C7QT/ref=lp_21345040031_1_20?s=computers&ie=UTF8&qid=1589612430&sr=1-20'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()


def send_mail_3():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Fell Down'
	body = 'https://www.amazon.in/dp/B083PFZXC4/ref=psdc_1375424031_t1_B07N16C7QT'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()

def send_mail_4():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Rised Up'
	body = 'https://www.amazon.in/dp/B083PFZXC4/ref=psdc_1375424031_t1_B07N16C7QT'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()


def send_mail_5():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Fell Down'
	body = 'https://www.amazon.in/dp/B073Q5R6VR/ref=psdc_1375424031_t2_B07N16C7QT'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()

def send_mail_6():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Rised Up'
	body = 'https://www.amazon.in/dp/B073Q5R6VR/ref=psdc_1375424031_t2_B07N16C7QT'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()


def send_mail_7():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Fell Down'
	body = 'https://www.amazon.in/dp/B07V6SHBJP/ref=psdc_1375424031_t3_B07N16C7QT'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()

def send_mail_8():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('mydevprojects.soumi@gmail.com', 'qlhhppdqceomrecx')

	subject = 'Price Rised Up'
	body = 'https://www.amazon.in/dp/B07V6SHBJP/ref=psdc_1375424031_t3_B07N16C7QT'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
	   'mydevprojects.soumi@gmail.com',
	   'dev.soumallya@gmail.com',
	   msg
		)
	print('EMAIL HAS BEEN SENT!')

	server.quit()

while(True):
	check_price()
	time.sleep(60*60*24)

