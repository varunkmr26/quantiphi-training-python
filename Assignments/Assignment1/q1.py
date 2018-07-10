import re
import logging
logging.basicConfig(filename='logfile-q1.log',level=logging.DEBUG)

#Validate Function
def validate(s):
	if not re.search("[A-Z]",s):
		logging.warning('This string does not have capital letters')
		pass
	elif not re.search("[a-z]",s):
		logging.warning('This string does not have lower letter')
		pass
	elif not re.search("[0-9]",s):
		logging.warning('This string does not have numerical characters')
		pass
	elif not re.search("[$#@]",s):
		logging.warning('This string does not have desired special characters')
		pass
	elif (len(s)<6 or len(s)>12):
		logging.warning('This is not a valid password')
		pass
	else:
		print("valid")
		logging.info('This is a valid password')
		return
	print ("not valid")
	logging.warning('This is not a valid password')
	return

#Main Function
def main():
	s = raw_input("Please enter a string to validate: ")
	validate(s)

#Calling the main function
main()
