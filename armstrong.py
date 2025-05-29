num = int(input("Enter a number: "))
digits = len(str(num))

resultnumber = 0

temp = num
while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digits
    temp //= 10
    
if resultnumber == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")