'''1. Sales Report:
   You are a store manager, and you want to generate a sales report for the past week. Write a Python program that takes a list of daily sales amounts as input and calculates the total sales for the week.

   Guidelines:
   - Create a list that contains the daily sales amounts for the week.
   - Use a loop to iterate over the list and calculate the total sales by adding each daily amount to a running total.
   - After the loop, print the total sales for the week.'''

weekly_sales = []
# days = int(input("How many days you want to count:")) 
# for i in range(1,days+1):
# As week = 7 days we can set the range(7) or
total_sales = 0
for i in range(1,8):
    daily_sales = int(input(f"Sales at day {i}: "))
    weekly_sales.append(daily_sales)
    total_sales+=daily_sales
print(f"Total sales for the week is: {total_sales}")
