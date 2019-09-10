import smtplib
import subprocess

def send_mail(ip_str):

	fromaddr = "" #!!!!!!!!

	password = "" #!!!!!!!!

	toaddrs = "" #!!!!!!!!!

	server = smtplib.SMTP("smtp.gmail.com:587")

	server.starttls()

	server.login(fromaddr, password)

	server.sendmail(fromaddr, toaddrs, f"Your IPv4 is {ip_str}.")

def run_cmd(cmd):

	process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)

	output, error = process.communicate()

	if error is not None:

		return error

	else:

		return output


ip = run_cmd("curl ifconfig.me")

ip = str(ip).strip("b")

#send_mail(ip)
