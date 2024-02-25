def perms(lst):
    if len(lst) == 0:
        return [[]]
    elif len(lst) == 1:
        return [lst]

    res = []
    for i in range(len(lst)):
        cur = lst[i]
        rest = lst[:i] + lst[i+1:]
        rest_perms = perms(rest)
        for p in rest_perms:
            if isinstance(p, int):
                p = [p]
            num = int(str(cur) + ''.join(str(x) for x in p))
            res.append(num)

    return res

def next_permutation(n, lst):
    perms_list = sorted(perms(lst))
    for i in range(len(perms_list)):
        if perms_list[i] == n:
            if i == len(perms_list) - 1:
                return "No greater permutation"
            else:
                return perms_list[i + 1]

elems = [1, 2, 3]
n = int(''.join(map(str, elems)))
result = next_permutation(n, elems)
print(result)
