import math

a = int(input())

if a <= 0:
    print(f"Число {a} не является степенью числа 3.")
else:
    log = math.log(a, 3)
    if math.isclose(log, round(log)):
        print(f"Число {a} является степенью числа 3.")
    else:
        print(f"Число {a} не является степенью числа 3.")
