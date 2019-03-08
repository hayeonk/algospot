def ways_to_buy(psum, k):
    ret = 0
    MOD = 20091101
    count = [0 for i in range (k)]

    for i in range (len(psum)):
        count[psum[i]] += 1

    for i in range (k):
        if count[i] >= 2:
            ret = (ret + count[i] * (count[i]-1) / 2) % MOD

    return ret

def max_buys(psum, k):
    ret = [0 for i in range (len(psum))]
    prev = [-1 for i in range (k)]

    for i in range (len(psum)):
        if i > 0:
            ret[i] = ret[i-1]

        loc = prev[psum[i]]
        if loc != -1:
            ret[i] = max(ret[i], ret[loc] + 1)
        prev[psum[i]] = i

    return ret[-1]

for i in range (input()):
    n, k = map(int, raw_input().split())
    D = map(int, raw_input().split())

    psum = [0]
    for i in range (len(D)):
        psum.append((psum[-1] + D[i]) % k)

    print ways_to_buy(psum, k), max_buys(psum, k)