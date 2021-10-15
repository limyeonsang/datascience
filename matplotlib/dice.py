import random
import matplotlib.pyplot as plt

def sum(num):
    result = []
    for _ in range(0, num):
        a = random.randint(1,6)
        b = random.randint(1,6)
        result.append(a+b)

    plot(result) 

def plot(result):
    plt.scatter(range(1,501), result )
    plt.show()

sum(500)

