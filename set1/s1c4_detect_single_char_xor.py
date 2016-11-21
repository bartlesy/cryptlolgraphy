from s1c3_crack_single_byte_xor import *


def read_file(fp):
    with open(fp, 'r') as f:
        res = [line.rstrip() for line in f]
    return res


def hax_them_lines(fp):
    all_lines = read_file(fp)
    hax_res = {k: hax_the_gibson(line) for k, line in enumerate(all_lines)}
    best = max(hax_res, key=lambda x: hax_res.get(x)[1][0])
    return best, all_lines[best], hax_res[best]


if __name__ == '__main__':
    fp = './4.txt'
    print(hax_them_lines(fp))

