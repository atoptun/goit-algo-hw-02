from collections import deque


def is_palindrome(line: str):
    cleared = ''.join([ch.lower() for ch in line if ch.isalnum()])
    dq = deque(cleared)
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True

def main():
    lines = [
        'Я несу гусеня.',
        'Аргентина манить негра.',
        'A man, a plan, a canal, Panama!',
        'Was it a car or a cat I saw?',
    ]
    for line in lines:
        res = is_palindrome(line)
        print(f'"{line}" -- {res} ')


if __name__ == '__main__':
    main()
