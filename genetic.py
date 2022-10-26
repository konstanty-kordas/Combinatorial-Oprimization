import numpy as np

values = np.random.random(10)


def generate():
    a = np.arange(10)
    np.random.shuffle(a)
    solution = ( a, np.random.randint(0,10))
    return solution


def evaluate(solution) -> float:
    solution, split = solution
    s1 = solution[split:]
    s2 = solution[:split]
    # print(s1, s2)
    a1 = sum([values[i] for i in s1])
    a2 = sum([values[i] for i in s2])
    return abs(a1-a2)

def small_mutate(solution):
    x = solution[1]
    x += 5-np.random.binomial(10,1/2)
    if x>10:
        x=10
    if x<0:
        x=0
    return (solution[0],x)


generation = [generate() for i in range(100)]
probs = []
s = sum(evaluate(i) for i in generation)
print(s)
for j in generation:
    probs.append(evaluate(j)/s)
print(probs)
print(sum(probs))
rng = np.random.default_rng()
print(rng.choice(100,p=probs,size=25))
# return 


