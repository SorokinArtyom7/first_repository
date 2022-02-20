import sys
from typing import List

def calc(*ip: tuple) -> str:
    """We calculate the masks and take the best option."""
    if len(ip) < 2: 
        raise TypeError(" Need more ip ")
    ip1 = parse(ip[0])
    cur_mask = [0, 0, 0, 0]
    best_mask = [255, 255, 255, 255]
    for i in range(1, len(ip)):
        ip2 = parse(ip[i])
        cur_mask = get_mask(ip1, ip2)
        if cur_mask < best_mask:
            best_mask = cur_mask.copy()
    res = '.'.join(map(str, best_mask)) + '   ' + '.'.join(map(str, get_net(ip1, best_mask)))
    return res

def parse(_str: str) -> List[int]:
    """Divide the IP into 4 octets"""
    buf = _str.split('.')
    buf = [int(x) for x in buf]
    for i in buf:
        if i > 255 or i < 0:
            raise TypeError(" Wrong ip ")
    return buf


def get_mask(_ip1: list, _ip2: list) -> List[int]:
    """Searches for a subnet mask for two IP."""
    mask = [0, 0, 0, 0]
    for i in range(0, 4):
        mask[i] = 255 ^ (_ip1[i] ^ _ip2[i])    # Операция эквиваленции.
        if mask[i] < 255:
            string = str(bin(mask[i]))
            if len(string) < 10:  # Если какая-то из масок, начинаться с нуля...
                mask[i] = 0
            else:
                for j in range(2, len(string)):
                    if string[j] == '0':
                        string = string[:j]+string[j:].replace('1', '0')    # Обрезаем маску после первого нуля.
                        break
                mask[i] = int(string, 2)
            break
    return mask


def get_net(ip1: list, mask: list) -> List[int]:
    """Calculates the subnet address."""
    net = [0, 0, 0, 0]
    for i in range(0, 4):
        net[i] = ip1[i] & mask[i]
    return net

if __name__ == "__main__":
    ips = []
    path = sys.argv[1]
    file = open(path, 'r')
    ipver = sys.argv[2]
    for line  in file:
        ips.append(line)
    file.close()
    print("Вывод маски и минимальной подсети :",calc(*ips))