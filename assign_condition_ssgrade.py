score = []
result = 0
avg = 0
sub = int(input("How many subjects are there:"))
for i in range(1,sub+1):
    scores = int(input(f"Subject {i}: "))
    score.append(scores)
    result += scores   
avg = result/len(score)
print(f"Average score is :{avg}")
if(90<=avg<=100):
    print("A")
elif(80<=avg<=89):
    print("B")
elif(70<=avg<=79):
    print("C")
elif(60<=avg<=69):
    print("D")
elif(avg<60):
    print("F")



