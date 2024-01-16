from utils.dns_client import DnsClient
import socket


def get_ipv6():
    hostname = socket.gethostname()
    addr_v6s = socket.getaddrinfo(hostname, None, socket.AF_INET6)
    ipv6s = []
    for addr in addr_v6s:
        ipv6s.append(addr[4][0]) if len(addr[4][0]) == 39 else None
    return ipv6s[0]


class DDNS:
    def __init__(self, access_key_id, access_key_secret, domain_name, rrkey_word, rtype):
        self.client = DnsClient(access_key_id, access_key_secret)
        self.domain_name = domain_name
        self.rrkey_word = rrkey_word
        self.rtype = rtype

    def set_domain_name(self, domain_name):
        self.domain_name = domain_name

    def set_rrkey_word(self, rrkey_word):
        self.rrkey_word = rrkey_word

    def set_rtype(self, rtype):
        self.rtype = rtype

    def update_args(self, domain_name=None, rrkey_word=None, rtype=None):
        self.set_domain_name(domain_name) if domain_name is not None else None
        self.set_rrkey_word(rrkey_word) if rrkey_word is not None else None
        self.set_rtype(rtype) if rtype is not None else None

    def ddns(self):
        self.client.describe_sub_domain_records("%s.%s" % (self.rrkey_word, self.domain_name))
        record = None
        for r in self.client.describe_sub_domain_records("%s.%s" % (self.rrkey_word, self.domain_name)):
            record = r if r.get("Type") == self.rtype else None
        if record is None:
            print("[DDNS]解析记录不存在")
            return
        ipv6 = get_ipv6()
        old_ipv6 = record.get("Value")
        if old_ipv6 != ipv6:
            result = self.client.update_domain_record(record.get("RecordId"), self.rrkey_word, self.rtype, ipv6)
            print("[DDNS]成功修改 %s 为 %s" % (old_ipv6, ipv6) if result else "解析记录修改失败")
