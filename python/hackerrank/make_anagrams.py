def make_anagrams(string_a, string_b):
    dic_a = {}
    dic_b = {}
    for i in string_a:
        if i in dic_a:
            dic_a[i] += 1
        else:
            dic_a[i] = 1
    for j in string_b:
        if j in dic_b:
            dic_b[j] += 1
        else:
            dic_b[j] = 1

    diff = 0
    for key in dic_a:
        if key in dic_b:
            diff += abs(dic_a[key] - dic_b[key])
        else:
            diff += dic_a[key]
    for key in dic_b:
        if key not in dic_a:
            diff += dic_b[key]
    print(diff)
    return diff


def test():
    assert make_anagrams("cde", "abc") == 4
    assert make_anagrams("cde", "dcf") == 2
    assert make_anagrams("fcrxzwscanmligyxyvym",
                         "jxwtrhvujlmrpdoqbisbwhmgpmeoke") == 30
    assert make_anagrams("showman", "woman") == 2


test()
