# Faab Reducer FUnction Test

x = [5,4,6,7,4,5]
faab = 40
print(len(x))

def test():
    global faab
    global x
    i = 0

    while faab >= 0:
        while sum(x) >= len(x):

            while x[i] == 1:
                i = i + 1

            else:
                x[i] = x[i] - 1
                faab = faab -1
                i = i + 1
                print("my faab" + str(faab))
                print("salary " + str(x[i]))
                print(x)
                if i >= ( len(x) - 1):
                    i = 0

        else:
            print("Salaries are all $1")
            break

    else:
        print("Out of Faab")



test()
