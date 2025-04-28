def solution(s):
    stack = []
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack:
                return False
            top = stack.pop()
            
            if pairs[top] != char:
                return False
    
    return True


if __name__ == "__main__":
    s = input()
    result = solution(s)
    print(result)