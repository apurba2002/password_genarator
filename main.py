import random

def pass_gen():
    lowwer_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "1234567890"
    symbol = "!@#$%^&*()_+{}|:"

    n = 1
    for n in range (4):
        password1 = lowwer_case[random.randint(1,25)]+upper_case[random.randint(1,25)]+number[random.randint(1,9)]+symbol[random.randint(1,5)]
        password2 = lowwer_case[random.randint(1,25)]+upper_case[random.randint(1,25)]+number[random.randint(1,9)]+symbol[random.randint(1,5)]
        password3 = lowwer_case[random.randint(1,25)]+upper_case[random.randint(1,25)]+number[random.randint(1,9)]+symbol[random.randint(1,5)]
        password4 = lowwer_case[random.randint(1,25)]+upper_case[random.randint(1,25)]+number[random.randint(1,9)]+symbol[random.randint(1,5)]
    return password1+password2+password4+password3



while True:
    n = pass_gen()
    print("your genarated password is :-", n)
    print("press any key for continue")
    print("Press 0 for exit")
    key = input()

    if (key=="0"):
        break






