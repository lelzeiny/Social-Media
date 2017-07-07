#import time
class Fremoga:
    def __init__ (self, name):
        #adding characteristics
        self.name = name
        self.age = 13
        self.connect = []
    def born (self, age):
        if age < 13:
            print ("This is a big kid website. Go play outside.")
        else:
            print ("Welcome!")
    def getname (self):
        return self.name
    def addconnect (self, otherUser):
        self.connect.append(otherUser)
    def printconnect (self):
        for i in self.connect:
            print (i)
    def checkconnect (self, againstThis, a): #againstThis is user input, checkConnect makes sure the input is a username
        for i in self.connect:
            if i == againstThis:
                print("Sorry, they are already in your connections")
    def getconnect (self):
        return self.connect
class FremogaNetwork:
    def __init__ (self):
        self.user = []
    def addUser(self, username):
        self.user.append(Fremoga(username))    #list of profiles
    def checkUser (self, username): #Based on imput, plz find name of instance w/ that username
        for i in user:
            if i.getname() == username:
                print (i)

def listChoice ():
    print ("Would you like to:")
    print("a) add a user")
    print("b) add connections")
    print("c) delete conection")
    print("d) print connections")
    print("e) quit program")
    print("Write the letter")


def main():
    Database = FremogaNetwork()
    Tester = Fremoga("Testing")
    print ("Welcome to Fremoga! What is your name?")
    M_name = input()
    MainUser = Fremoga(M_name)
    Database.addUser(M_name)
    print ("Nice to meet you ", M_name, "What is your age?")
    aging = int (input())
    MainUser.born (aging)
    listChoice()
    choice = input()
    if choice == "a":
        print ("Enter a username:")
        one_name = input()
        User1 = Fremoga(one_name)
        Database.addUser(one_name)
        print ("You have now added", one_name, ". Would you like to become friends?")
        print("Type: 'yes' or 'no'")
        IsFriend = input()
        if IsFriend == 'yes':
             User1.addconnect(MainUser)
             MainUser.addconnect(User1)
             print (M_name, "and", one_name, "are now friends!")
        elif IsFriend == 'no':
            listChoice()
        else:
            print ("Please type that again correctly.")
            IsFriend = input()
    elif choice == "b":
        print ("Enter the two users you would like to connect:")
        print ("User 1:")
        marcone = input ()
        User2 = Fremoga(marcone)
        print ("User 2:")
        marctwo = input()
        User3 = Fremoga(marctwo)
        User2.addconnect(marctwo)
        User3.addconnect(marcone)
        User2.printconnect()
    # elif choice == "c":
    elif choice == "d":
        print ("Whose connections would you like to check?")
        checkMe = input()
        #Database.get

    # elif choice == "e":
    else:
        print("Oh no! That is not an input! Please input a letter.")
main()
