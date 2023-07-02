from db import db
from userInterface import UserInterface

filename = "data.json"
base = db(filename)
userInterface = UserInterface(base)
while userInterface.userHere:
    userInterface.start()
base.saveDatabase(filename)
