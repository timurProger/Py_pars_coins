#!C:\Users\asd\AppData\Local\Programs\Python\Python36-32\pythonw.exe
#империя https://www.reviewdetector.ru/index.php?showforum=69&prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all&st=
#советы https://www.reviewdetector.ru/index.php?showforum=70&prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all&st=
import smtplib
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import urllib.request
from bs4 import BeautifulSoup
import xml.etree.ElementTree as xml
import lxml.etree as ET
from lxml import etree
import re
from sys import getdefaultencoding
from datetime import datetime, date, time

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()
def get_soup(hrefs):
	soups = []
	for i in range(len(hrefs)):
		html = get_html(hrefs[i])
		soup = BeautifulSoup(html,'html.parser')
		soups.append(soup)
	return soups

def currentNumber():
	day = datetime.today() 
	day = str(day.date())
	mon = day[8:]
	date_num = day[5:7]
	full_date = mon + '.' + date_num;
	return full_date

def sendSovet():

	subject = "Советы"
	body = "This is an email with attachment sent from Python"
	sender_email = "timurahaha@gmail.com"
	receiver_email = "igorch1@mail.ru"
	password = "tim9162001"
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	sovet = "sovet.html"

	# Open html file in binary mode
	with open(sovet, "rb") as attachment:
		# Add file as application/octet-stream
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)
	#encoders.encode_base64()

	# Add header as key/value pair to attachment part
	part.add_header(
		"Content-Disposition",
		f"attachment; filename = {sovet};"

	)	

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Localg in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)


def sendImper():
	subject = "Имперцы"
	body = "This is an email with attachment sent from Python"
	sender_email = "timurahaha@gmail.com"
	receiver_email = "igorch1@mail.ru"
	password = "tim9162001"
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	imper = "imper.html"  # In same directory as script
	

	# Open html file in binary mode
	with open(imper, "rb") as attachment:
		# Add file as application/octet-stream
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)
	#encoders.encode_base64()

	# Add header as key/value pair to attachment part
	part.add_header(
		"Content-Disposition",
		f"attachment; filename = {imper};"

	)	

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Localg in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)

def sendZolotaia():
	subject = "Чешуя"
	body = "This is an email with attachment sent from Python"
	sender_email = "timurahaha@gmail.com"
	receiver_email = "igorch1@mail.ru"
	password = "tim9162001"
	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	message["Subject"] = subject
	message["Bcc"] = receiver_email  # Recommended for mass emails

	# Add body to email
	message.attach(MIMEText(body, "plain"))

	Zolotaia_orda = "Zolotaia_orda.html"  # In same directory as script
	

	# Open html file in binary mode
	with open(Zolotaia_orda, "rb") as attachment:
		# Add file as application/octet-stream
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())

	# Encode file in ASCII characters to send by email    
	encoders.encode_base64(part)
	#encoders.encode_base64()

	# Add header as key/value pair to attachment part
	part.add_header(
		"Content-Disposition",
		f"attachment; filename = {Zolotaia_orda};"

	)	

	# Add attachment to message and convert message to string
	message.attach(part)
	text = message.as_string()

	# Localg in to server using secure context and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, text)	




















def main():
	imp_sov = ['https://www.reviewdetector.ru/index.php?showforum=69&prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all&st=', 'https://www.reviewdetector.ru/index.php?showforum=70&prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all&st=',
	'https://www.reviewdetector.ru/index.php?showforum=68&prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all&st=0']
	forum_name = ['imper.html','sovet.html','Zolotaia_orda.html']
	for q in range (3):
		currentNumber();
		userDate = currentNumber()
		allPages = []
		page = 0
		for i in range(10):
			url1 = imp_sov[q]+str(page)
			text = parse(get_html(url1))
			result = sortHrefs(text, userDate)
			allPages +=result
			page+=30
		soups = get_soup(allPages)
		description =  showInfo(soups)
		pictures = showInfo1(soups)
		lot_price = showPrice(soups)
		createXML(description,allPages,pictures,lot_price)
		CuteXML(forum_name[q])
	sendImper()
	sendSovet()
	sendZolotaia()







def parse(html):
	hrefs = []
	soup = BeautifulSoup(html, 'html.parser')
	text = soup.find_all(valign = 'middle', class_ = 'row2')
	for href in text:
		a = href.find_all(href!="#")
		hrefs.append(a)
	return hrefs

def sortHrefs(arr,date):
	chek = []
	hrefsId = []
	for elem in arr:
		elem = str(elem)
		a = elem.find("hint")
		b = elem.find(date)
		if b != -1: 
			elem ="https://www.reviewdetector.ru/index.php?showtopic=" + elem[a+4:a+11]
			elem = str(elem)
			hrefsId.append(elem)

	return hrefsId

def showInfo(soups):
	description = []
	for i in range (len(soups)):
		text = soups[i].find(class_ = "maintitle")
		text = str(text)
		text = text[32:]
		lastId = text.find('окончание')
		text = text[:lastId+26]
		text = re.sub(r'</b>,','  ',text)
		description.append(text)
	return description

def showInfo1(soups):
	pics = []
	spl = []
	for i in range(len(soups)):
		pic_wall = soups[i].find(class_="postcolor")
		pic_wall = str(pic_wall)
		soup1 = BeautifulSoup(pic_wall,'lxml')
		pic = soup1.select("a")
		pics.append(pic)
	return pics

def showPrice(soups):
	prices = []
	for ui in range(len(soups)):
		postcolor = soups[ui].find_all(class_="postcolor")
		last_pr = len(postcolor)
		prices.append(postcolor[last_pr-1])
	return prices






def createXML(title,lotsHrefs,pics,last_prices):
	"""
	Создаем XML файл.
	"""
	filename = "loots1.xml"
	root = xml.Element("ROOT")
	appt = xml.Element("Lots")
	root.append(appt)	
	# Data of lots
	for i in range (len(title)):
		page_pic = []
		Order = xml.SubElement(appt,"lot")
		description = xml.SubElement(Order,"description")
		description.text = title[i]
		hrefs = xml.SubElement(Order,"link")
		hrefs.text = lotsHrefs[i]
		#creating pictures---------------------------------------
		for q in range(2):
			try:
				current = pics[i][q]
			except IndexError:
				current = "src = asasdasd.jpg"

			current = str(current)
			aleft = current.find("<")
			aright = current.rfind("\">")
			current = current[aleft+9:]
			find_rew = current.find("www.reviewdetector.ru")
			if find_rew!=-1:
				pc_id =current.find("id=") 
				find_target = current.find("target")
				current = "https://www.reviewdetector.ru/index.php?act=Attach&type=post&id="+current[pc_id+3:find_target-2]
			else:
				find_src = current.find("src")
				find_jpg = current.find("jpg")
				current = current[find_src+5:find_jpg+3]
			page_pic.append(current)

		last_price = str(last_prices[i])
		find_pr_l = last_price.find("\">")
		find_pr_r = last_price.find("<!")
		last_price = last_price[find_pr_l+2:find_pr_r]
		if len(last_price)>7:
			last_price = "Ставок еще нет"
		xml_priec = xml.SubElement(Order,"Bet")
		xml_priec.text = str(last_price)

		xmlpic1 = xml.SubElement(Order,"picture1")
		xmlpic1.text = str(page_pic[0])
		xmlpic2 = xml.SubElement(Order,"picture2")
		xmlpic2.text = str(page_pic[1])


	tree = xml.ElementTree(root)
	#with open(filename, "w") as fh:
	tree.write(filename,encoding="UTF-8")
 
def CuteXML(forum_name):
	getdefaultencoding()
	data = open('C:\\xampp\\htdocs\\pars\\pars.xslt')
	xslt_content = data.read()
	#xslt_content = etree.tostring(xslt_content)
	xslt_content= xslt_content.encode()
	xslt_root = etree.XML(xslt_content)
	#xslt_root = etree.tostring(xslt_root)
	dom = etree.parse('C:\\xampp\\htdocs\\pars\\loots1.xml')
	transform = etree.XSLT(xslt_root)
	result = transform(dom)
	f = open('C:\\xampp\\htdocs\\pars\\' + forum_name, 'w')
	f.write(str(result))
	f.close()



if __name__ == '__main__':
	main()

