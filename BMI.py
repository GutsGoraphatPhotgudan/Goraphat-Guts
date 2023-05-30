h = int(input("Pls input your Height:"))
w = int(input("Pls input your Weight:"))
total = w/h**2

print("Your BMI is:",total)

if total <18.5:
  print("You are Underweight")
elif total <=24.9:
  print("You have a Normal weight")
else:
  print("You are Overweight")
