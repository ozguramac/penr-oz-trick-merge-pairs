def foo(pl):
    ml = []
    for p in sorted(pl):
        if len(ml) > 0 and ml[-1][1] >= p[0]:
            ml[-1][1] = p[1]
        else:
            ml.append(p)
    return ml


def test(pl, eml):
    ml = foo(pl)
    print("{} => {}".format(pl, ml))
    assert eml == foo(pl)


test([], [])
test([[1, 3]], [[1, 3]])
test([[4, 5], [1, 4]], [[1, 5]])
test([[2, 6], [1, 5], [4, 8], [8, 10], [15, 18]], [[1, 10], [15, 18]])
