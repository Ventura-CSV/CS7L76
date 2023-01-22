def main():
    ##################################################
    # Comlete your code here
    ##################################################

    inputvalues = input('Enter all elements values: ')
    numbers1 = inputvalues.split()
    for i in range(len(numbers1)):
        numbers1[i] = int(numbers1[i])
    # print("The original list: ", numbers1)

    numbers2 = []
    for i in range(len(numbers1)):
        numbers2.append(numbers1.pop())

    # print("The original list: ", numbers1)
    print("The reverse list: ", numbers2)

    pass


if __name__ == '__main__':
    main()
