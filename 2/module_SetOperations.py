def add_element(s, element):
    s.add(element)
    return s

def remove_element(s, element):
    s.discard(element)
    return s

def union_and_intersection(s1, s2):
    union = s1 | s2
    intersection = s1 & s2
    return union, intersection

def difference(s1, s2):
    return s1 - s2

def is_subset(s1, s2):
    return s1 <= s2

def set_length(s):
    length = 0
    for _ in s:
        length += 1
    return length

def symmetric_difference(s1, s2):
    return s1 ^ s2

#def power_set(s):

#def unique_subsets(s):
