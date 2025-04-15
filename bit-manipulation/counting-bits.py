# Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].
# Return an array output where output[i] is the number of 1's in the binary representation of i.

def countBits(n):
    result = [0] * ( n + 1 )
    curN = 0
    curPower = 0
    while curN <= n:
        if 2 ** curPower == curN:
            result[curN] = 1
            curPower += 1
        else:
            lastPow = int(2 ** (curPower - 1))
            result[curN] = result[lastPow] + result[curN - lastPow]
        curN += 1
    return result

def main():
    # Input: n = 4
    # Output: [0,1,1,2,1]
    print(countBits(4))

if __name__ == "__main__":
    main()