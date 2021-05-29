import sys


def Change_Helper(coins, amount):
    #initialize running sum array for the number of ways we can make 'amount' change using coins
    # dynamic programming
    
    running_sum = [1] 
    running_sum.extend([0] * amount) 
    for coin_val, n_left in coins.items():
        rs_copy = running_sum.copy()
        for i in range(coin_val, amount+1):
            next_coin = rs_copy[i-coin_val]
            rs_copy[i] += next_coin
            if i < coin_val*(n_left + 1):
                running_sum[i] += next_coin 
            else:
                running_sum[i] += next_coin - rs_copy[i - coin_val*(n_left +1)]
    return running_sum[amount]

'''
Input:  coins is a dictionary representing how many of each type of coin you have (value -> amount)
        amount is the target amount you want to make change for
Output: True if it possible to make exact change using the coins provided, False otherwise
'''

def canMakeChange(coins, amount):

    if Change_Helper(coins, amount) > 0:
        return True
    else:
        return False

    



def main():
    f = sys.stdin
    num_coins, amount = [int(x.strip()) for x in f.readline().split()]
    coins = {}
    for _ in range(num_coins):
        coin_val, coin_amt = [int(x.strip()) for x in f.readline().split()]
        coins[coin_val] = coin_amt
    print(canMakeChange(coins, amount))

if __name__ == "__main__":
    main()