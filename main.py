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