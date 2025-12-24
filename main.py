"""attemps=3
spass="andisheh1381"
while attemps>0:
    password=input("Enter a valid pass:")
    if spass==password:
        print("welcom")
        break
    else:
        print("wrong pass")
        attemps-=1
        if attemps>0:
            print("Try again")
        else:
            print("Locked")"""

#question 2:
"""snum=int(input("Enter a starting number:"))
enum=int(input("Enter a starting number:"))
num=snum
count=0 
while num<=enum:
     if num%2==0:
         print(num,end=" ")
         count=count+1
    num+=1
    
print("")

print(count)"""

#third question:
"""column=int(input("Enter a column number:"))
rows=int(input("Enter a row number:"))

for x in range(rows):
    for y in range(column):
        print("*",end="")
    print("")"""
#shopping cart

cart=["apple", "milk", "bread"]
cart.append("banana")
cart.remove("apple")
list={"milk":2.50,"bread":1.20,"banana":4.00}
name=input("Enter your name:")
name=name.capitalize()

print(f"Hello {name},your items:{list.keys()}and costs:{list.values()}")