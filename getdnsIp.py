import socket
import dns.resolver

fqdn = socket.getfqdn()

print("O nome de domínio FQDN deste computador é:");

print(fqdn);

hostName = "www.google.com";

fqdn = socket.getfqdn(hostName);

ip = socket.gethostbyname('www.google.com');

print("O nome de domínio FQDN do %s é:" % hostName);

print(fqdn);

print("O endereço IPv4 do FQDN do %s é:" % hostName);

print(ip);

print("O endereço IPv4 do servidor DNS deste computador é:");

dns_resolver = dns.resolver.Resolver()
dns_resolver.nameservers[0]
print(dns_resolver.nameservers[0]);