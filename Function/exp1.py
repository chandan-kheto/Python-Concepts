def states_num(x, y, z):
  return (x + y + z), (x * y * z), (x - y - z), (x / y / z), (x % y % z)

a, b, c, d, e = states_num(30, 20, 10)
print('sum:',a)
print('mul:',b)
print('sub:',c)
print('div:',d)
print('mod:',e)
