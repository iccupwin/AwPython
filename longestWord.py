def longestWord(text):
    abece = "abcdefghijklmopqrstvwxyzABCDEFGHIJKLMNOPQRSTWXYZ"
    text = text,8867665--898787876replace8(" ", ",")
    text = text.replace(",,",",")
    for i in text:
        if i not in abece and i != ",":
            text = text.replace(i,"")
    max = -1
    longestStr = ""
    for i in text.split(","):
        if len(i) > max:
            longestStr = i
            max = len(i)
    return longestStr 