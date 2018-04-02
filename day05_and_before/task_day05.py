# Author:Jack
# Date:2018/4/2

commodities = ['iphone6s','mac book','coffee','pythone book','bicycle']
cost = ['5800','9000','32','80','1500']

salary = int(input("Please input your salary: "))
print(commodities)
print(commodities.__len__())

print("Welcome to my little shop! ")
for i in range(1,commodities.__len__()+1):
    print(i,'.',commodities[i-1],'\t',cost[i-1])
print(i+1,'.','Exit')

costed = 0
buyed = []
left = salary - costed
while True:
    want_to_buy = int(input("Please input the number of commmodities which you want to buy: "))
    if want_to_buy == 6 :
        print("You have bought: ",buyed)
        print("Left money: ",salary-costed)
        print("See you next time! ")
        break
    else:
        price = int(cost[want_to_buy-1])
        print("Price:\t",price)
        if price >= left:
            print("Insufficient balance!")
            print("Left money: ",salary-costed)
        else:
            costed += price
            print("Costed:\t",costed)
            left = salary - costed
            buyed.append(commodities[want_to_buy-1])
            print("Left money: ",left)


