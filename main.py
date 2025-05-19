import pywhatkit as pwk

phone_number = "<<mobile no u want to send message>>"
message = "Hello, this is an automated message sent using Python!"

# Time at which u want to send the message
pwk.sendwhatmsg(phone_number, message, time_hour=8, time_min=5)