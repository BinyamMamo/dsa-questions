if __name__ == '__main__':
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    rotated = arr[d:] + arr[:d]
    print(*rotated)
