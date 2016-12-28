import os
import re

IP_SPLIT_PATTERN = re.compile(r'\[|\]')


def split_ip(ip):
    parts = IP_SPLIT_PATTERN.split(ip)

    # Because normal and hypernet parts can't overlap, they alternate.
    # Therefore, they can be grouped by taking even and odd indexes.
    normal_parts, hypernet_parts = parts[::2], parts[1::2]

    # Inverse if the IP started with an hypernet packet.
    if ip[0] == '[':
        normal_parts, hypernet_parts = hypernet_parts, normal_parts

    return normal_parts, hypernet_parts


def has_abba(part):
    for i in range(len(part) - 3):
        same_letter = part[i] == part[i + 1]
        if same_letter:
            continue

        a_match = part[i] == part[i + 3]
        b_match = part[i + 1] == part[i + 2]
        if a_match and b_match:
            return True

    return False


def support_tls(ip):
    normal_parts, hypernet_parts = split_ip(ip)

    # An IP does not support TLS if any hypernet sequence has an ABBA.
    if any(map(has_abba, hypernet_parts)):
        return False

    # An IP support TLS if any normal sequence has an ABBA.
    return any(map(has_abba, normal_parts))


def count_ips_with_tls_support(ips):

    count = 0

    for ip in ips.splitlines():
        if support_tls(ip):
            count += 1

    return count


if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    count = count_ips_with_tls_support(data)
    print('{count} IPs support TLS'.format(count=count))
