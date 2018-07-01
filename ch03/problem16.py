n = input('n : ')

prepre = 1
pre = 1

for i in range(0, n - 2):
    now = prepre + pre
    prepre = pre
    pre = now
print(pre)
