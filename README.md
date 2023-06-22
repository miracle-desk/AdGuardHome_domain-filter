# AdGuardHome_domain-filter
[test] domain filter-AdGuardHome
## Daftar block list DNS
```yml
filters:
  - enabled: true
    url: https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/subscriptions/abpindo.txt
    name: 'IDN: ABPindo'

  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/Malicious-hosts.txt
    name: 'Malicious-hosts'

  - enabled: true
    url: https://raw.githubusercontent.com/miracle-desk/AdGuardHome_domain-filter/main/Malicious-ipv4.txt
    name: 'Malicious-ipv4'
```
## Pengaturan DNS
### Quad9 DNS
##### server DNS hulu
```yml
https://dns.quad9.net/dns-query
tls://dns.quad9.net
```
##### server DNS bootstrap
```yml
9.9.9.9
149.112.112.112
2620:fe::fe
2620:fe::fe:9
```

