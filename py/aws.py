import sys, json, ipaddress
data = json.load(sys.stdin)
for field in data["prefixes"]:
    if field.get("ip_prefix"):
        print("-{}".format(field["ip_prefix"]))
for field in data["ipv6_prefixes"]:
    if field.get("ipv6_prefix"):
        print("~{}".format(field["ipv6_prefix"]))