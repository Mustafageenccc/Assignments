name = "Mike"
user_name = input("Please enter your name: \n").strip().title()
if name == user_name:
    print("Hello Mike! The password is W@12")
else:
    print("Hello ", user_name, "See you later!")