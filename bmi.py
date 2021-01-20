userWeight = float( input( "Please enter your weight: ") )
userHeight = float( input( "Please enter your height: ") )
userBmi = ( userWeight * 703 ) / ( userHeight ** 2 )

print()

if userBmi < 18.5:
    print( "A person with a BMI of " + format( userBmi, ".1f" ) + "is underweight"  )
elif userBmi < 26:
    print( "A person with a BMI of " + format( userBmi, ".1f" ) + \
    " has an optimal weight" )
else:
    print( "A person with a BMI of " + format( userBmi, ".1f" ) + \
    " is overweight")
