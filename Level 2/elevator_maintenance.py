#level 2-2
#actually had to do this one
# Python 3.6 version

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

def cmp_helper(x, y):
    return int(x) - int(y)

def cmp_versions(s1, s2):
    v1 = s1.split(".")
    v2 = s2.split(".")

    if len(v1) == 2:
        v1.append("-1")
    elif len(v1) == 1:
        v1.append("-1")
        v1.append("-1")

    if len(v2) == 2:
        v2.append("-1")
    elif len(v2) == 1:
        v2.append("-1")
        v2.append("-1")

    diff = cmp_helper(v1[0], v2[0])
    if diff != 0:
        return diff
    else:
        diff = cmp_helper(v1[1], v2[1])
        if diff != 0:
            return diff
        else:
            return cmp_helper(v1[2], v2[2])

def answer(l):
    return sorted(l, key = cmp_to_key(cmp_versions))

print(answer(["1.1.1", "1.1", "1"]))