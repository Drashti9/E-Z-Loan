def round_cents(num):
    return int(num * 100 + .5000001) / 100


def calculate_payment(amount, apr, num_months):
    monthly_interest_rate = apr / 12 / 100
    payment = (amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_months)
    return round_cents(payment)


def total_loan_cost(amount, apr, num_months):
    payment = calculate_payment(amount, apr, num_months)
    return round_cents(payment * num_months)


def total_interest_paid(amount, apr, num_months):
    return round_cents(total_loan_cost(amount, apr, num_months) - amount)


def apply_payment(payment, balance, apr):

    monthly_interest_rate = apr / 12 / 100
    interest = round_cents(balance * monthly_interest_rate)

    if balance < payment:
        payment = round_cents(balance + interest)

    principal = round_cents(payment - interest)
    balance = round_cents(balance - principal)

    return payment, principal, interest, balance
