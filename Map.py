students = ["jay", "loga", "kishore", "krishna", "parithiran", "navin"]


def find(name):
    if name == "jay":
        return "Match found"
    elif name == "navin":
        return "poor"
    else:
        return "Not found"


result = map(find, students)
print(list(result))
