# Faab Reducer FUnction Test

x = [5, 4, 6, 7, 40, 5]
faab = 40
print(len(x))


def test():
    global faab
    global x
    i = 0

    while faab > 0:                    # If you have faab
        while sum(x) > len(x):         # if the sum of all salaries is greater than the number of players
                                            # Goal is to see if all $1
            while x[i] == 1:            # when a salary = 1 skip
                i = i + 1
                continue

            else:
                if faab > 0:
                    x[i] = x[i] - 1         # reduce Salary
                    faab = faab - 1          # reduce faab
                    i = i + 1               # next entry
                    print("my faab" + str(faab))
                    print(x)
                    if i >= (len(x) - 1):  # when we reach the last entry
                        i = 0
                        continue
                    continue            # reset to 0
                break

        else:
            print("Salaries are all $1")
            break

    else:
        print("Out of Faab")


test()
