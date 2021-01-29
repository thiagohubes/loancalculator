import argparse
from math import floor, ceil, log

parser = argparse.ArgumentParser()
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
args = parser.parse_args()
if args.type is None:
    print('Incorrect parameters.')
    exit()
elif args.type == 'diff':
    if args.interest is None or \
            args.principal is None or \
            args.periods is None or \
            float(args.interest) < 0 or \
            int(args.principal) < 0 or \
            int(args.periods) < 0:
        print('Incorrect parameters.')
        exit()
    i = float(args.interest) / (12 * 100)
    P = int(args.principal)
    n = int(args.periods)
    sum = 0
    for m in range(1, n + 1):
        D = (P / n) + i * (P - (P *(m - 1)) / n)
        print(f'Month {m}: payment is {ceil(D)}')
        sum += ceil(D)
    print()
    print(f'Overpayment = {sum - P}')
elif args.type == 'annuity':
    if args.payment is None and (\
            args.interest is None or \
            args.principal is None or \
            args.periods is None):
        print('Incorrect parameters.')
    elif args.payment is None and \
            float(args.interest) >= 0 and \
            int(args.principal) >= 0 and \
            int(args.periods) >= 0:
        i = float(args.interest) / (12 * 100)
        P = int(args.principal)
        n = int(args.periods)
        a = P * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        print(f'Your annuity payment = {ceil(a)}!')
        print(f'Overpayment = {ceil(a) * n - P}')
    elif args.principal is None and (\
            args.payment is None or \
            args.periods is None or \
            args.interest is None):
        print('Incorrect parameters.')
    elif args.principal is None and \
            int(args.payment) >= 0 and \
            int(args.periods) >= 0 and \
            float(args.interest) >= 0:
        i = float(args.interest) / (12 * 100)
        a = int(args.payment)
        n = int(args.periods)
        P = a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
        print(f'Your loan principal = {floor(P)}!')
        print(f'Overpayment = {a * n - floor(P)}')
    elif args.periods is None and (\
         args.principal is None or \
         args.payment is None or \
         args.interest is None):
        print('Incorrect parameters.')
    elif args.periods is None and \
            int(args.principal) >= 0 and \
            int(args.payment) >= 0 and \
            float(args.interest) >= 0:
        i = float(args.interest) / (12 * 100)
        a = int(args.payment)
        P = int(args.principal)
        n = log(a / (a - i * P), 1 + i)
        n = ceil(n)
        if n == 1:
            print('It will take 1 month to repay this loan!')
        elif n < 12:
            print(f'It will take {n} months to replay this loan!')
        elif n == 12:
            print('It will take 1 year to repay this loan!')
        elif n % 12 == 0:
            print(f'It will take {round(n / 12)} years to repay this loan!')
        else:
            print(f'It will take {n // 12} years and {n % 12} months to repay this loan!')
        print(f'Overpayment = {a * n - floor(P)}')
    else:
        print('Incorrect parameters.')
