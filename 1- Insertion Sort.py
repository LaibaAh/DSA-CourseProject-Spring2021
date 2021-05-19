# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.


#Exercise # 2. Read lab manual for details.
##def insertion_sort(list):
##    for i in range(len(list)):
##        j=i
##        while j>0 and list[j]<list[j-1]:
##            list[j],list[j-1]=list[j-1],list[j]
##            j-=1
##    return list

def insertion_sort(list):
    for i in range(len(list)):
        j=i
        for j in range(i,0,-1):
            if list[j]<list[j-1]:
                list[j],list[j-1]=list[j-1],list[j]
    return list
print(insertion_sort([1]))
                
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    # ============================================================================ #

    print()
    print('insertion_sort')
    # Each line calls insertion_sort, compares its result to the expected for that call.
    test(insertion_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]), [17, 20, 26, 31, 44, 54, 55, 77, 93])
    test(insertion_sort(["Aisha", "Nadia", "Ata", "Waqar", "Saleha", "Hasan", "Shahid", "Shah Jamal", "Abdullah", "Neelum", "Umair", "Taj"]),
        ['Abdullah', 'Aisha', 'Ata', 'Hasan', 'Nadia', 'Neelum', 'Saleha', 'Shah Jamal', 'Shahid', 'Taj', 'Umair', 'Waqar'])
    
    # ============================================================================ #

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
