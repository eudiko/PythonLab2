def merging_Dict(*args):
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args):
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for d in args[1:]:
        common_keys_set.intersection_update(d.keys())
    return common_keys_set

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

def common_key_value_pairs(*args):
    if not args:
        return {}
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs.intersection_update(d.items())
    return dict(common_pairs)

def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 5}
    dict3 = {'c': 3, 'd': 5, 'e': 6}

    merged = merging_Dict(dict1, dict2, dict3)
    print(f"Merged dictionary: {merged}")

    common_keys_result = common_keys(dict1, dict2, dict3)
    print(f"Common keys: {common_keys_result}")

    inverted = invert_dict(dict1)
    print(f"Inverted dictionary: {inverted}")

    common_pairs = common_key_value_pairs(dict1, dict2, dict3)
    print(f"Common key-value pairs: {common_pairs}")

if __name__ == "__main__":
    main()
