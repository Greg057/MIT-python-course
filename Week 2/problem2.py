balance = 3329
annualInterestRate = 0.2

monthlyPayment = 10
monthlyInterestRate = annualInterestRate / 12.0

def monthlyInterest(balance, month, monthlyPayment):
    if month == 0:
        return balance 
    else:
        monthlyUnpaidBalance = balance - monthlyPayment
        updatedBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        return monthlyInterest(updatedBalance, month - 1, monthlyPayment)


while True:
    if monthlyInterest(balance, 12, monthlyPayment) > 0:
        monthlyPayment += 10
    else:
        break
    
print("Lowest Payment:", monthlyPayment)