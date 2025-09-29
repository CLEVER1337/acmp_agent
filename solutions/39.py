
def max_earnings():
    with open('INPUT.TXT', 'r') as f:
        n = int(f.readline())
        prices = list(map(int, f.readline().split()))
    
    dp = [0] * (n + 1)  # dp[i]: максимальная денежная сумма за i-й день
    max_price = 0  # максимальная цена волос, которую может получить неформал в текущий момент
    
    for i in range(n - 1, -1, -1):
        max_price = max(max_price, prices[i])
        dp[i] = max(dp[i + 1], max_price - prices[i])
        
    with open('OUTPUT.TXT', 'w') as f:
        f.write(str(dp[0]))

max_earnings()
