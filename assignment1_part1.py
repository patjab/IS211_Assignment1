def listDivide(numbers, divide = 2):
    count = 0

    for x in range(0, len(numbers)):
        if numbers[x]%divide == 0:
            count += 1
        else:
            count += 0

    return count


class ListDivideException(Exception):
    pass


def testListDivide():
    try:
        print(listDivide([1,2,3,4,5]))
        print(listDivide([2,4,6,8,10]))
        print(listDivide([30, 54, 63,98, 100], divide=10))
        print(listDivide([]))
        print(listDivide([1,2,3,4,5], 1))
    except:
        raise ListDivideException




testListDivide()