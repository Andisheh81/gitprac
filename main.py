## the power user profile creator
fname=input("Please enter your first name:")
lname=input("Please enter your last name:")
byear=input("Please enter your Birth year:")
name=fname+" "+lname
age=2025-int(byear)
secretname=name[:3]+byear[-3:]
height=int(input("Enter your height in cm:"))
height=height/100


print("--- PROFILE SUMMARY ---")
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
    fname="guest"

