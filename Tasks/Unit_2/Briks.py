x = input("Enter three digits (each digit for one pig):")
x = int(x)
a = x // 100
b = x % 100 // 10
c = x % 100 % 10
y = a + b + c
print(y,y//3, y % 3, y % 3 == 0 , sep = '\n')