import pywhatkit as kit

phone_no = input("\tEnter the Phone Number of the person : ")
message = input("\tEnter the message u what to convey : ")
hour = int(input("\tEnter the Hour : "))
minute = int(input("\tEnter the minute : "))

kit.sendwhatmsg(phone_no, message, hour, minute)
