i=0
while i < 5:
    try:
        choice = int(input("Select from Below\n1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit\n3.Inches to cm\n4.Cm to inch\n5.Exit\n"))
        if choice==1:
            f = float(input("Enter the temperature in Fahrenheit : \n"))
            print(f"Celsius = {round(((f - 32.0) * 5.0 / 9.0),2)}")
        elif choice==2:
            c=float(input("Enter the temperature in Celsius : \n"))
            print(f"Fahrenheit = {round(((c * 9/5) + 32),2)}")
        elif choice == 3:
            n = float(input(f"Enter the length in Inch : \n"))
            print(f"Cm = {round((n*2.54),2)}")
        elif choice==4:
            n = float(input("Enter the length in Cm : \n"))
            print(f"Inch = {round((n/2.54),2)}")
        elif choice==5:
            exit()
        else:
            print ("Invalid Input")
    except ValueError as e:
        print(f"Error : {e}")