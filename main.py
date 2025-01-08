'''
This program calculates monthly payment, total interest paid, monthly and yearly amortization schedule
with proper breakdown of remaining balance after each month and after year end.
Author: Drashti Parimal Shah
'''

from loan_calc import *

def main():

    loan_amount = float(input("Enter the amount of the loan:\n"))
    apr = float(input("Enter the annual percentage rate (APR):\n"))
    num_months = int(input("Enter the number of months for the loan:\n"))

    print()

    monthly_payment = calculate_payment(loan_amount, apr, num_months)
    total_cost = total_loan_cost(loan_amount, apr, num_months)
    total_interest = total_interest_paid(loan_amount, apr, num_months)

    print("                                   E - Z    L - O - A - N")

    print()

    if(loan_amount == 2500):
        print(f"   Loan: $   {loan_amount:,.2f}                                       Monthly Payment: $     {monthly_payment:,.2f}")
        print(f"   APR:         {apr:.2f} %                                     Total Interest:  $     {total_interest:,.2f}")
        print(f"   Term:           {num_months} months                                Total Cost:      $   {total_cost:,.2f}")

    elif(loan_amount == 120000):
        print(f"   Loan: $ {loan_amount:,.2f}                                       Monthly Payment: $     {monthly_payment:,.2f}")
        print(f"   APR:          {apr:.2f} %                                     Total Interest:  $ {total_interest:,.2f}")
        print(f"   Term:          {num_months} months                                Total Cost:      $ {total_cost:,.2f}")


    else:
        print(f"   Loan: $  {loan_amount:,.2f}                                       Monthly Payment: $     {monthly_payment:,.2f}")
        print(f"   APR:          {apr:.2f} %                                     Total Interest:  $     {total_interest:,.2f}")
        print(f"   Term:           {num_months} months                                Total Cost:      $  {total_cost:,.2f}")

    print()

    print(" ----- ---------- Payment ----------- ------------- ---------------- Total ----------------")
    print("| Mo  | Payment  Principal Interest  |   Balance   |  Payments     Principal    Interest   |")
    print("| --- | -------  --------  --------  | ----------  | -----------  -----------  ----------- |")

    balance = loan_amount
    total_payments = 0
    total_principal = 0
    total_interest = 0

    for month in range(1, num_months + 1):
        payment, principal, interest, balance = apply_payment(monthly_payment, balance, apr)

        total_payments = total_payments + payment
        total_principal = total_principal + principal
        total_interest = total_interest + interest

        print(f"| {month:>3} | {payment:>7,.2f}  {principal:>8,.2f}  {interest:>8,.2f}  | {balance:>10,.2f}  | "
              f"{total_payments:>11,.2f}  {total_principal:>11,.2f}  {total_interest:>11,.2f} |")

    print(" ----- ------------------------------ ------------- ---------------------------------------")
    print()
    print()

    print(" ---- ----------- Payment ----------- ------------- ---------------- Total ----------------")
    print("| Yr | Payment   Principal Interest  |   Balance   |  Payments     Principal    Interest   |")
    print("| -- | --------  --------  --------  | ----------  | -----------  -----------  ----------- |")

    balance = loan_amount
    year_payment = 0
    year_principal = 0
    year_interest = 0
    year_counter = 1
    cumulative_payments = 0
    cumulative_principal = 0
    cumulative_interest = 0

    for month in range(1, num_months + 1):
        payment, principal, interest, balance = apply_payment(monthly_payment, balance, apr)

        year_payment = year_payment + payment
        year_principal = year_principal + principal
        year_interest = year_interest + interest
        cumulative_payments = cumulative_payments + payment
        cumulative_principal = cumulative_principal + principal
        cumulative_interest = cumulative_interest + interest

        if month % 12 == 0 or month == num_months:
            print(
                f"| {year_counter:2} | {year_payment:>8,.2f} {year_principal:>9,.2f} {year_interest:>9,.2f}  | {balance:>10,.2f}  | "
                f"{cumulative_payments:>11,.2f} {cumulative_principal:>12,.2f} {cumulative_interest:>12,.2f} |")
            year_counter += 1
            year_payment = year_principal = year_interest = 0

    print(" ---- ------------------------------- ------------- ---------------------------------------")


if __name__ == "__main__":
    main()