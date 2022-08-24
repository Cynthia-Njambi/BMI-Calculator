# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#under 18.5 = underweight
#over 18.5< 25 = normal weight
#over 25<30 = overweight
#over 30<35= obese
#above 35= clinically obese
# BMI= weight/ height^2
bmi= round(weight/height**2)

if bmi<=18.5:
  print(f"Your bmi is {bmi} and you are underweight")
elif bmi>18.5<=25:
  print(f"Your bmi is {bmi} and you are of normal weight")
elif bmi>25<=30:
  print(f"Your bmi is {bmi} and you are overweight")
elif bmi >30<=35:
  print(f"Your bmi is {bmi} and you are obese")
else:
  print(f"Your bmi is {bmi} and you are clinically obese")
  



