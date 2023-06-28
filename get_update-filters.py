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
                    # jika domain memiliki karakter "github", "tiktok", "pinterest", "twitter", "linkedin", "facebook", "instagram", "whatsapp" maka baris tersebut tidak akan ditambahkan
                    elif any(prefix in domain for prefix in ("github", "pinterest", "pinimg")):
                        continue
                    else:
                        domains.append("||" + domain + "^")
        rules = domains + ["||" + ip for ip in ips]
        return rules
    except Exception as e:
        print(e)
        return None

def get_update_custom_filter(url):
    try:
        r = requests.get(url)
        update_custom_filter = r.text.split("\n")
        keywords = ["github", "pinterest", "pinimg", "twitter"]
        update_custom_filter = [line for line in update_custom_filter if not any(keyword in line for keyword in keywords)]
        return update_custom_filter
    except Exception as e:
        print(e)
        return None
    
update_StevenBlackList_gambling_fakenews_only = get_update_filter("https://raw.githubusercontent.com/miracle-desk/clash_rule-provider/main/rule_StevenBlackList.yaml")
if  update_StevenBlackList_gambling_fakenews_only:
    with open("filter_StevenBlackList-gambling-fakenews-only.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_StevenBlackList_gambling_fakenews_only))

update_Malicious_hosts = get_update_filter("https://raw.githubusercontent.com/elliotwutingfeng/Inversion-DNSBL-Blocklists/main/Google_hostnames.txt")
if  update_Malicious_hosts:
    with open("filter_Malicious-hosts.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_Malicious_hosts))

update_Malicious_ipv4 = get_update_filter("https://raw.githubusercontent.com/elliotwutingfeng/Inversion-DNSBL-Blocklists/main/Google_ipv4.txt")
if  update_Malicious_ipv4:
    with open("filter_Malicious-ipv4.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_Malicious_ipv4))

update_AdGuard_DNS_filter = get_update_custom_filter("https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt")
if  update_AdGuard_DNS_filter:
    with open("filter_AdGuard-DNS.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_AdGuard_DNS_filter))

update_oisd_full = get_update_custom_filter("https://adguardteam.github.io/HostlistsRegistry/assets/filter_27.txt")
if  update_oisd_full:
    with open("filter_oisd-full.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_oisd_full))

update_AdAway = get_update_custom_filter("https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt")
if  update_oisd_full:
    with open("filter_AdAway.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_AdAway))