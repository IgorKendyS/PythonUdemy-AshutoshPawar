principal = float(input("Enter the amount borrowed "))
years = float(input("Enter the period in years "))
rate = float(input("Enter rate of interest "))

interest = principal * years * rate / 100
print(f"The simple interest calculated is {interest} For a period of {years} years at the rate of {rate} % is $interest")