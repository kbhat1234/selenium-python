def usd_inr(dollar, rupees):
    inr_currency = dollar * rupees
    print(f'USD to INR conversion amount is {inr_currency}')

def even_odd(number):
    if (number % 2 == 0):
        print(f'{number} is even number')
    else:
        print(f'{number} is odd number')


usd = float(input("Enter the USD amount: "))
inr = float(input("Enter the INR amount as of today for 1$: "))
usd_inr(usd, inr)
even_odd(11)