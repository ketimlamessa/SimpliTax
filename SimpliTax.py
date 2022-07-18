print('Welcome to Simpli Tax Solutions')
print('This will allow you to calculate your minnesota taxes for the fisical year.')
ans = input('Do you live in MN? Y or N  ')
if ans == 'Y':
    name = input("Enter name: ")
    income = eval(input("Please enter income: "))
    ans2 = input('Would you like to continue simple deductions? (D) or end now to see see your final income? (F)')
    tax = 0.0

    if income >= 171220:
        tax = ((income - 171220) * .1) + (15000 * .9.85)
        income = income - tax
    elif income >= 92230:
        tax = (income - 92230) * .0785
        income = income - tax
    elif income >= 28080:
        print('Your income is non-taxable')
    else:
        print("Please enter a valid income")
    if ans2 == "F":
        print("\nYour name:",name)
        print("Amount you will pay in tax: $",tax)
        print("Amount you will have after tax: $",income)
        print("Info is from Department of Revenue MN")
else:
    print('sorry only MN taxes can be done at this time')
