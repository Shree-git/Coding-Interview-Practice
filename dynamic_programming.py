import time
import sys
 
sys.setrecursionlimit(20000000)

# Memoization

def fib_r(n):
    if n <= 1:
        return 1
    return fib_r(n-1) + fib_r(n-2)

def fib_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = fib_r(n-1,memo) + fib_r(n-2,memo)
    return memo[n]

def fib_dp(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = fib_r(n-1,memo) + fib_r(n-2,memo)
    return memo[n]

def ways_in_a_grid(x, y, memo={}):
    pos = str(x) + ',' + str(y)
    if pos in memo.keys():
        return memo[pos]
    if x == 1 and y == 1:
        return 1
    if x <= 0 or y <=0:
        return 0
    memo[pos] = ways_in_a_grid(x-1, y) + ways_in_a_grid(x,y-1)
    return memo[pos]

def can_sum(target, numbers, memo={}):
    if target in memo.keys():
        return memo[target]
    if target == 0:
        return True
    if target < 0 :
        return False
    for number in numbers:
        temp = target-number
        if can_sum(temp, numbers, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

def how_sum(target, numbers, memo={}):
    if target in memo.keys():
        return memo[target]
    if target == 0:
        return []
    if target < 0 :
        return 0
    for number in numbers:
        temp = target-number
        if how_sum(temp, numbers, memo) != 0:
            s = how_sum(temp, numbers, memo)
            s.append(number) 
            memo[target] = s
            return memo[target]
    memo[target] = 0
    return 0

def num_sum(target, numbers, memo={}, num=0):
    smallest = []
    if target in memo.keys():
        return memo[target]
    if target == 0:
        return []
    if target < 0 :
        return 0
    for number in numbers:
        temp = target-number
        s = []
        if how_sum(temp, numbers, memo) != 0:
            s = how_sum(temp, numbers, memo)
            s.append(number) 
            memo[target] = s
            return memo[target]
        smallest = min(smallest, len(s))
    memo[target] = 0
    return 0

def can_convert(target:str, words, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in words:
        if target.find(word) == 0:
            s = target.removesuffix(word)
            if can_convert(s, words, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False

def count_convert(target:str, words, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    totalCount = 0
    for word in words:
        if target.find(word) == 0:
            numOfWaysForRest = can_convert(target[len(word):], words, memo)
            totalCount += numOfWaysForRest 

    memo[target] = totalCount
    return totalCount

def total_convert(target:str, words, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in words:
        if target.find(word) == 0:
            s = target.removesuffix(word)
            memo[target].append[word]
                # return memo[target]
    # memo[target] = []
    # return memo[target]

# tic = time.time()
# s = ways_in_a_grid(9,7)
# toc = time.time()
# print(s)
# print(1000*(toc-tic))

# tic = time.time()
# print(sys.getrecursionlimit())
# s = count_convert('potato', ['po', 'ta', 'to', 'o'])
# toc = time.time()
# print(s)

# print(1000*(toc-tic))


# Tabulation

# O(n) time
# O(n) space
def fibT(n):
    arr = [0]*(n+1) 
    arr[0] = 0
    arr[1] = 1
    
    for x in range(len(arr)): # O(n) time
        if x+1 < len(arr):
            arr[x+1] += arr[x]
        if x+2 < len(arr):
            arr[x+2] += arr[x]
        
    return arr[n]

# O(mn) time
# O(n) space
def canSumT(n, numbers):
    arr = [False] * (n+1) # O(n) space
    arr[0] = True
    
    for x in range(len(arr)): # O(n)
        if arr[x]:
            for number in numbers: # O(m) 
                if x + number < len(arr):
                    arr[x+number] = True
    return arr[n]

# O(mn) time
# O(mn) space
def howSumT(n, numbers):
    arr = [None] * (n+1) # O(n) space
    arr[0] = []
    
    for x in range(len(arr)): # O(n)
        if arr[x] != None:
            for number in numbers: # O(m) 
                if x + number < len(arr):
                    arr[x+number] = [*arr[x], number] # O(m) space
    return arr[n]
    
# O(mn) time
# O(mn) space
def bestSumT(n, numbers):
    arr = [None] * (n+1) # O(n) space
    arr[0] = []
    
    for x in range(len(arr)): # O(n)
        if arr[x] != None:
            for number in numbers: # O(m) 
                if x + number < len(arr):
                    combination = [*arr[x], number] # O(m) space
                    if arr[x+number] == None or len(arr[x+number]) > len(combination):
                        arr[x+number] = combination
    return arr[n]
 
# O(mn) time
# O(n) space
def canConstructT(n, words):
    arr = [False] * (len(n)+1) # O(n) space
    arr[0] = True
    
    for x in range(len(arr)): # O(n)
        if arr[x] == True:
            for word in words: # O(m)
                wordLen = len(word)
                if x+wordLen < len(arr) and n[x:x+wordLen] == word:
                    arr[x+wordLen] = True
    return arr[len(n)]
    
# O(mn) time
# O(mn) space
def howConstructT(n, words):
    arr = [None] * (len(n)+1) # O(n) space
    arr[0] = []
    
    for x in range(len(arr)): # O(n)
        if arr[x] != None:
            for word in words: # O(m)
                wordLen = len(word)
                if x+wordLen < len(arr) and n[x:x+wordLen] == word:
                    arr[x+wordLen] = [*arr[x], word] # O(m) space
    return arr[len(n)]
    
# O(mn) time
# O(mn) space
def allConstructT(n, words):
    arr = [None] * (len(n)+1) # O(n) space
    arr[0] = []
    
    for x in range(len(arr)): # O(n)
        if arr[x] != None:
            for word in words: # O(m)
                wordLen = len(word)
                if x+wordLen < len(arr) and n[x:x+wordLen] == word:
                    if arr[x+wordLen] == None:
                        arr[x+wordLen] = []
                    print(arr[x])
                    temp = [*arr[x], word]
                    arr[x+wordLen].append(temp) # O(m) space
    return arr

# O(n^2) time
# O(mn) space
def LIS(array):
    arr = [1] * len(array) # O(n) space
    for x in range(1, len(arr)): # O(n) time
        subproblems = [arr[k] for k in range(x) if array[k] < array[x]] # O(n/2) time, O(m) space
        arr[x] = 1 + max(subproblems, default = 0) # O(n)
    return max(arr)

# def highest(boxes):
#     heights = {box: box[2] for box in boxes}
#     boxes = [box for x in range(len(boxes)) if boxes[x] < box
        

# print(LIS([5,2,8,6,3,6,9,5]))
    
# print(fibT(6))

# print(canSumT(7, [2,5]))

# print(howSumT(7, [2,5]))

# print(bestSumT(7, [2,5,7]))

# print(canConstructT('banana', ['bana', 'na']))

# print(howConstructT('banana', ['bana', 'na']))

print(allConstructT('banana', ['bana', 'ban', 'n', 'ana', 'na', 'b', 'a']))
