balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthlyInterestRate) ** 12) / 12
monthlyPayment = round((low + high) / 2, 2)

def monthlyInterest(balance, month, monthlyPayment):
    if month == 0:
        return balance 
    else:
        monthlyUnpaidBalance = balance - monthlyPayment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        return monthlyInterest(updatedBalance, month - 1, monthlyPayment)


while True:
    remainingBalance = monthlyInterest(balance, 12, monthlyPayment)
    if remainingBalance >= 0.12:
        low = monthlyPayment
        monthlyPayment = round((low + high) / 2, 2)
    elif remainingBalance <= -0.12:
        high = monthlyPayment
        monthlyPayment = round((low + high) / 2, 2)
    else:
        break
    
print("Lowest Payment:", monthlyPayment)