inp = input("Enter Input : ").split("/")
fir, sec, ans = [int(i) for i in inp[0].split()], inp[1].split(","), 0
ans = sum(fir)
print(ans)

for i in sec:
    a, b = int(i.split(" ")[0]), int(i.split(" ")[1])
    if 2*a+1 >= len(fir):
        a1 = 0
    else:
        a1 = fir[2*a+1]
    if 2*a+2 >= len(fir):
        a2 = 0
    else:
        a2 = fir[2*a+2]
    if 2*b+1 >= len(fir):
        b1 = 0
    else:
        b1 = fir[2*b+1]
    if 2*b+2 >= len(fir):
        b2 = 0
    else:
        b2 = fir[2*b+2]
    sum_a = fir[a] + a1 + a2
    sum_b = fir[b] + b1 + b2
    if sum_a > sum_b:
        print(f'{a}>{b}')
    elif sum_a < sum_b:
        print(f'{a}<{b}')
    else:
        print(f'{a}={b}')