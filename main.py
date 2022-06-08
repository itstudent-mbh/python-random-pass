import argparse
from ast import arg
import string

from random import choices

def create_password(length=8, lower=False, upper=False, digit=False, pun=False):
    pool = ''

    if lower:
        pool += string.ascii_lowercase
    
    if upper:
        pool += string.ascii_uppercase

    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if pool == '':
        pool = string.ascii_letters



    return ''.join(choices(pool, k=length))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lenght', type=int, help="Lenght of password")
    parser.add_argument('-u', '--upper', help="Use upper case in password", action='store_true')
    parser.add_argument('-l', '--lower', help="Use lower case in password", action='store_true')
    parser.add_argument('-d', '--digits', help="Use digits in password", action='store_true')
    parser.add_argument('-p', '--punctuation', help="Use punctuation in password", action='store_true')

    args = parser.parse_args()
    
    print(create_password(args.lenght, lower=args.lower, upper=args.upper, digit=args.digits, pun=args.punctuation))
