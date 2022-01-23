import sys

F6=65535

def bin_to_dec(ip):
    """Conversion to decimal system."""
    for j in range(0,8):
        ip[j]="0b"+ str(ip[j])
        ip[j]=int(ip[j],2)
    return ip

def dec_to_hex(list):
    """Conversion to hexadecimal system."""
    for j in range(0,8):
        list[j]=(hex(int(list[j]))[2:].upper())
    return list

def calc(*ip):
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


def parse(_str: str):
    """Divide the IP into 4 octets"""
    buf = _str.split('.')
    buf = [int(x) for x in buf]
    for i in buf:
        if i > 255 or i < 0:
            raise TypeError(" Wrong ip ")
    return buf


def get_mask(_ip1, _ip2):
    """Searches for a subnet mask for two IP."""
    for i in range(0, quantity):
        mask[i] = max ^ (_ip1[i] ^ _ip2[i])    # Операция эквиваленции.
        if mask[i] < max:
            string = str(bin(mask[i]))
            if len(string) < (len_bit+2):  # Если какая-то из масок, начинаться с нуля...
                mask[i] = 0
            else:
                for j in range(2, len(string)):
                    if string[j] == '0':
                        string = string[:j]+string[j:].replace('1', '0')    # Обрезаем маску после первого нуля.
                        break
                mask[i] = int(string, 2)
            break
    return mask


def get_net(ip1, mask):
    """Calculates the subnet address."""
    for i in range(0, quantity):
        net[i] = ip1[i] & mask[i]
    return net

def transform(ip):
    """Making the correct entry"""
    if ':::' in ip:
        raise ValueError("IPv6 address can't contain :::")
    list_ip = ip.split(':') # Делим на 8 хетсетов.
    if len(list_ip) > 8:
        raise ValueError('IPv6 address with more than 8 hexlets')
    elif len(list_ip) < 8:
        # No :: in address
        if '' not in list_ip:
            raise ValueError('IPv6 address invalid: ''compressed format malformed')
        index_0 = list_ip.index('')
        px = len(list_ip[index_0 + 1:]) # Количество чисел после пустого.
        for x in range(index_0 + px + 1, 9): # До 9ти, потому что пустой еще лишний.
            list_ip.insert(index_0 + 1, '0') # Заполняем пустые нулями.
        list_ip.remove('')
    ip=''
    for h in list_ip:
        if len(h) < 4: # Каждая строка списка должна содержать 4-ре символа в 16-ой.
            h = '%04x' % int(h, 16) 
            if not 0 <= int(h, 16) <= 0xffff: 
                raise ValueError('IPv6 address invalid: hexlets should be between 0x0000 and 0xffff')
        ip += h + "." # Делаем обратно общую строку и ставим точки между каждым хетсетом. 
    return(ip)

def parse6(_str):
    """Divide the ip into 8 hetsets"""
    buf = _str.split('.')
    buf.remove('') # Убираем последний лишний элемент.
    buf = [bin(int(x, 16))[2:].zfill(16) for x in buf] # Каждое значение списка, преобразуется в 
# двоичное и с помощью zfill дополняется нулями слева.
    for i in buf:
        if int(i) > 1111111111111111 or int(i) < 0:
            raise TypeError(" Wrong ip ")
    return buf


def calc6(*ip):
    """We calculate the masks and take the best option."""
    if len(ip) < 2:
       raise TypeError(" Need more ip ")
    _str=transform(ip[0])
    ip1=parse6(_str)
    ip1=bin_to_dec(ip1)
    cur_mask = [0, 0, 0, 0, 0, 0, 0, 0]
    best_mask = [F6, F6, F6, F6, F6, F6, F6, F6]
    for i in range(1, len(ip)):
        _str=transform(ip[i])
        ip2 = parse6(_str)
        ip2=bin_to_dec(ip2)
        cur_mask = get_mask(ip1, ip2)
        if cur_mask < best_mask:
            best_mask = cur_mask.copy()
    res = ':'.join(map(str, dec_to_hex(get_net(ip1, best_mask))))
    return res


if __name__ == "__main__":
    ips = []
    path = sys.argv[1]
    file = open(path, 'r')
    ipver = sys.argv[2]
    for line  in file:
        ips.append(line)
    if str(ipver)=="ipv6":
        net = [0, 0, 0, 0, 0, 0, 0, 0]
        mask = [0, 0, 0, 0, 0, 0, 0, 0]
        max=65535
        len_bit=16
        quantity=8
        print(calc6(*ips))
    else:
        net = [0, 0, 0, 0]
        mask = [0, 0, 0, 0]
        max=255
        quantity=4
        len_bit=8
        print(calc(*ips))