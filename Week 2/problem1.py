balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

def monthlyPayment(balance, month):
    if month == 0:
        return balance 
    else:
        balance -= balance * monthlyPaymentRate
        balance += annualInterestRate / 12 * balance
        return monthlyPayment(balance, month - 1)
    

balance = round(monthlyPayment(balance, 12), 2)

print("Remaining balance:", balance)

        