Meter=float(input("Enter your units input:  "))

if(Meter>=0 and Meter<=100):
    print("Electricity Bill:", Meter*5)
elif(Meter>=101 and Meter<=200):
    print("Electricity Bill:", Meter*7)
elif(Meter>=201 and Meter<=500):
    print("Electricity Bill:", Meter*10)
elif(Meter>=501):
    print("Electricity Bill:", Meter*15)