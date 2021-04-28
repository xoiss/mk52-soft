def convert(file_1, file_2, file_out):

    def read_origin(file_in):
        # Dumps from sfrolov are raw arrays of bytes strictly following the internal address space of 1/2 of BRP unit.
        return file_in.read() if file_in is not None else bytes(2048)

    def write_derivative(bytes_4096, file_out):
        s = bytes_4096.hex('\t').expandtabs(2)
        # Writes bytes in rows of 8.
        file_out.write(''.join([s[i:i + 8*4].strip() + '\n' for i in range(0, len(s), 8*4)]))

    write_derivative(read_origin(file_1) + read_origin(file_2), file_out)


convert(open('BRP2-1.BIN', 'rb'), open('BRP2-2.BIN', 'rb'), open('brp-2-directly.hex', 'w'))
convert(open('BRP2-1A.BIN', 'rb'), open('BRP2-2A.BIN', 'rb'), open('brp-2-directly-bis.hex', 'w'))

convert(open('brp3-0005-P2-1.BIN', 'rb'), open('brp3-0005-P2-2.BIN', 'rb'), open('brp-2.hex', 'w'))
convert(open('brp3-0005-P2A-1.BIN', 'rb'), open('brp3-0005-P2A-2.BIN', 'rb'), open('brp-2-bis.hex', 'w'))

convert(open('brp3-0005-P1-1.BIN', 'rb'), open('brp3-0005-P1-2.BIN', 'rb'), open('brp-3.hex', 'w'))
convert(open('brp3-0005-P1A-1.BIN', 'rb'), open('brp3-0005-P1A-2.BIN', 'rb'), open('brp-3-bis.hex', 'w'))

convert(open('BRP4-0006-P2-1.BIN', 'rb'), open('BRP4-0006-P2-2.BIN', 'rb'), open('brp-4.hex', 'w'))
convert(open('BRP4-0006-P2-1A.BIN', 'rb'), open('BRP4-0006-P2-2A.BIN', 'rb'), open('brp-4-bis.hex', 'w'))

convert(open('BRP4-0006-P1-1.BIN', 'rb'), open('BRP4-0006-P1-2.BIN', 'rb'), open('brp-5.hex', 'w'))
convert(open('BRP4-0006-P1-1A.BIN', 'rb'), open('BRP4-0006-P1-2A.BIN', 'rb'), open('brp-5-bis.hex', 'w'))
