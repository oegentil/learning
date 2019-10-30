def alternatingCharacters(s):
    count = 0
    while len(s) > 1:
        if s[0] == s[1]:
            count += 1
        s = s[1:]

    return count


def test():
    assert alternatingCharacters("AAAA") == 3
    assert alternatingCharacters("BBBBB") == 4
    assert alternatingCharacters("ABABABAB") == 0
    assert alternatingCharacters("BABABA") == 0
    assert alternatingCharacters("AAABBB") == 4


test()
