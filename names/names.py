#
# Dependencies
#

import time

#
# Define method
#

def checkDuplicates():
    start_time = time.time()

    f = open('names_1.txt', 'r')
    names_1 = f.read().split("\n")  # List containing 10000 names
    f.close()

    f = open('names_2.txt', 'r')
    names_2 = f.read().split("\n")  # List containing 10000 names
    f.close()

    duplicates = []
    for name_1 in names_1:
        for name_2 in names_2:
            if name_1 == name_2:
                duplicates.append(name_1)

    end_time = time.time()
    print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
    #=> 64 duplicates: ...
    print (f"runtime: {end_time - start_time} seconds")
    #=> runtime: 1.871626377105713 seconds

#
# Run method
#

if __name__ == '__main__':
    checkDuplicates()
