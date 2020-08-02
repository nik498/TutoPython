import argparse
import math
import sys


def print_duree(y, m):
    if y == 0:
        return "{} months".format(m)
    elif y == 1 and m != 0:
        return "1 year and {} months".format(m)
    elif y == 1 and m == 0:
        return "1 year"
    elif y > 1 and m != 0:
        return "{} years and {} months".format(y, m)
    elif y > 1 and m == 0:
        return "{} years".format(y)


def calcul_annuity(credit, n_periods, interest):
    result = credit * ((interest * math.pow((1 + interest), n_periods)) / (math.pow((1 + interest), n_periods) - 1))
    print("Your annuity payment is {}!".format(math.ceil(result)))
    calcul_overpayment(math.ceil(result) * math.ceil(n_periods), credit)


def calcul_credit_principal(monthly_payment, n_periods, interest):
    result = monthly_payment / ((interest * math.pow((1 + interest), n_periods)) / (math.pow((1 + interest), n_periods) - 1))
    print("Your credit principal is {}!".format(math.ceil(result)))
    calcul_overpayment(monthly_payment * n_periods, result)


def calcul_periods(credit, monthly_payment, interest):
    argument = monthly_payment / (monthly_payment - (interest * credit))
    result = math.ceil(math.log(argument, interest + 1))
    months = result % 12
    years = result // 12
    print(print_duree(years, months))
    calcul_overpayment(math.ceil(result * monthly_payment), credit)


def calcul_diff(credit, n_periods, interest):
    sum = 0
    for i in range(n_periods):
        result = (credit / n_periods) + (interest * (credit - (credit * i / n_periods)))
        sum += math.ceil(result)
        print("Month {}: paid out {}".format((i + 1), math.ceil(result)))

    calcul_overpayment(math.ceil(sum), credit)


def calcul_overpayment(total, debut):
    over = total - debut
    print("Overpayment = {}".format(over))


parser = argparse.ArgumentParser(description="process input")
parser.add_argument("--type", "-t", type=str, default="erreur")
parser.add_argument("--payment", "-p", type=float, default=0.0)
parser.add_argument("--principal", "-c", type=float, default=0.0)
parser.add_argument("--periods", "-n", type=int, default=0)
parser.add_argument("--interest", "-i", type=float, default=0.0)

arguments = parser.parse_args()

if len(sys.argv) < 4:
    print("Incorrect parameters")

choix = arguments.type
principal = arguments.principal
periods = arguments.periods
processed_interest = arguments.interest / 1200
m_payment = arguments.payment

if choix != "diff" and choix != "annuity":
    print("Incorrect parameters")
elif choix == "annuity":
    if principal == 0:
        calcul_credit_principal(m_payment, periods, processed_interest)
    elif periods == 0 and principal > 0 and processed_interest > 0:
        calcul_periods(principal, m_payment, processed_interest)
    elif m_payment == 0:
        calcul_annuity(principal, periods, processed_interest)
    else:
        print("Incorrect parameters")
elif choix == "diff":
    if principal > 0 and periods > 0 and processed_interest > 0:
        calcul_diff(principal, periods, processed_interest)
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
