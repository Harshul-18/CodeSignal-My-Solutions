# You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

def solution(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit += deposit*(rate/100)
        count += 1
    return count