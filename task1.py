# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = 2000

pi_num = 4 * (sum(1/x for x in range(1, d + 1, 4)) + sum(-1/x for x in range(3, d + 1, 4)))

print(round(pi_num, 3))

#===================
# import math
# from math import pi

# n = pi
# print(n)