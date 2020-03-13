def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [y for x in lists for y in x]


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return sum(1 for x in list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for x in list:
        initial = function(initial, x)
    return initial


def foldr(function, list, initial):
    for x in list[::-1]:
        initial = function(x, initial)
    return initial


def reverse(list):
    return list[::-1]
