# import random
#
# Flightseats = {"economy": 30, "business": 20, "premium business class": 10}
# Flightseats['economy'] -= 2
# print(Flightseats)
a=[]
FlightChoice_dict = {1: ["Economy", 350, 20], 2: ["Business Class", 500, 10],
                     3: ["Premium Business Class", 850, 10]}
def FlightClass(FlightC):

    temp=FlightChoice_dict.get(FlightC)
    print("E : {}".format(temp[2]))
    print("Welcome To {} Class Ticket Booking , Please Enter No of Tickets below ".format(temp[0]))
    t = int(input("No of Tickets : "))

    price = t * temp[1]
    a.append(temp[0])
    FlightChoice_dict[FlightC][2]-=t
    return price,FlightChoice_dict

a.append(FlightClass(int(input("ENter class"))))
print(a)
print(FlightChoice_dict)

# if No_classes == 1:
#     print("Welcome To Economy Class Ticket Booking , Please Enter No of Tickets below ")
#     t = int(input("No of Tickets : "))
#     price = t * 350
#     self.Flightseats['economy'] -= t
#     # Transaction.append(price)
#     Transaction.append('Economy Class')
# elif No_classes == 2:
#     print("Welcome To Business Class Ticket Booking , Please enter No of Tickets below ")
#     t = int(input("No of Tickets : "))
#     price = t * 500
#     # Transaction.append(price)
#     self.Flightseats['economy'] -= t
#     Transaction.append('Business Class')
# elif No_classes == 3:
#     print("Welcome To Premium Business Class Ticket Booking , Please enter No of Tickets below ")
#     t = int(input("No of Tickets : "))
#     price = t * 850
#     # Transaction.append(price)
#     self.Flightseats['economy'] -= t
#     Transaction.append('Premium Business Class')
