import time
from pyRpc import RpcConnection

def response(resp):
    print("Got response:", resp)
    print("Result:", resp.result)

remote = RpcConnection("com.myCompany.MyApplication")
time.sleep(.1)

resp = remote.availableServices()
for service in resp.result:
    print("\nService: %(service)s \nDescription: %(doc)s \nUsage: %(format)s\n" % service)

remote.call("add", args=(1, 2), callback=response)

remote.call("subtract", args=(5, 3), callback=response)

remote.call("multiply", args=(2, 3), callback=response)

remote.call("divide", args=(10, 2), callback=response)

time.sleep(1)

remote.close()

time.sleep(1)

