def twoStrings(s1, s2):
    ss1 = set()
    ss2 = set()
    for _ in s1:
        ss1.add(_)
    for _ in s2:
        ss2.add(_)
    if ss1.intersection(ss2):
        print("YES")
    else:
        print("NO")


twoStrings(
    "wouldyoulikefries",
    "abcabcabcabcabcabc")
twoStrings(
    "hackerrankcommunity",
    "cdecdecdecde")
twoStrings(
    "jackandjill",
    "wentupthehill")
twoStrings(
    "writetoyourparents",
    "fghmqzldbc")
