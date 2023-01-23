def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return 'Underweight'
    elif bmi <= 25:
        return 'Normal'
    elif bmi <= 30:
        return 'Overweight'
    elif bmi >30:
        return 'Obese'


#bmi = weight / height ** 2
#    return 'Underweight' if bmi <= 18.5 else 'Normal' if bmi <= 25.0 else 'Overweight' if bmi <= 30.0 else "Obese"