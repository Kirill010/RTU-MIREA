def main(n):
    if n == 0:
        return 0.01
    elif n >= 1:
        return (main(n - 1) ** 2) + 83 * (main(n - 1) ** 2) + (main(n - 1) ** 3)


print(main(3))
print(main(6))
print(main(7))
print(main(4))
print(main(8))
