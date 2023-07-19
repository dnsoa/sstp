import sys, json, ipaddress
data = json.load(sys.stdin)
for field in data["prefixes"]:
    if field.get("ipv4Prefix"):
        print("-{}".format(field["ipv4Prefix"]))
    if field.get("ipv6Prefix"):
        print("~{}".format(field["ipv6Prefix"]))