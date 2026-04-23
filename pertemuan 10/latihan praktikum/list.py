browser_history = []

def is_empty(stack):
    return len(stack) == 0

def push(stack, url):
    stack.append(url)

def pop(stack):
    if is_empty(stack):
        return "Riwayat kosong"
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        return None
    return stack[-1]

def size(stack):
    return len(stack)