import sys, json, ipaddress
data = json.load(sys.stdin)
fields = ['hooks', 'web', 'api', 'git', 'packages', 'pages', 'importer']
for f in fields:
    print("#", f)
    for ip in data[f]:
        try:
            ip_addr = ipaddress.ip_network(ip)
            pre = isinstance(ip_addr, ipaddress.IPv4Network) and "-" or "~"
            print("{}{}".format(pre, ip_addr))
        except ValueError:
            # print("Invalid IP address: {}".format(ip))
            pass