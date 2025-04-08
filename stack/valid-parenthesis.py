# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

def isValid(s):
    stack = []

    for c in s:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        
        # If we aren't an opening parenthesis and stack is empty, it is not valid
        elif not stack: return False
        
        if c == ']':
            if stack.pop() != '[':
                return False
        elif c == '}':
            if not stack or stack.pop() != '{':
                return False
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False

    if stack: return False
    return True

def main():
    # Input: s = "[]"
    # Output: true
    s = "[]"
    print(isValid(s))

    # Input: s = "([{}])"
    # Output: true
    s = "([{}])"
    print(isValid(s))

    # Input: s = "[(])"
    # Output: false
    s = "[(])"
    print(isValid(s))

if __name__ == "__main__":
    main()