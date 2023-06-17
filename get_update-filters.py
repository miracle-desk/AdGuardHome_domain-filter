import requests
import ipaddress

def get_update_filter_test(url):
    try:
        r = requests.get(url)
        update_filter_test = r.text.split("\n")
        update_filter_test = [line.replace("||", "").replace("|", "").replace("127.0.0.1", "").replace('- "+.', '').replace('"', '').replace('- ', '') for line in update_filter_test if not line.startswith(('#', "*", '!', '/', ':', '&', 'payload:'))]
        domains = []
        ips = []
        for line in update_filter_test:
            if line:
                if line[0].isdigit():
                    # Jika baris dimulai dengan angka, itu kemungkinan adalah alamat IP
                    try:
                        # Coba parsing IP dengan modul ipaddress
                        ip = ipaddress.ip_network(line.strip().split('$')[0])
                        ips.append(ip.with_prefixlen)
                    except ValueError:
                        # Jika parsing gagal, abaikan baris ini
                        pass
                else:
                    # Jika bukan alamat IP, itu kemungkinan adalah domain
                    domain = line.split("$")[0].strip()
                    if domain.startswith("*."):
                        domain_suffix = domain[2:] + "^"
                        domains.append("@@||*." + domain_suffix)
                    else:
                        domains.append("@@||" + domain)
        rules = [domain + "^" for domain in domains] + ["@@||" + ip for ip in ips]
        return rules
    except Exception as e:
        print(e)
        return None

update_filter_test = get_update_filter_test("https://raw.githubusercontent.com/malikshi/open_clash/main/rule_provider/rule_porn.yaml")
if update_filter_test:
    with open("filter-test.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(update_filter_test))