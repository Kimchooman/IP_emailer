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

		self.current_ip = None

		intitialize_server(self.user,self.password,self.server)

	def send_mail(self):

		self.server.sendmail(self.user, self.user, f"Hello God-san. Your external IP is {self.current_ip}.")
	
	def check_ip(self):

		ip = get('https://api.ipify.org').text

		if ip is not self.current_ip:
			self.current_ip = ip

			self.send_mail()

usr = "------@gmail.com" #!!!!!!!!!!
password = "---------" #!!!!!!!!!!

bot = IP_mailBot(usr, password, usr)

while True:

	time.sleep(60 * 5)
	bot.check_ip()
