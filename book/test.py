if __name__ == '__main__':
    array = [5, 12, 17, 22, 34, 4, 7]
    max = 0
    size = len(array)

    while True:
        n = int(input("Insert number: "))

        for i in range(0, size-1):
            aux = array[i]
            if i <= len(array)-n:
                for j in range(0, n-1):
                    aux += array[i+j+1]
                if aux > max:
                    max = aux

        print(max)
        max = 0
