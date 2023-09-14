def rev_words(string):
    ans = ""
    for _ in string:
        ans = string.split(".")
    return " ".join(ans[::-1])


string = "this.is.a.cow"
print(rev_words(string))
