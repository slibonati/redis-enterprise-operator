import redis
from jproperties import Properties

configs = Properties()
def client():
    r = redis.Redis(
    host=configs.get("hostname").data,
    port=configs.get("port").data,
    ssl=True,
    ssl_cert_reqs="required",
    ssl_ca_certs="redis.pem")

    #print(r.info)
    r.set('foo', 'bar')
    value = r.get('foo')
    print(value)


def main():
    with open('config.properties', 'rb') as read_prop:
     configs.load(read_prop)

     client()
 
if __name__=="__main__":
    main()
