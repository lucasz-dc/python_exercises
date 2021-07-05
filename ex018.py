import math

a = float(input('Digite um ângulo: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O ângulo de {}° tem o SENO de {:.2f}'.format(a, s))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(a, c))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(a, t))
