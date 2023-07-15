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
Standard Regular DNS servers
#### server DNS hulu
`https://adguard-dns.io/kb/general/dns-providers/?clid=EksnWn--1tGt9Z--wWTQSv--P3CDXC--A2JJwd--X84IFW--ODXqSW--q1wGpY--fVeSc0--XBz04h--2JBENI--hDHFEk--W9riq5&utm_campaign=dns_kb_providers&utm_medium=ui&utm_source=home`
```yml
https://dns.cloudflare.com/dns-query
https://dns.google/dns-query
tls://1dot1dot1dot1.cloudflare-dns.com
tls://dns.google
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
```

