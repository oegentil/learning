def checkMagazine(magazine, note):
    possible = False
    dicNote = {}
    dicMag = {}
    for _ in note:
        if _ in dicNote.keys():
            dicNote[_] += 1
        else:
            dicNote[_] = 1

    for _ in magazine:
        if _ in dicMag.keys():
            dicMag[_] += 1
        else:
            dicMag[_] = 1

    for _ in dicNote.keys():
        # print(_, dicNote[_], magazine.count(_))
        if (_ in dicMag.keys()) and (dicNote[_] <= dicMag[_]):
            possible = True
        else:
            possible = False
            break
    if possible is True:
        print("Yes")
    else:
        print("No")


def test():
    assert checkMagazine(
        ["two", "times", "three", "is", "not", "four"],
        ["two", "times", "two", "is", "four"])


checkMagazine(
    ["two", "times", "three", "is", "not", "four"],
    ["two", "times", "two", "is", "four"])
checkMagazine(
    ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"],
    ["ive", "got", "some", "coconuts"])
