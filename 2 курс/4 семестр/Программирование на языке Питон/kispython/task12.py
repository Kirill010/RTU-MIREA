from struct import unpack_from, calcsize


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


class BinaryReader:
    def __init__(self, stream, offset, order=">"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.int16)
    d2_size = reader.read(Types.uint32)
    d2_offset = reader.read(Types.uint32)
    d2_reader = reader.jump(d2_offset)
    d2 = [d2_reader.read(Types.uint16) for _ in range(d2_size)]
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.int32)
    c2 = reader.read(Types.int8)
    c3 = reader.read(Types.int32)
    c4_size = reader.read(Types.uint16)
    c4_offset = reader.read(Types.uint32)
    c4_reader = reader.jump(c4_offset)
    c4 = [c4_reader.read(Types.int16) for _ in range(c4_size)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1 = read_c(reader)
    b2 = reader.read(Types.uint16)
    b3 = reader.read(Types.int8)
    b4 = reader.read(Types.int8)
    b5 = reader.read(Types.uint32)
    b6 = reader.read(Types.uint8)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6)


def read_a(reader):
    a1 = reader.read(Types.int32)
    a2 = reader.read(Types.uint8)
    a3 = [reader.read(Types.char) for _ in range(5)]
    a3 = b"".join(a3).decode("utf-8")
    a4 = reader.read(Types.int32)
    a5 = reader.read(Types.uint64)
    a6 = [read_b(reader) for _ in range(3)]
    a7 = read_d(reader)
    a8_size = reader.read(Types.uint32)
    a8_offset = reader.read(Types.uint32)
    a8_reader = reader.jump(a8_offset)
    a8 = [a8_reader.read(Types.uint16) for _ in range(a8_size)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(stream):
    return read_a(BinaryReader(stream, 4))


binary_data = (b'UPBU\x15^v%\xd2qyctr\x083\xc9\xf8\xca"\xc4s\x10\x1e\xee\xaft\x05Tt\xd6\xb0'
               b'\xc0\r\xef\x00\x03\x00\x00\x00t\xd3\xe2\x96W\xfd\xb5q\xcd\xcc\x0e\xf1'
               b'B"\x82\xf4\xea\xa4i\x00\x02\x00\x00\x00z\xac\xb8\xa8\x92\xb3\x8f\x90'
               b'\x06N\xcd\xf5\x88E\x84X7\xa4\x92\x00\x03\x00\x00\x00~p\xa5\xc4\x99\xa3K\xdf'
               b'\xcf\xcc\x18a\x00\x00\x00\x05\x00\x00\x00\x84\x00\x00\x00\x05'
               b'\x00\x00\x00\x8e\xfc\xfb\xf7\xc6\x04\xb5Op\xee>\x03T>\xc3\x98\xdd'
               b'\xfa\x96\x18$\xff\x13\x9d\x9c6\xd16EYA\xc1\x0b\xd8\r&\xc2')

result = main(binary_data)
print(result)
