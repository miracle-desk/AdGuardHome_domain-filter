# AdGuardHome_domain-filter
[test] domain filter-AdGuardHome
## Daftar block list DNS
```yml
filters:
  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/filter_AdGuard-DNS.txt
    name: 'AdGuard DNS filter'

  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/filter_AdAway.txt
    name: 'AdAway Default Blocklist'

  - enabled: true
    url: https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/abpindo.txt
    name: 'IDN: ABPindo'

  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/filter_Malicious-hosts.txt
    name: 'Malicious-hosts'

  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/filter_Malicious-ipv4.txt
    name: 'Malicious-ipv4'

  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/filter_oisd-full.txt
    name: 'OISD Blocklist Big'
    
  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/filter_StevenBlackList-gambling-fakenews-only.txt
    name: 'StevenBlackList-gambling-fakenews-only'
```
## Pengaturan DNS
### Quad9 DNS
Standard Regular DNS servers which provide protection from phishing and spyware. They include blocklists, DNSSEC validation, and other security features
#### server DNS hulu
```yml
https://dns.cloudflare.com/dns-query
https://dns.google/dns-query
https://dns.quad9.net/dns-query
tls://dns.google
tls://dns.quad9.net
```
#### server DNS bootstrap
```yml
1.1.1.1
1.0.0.1
2606:4700:4700::1111
2606:4700:4700::1001
8.8.8.8
8.8.4.4
2001:4860:4860::8888
2001:4860:4860::8844
9.9.9.9
149.112.112.112
2620:fe::fe
2620:fe::fe:9
```

