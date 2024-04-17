# Program to Check If the Number is Armstrong or Not
num = int(input("enter a number here: "))
order = len(str(num))

sum = 0
# storing value of num in temp to make changes
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    # to remove last element in temp
    temp //= 10

if sum == num:
    print("it is an armstrong number.")
else:
    print("it is not an armstrong number.")
