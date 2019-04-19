for i in range (input()):
    n, k = [int(x) for x in raw_input().split()]
    def josephus (n, k):
        survivors = range(1, n+1)
        kill_idx = 0
        while len(survivors) > 2:
            survivors.pop(kill_idx)
            kill_idx += k-1
            kill_idx %= len(survivors)
        return survivors
    idx_1, idx_2 = josephus (n, k)
    print idx_1, idx_2