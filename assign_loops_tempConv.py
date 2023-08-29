'''3. Temperature Converter:
   You are developing a weather application, and you need to convert temperatures from Celsius to Fahrenheit. Write a Python program that takes a list of temperatures in Celsius as input and converts them to Fahrenheit.

   Guidelines:
   - Create a list that contains temperatures in Celsius.
   - Use a loop to iterate over the list.
   - Within the loop, apply the conversion formula (F = C * 9/5 + 32) to each temperature.
   - Create a new list to store the converted temperatures.
   - After the loop, print the list of temperatures in Fahrenheit.'''

temp_cel=[]
temp_fah=[]
iter = int (input("Total amount in list: "))
for i in range(iter):
    C = float(input(f"Enter value in celcius: °C", ))
    temp_cel.append(C)
    F = ((C*9)/5)+32
    temp_fah.append(F)
print(temp_fah)




