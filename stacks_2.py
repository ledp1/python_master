def is_paren_balanced(paren_string):
    stack = []
    is_balanced = True
    index = 0
    opening_paren = {')': '(', ']' : '[', '}': '{'} # a matching opening parenthesis for every closing one
    # Traversing all string characters
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            # We met an opening parenthesis, just putting it on stack
            stack.append(paren)
        else:
            # We met a closing parenthesis
            if not stack:
                # The parenthesis is closing, but there are no items in the stack
                is_balanced = False
            else:
                if stack[-1] != opening_paren[paren]:
                    # The parenthesis on top of the stack doesn't match
                    is_balanced = False
                else:
                    stack.pop()
        index += 1
    if stack:
        # If after traversing all characters, there is something left, it's bad
        is_balanced = False
    return is_balanced

print(is_paren_balanced("(())")) # Outputs: True
print(is_paren_balanced("({[)}")) # Outputs: False