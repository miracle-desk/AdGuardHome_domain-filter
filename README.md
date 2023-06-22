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
#### server DNS hulu
```yml
https://security.cloudflare-dns.com/dns-query
tls://security.cloudflare-dns.com
```
#### server DNS bootstrap
```yml
1.1.1.2
1.0.0.2
2606:4700:4700::1112
2606:4700:4700::1002
```

