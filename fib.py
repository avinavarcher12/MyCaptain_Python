terms = int(input("Enter the Number to find the Fibonacci Series "))
a = 0
b = 1
count = 0
if terms <=0:
    print("Kindly enter the Positive Number")
else:
    print("Fibonacci Series: ")
    while count < terms:
        print(a)
        c = a + b
        a = b
        b = c
        count += 1