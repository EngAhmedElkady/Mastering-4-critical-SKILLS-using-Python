# Homework 3: Even and Odd sum
sum1=0
sum2=0
list_numbers=input("enter numbers: ").split()
for i in range(0,8):
    if i%2!=0:
        sum1=sum1+int(list_numbers[i])
    else:
        sum2=sum2+int(list_numbers[i])
print(sum1,sum2)


