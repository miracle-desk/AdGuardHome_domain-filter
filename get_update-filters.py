import requests
import ipaddress

def get_update_filter(url):
    try:
        r = requests.get(url)
        update_filter = r.text.split("\n")
        update_filter = [line.replace("  - DOMAIN,", "").replace("  - DOMAIN-SUFFIX,", "").replace("  - IP-CIDR,", "").replace("://", "").replace("127.0.0.1 ", "").replace("0.0.0.0 ", "").replace("^", "") for line in update_filter if not line.startswith(('#', '!', '/', '@', '-', '&', 'payload:'))]
        domains = []
        ips = []
        for line in update_filter:
            if line:
                if line[0].isdigit():
                    # Jika baris dimulai dengan angka, itu kemungkinan adalah alamat IP
                    try:
                        # Coba parsing IP dengan modul ipaddress
                        ip = ipaddress.ip_network(line.strip().split('$')[0])
                        # Karakter setelah ip / akan di hilangkan + tanda ^
                        ips.append(str(ip).split('/')[0] + "^")
                    except ValueError:
                        # Jika parsing gagal, abaikan baris ini
                        pass
                else:
                    # Jika bukan alamat IP, itu kemungkinan adalah domain
                    domain = line.split("$")[0].strip()
                    if domain.startswith("*."):
                        domain_suffix = domain + "^"
                        domains.append("||" + domain_suffix)                       
                    elif domain.startswith("."):
                        domain_suffix = domain + "^"
                        domains.append("||*" + domain_suffix)
                    elif domain.endswith("."):
                        domain_suffix = domain + "*^"
                        domains.append("||" + domain_suffix)
                    elif domain.startswith("://"):
                        domain_suffix = domain + "^"
                        domains.append("||*." + domain_suffix)
                    else:
                        domains.append("||" + domain + "^")
        rules = domains + ["||" + ip for ip in ips]
        return rules
    except Exception as e:
        print(e)
        return None
    
update_StevenBlackList_gambling_fakenews_only = get_update_filter("https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_StevenBlackList.yaml")
if  update_StevenBlackList_gambling_fakenews_only:
    with open("StevenBlackList-gambling-fakenews-only.txt", "w", encoding='utf-8') as f:
        f.write("\n".join( update_StevenBlackList_gambling_fakenews_only))

update_Malicious_hosts = get_update_filter("https://raw.githubusercontent.com/elliotwutingfeng/Inversion-DNSBL-Blocklists/main/Google_hostnames.txt")
if  update_Malicious_hosts:
    with open("Malicious-hosts.txt", "w", encoding='utf-8') as f:
        f.write("\n".join( update_Malicious_hosts))

update_Malicious_ipv4 = get_update_filter("https://raw.githubusercontent.com/elliotwutingfeng/Inversion-DNSBL-Blocklists/main/Google_ipv4.txt")
if  update_Malicious_ipv4:
    with open("Malicious-ipv4.txt", "w", encoding='utf-8') as f:
        f.write("\n".join( update_Malicious_ipv4))