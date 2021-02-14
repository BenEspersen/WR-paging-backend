def loadNotes():
    with open("./notes.txt") as file:
        data = file.readlines()
    res = ""
    for line in data:
        res += line + "\n"
    return str(res)


def replaceNotes(newNotes):
    with open("./notes.txt", "w") as file:
        file.write(newNotes)
