from alibabacloud_alidns20150109.client import Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as dns_models


class DnsClient:
    def __init__(self, access_key_id, access_key_secret):
        config = open_api_models.Config(access_key_id=access_key_id, access_key_secret=access_key_secret)
        self.client = Client(config)

    def add_domain_record(self, domain_name, rrkey_word, rtype, value):
        result = None
        request = dns_models.AddDomainRecordRequest()
        request.domain_name = domain_name
        request.rr = rrkey_word
        request.type = rtype
        request.value = value
        try:
            response = self.client.add_domain_record(request).body.to_map()
            print(response)
            result = response.get("RecordId")
        except Exception as e:
            print(e)
        return result

    def del_domain_record(self, record_id):
        result = False
        request = dns_models.DeleteDomainRecordRequest()
        request.record_id = record_id
        try:
            response = self.client.delete_domain_record(request).body.to_map()
            if "RecordId" in response.keys():
                result = True
        except Exception as e:
            print(e)
        return result

    def describe_sub_domain_records(self, sub_domain):
        result = None
        request = dns_models.DescribeSubDomainRecordsRequest()
        request.sub_domain = sub_domain
        try:
            response = self.client.describe_sub_domain_records(request).body.to_map()
            result = response.get("DomainRecords").get("Record")
        except Exception as e:
            print(e)
        return result

    def update_domain_record(self, record_id, rrkey_word, rtype, value):
        result = False
        request = dns_models.UpdateDomainRecordRequest()
        request.record_id = record_id
        request.rr = rrkey_word
        request.type = rtype
        request.value = value
        try:
            response = self.client.update_domain_record(request).body.to_map()
            if "RecordId" in response.keys():
                result = True
        except Exception as e:
            print(e)
        return result


    