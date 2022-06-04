# import pyrebase
import requests
from gpiozero import Motor

motorright = Motor(17, 18)
motorleft = Motor(22, 23)

'''config = {
    "apiKey": "AIzaSyD6YFZ2kJd7reg_hZ2-HXa1pDfPQ0mohIY",
    "authDomain": "gameofthings-92.firebaseapp.com",
    "databaseURL": "https://gameofthings-92-default-rtdb.firebaseio.com",
    "projectId": "gameofthings-92",
    "storageBucket": "gameofthings-92.appspot.com",
    "messagingSenderId": "137667656555",
    "appId": "1:137667656555:web:e09a74511b374fbfe8ea2e",
    "measurementId": "G-HEWQL7YW9X"
}

firebase = pyrebase.initialize_app(config)
'''

def forward():
    motorright.forward()
    motorleft.forward()

def backward():
    motorright.reverse()
    motorleft.reverse()

def turnRight():
    motorleft.forward()
    motorright.reverse()

def turnLeft():
    motorright.forward()
    motorleft.reverse()

def stop():
    motorright.stop()
    motorleft.stop()

while True:
    # database = firebase.database()
    # value = database.child("Robot").child("Movement").get().val()
    
    url = "http://192.168.1.9:8080/robot/RBT-6052fc99-a076-461d-bd21-eadce9c2a5b0"
    
    value = requests.get(url).text
    
    # print("\n\tThe Movement is: " + value.json())
    
    print(f"Value inside Database is: {value}")
    
    if value == "Forward":
        print("Forward")
        forward()
    elif value == "Backward":
        print("Backward")
        backward()
    elif value == "Right":
        print("Right")
        turnRight()
    elif value == "Left":
        print("Left")
        turnLeft()
    else:
        print("Stop")
        stop()

