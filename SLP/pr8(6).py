def emi(loan_amount, no_of_years, interest_rate):
    interest_rate = interest_rate / (12 * 100)
    no_of_months = no_of_years * 12
    emi = (loan_amount * interest_rate * (1 + interest_rate) ** no_of_months) / ((1 + interest_rate) ** no_of_months - 1)
    total_payment = emi * no_of_months
    amortization_schedule = []
    while no_of_months > 0:
        interest = loan_amount * interest_rate
        principal = emi - interest
        loan_amount = loan_amount - principal

        amortization_schedule.append([interest, principal, loan_amount])
        no_of_months -= 1
    return emi, total_payment, amortization_schedule


loan_amount = float(input("Enter the loan amount: "))
no_of_years = float(input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate: "))
emi, total_payment, amortization_schedule = emi(loan_amount, no_of_years, interest_rate)
print("Monthly EMI: ", emi)
print("Total payment: ", total_payment)
print("Amortization schedule:")
for payment in amortization_schedule:
    print("Interest: {:.2f}, Principal: {:.2f}, Loan Amount: {:.2f}".format(*payment))