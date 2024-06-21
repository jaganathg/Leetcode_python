def valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            first_char = stack.pop() if stack else "#"
            if mapping[char] != first_char:
                return False
        else:
            stack.append(char)
    return not stack

def isValid( s: str) -> bool:
        stack = []
        special_chars = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in special_chars:
                opposite_char = special_chars[c]
                if len(stack) > 0 and stack[-1] == opposite_char:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        return False

if __name__ == "__main__":
    s = "()"
    print(valid_parentheses(s))
    s = "()[]{}"
    print(valid_parentheses(s))
    s = "(]"
    print(valid_parentheses(s))
    s = "([)]"
    print(valid_parentheses(s))
    s = "{[]}"
    print(valid_parentheses(s))
    