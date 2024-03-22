m = {
    'INI': {'AWK': {
        'MESON': {
            'ASN.1': 0,
            'URWEB': 1,
            'CSON': 2
        },
        'NL': {
            'ASN.1': 3,
            'URWEB': 4,
            'CSON': 5
        },
        'TWIG': {
            'HACK': 6,
            'HAML': 7,
            'XC': 8
        }
    },
        'IDL': 9

    },
    'NUMPY': 10
}
c = {
    'INI': 3,
    'AWK': 0,
    'MESON': 1,
    'NL': 1,
    'TWIG': 2
}


def main(x):
    global m
    return main1(x, m, 4)


def main1(x, _map, command_number):
    global c
    command = str(x[command_number])
    if type(_map[command]) == dict:
        _map = _map[command]
        return main1(x, _map, c[command])
    elif type(_map[command]) == int:
        return _map[command]
    else:
        raise Exception


arr = ["TWIG", "URWEB", "XC", "IDL", "INI"]
print(main(arr))

arr1 = ["NL", "URWEB", "HACK", "IDL", "NUMPY"]
print(main(arr1))

arr2 = ["MESON", "URWEB", "XC", "AWK", "INI"]
print(main(arr2))

arr3 = ["MESON", "CSON", "XC", "AWK", "INI"]
print(main(arr3))

arr4 = ["NL", "ASN.1", "HAML", "AWK", "INI"]
print(main(arr4))

arr5 = ['TWIG', 'URWEB', 'XC', 'AWK', 'INI']
print(main(arr5))
