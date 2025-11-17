
import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    n = int(data[0])
    d = float(data[1])
    k1 = int(data[2])
    k2 = int(data[3])
    index = 4
    
    # Read the list of products and their required quantities
    products = []
    quantities_required = []
    for i in range(n):
        name = data[index]; index += 1
        qty = float(data[index]); index += 1
        products.append(name)
        quantities_required.append(qty)
    
    # Read the old base offers (k1 entries)
    old_prices = {}
    for i in range(k1):
        name = data[index]; index += 1
        price = float(data[index]); index += 1
        old_prices[name] = price
    
    # Read the new base offers (k2 entries)
    new_prices = {}
    for i in range(k2):
        name = data[index]; index += 1
        price = float(data[index]); index += 1
        new_prices[name] = price
    
    # For each product, we have:
    #   old_price = old_prices.get(product, 0.0)
    #   new_price = new_prices.get(product, 0.0)
    # But note: the products list from the plan might have products not in the bases? But the problem says the goods can be purchased from the old base, so we assume the old base has all products? Actually, the problem says: "the company has an old base that can supply all goods", but the input only gives k1 offers from the old base. So we must assume that the old base has all n products? Actually, the problem says: "the manager wants to purchase from the new base without exceeding d in total cost at the old base prices". So the old base has all n products? But the input gives k1 offers which might be less than n? Actually, the problem says: "the company has an old base that can supply all goods" meaning the old base has all n products. So we assume that the old base has all n products? But the input gives k1 which might be less than n? Actually, the problem says: "the company has an old base that can supply all goods" so we assume the old base has all n products. However, the input only gives k1 offers. So we must be cautious.

    # Actually, the problem says: "the input has k1 lines for the old base and k2 for the new base". So we have to map the product names to their prices. But note: the product names in the plan might not be in the bases? But the problem says the goods can be purchased from the old base, so the old base must have all n products. So we assume that the old base has all n products? But the input only gives k1 offers. This might be a problem.

    # Actually, the problem says: "the company has an old base that can supply all goods" meaning the old base has all n products. So the k1 must be at least n? But the input might have k1 >= n? Actually, the problem says: "the input has k1 lines for the old base" which might include more than n? But we only care about the n products.

    # We need to get the prices for the n products from the old base and new base.
    # For each product i in the n products, we need:
    #   old_price_i = price from old base for that product
    #   new_price_i = price from new base for that product
    # But the input only gives k1 offers for the old base, which might not include all n products? But the problem says the old base can supply all, so we assume the old base has all n products. Similarly for the new base? But the problem says: "the new base has k2 offers" which might not include all n products.

    # Actually, the problem states: "the company has an old base that can supply all goods" meaning the old base has all n products. So we assume that the old base has all n products. Similarly, the new base might not have all? But the problem says: "the new base has k2 offers". So for products not in the new base, we cannot buy from there.

    # So for each product i, if it is not in the new base, we cannot buy it from the new base. So we must buy it from the old base.

    # Therefore, we need to determine for each product, whether to buy it from the new base or the old base.

    # But note: the goal is to maximize the unspent money, which is equivalent to minimizing the amount spent at the old base? Actually, the money is spent at the old base only if we buy from the old base. But if we buy from the new base, we pay the new base price, but the cost at the old base is what is saved? Actually, the problem says: "the manager wants to purchase from the new base without exceeding d in total cost at the old base prices". So the cost at the old base is the reference.

    # Specifically: for each product i, if we buy it from the old base, the cost is old_price_i * q_i (where q_i is the required quantity). But if we buy it from the new base, the cost is new_price_i * q_i. However, the constraint is that the total cost at the old base prices of the goods purchased from the new base must not exceed d. So if we let x_i be the quantity of product i purchased from the new base, then the cost at the old base prices is sum_i (old_price_i * x_i) <= d.
    # And the goal is to maximize the amount saved? Actually, the money that is saved is the money that is not spent at the old base? Actually, the company pays the old base for the goods purchased from the old base. But the manager wants to take the unspent money? Actually, the problem says: "the unspent money can be taken by him". So the manager wants to maximize the amount of money that is not spent at the old base? But note: the company pays the old base for the goods purchased from the old base. But for goods purchased from the new base, the company pays the new base? But the problem says: "the manager wants to utilize the new base without exceeding d in total cost at the old base prices". So the constraint is: the total cost of the goods purchased from the new base, evaluated at the old base prices, must not exceed d.

    # So the constraint is: for each product i, let x_i be the quantity purchased from the new base. Then the cost at the old base prices is sum_i (old_price_i * x_i) <= d.
    # And the goal is to maximize the amount of money that is not spent at the old base? Actually, the company will pay the old base for the goods purchased from the old base. But if we purchase from the new base, the company pays the new base instead. So the money that is saved is the money that is not spent at the old base? But note: the company must purchase the entire required quantity of each product. So for each product i, let q_i be the required quantity. Then the amount that must be purchased from the old base is (q_i - x_i) for each i. So the total cost at the old base is sum_i (old_price_i * (q_i - x_i)) = sum_i (old_price_i * q_i) - sum_i (old_price_i * x_i)
    # So the amount of money that is spent at the old base is: total_cost_old = sum_i (old_price_i * (q_i - x_i)) = sum_i (old_price_i * q_i) - sum_i (old_price_i * x_i)
    # The company will pay this amount to the old base. But the manager wants to minimize the amount spent at the old base? Because the unspent money can be taken by him? Actually, the problem says: "the unspent money can be taken by the manager". So the manager wants to maximize the amount that is not spent at the old base. That is, maximize the amount that is spent at the new base? But note: the company also pays the new base for the goods purchased there. So the company pays both bases? Actually, the company must purchase the entire quantity. So the total amount that the company pays is:
    #   amount_to_old_base = sum_i (old_price_i * (q_i - x_i)) 
    #   amount_to_new_base = sum_i (new_price_i * x_i)
    # So the total amount paid by the company is: amount_to_old_base + amount_to_new_base.
    # But the manager wants to take the unspent money? Actually, the problem says: "the unspent money can be taken by him". But what is the unspent money? It is the money that was allocated for the old base but not spent because some goods were bought from the new base. So the amount allocated for the old base was: sum_i (old_price_i * q_i). But the amount actually spent at the old base is only for the quantity purchased there: sum_i (old_price_i * (q_i - x_i)) = sum_i (old_price_i * q_i) - sum_i (old_price_i * x_i)
    # So the amount that is not spent at the old base is: sum_i (old_price_i * x_i). And this amount can be taken by the manager? But wait, the problem says: "the unspent money can be taken by the manager". So the manager wants to maximize the unspent money, which is: sum_i (old_price_i * x_i). 
    # However, note that the constraint is: the total cost at the old base prices of the goods purchased from the new base must not exceed d. That is: sum_i (old_price_i * x_i) <= d.
    # So the manager wants to maximize the unspent money, which is exactly sum_i (old_price_i * x_i), subject to the constraint that this sum is at most d.
    # But wait: is that correct? Actually, the unspent money is the money that was allocated for the old base but not spent because the goods were bought from the new base. And that is exactly: for each product i, the amount allocated for it at the old base is (old_price_i * q_i). But if we buy it from the new base, we don't use that allocation. So the unspent amount is: sum_i (old_price_i * x_i). 
    # So the manager wants to maximize U = sum_i (old_price_i * x_i), subject to the constraint that the total cost at the old base prices of the goods purchased from the new base is at most d. But note: we can choose x_i arbitrarily as long as we do not exceed the required quantity? Actually, for each product i, we can purchase any amount from 0 to q_i from the new base. So we have: 0 <= x_i <= q_i.
    # So the problem becomes: 
    #   maximize U = sum_i (old_price_i * x_i)
    #   subject to: 
    #       0 <= x_i <= q_i for each i
    #        sum_i (old_price_i * x_i) <= d
    # But wait, is that correct? Actually, the constraint is exactly: the total cost at the old base prices of the goods purchased from the new base must not exceed d. So the constraint is: sum_i (old_price_i * x_i) <= d.
    # And the objective is to maximize U = sum_i (old_price_i * x_i)? 
    # But note: that is exactly the same as the constraint. So we are simply trying to make sum_i (old_price_i * x_i) as large as possible, but without exceeding d. So the maximum value of the sum is min(d, maximum_possible_value).
    # But what is the maximum possible value of the sum? It is the sum over i of (old_price_i * q_i) if we could take the entire quantity from the new base. But we are limited by d. So the maximum value is min(d, sum_i (old_price_i * q_i)).
    # However, wait: we are allowed to take any amount x_i between 0 and q_i for each product. So the maximum value of the sum without the d constraint is: sum_i (old_price_i * q_i). So if that is less than d, then we can set x_i = q_i for all i, and the sum would be that value. If it is greater than d, then we can only achieve d by taking x_i such that the sum is exactly d? But note: we can take fractional amounts.

    # So the solution is: for each product i, we want to set x_i as large as possible, but without exceeding d in total. So we should rank the products by some criterion? Actually, the objective function is linear: we want to maximize sum_i (old_price_i * x_i). And the constraint is also the same: sum_i (old_price_i * x_i) <= d. But note: the variables x_i are independent and each has an upper bound of q_i. So the maximum value of the sum is achieved by taking x_i = q_i for all i, which gives a total of S = sum_i (old_price_i * q_i). But if S <= d, then the maximum is S.
    # If S > d, then we can only achieve d by taking x_i such that the sum is d. But wait, we don't need to maximize the sum? Actually, we are allowed to set x_i to any value between 0 and q_i. So to maximize the sum subject to the sum being <= d, we can simply set x_i = q_i for all i if S <= d. If S > d, then we need to reduce the x_i such that the sum is d. But note: we are not required to maximize the sum? Actually, we are allowed to set x_i arbitrarily. So if S > d, then the maximum value we can achieve without exceeding d is d itself. Because we can set x_i = (d / S) * q_i? But that would not be per-product. Actually, we can set the x_i arbitrarily as long as the total is <= d. So the maximum value of the sum is min(d, S).

    # However, wait: is that correct? Consider: we want to maximize the sum U = sum_i (old_price_i * x_i). And we have for each product i: 0 <= x_i <= q_i. And we have no other constraints? But wait, there is the constraint that the total must be <= d. So the problem is: maximize U subject to U <= d and U <= S. So the maximum value of U is min(d, S).

    # Therefore, the solution is: for each product i, we set x_i = (d / S) * q_i? But that would yield a total of d if S >= d, and S if S < d. But is that the best we can do? Actually, we are allowed to set x_i arbitrarily as long as x_i <= q_i. So to maximize the total U, we should set x_i as large as possible for the products that have the highest ratio of (old_price_i) per unit? But wait, the objective is linear: U = sum_i (old_price_i * x_i). So to maximize U, we should allocate more x_i to the products that have high old_price_i. But we are limited by d. So we should sort the products by old_price_i (descending) and then assign as much as possible to the products with the highest old_price_i.

    # However, note: the constraint is on the total: sum_i (old_price_i * x_i) <= d. So if we want to maximize U = sum_i (old_price_i * x_i), we are actually trying to maximize the same quantity subject to the same constraint? That seems circular.

    # Actually, the problem is: we want to maximize the unspent money, which is the amount that was allocated for the old base but not spent because we bought from the new base. That amount is exactly U = sum_i (old_price_i * x_i). And we are constrained by U <= d. So the maximum value of U is min(d, S). 

    # But how do we achieve that? We need to choose x_i such that the total U = sum_i (old_price_i * x_i) is as large as possible but not exceeding d. And we also have the constraint that x_i cannot exceed q_i. So the maximum possible value of U is min(d, S). 

    # So if S <= d, then we can set x_i = q_i for all i, and then U = S. 
    # If S > d, then we need to set x_i such that U = d. How? We can set x_i = (d / S) * q_i? That would yield: 
    #   U = sum_i (old_price_i * x_i) = sum_i (old_price_i * (d/S)*q_i ) = (d/S) * sum_i (old_price_i * q_i) = (d/S)*S = d.
    # So that works. 

    # Therefore, the solution is: for each product i, 
    #   if S <= d, then x_i = q_i
    #   if S > d, then x_i = (d / S) * q_i

    # But wait: is that the only way? Actually, we are allowed to set x_i arbitrarily as long as x_i <= q_i. So for the case S > d, we can set x_i = (d / S) * q_i, which will yield a total of d. Alternatively, we can set x_i = q_i for some products and 0 for others, as long as the total is d. But to achieve the maximum U, we need to make sure that the total is d. And the way to achieve that is to set x_i proportional to q_i. 

    # However, is that the only way? Actually, we are not required to maximize U? Wait, we are required to maximize the unspent money, which is U itself. So we want U to be as large as possible. In the case S > d, the maximum U we can achieve is d. So we must set the x_i such that U = d. And one way to do that is to set x_i = (d / S) * q_i. 

    # Therefore, the code is:

    # Step 1: Calculate S = sum_i (old_price_i * q_i)
    # Step 2: If S <= d, then for each i, x_i = q_i
    # Step 3: If S > d,