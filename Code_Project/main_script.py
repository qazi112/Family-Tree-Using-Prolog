
from pyswip import Prolog
prolog=Prolog()
prolog.consult("back_end_prolog.pl")


def display():
    print("*****************************************************************")
    print("*\t\t\t\t\t\t\t\t*\n*FUNCTIONS/QUERIES:\t\t\t\t\t\t*\n*\t\t\t\t\t\t\t\t*")
    print("*Enter 1 for Beti", "Enter 2 for Beta\t\t\t\t*",sep="------")
    print("*Enter 3 for Dada", "Enter 4 for Nana\t\t\t\t*", sep="------")
    print("*Enter 5 for Dadi", "Enter 6 for Nani\t\t\t\t*", sep="------")
    print("*Enter 7 for Sala", "Enter 8 for Bahu\t\t\t\t*", sep="------")
    print("*Enter 9 for Pota", "Enter 10 for Nawasa\t\t\t*", sep="------")
    print("*Enter 11 for BaapDada", "Enter 12 for Khala\t\t\t*", sep="------")
    print("*Enter 13 for Pota", "Enter 0 for Exit\t\t\t*\n*\t\t\t\t\t\t\t\t*", sep="------")
    print("*****************************************************************")

def membersOfKhanFamily():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+\t\t\t\t\t\t\t\t+\n+Members of Khan Family:\t\t\t\t\t+\n+\t\t\t\t\t\t\t\t+")
    print("+ChoteKhan, ChotiRani, BarreKhan, BarriRani\t\t\t+")
    print("+Salim, Kausar, Nadir, Asad, Nahid, Sumra\t\t\t+")
    print("+Rizwan, Burhan, Rashid, Akram, Salima, Sanam, Rabia\t\t+")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

def decisionToContinue():
        while(True):
            decision = input("\n----------> Enter Y to Continue and N to Stop <----------\n")
            if decision == "Y" or decision == "y":
                return True
            elif decision == "N"  or decision == "n":
                return False
            else:
                print("----------> Invalid Choice ! <----------\n")  


def main():
    print("*****************************************************************")
    print("*\t\t\t\t\t\t\t\t*\n*--------------------- (: WELL COME :) -------------------------*\n*\t\t\t\t\t\t\t\t*")

    number = None
    exist = False

    while(number!=0):
        display()    
        while True: 
            valid_choices = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13"}
            number=input("\n---> Enter your Choice for the Relationship that you are interested in <---\n")
            if number in valid_choices:
                number = int(number)
                break
            else:
                print("\n--->Invalid Choice :( ")
                continue
        if(number==1):
            membersOfKhanFamily()
            Y=input("Enter name of person whose Beti is required : ")
            Y=Y.lower()
            for val in prolog.query("beti(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Ms.{0} is the beti of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==2):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Beta is required : ")
            Y=Y.lower()
            for val in prolog.query("beta(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the beta of {1}.".format(val["X"], Y))
                print("============================================================")

        if(number==3):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Dada is required : ")
            Y=Y.lower()
            for val in prolog.query("dada(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the dada of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==4):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Nana is required : ")
            Y=Y.lower()
            for val in prolog.query("nana(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the nana of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==5):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Dadi is required : ")
            Y=Y.lower()
            for val in prolog.query("dadi(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Ms.{0} is the dadi of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==6):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Nani is required : ")
            Y=Y.lower()
            for val in prolog.query("nani(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Ms.{0} is the nani of {1}.".format(val["X"], Y))
                print("============================================================")
            
        if(number==7):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Sala is required : ")
            Y=Y.lower()
            for val in prolog.query("sala(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the sala of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==8):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Bahu is required : ")
            Y=Y.lower()
            for val in prolog.query("bahu(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Ms.{0} is the bahu of {1}.".format(val["X"], Y))
                print("============================================================")
                

        if(number==9):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Pota is required : ")
            Y=Y.lower()
            for val in prolog.query("pota(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the pota of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==10):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Nawasa is required : ")
            Y=Y.lower()
            for val in prolog.query("nawasa(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the nawasa of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==11):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose BaapDada is required : ")
            Y=Y.lower()
            for val in prolog.query("baapDada(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the baapDada of {1}.".format(val["X"], Y))
                print("============================================================")
                
        if(number==12):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose Khala is required : ")
            Y=Y.lower()
            for val in prolog.query("khala(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Ms.{0} is the khala of {1}.".format(val["X"], Y))
                print("============================================================")
                

        if(number==13):
            membersOfKhanFamily()  
            Y=input("Enter name of person whose ChachaTaya is required : ")
            Y=Y.lower()
            for val in prolog.query("chachataya(X,"+Y+")"):
                exist = True
                print("\n============================================================")
                print("Mr.{0} is the chachataya of {1}.".format(val["X"], Y))
                print("============================================================")

        if exist == False:
            print("\n============================================================")
            print("Relationship does't Exist or Invalid Input.")
            print("============================================================")

        if decisionToContinue() == True:
            continue
        else:
            break
    print("\n\n===================> Thank You for Coming :) <=====================\n")
        

if __name__=="__main__":
    main()
