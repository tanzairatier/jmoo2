

from Problems import Schaffer

prob = Schaffer.Schaffer()
X = [prob.generate_input() for i in range(10)]
Y = [prob.evaluate(x) for x in X]
for x,y in zip(X, Y):
    print(x, "->", y)
    



from jmoo import jmoo

J = jmoo()
J.population_size = 150

print(J.population_size)

