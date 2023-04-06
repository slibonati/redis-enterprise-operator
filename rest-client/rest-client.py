import ssl
import urllib3
import json
from jproperties import Properties

configs = Properties()

def getdbs():
     cert_reqs = ssl.CERT_NONE
     http = urllib3.PoolManager(cert_reqs = cert_reqs)

     headers = urllib3.make_headers(basic_auth=configs.get("username").data + ":" + configs.get("password").data)
     headers.update({'Accept': 'application/json'})
     
     resp = http.request(
          'GET',
          configs.get("url").data + "/v1/bdbs",
          headers=headers)
     print(resp.status)
     data = json.loads(resp.data.decode('utf-8'))
     print(data)

def createdb():
     cert_reqs = ssl.CERT_NONE
     http = urllib3.PoolManager(cert_reqs = cert_reqs)

     payload = {"name": "redis-enterprise-database-rest","type": "redis","memory_size": 1073741824,"tls_mode":"enabled","enforce_client_authentication":"disabled"}
     encoded_data = json.dumps(payload).encode('utf-8')
     
     headers = urllib3.make_headers(basic_auth=configs.get("username").data + ":" + configs.get("password").data)
     headers.update({'Accept': 'application/json'})
     headers.update({'Content-type': 'application/json'})
     
     resp = http.request(
          'POST',
          configs.get("url").data + "/v1/bdbs",
          body=encoded_data,
          headers=headers)

     print(resp.status)
     data = json.loads(resp.data.decode('utf-8'))
     print(data)

def configure_cluster_audit():
     cert_reqs = ssl.CERT_NONE
     http = urllib3.PoolManager(cert_reqs = cert_reqs)

     payload = {"audit_address": "audit", "audit_port": 2200, "audit_protocol": "TCP","audit_reconnect_interval": 1,"audit_reconnect_max_attempts": 0}
     encoded_data = json.dumps(payload).encode('utf-8')
     
     headers = urllib3.make_headers(basic_auth=configs.get("username").data + ":" + configs.get("password").data)
     headers.update({'Accept': 'application/json'})
     headers.update({'Content-type': 'application/json'})
     
     resp = http.request(
          'PUT',
          configs.get("url").data + "/v1/cluster/auditing/db_conns",
          body=encoded_data,
          headers=headers)

     print(resp.status)
     data = json.loads(resp.data.decode('utf-8'))
     print(data)

def configure_db_audit(uid):
     cert_reqs = ssl.CERT_NONE
     http = urllib3.PoolManager(cert_reqs = cert_reqs)

     payload = { "db_conns_auditing": True }
     encoded_data = json.dumps(payload).encode('utf-8')
     
     headers = urllib3.make_headers(basic_auth=configs.get("username").data + ":" + configs.get("password").data)
     headers.update({'Accept': 'application/json'})
     headers.update({'Content-type': 'application/json'})
     
     resp = http.request(
          'PUT',
          configs.get("url").data + "/v1/bdbs/" + uid,
          body=encoded_data,
          headers=headers)

     print(resp.status)
     data = json.loads(resp.data.decode('utf-8'))
     print(data)


def main():
    with open('config.properties', 'rb') as read_prop:
     configs.load(read_prop)
     #getdbs()
     #createdb()
     #configure_cluster_audit()
     configure_db_audit("2")
 
if __name__=="__main__":
    main()

  
