## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

user_city = input("Enter your city: ")

if user_city in india:
    print(f"{user_city} is in India")
elif user_city in pakistan:
    print(f"{user_city} is in Pakistan")
elif user_city in bangladesh:
    print(f"{user_city} is in Bangladesh")
else:
    print("City not avaible in db")
