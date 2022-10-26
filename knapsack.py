import pprint

number_of_items = 0
capacity = 0
item = (0,0)
items = []
with open("input.txt","r") as f:
    number_of_items, capacity = [int(k) for k in f.readline().split()]
    for i in range(number_of_items):
        item = [int(k) for k in f.readline().split()]
        item = tuple(item)
        items.append(item)

def knapsack_problem(n, capacity, items):
    knapsack_table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]     
    for i in range(n+1):
        for j in range(capacity+1):
            if j==0 or i==0:
                knapsack_table[i][j]=0
                continue
            item_value = items[i-1][0]
            item_size = items[i-1][1]
            # print(item_value,item_size)
            if item_size>j:
                knapsack_table[i][j] = knapsack_table[i-1][j]
                continue
            # pprint.pprint(knapsack_table)
            knapsack_table[i][j] = max(knapsack_table[i-1][j], knapsack_table[i-1][j-item_size]+item_value)
    return knapsack_table
    
pprint.pprint(knapsack_problem(5,capacity,items))

def set_partition_problem(items):
    capacity = int(sum(items)/2)
    n = len(items)
    print(capacity)
    print(n)
    knapsack_table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]     
    for i in range(n+1):
        for j in range(capacity+1):
            if j==0 or i==0:
                knapsack_table[i][j]=0
                continue
            item_value = items[i-1]
            item_size = 1
            if item_size>j:
                knapsack_table[i][j] = knapsack_table[i-1][j]
                continue
            knapsack_table[i][j] = max(knapsack_table[i-1][j], knapsack_table[i-1][j-item_size]+item_value)
    print(knapsack_table)
    if knapsack_table[n][capacity]==capacity:
        return True
    return False
    return knapsack_table

print(set_partition_problem([1,5,11,5]))


