suite = "abcdefghijklmnopqrstuvwxyz" * 10
i = 1
while i <= len(suite):
    print(suite[:i])
    suite = suite[i:]
    i += 1
