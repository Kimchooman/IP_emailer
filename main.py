from requests import get
import smtplib
import subprocess
import imaplib
import time

def intitialize_server(user,password,obj):
	obj.starttls()
	obj.login(user,password)

class IP_mailBot:

	def __init__(self, user, password, recipient):

		self.user = user
		self.password = password
		self.recipient = recipient

		self.server = smtplib.SMTP("smtp.gmail.com:587")

		file1 = open("ip.txt","r")
		self.current_ip = file1.read()

		print(self.current_ip)

		intitialize_server(self.user,self.password,self.server)

	def send_mail(self):

		self.server.sendmail(self.user, self.user, f"Hello your external IP is {self.current_ip}.")
	
	def check_ip(self):

		ip = get('https://api.ipify.org').text

		if self.current_ip.find(ip) is -1:
			self.current_ip = ip

			file1 = open("ip.txt","w")
			file1.write(ip)

			self.send_mail()

usr = "---------"
password = "----------"

bot = IP_mailBot(usr, password, usr)

while True:

	bot.check_ip()
	time.sleep(60 * 1)
