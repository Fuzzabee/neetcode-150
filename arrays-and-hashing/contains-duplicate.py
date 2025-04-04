def main():
    nums = [1,2,3,3]
    print(hasDuplicate(nums))
    nums = [1,2,3,4]
    print(hasDuplicate(nums))

def hasDuplicate(nums) -> bool:
    frequency = dict()
    for n in nums:
        if n in frequency:
            return True
        else:
            frequency[n] = 1

    return False

if __name__ == "__main__":
    main()