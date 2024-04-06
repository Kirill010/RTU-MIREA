import re


def main(string):
    string = string.replace(".do", "")
    string = string.replace(".end", "")
    string = string.replace("store", "")
    pattern = r'([-+]?\w+)'
    data = {}
    matches = re.findall(pattern, string)
    matches.reverse()

    for i in range(len(matches)):
        arr = []
        if re.match(r"[-+]?\d+", matches[i]) is None:
            j = i + 1
            while j < len(matches) and re.match(r"[-+]?\d+",
                                                matches[j]) is not None:
                arr.append(int(matches[j]))
                j += 1
            arr.reverse()
            data[matches[i]] = arr
    return dict(reversed(list(data.items())))


string = ".do <:store[4462 -9763 -420 ] => biorre_972 :> <: store[ -4074 -4935 7283] =>ororce_784:> <: store[ -5397 -6655 5171 ]=> soor :> <: store[7581 -3142 6972 ] => geat:> .end"
string1 = ".do<: store[6582 538]=> beri_642 :> <: store [ -633 2805 -460] =>ente :><: store [5704 3178]=>cema :> <: store [ 4478 3577 -520 ]=>erge:> .end"
result = main(string)
result1 = main(string1)
print(result)
print(result1)
