weight = int(input("Whats your weight?: "))
unit = input("Is it in Kg or Lbs?: ")
if unit.upper() == 'KG' :
    convertable= weight * float(2.205)
    print('Your weight is ' + str(convertable) + 'Lbs')
elif unit.upper() == 'LBS' :
    convertable= weight * float(0.45)
    print('Your weight is ' + str(convertable) + 'Kg')
