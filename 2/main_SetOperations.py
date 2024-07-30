import module_SetOperations as mso

def main():
    s1 = {1, 2, 3}
    s2 = {3, 4, 5}

    print("Add element 4 to s1:", mso.add_element(s1, 4))
    
    print("Remove element 4 from s1:", mso.remove_element(s1, 4))
    
    union, intersection = mso.union_and_intersection(s1, s2)
    print(f"Union of s1 and s2: {union}")
    print(f"Intersection of s1 and s2: {intersection}")
    
    print(f"Difference s1 - s2: {mso.difference(s1, s2)}")
    
    print(f"s1 is a subset of s2: {mso.is_subset(s1, s2)}")
    
    print(f"Length of s1: {mso.set_length(s1)}")
    
    print(f"Symmetric difference of s1 and s2: {mso.symmetric_difference(s1, s2)}")
    
    #print(f"Power set of s1: {mso.power_set(s1)}")
    
    #print(f"Unique subsets of s1: {mso.unique_subsets(s1)}")

if __name__ == "__main__":
    main()
