import module_ListFunction as mlf

def main():
    list1 = [i for i in range(10)]       # List from 0 to 9
    list2 = [i * 2 for i in range(10)]    # List of first 10 even numbers
    list3 = [i**2 for i in range(11)]     # List of squares from 0 to 10
    list4 = [i for i in range(1, 11)]    # List from 1 to 10


    for lst in [list1, list2, list3, list4]:
        print(f"List: {lst}")
        print(f"Max value: {mlf.find_max(lst)}")
        print(f"Min value: {mlf.find_min(lst)}")
        print(f"Sum: {mlf.calculate_sum(lst)}")
        print(f"Average: {mlf.compute_average(lst)}")
        print(f"Median: {mlf.find_median(lst)}")
        print("-"*20)

if __name__ == "__main__":
    main()
