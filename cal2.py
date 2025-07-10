# python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("enter the principle amount: "))
    if principle <= 0 :
        print("principle cant be less than or equal to zero")



while rate <= 0 :
    rate = int(input("enter the intrest rate : "))
    if rate <=0 :
        print("intrst rate can't br equa to less than zero")


while time <= 0:
    time = int(input("Enetr the time in year"))
    if time<=0:
        print("time cant be zero or eauql to 0 ")


total = principle*pow((1+rate/100), time)
print(f"Balance after {time} year/s :{total:.2f}")   # here f is a formate identifier


