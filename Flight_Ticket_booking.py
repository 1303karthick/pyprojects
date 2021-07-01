#Flight Ticket Booking
import random


FlightChoice_dict = {1: ["Economy", 350, 20], 2: ["Business Class", 500, 10], 3: ["Premium Business Class", 850,10]}

def FlightInput(Flightinput,FromLocation ,temp2):
    if Flightinput == 1:
        c = temp2[Flightinput - 1].index(FromLocation)
        # t2.pop(c)
        temp2_u = temp2[Flightinput - 1]
        temp2_u.pop(c)
        print("Available routes from {} are {} ".format(FromLocation, temp2_u).upper())
        ToLocation = input("To :").lower()
    else:
        print("Available routes from {} are {} ".format(FromLocation, temp2[Flightinput - 1]).upper())
        ToLocation = input("To :").lower()
        temp2_u = temp2[Flightinput - 1]
    return ToLocation,temp2_u
def FlightClass(FlightC):
    temp=FlightChoice_dict.get(FlightC)
    print("Welcome To {} Class Ticket Booking , Please Enter No of Tickets below ".format(temp[0]))
    TicketNos = int(input("No of Tickets : "))
    price = TicketNos * temp[1]
    FlightChoice_dict[FlightC][2]-=TicketNos
    return price,temp[0]

class Flight_Ticket(object):
    Flights ={
        "jetairways": ['Chennai ---> Bangalore','Chennai ---> Delhi','Chennai ---> Mumbai',
                        'Bangalore ---> Chennai','Bangalore ---> Delhi','Bangalore ---> Mumbai',
                        'Delhi ---> Chennai','Delhi ---> Bangalore','Delhi ---> Mumbai',
                        'Mumbai ---> Chennai','Mumbai ---> Bangalore','Mumbai ---> Delhi',
                        ],
        "lufthansa": ['Chennai ---> Paris','Chennai ---> Dubai','Chennai ---> NewYork',
                        'Bangalore ---> Paris','Bangalore ---> Dubai','Bangalore ---> NewYork',
                        'Delhi ---> Paris','Delhi ---> Dubai','Delhi ---> NewYork',
                        'Mumbai ---> Paris','Mumbai ---> Dubai','Mumbai ---> NewYork',
                        ]
    }
    Flightseats={"economy" : 30 , "business": 20, "premium business class" : 10}
    AvailableAirports=["chennai","bangalore","delhi","mumbai"]
    AvailableCities=[["chennai","bangalore","delhi","mumbai"],["paris","dubai","newyork"]]
    #Initialization
    def __init__(self,Customer_Name):
        self.Customer_name = Customer_Name

    #Book Ticket
    def book_ticket(self):
        Transaction = []
        Transaction.append(self.Customer_name)
        print("------------------------------------------------------------------------------------------------------")
        print("Welcome To Jet Dash Ticket Booking")
        inp=int(input("Press 1 to Continue \n"
                      "Press 2 to Exit Booking \n"))
        if inp==2:
            exit(0)
        print("Available Locations : {}".format(self.AvailableAirports).upper())
        FromLocation=input("From :").lower()
        n=0
        temp=self.AvailableAirports
        temp2=self.AvailableCities
        ValidInput={1,2}
        ValidAirways={"jetairways","lufthansa"}
        while n==0:
            if FromLocation in temp:
                Transaction.append(FromLocation)
                Flightinput=int(input("Enter 1 for Domestic Flights \n"
                                      "Enter 2 for International Flights \n"))
                if Flightinput not in ValidInput:
                    print("Choose a valid option")
                    Flightinput = int(input("Enter 1 for  Domestic Flights \n"
                                            "Enter 2 for International Flights\n"))
                flag=FlightInput(Flightinput,FromLocation,temp2)
                ToLocation = flag[0]
                temp2_u = flag[1]
                # print(ToLocation,temp2_u)
                if ToLocation in temp2_u:
                    Transaction.append(ToLocation)
                    Flights_u = list(self.Flights)
                    print("Available Flights : {}".format(Flights_u).upper())
                    FlightChoice = input("Select the Flight of your choice \n").lower()
                    if FlightChoice not in ValidAirways:
                        print("Enter a Valid Operator")
                        FlightChoice = input("Select the Flight of your choice \n").lower()
                    Transaction.append(FlightChoice)
                    print("------------------------------------------------------------------------------------------------------")
                    No_classes = int(input("Enter 1 for Economy class \n"
                                       "Enter 2 for Business class \n"
                                       "Enter 3 for Premium Business class \n"
                                       "Available seats \nEconomy : {}\n"
                                       "Business Class : {} \n"
                                       "Premium Business Class : {} \n".format(self.Flightseats['economy'],
                                                                               self.Flightseats['business'],
                                                                               self.Flightseats['premium business class'])))
                    TransactionId = random.randint(10000,99999)
                    Transaction.append(TransactionId)
                    FlightclassOp = FlightClass(No_classes)
                    Transaction.append(FlightclassOp[1])
                    Transaction.append(FlightclassOp[0])


                    Transaction_d=["Name","From","To","Airways","TransactionId","Class","Total Cost"]

                    print("----------------Ticket Summary--------------")
                    for i in range(len(Transaction)):
                        try:
                            print(str(Transaction_d[i].upper())+" : "+ str(Transaction[i].upper()))
                        except:
                            print(str(Transaction_d[i])+" : "+ str(Transaction[i]))

                    n = 1
                else:
                    print("Enter Valid To Location")

            else:
                print("Enter Valid From Location")
                FromLocation=input("From :").lower()


    def check_availability(self):
        pass


name=input("Enter Your Name : ")
print("------------------------------------------------ Welcome to Dash Jet " + name + " ------------------------------------------------")
user_input=int(input("Press 1 To Book a Ticket \n"
      "press 2 To Cancel A  Ticket \n"
      "press 3 To Check Availabilty \n"
      "press 4 To Check Your Booking Status \n"
      "press 5 To Exit \n"))

if user_input == 1:
    customer1=Flight_Ticket(name)
    customer1.book_ticket()
    customer1.book_ticket()
