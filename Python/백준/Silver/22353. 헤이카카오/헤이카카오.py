a, d, k = map(int, input().split())

def expected_time(d):
    if d >= 100:
        return a
    tmp = d * 0.01 * a + (1 - 0.01 * d) * (a + expected_time(d * (1 + k * 0.01)))
    return tmp

print('%.10f' % expected_time(d))