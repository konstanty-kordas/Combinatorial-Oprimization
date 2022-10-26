import pprint
from copy import deepcopy
from random import randint


def ex1():
    vertices = [[randint(0,100) for k in range(10)] for l in range(10)]
    for i in range(10):
        for j in range(i+1):
            if i==j:
                vertices[i][j]=float('inf')
                continue
            vertices[j][i] = vertices[i][j]


    def TSPSolve(vertices):

        for i in range(10):
            v2 = deepcopy(vertices)
            visited = set([i])
            current_vertex = i
            current_pathlen = 0
            while(len(visited)) < 10:
                next = v2[current_vertex].index(min(v2[current_vertex]))
                current_pathlen+= v2[current_vertex][next]
                v2[current_vertex][next] = float('inf')
                v2[next][current_vertex] = float('inf')
                current_vertex = next
                visited.add(next)
                # pprint(vertices)
                # break
            print(current_pathlen)

    # pprint(vertices)
    # TSPSolve(vertices)

def ex2():
    items = [(randint(1,100),randint(1,100)) for k in range(10)]
    cap = randint(0,250)
    def GreedyKnapsack(n, capacity,items):
        solution = []
        density = []
        for i in range(n):
            density.append((i,items[i][0]/items[i][1]))
        s = 0
        density.sort(key=lambda x: x[1],reverse=True)
        while True:
            c = density.pop(0)
            if s+items[c[0]][1] > capacity:
                break
            solution.append(c[0])
            s+=items[c[0]][1]
        print(s)
        print(solution)


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
        return knapsack_table[i][j]
        
    print(knapsack_problem(10,cap,items))
    GreedyKnapsack(10,cap,items)
    pprint.pprint(items)
    print("capacity", cap)


activities = [(randint(0,23),randint(1,3)) for k in range(10)]
i=0
while i <len(activities):
    if sum(activities[i])>24:
        activities.pop(i)
        i-=1
    i+=1
activities.sort()
curr = 0
d = []
print(activities        )
while curr<24 and len(activities)!=0:
    next = activities.pop(0)
    if next[0]<curr:
        continue
    if next[0]>curr:
        curr=next[0]
    curr+=next[1]
    d.append(next)
print(d)
