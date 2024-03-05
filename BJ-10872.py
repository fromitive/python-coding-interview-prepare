number = int(input())

def factorial(number):
    if number == 0:
        return 1
    
    dp = [0] * (number + 1)
    dp[0] = 1
    for index in range(1,number + 1):
        dp[index] = dp[index - 1] * index
        
    return dp[number]

print(factorial(number))