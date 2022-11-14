# Name: Mike Vance
# Prog Purpose: This program calculates Fresh Food Marketplace weekly employee pay
#	Fed income tax - 12%
#	State income tax - 3%
#	Social Security tax - 6.2%
#	Medicare tax - 1.45%
#	Pay Rates
#       Cashier - 16.50
#       Stocker - 15.75
#       Janitor - 15.75
#       Maintenance - 19.50


import datetime

############## define global variables ##############
#define pay and tax rates
DEDUCTIONS = (.15, .03, .062, .0145)
PAY_RATES = (16.50, 15.75, 15.75, 19.50)
# define global variables
qty_hrs = 0
job_cat = 0
pay_gross = 0
pay_net = 0
total_deduct = 0
fed = 0
state = 0
socsec = 0
medi = 0


############## define program functions ##############
def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('\nWould you like to calculate another employee? (Y/N): ')
        if yesno.upper() != 'Y':
            another_employee = False

def get_user_data(): 
    global job_cat, qty_hrs
    job_cat = str(input('\nEmployee Categories: Cashier (C), Stocker (S), Janitor (J), Maintenance (M)\nWhat is the job category? (C, S, J, M): '))
    qty_hrs = int(input("How many hours were worked? "))
	
def perform_calculations():
    global qty_hrs, job_cat, pay_gross, pay_net, fed, state, socsec, medi, DEDUCTIONS, total_deduct
    if job_cat.upper() == 'C':
        pay_gross = PAY_RATES[0] * qty_hrs
    elif job_cat.upper() == 'S':
        pay_gross = PAY_RATES[1] * qty_hrs
    elif job_cat.upper() == 'J':
        pay_gross = PAY_RATES[2] * qty_hrs
    elif job_cat.upper() == 'M':
        pay_gross = PAY_RATES[3] * qty_hrs

    fed = pay_gross * DEDUCTIONS[0]
    state = pay_gross * DEDUCTIONS[1]
    socsec = pay_gross * DEDUCTIONS[2]
    medi = pay_gross * DEDUCTIONS[3]
    total_deduct = fed + state + socsec + medi
    pay_net = pay_gross - total_deduct
	
def display_results():
    emp_type = job_cat
    hours = qty_hrs
    ordertxt = 'Employee Type: {}\nHours Worked: {} '

    print('-----------------------------')
    print('**** Fresh Food Marketplace ****')
    print('*******It\'s Pretty Fresh*******')
    print('-----------------------------')
    print(ordertxt.format(emp_type, hours,))
    print('-----------------------------')
    print('Gross Pay         $' + format(pay_gross,'8,.2f'))
    print('-----------------------------')
    print('Fed Income Tax    $' + format(fed,'8,.2f'))
    print('State Income Tax  $' + format(state,'8,.2f'))
    print('Social Security   $' + format(socsec,'8,.2f'))
    print('Medicare Tax      $' + format(medi,'8,.2f'))
    print('Total Deductions  $' + format(total_deduct,'8,.2f'))
    print('-----------------------------')
    print('Net Pay           $' + format(pay_net,'8,.2f'))
    print(str(datetime.datetime.now()))

############## Call on main program to execute ##############
main()