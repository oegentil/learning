import math

def countTriplets(arr, r):
    dicNumbers = {}
    for  _ in arr:
        if (_ % r) != 0:
            if _ not in dicNumbers.keys():
                dicNumbers[_] = 1
            else:
                dicNumbers[_] += 1

        for key in dicNumbers.key():
            exp = math.log(key,r)
            print(key, dicNumbers[key], key , dicNumber[math.exp(key,(exp + 2)),
                ]


countTriplets(2, [ 1, 2, 2, 4])
countTriplets(3, [ 1, 3, 9, 9, 27, 81])
countTriplets(5, [ 1, 5, 5, 25, 125])
