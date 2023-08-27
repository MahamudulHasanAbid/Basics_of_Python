'''Create a Python program that assists users in deciding what to wear based on the weather conditions. Ask the user to input the current temperature. Provide the following suggestions:
"Wear a light jacket" if the temperature is between 50°F and 65°F
"Wear a sweater" if the temperature is between 30°F and 50°F
"Wear a heavy coat" if the temperature is below 30°F
"Wear comfortable clothes" if the temperature is above 65°F'''

temp = float(input("Current temperature: "))
print(f"The temperature is: {temp}F")
if(temp>65):
    print("Wear comfortable clothes.")
elif(50<temp<=65):
    print("Wear a light jacket")
elif(30<temp<=50):
    print("Wear a sweater.")
elif(temp<30):
    print("Wear a heavy coat.")
