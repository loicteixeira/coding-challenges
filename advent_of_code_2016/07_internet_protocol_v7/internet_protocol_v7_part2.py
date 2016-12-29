import os

from internet_protocol_v7_part1 import split_ip


def is_aba(candidate):
    if len(candidate) != 3:
        return False

    different_middle_letter = candidate[0] != candidate[1]
    same_ends = candidate[0] == candidate[2]
    return different_middle_letter and same_ends


def get_aba_parts(supernet):
    for i in range(len(supernet) - 2):
        group = supernet[i:i + 3]
        if is_aba(group):
            yield group


def inverse(aba):
    # This assume `is_aba == True`
    bab = aba[1] + aba[0] + aba[1]
    return bab


def support_ssl(ip):
    supernet_parts, hypernet_parts = split_ip(ip)

    for supernet in supernet_parts:
        for aba in get_aba_parts(supernet):
            bab = inverse(aba)
            for hypernet in hypernet_parts:
                if bab in hypernet:
                    return True

    return False


def count_ips_with_ssl_support(ips):

    count = 0

    for ip in ips.splitlines():
        if support_ssl(ip):
            count += 1

    return count

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    count = count_ips_with_ssl_support(data)
    print('{count} IPs support SSL'.format(count=count))
