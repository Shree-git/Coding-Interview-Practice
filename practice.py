def bestSum(arr, target, memo={}):
    if memo.get(target):
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortestCombo = None
    for num in arr:
        remainder = target - num
        remainderCombo = bestSum(arr, remainder, memo)
        if remainderCombo != None:
            combination = [*remainderCombo, num]
            if shortestCombo == None or len(combination) < len(shortestCombo):
                shortestCombo = combination
    memo[target] = shortestCombo
    return shortestCombo


print(bestSum([2, 4], 7))
print(bestSum([2, 4, 5], 8))
print(bestSum([2, 4, 5], 7))
