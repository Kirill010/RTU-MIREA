class MealyError(Exception):
    pass


class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def slog(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'C':
            self.state = 'D'
            return 4
        elif self.state == 'D':
            self.state = 'E'
            return 5
        elif self.state == 'E':
            self.state = 'F'
            return 6
        elif self.state == 'G':
            self.state = 'H'
            return 8
        else:
            raise MealyError("slog")

    def scan(self):
        if self.state == 'B':
            self.state = 'D'
            return 2
        elif self.state == 'F':
            self.state = 'G'
            return 7
        elif self.state == 'G':
            self.state = 'A'
            return 9
        else:
            raise MealyError("scan")

    def sit(self):
        if self.state == 'G':
            return 10
        elif self.state == 'B':
            self.state = 'H'
            return 3
        elif self.state == 'H':
            self.state = 'D'
            return 11
        else:
            raise MealyError("sit")


def main():
    return MealyMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.slog() == 0  # A -> B
    o.state = 'B'
    assert o.slog() == 1  # B -> C
    o.state = 'C'
    assert o.slog() == 4  # C -> D
    o.state = 'D'
    assert o.slog() == 5  # D -> E
    o.state = 'E'
    assert o.slog() == 6  # E -> F
    o.state = 'F'
    assert o.scan() == 7  # F -> G
    o.state = 'G'
    assert o.slog() == 8  # G -> H
    o.state = 'H'
    assert o.sit() == 11  # H -> D
    raises(lambda: o.sit(), MealyError)
    o.state = 'B'
    assert o.scan() == 2  # B -> D
    o.state = 'D'
    assert o.slog() == 5  # D -> E
    o.state = 'E'
    assert o.slog() == 6  # E -> F
    o.state = 'F'
    assert o.scan() == 7  # F -> G
    o.state = 'G'
    assert o.sit() == 10  # G -> G
    o.state = 'G'
    assert o.scan() == 9  # G -> A
    raises(lambda: o.scan(), MealyError)
    o = main()
    assert o.slog() == 0  # A -> B
    o.state = 'B'
    assert o.sit() == 3  # B -> H
    o.state = 'H'
    assert o.sit() == 11  # H -> D
    o.state = 'D'
    assert o.slog() == 5  # D -> E
    o.state = 'E'
    assert o.slog() == 6  # E -> F
    o.state = 'F'
    assert o.scan() == 7  # F -> G
    o.state = 'G'
    assert o.sit() == 10  # G -> G
    o.state = 'G'
    assert o.slog() == 8  # G -> H
    raises(lambda: o.slog(), MealyError)


test()
