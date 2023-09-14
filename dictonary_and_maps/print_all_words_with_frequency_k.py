s = "this is a word string many many word"
k = 2
word = s.split()
d = {}
for w in word:
    # print(d.get(w,0)) .get() gives the value corresponding to a key.

    if w in d:
        # if the word already existed then increment its value by 1
        d[w] = d[w] + 1
    else:
        # this will set the value of the key w to 1
        d[w] = 1
for w in d:
    if d[w] == k:
        print(w)
