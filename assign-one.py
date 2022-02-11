x = 50 + 50
y = 100 - 10
print(x)
print(y)


print("Hello World")
print("Hello World : 10")


P = float(input("Enter initial withdrawal: "))
r = float(input("Enter your interest rate: "))/1200
n = float(input("Loan duration in months: "))

top = r * ((1 + r) ** n)
bottom = ((1 + r) ** n) - 1

A = P * (top / bottom)

print(int(A))