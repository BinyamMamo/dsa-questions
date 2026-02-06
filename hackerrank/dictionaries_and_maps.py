import sys

if __name__ == '__main__':
    n = int(input())
    phone_book = {}
    for _ in range(n):
        name, number = input().split()
        phone_book[name] = number
    
    lines = sys.stdin.readlines()
    for line in lines:
        name = line.strip()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
