print("==== FITNESS & BMI TRACKER ====")

name = input("Enter your name:", )
height = float(input("Entre your height in meters:"))
weight = float(input("Entre your waight in kg:"))

bmi = weight/(height**2)

print("\n-----RESULT-----")
print("name:", name)
print("BMI:", bmi)

if bmi < 18.5:
    category = "underwaight"
    advice = "focus on balanced and nutritous meals"
elif bmi < 25:
    category = "normal range"
    advice = "maintain a balenced diet and regular activity"
elif bmi < 30:
    category = "overwaight"
    advice = "focus on regular phycal activity and balanced meal"
else:
    category = "obesity range"   
    advice = "consider discussing healthy lifestyle goals with a qualified proffessional "

print("Category:",category)    
print("suggestion:", advice)


print("\nthank you for using the fitnesss & BMI tracker !")



