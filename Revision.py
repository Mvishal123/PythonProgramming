def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                return False
        return True

print(isPrime(16))

def bs(ls, target):
    start = 0
    end = len(ls) - 1

    if(ls[start] < ls[end]):
        while start <= end:
            mid = int((start + (end - start) / 2))
            if ls[mid] == target:
                return mid

            elif ls[mid] > target:
                end = mid - 1

            else:
                start = mid + 1
    else:
        while start <= end:
            mid = int((start + (end - start) / 2))
            if ls[mid] == target:
                return mid

            elif ls[mid] > target:
                start = mid + 1

            else:
                end = mid - 1

    return -1


ls1 = [1,2,3,4,5,6,7,8,9]
ls2 = ls1[::-1]
print(bs(ls2, 2))

def finder(nums, target):
    for n1 in nums:
        for n2 in nums:
            if (n2 != n1):
                if n1 + n2 == target:
                    return [n1, n2]

    return -1

def finder2(nums, target):
    dict = {}
    for i, n in enumerate(nums):
        if n in dict:
            return [dict[n], i]
        else:
            dict[target - n] = i

nums = [2, 7, 11, 15]
target = 18

print(finder2(nums, target))

Bubble sort
def b_sort(ls):
    for i in range(len(ls) - 1):
        swapped = False
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1]:
                swapped = True
                temp = ls[j]
                ls[j] = ls[j+1]
                ls[j+1] = temp
        if not swapped:
            return

def largest(ls):
    l = 0
    for i in range(1,len(ls) - 1):
        if ls[i] > ls[l]:
            l = i
    return l

def selection_sort(ls):
    for i in range(len(ls) - 2):
        maxi = largest(ls[:len(ls) - i])
        temp = ls[len(ls) - 1 - i]
        ls[len(ls) - 1 - i] = ls[maxi]
        ls[maxi] = temp




ls = [3, 2, 1, 5, 12, -1]
print("unsorted:", ls)
selection_sort(ls)
print("sorted:", ls)

def selectionSort(ls):
    for i in range(len(ls) - 1):
        j = i + 1
        while j > 0:
            if ls[j] < ls[j-1]:
                temp = ls[j]
                ls[j] = ls[j-1]
                ls[j-1] = temp
                j -= 1
            else:
                break

ls = [4, 3, 5, 2, 1]
print(ls)

def cyclicSort(ls):
    for n in range(len(ls) - 1):
        temp = ls[n]
        ls[n] = ls[temp - 1]
        ls[temp - 1] = temp

    return ls

ls = [5, 4, 3, 2, 1]
print(cyclicSort(ls))


def numIdenticalPairs(nums):
    count = 0
    for i in range(len(nums)):
        j = i + 1
        while j <= len(nums) - 1:
            if (nums[i] == nums[j]):
                count += 1
            j += 1

    return count

ls = [1,1,1,1]
print(numIdenticalPairs(ls))