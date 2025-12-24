
## the power user profile creator
"""fname=input("Please enter your first name:")
lname=input("Please enter your last name:")
byear=input("Please enter your Birth year:")
name=fname+" "+lname
age=2025-int(byear)
secretname=name[:3]+byear[-3:]
height=int(input("Enter your height in cm:"))
height=height/100

attemps=3
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


"""print("--- PROFILE SUMMARY ---")
print(f"Full Name: [{name}]")
print(f"Age: [{age}]")
print(f"Secret Username: [{secretname}]")
print(f"Height: [{height}]m")

if age>18:
    print("Access Granted: You are an adult.")
else:
    print("Access Restricted: Minor detected.")

if height>2.00:
    print("You are very tall!")
elif height<2.00 and height>1.50:
    print("You are average height.")
elif height<1.50:
    print("You are a bit short!")
if fname=="":
    fname="guest"""




#third question:
"""column=int(input("Enter a column number:"))
rows=int(input("Enter a row number:"))

for x in range(rows):
    for y in range(column):
        print("*",end="")
    print("")
#shopping cart

cart=["apple", "milk", "bread"]
cart.append("banana")
cart.remove("apple")
list={"milk":2.50,"bread":1.20,"banana":4.00}
name=input("Enter your name:")
name=name.capitalize()

print(f"Hello {name},your items:{list.keys()}and costs:{list.values()}")"""
