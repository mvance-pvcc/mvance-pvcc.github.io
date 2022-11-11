# Name: Mike Vance
# Prog Purpose: This program takes your pizza order
#	Pizza Prices
#       Small - 9.99
#       Medium - 12.99
#       Large - 14.99
#       X-Large - 14.99
#	Sales tax rate: 5.5%

import datetime

############## define global variables ##############
#define tax rate and prices
SALES_TAX_RATE = .055
SMALL = 9.99
MEDIUM = 12.99
LARGE = 14.99
XLARGE = 17.99

# define global variables
size_pizza = 0
qty_pizza = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ##############
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input('\nWould you like to place another order? (Y/N): ')
        if yesno.upper() != 'Y':
            another_order = False

def get_user_data(): #Get qty_pizza & size_pizza
    global qty_pizza, size_pizza
    qty_pizza = int(input("How many pizzas would you like? "))
    size_pizza = str(input('\nOur pizza sizes: Small (S), Medium (M), Large(L), Xtra Large (XL)\nWhat size pizza would you like? (S, M, L, or XL): '))
	
def perform_calculations(): #subtotal = qty_pizza * size_pizza; sales_tax = subtotal * SALES_TAX_RATE; total = subtotal + sales_tax
    global subtotal, sales_tax, total, size_pizza
    if size_pizza == 'S':
        subtotal = SMALL * qty_pizza
    elif size_pizza == 'M':
        subtotal = MEDIUM * qty_pizza
    elif size_pizza == 'L':
        subtotal = LARGE * qty_pizza
    elif size_pizza == 'XL':
        subtotal = XLARGE * qty_pizza

    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
	
def display_results():
    ordersize = size_pizza
    orderqty = qty_pizza
    ordertxt = 'Your Order: {} size {} pizza(s)'
    print('-----------------------------')
    print('**** Mike\'s Pizza Palace ****')
    print('***The Okayest Pizza Place***')
    print('-----------------------------')
    print(ordertxt.format(orderqty, ordersize,))
    print('-----------------------------')
    print('Subtotal   $' + format(subtotal,'8,.2f'))
    print('Sales Tax  $' + format(sales_tax,'8,.2f'))
    print('Total      $' + format(total,'8,.2f'))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

############## Call on main program to execute ##############
main()