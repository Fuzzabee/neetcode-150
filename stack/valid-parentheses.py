### INSTRUCTIONS ###
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
#     Every open bracket is closed by the same type of close bracket.
#     Open brackets are closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
#
# Return true if s is a valid string, and false otherwise.
#
# Input: s = "[]"
# Output: true
#
# Input: s = "([{}])"
# Output: true
#
# Input: s = "[(])"
# Output: false
####################

def isValid(s):
    stack = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            print(f"add {c}")
            stack.append(c)
        else:
            if not stack: return False
            else:
                lhs = stack.pop()
                if c == ')' and not lhs == '(': return False
                elif c == ']' and not lhs == '[': return False
                elif c == '}' and not lhs == '{': return False

    return len(stack) == 0

def main():
    print(isValid("[]"))
    print(isValid("([{}])"))
    print(isValid("[(])"))
    print(isValid("(]"))

if __name__ == '__main__':
    main()