print("Please answer below questions as \"Yes\" or \"No\"")
age = input("Are you a cigarette addict older than 75 years old?: \n").strip().title()
if age == "Yes":
    age= True
else:
    age= False
chronic = input("Do you have a severe chronic disease?: \n").strip().title()
if chronic == "Yes":
    chronic= True
else:
    chronic= False
immune = input("Is your immune system too weak?: \n").strip().title()
if immune == "Yes":
    immune= True
else:
    immune= False
risk = (age or chronic or immune)
print(risk)
if risk:
    print ("You are in risky group")
else: 
    print("You are not in risky group")
