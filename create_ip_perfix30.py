import ipaddress

def generate_subnets(ip_range):
    network = ipaddress.ip_network(ip_range)
    subnets = list(network.subnets(new_prefix=30))

    result = []
    for subnet in subnets:
        result.append(str(subnet))

    return result

input_range = '172.16.10.0/24'
subnets = generate_subnets(input_range)

for subnet in subnets:
    print(subnet)