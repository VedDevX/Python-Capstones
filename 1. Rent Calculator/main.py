WELCOME_TEXT = '''
╔═══════════════════════════════════════════════════╗
║                                                   ║
║   ██████╗ ███████╗███╗   ██╗████████╗              ║
║  ██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝              ║
║  ██║  ███╗█████╗  ██╔██╗ ██║   ██║                 ║
║  ██║   ██║██╔══╝  ██║╚██╗██║   ██║                 ║
║  ╚██████╔╝███████╗██║ ╚████║   ██║                 ║
║   ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝                 ║
║                                                   ║
║     💸  WELCOME TO THE RENT CALCULATOR  💸         ║
║                                                   ║
║     Easily split your monthly rent in ₹ Rupees    ║
║         — Simple, Smart & Precise!                ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
'''
print(WELCOME_TEXT)

TOTAL_RENT = int(input("Enter the total rent of yours for 1 month: ₹ "))

TOTAL_FOOD_PAY = int(input("Enter your monthly total spend on food: ₹ "))

TOTAL_ELECTRICITY = int(input("Enter your total monthly electricity units spends: "))

CHARGE_PER_UNIT = int(input("Enter the charge of electricity per unit in your area: "))

PERSONS_LIVING = int(input("Enter the number of persons are living in a room: "))

TOTAL_ELECTRICITY_BILL = TOTAL_ELECTRICITY * CHARGE_PER_UNIT

TOTAL_MONTHLY_SPEND = TOTAL_ELECTRICITY_BILL + TOTAL_FOOD_PAY + TOTAL_RENT

SPLIT_PAY = round(TOTAL_MONTHLY_SPEND / PERSONS_LIVING)

print(f"The total of monthly spend is ₹ {TOTAL_MONTHLY_SPEND} , So According to that after splitting in the {PERSONS_LIVING} persons,Each individual need to pay ₹ {SPLIT_PAY}")