def convert(file_1, file_2, file_out):

    def read_origin(file_in):
        s = '\t'.join(map(lambda x: x.rstrip('\n'), file_in.readlines() if file_in is not None else []))
        h = list(filter(lambda x: bool(x), s.split('\t')))
        for i in range(0, len(h), 7):
            h[i:i + 7] = h[i + 1:i + 7] + h[i:i + 1]
        # Dumps from apgor are arrays of hex-codes (bytes) as they are placed in Elektronika MK-52 RAM.
        # They must be permuted (rotated in groups of 7) to following the internal address space of 1/2 of BRP unit.
        return h

    def write_derivative(hexcodes_4096, file_out):
        s = '  '.join(hexcodes_4096).lower()
        # Writes bytes in rows of 8.
        file_out.write(''.join([s[i:i + 8*4].strip() + '\n' for i in range(0, len(s), 8*4)]))

    write_derivative(read_origin(file_1) + read_origin(file_2), file_out)


convert(open('brp3-1.txt', 'r'), open('brp3-2.txt', 'r'), open('brp-3-apgor.hex', 'w'))

convert(open('brp4p2-1.txt', 'r'), open('brp4p2-2.txt', 'r'), open('brp-4-apgor.hex', 'w'))

convert(open('brp4p1-1.txt', 'r'), open('brp4p1-2.txt', 'r'), open('brp-5-apgor.hex', 'w'))
