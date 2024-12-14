from pulp import *
"""
Problem taken from DPV Algorithms (Problem 7.2)

Problem Description: Duckwheat is produced an Kansas and Mexico and consumed in NY and CA.
    Kansas produces 15 shnupells of duckwheat while Mexico produces 8. Meanwhile CA consumes
    10 shnupells and CA 13. The transportation cost per shnupell are $4 from Mexico to NY,
    $1 from Mexico to CA, $2 frome Kansas to NY, and $3 from Kansas to CA.
    
Goal: Number of shnupells from each producer to minimize costs.

x_a = # Mexico --> NY
x_b = # Mexico --> CA
x_c = # Kansas --> NY
x_d = # Kansas --> CA

Minimize 4*x_a + x_b + 2*x_c + 3*x_d

Constraints:

x_a + x_b <= 8
x_c + x_d <= 15
x_a + x_c == 10
x_b + x_d == 13
x_a, x_b, x_c, x_d >= 0

"""

model = LpProblem(sense=LpMinimize)

x_a = LpVariable('x_a', lowBound=0)
x_b = LpVariable('x_b', lowBound=0)
x_c = LpVariable('x_c', lowBound=0)
x_d = LpVariable('x_d', lowBound=0)

model += x_a + x_b <= 8
model += x_c + x_d <= 15
model += x_a + x_c == 10
model += x_b + x_d == 13

model += x_a * 4 + x_b + x_c * 2 + x_d * 3

status = model.solve(PULP_CBC_CMD(msg=False))
print(f"Amount Mexico --> New York = {x_a.value()} Shnupells")
print(f"Amount Mexico --> California = {x_b.value()} Shnupells")
print(f"Amount Kansas --> New York = {x_c.value()} Shnupells")
print(f"Amount Kansas --> California = {x_d.value()} Shnupells")