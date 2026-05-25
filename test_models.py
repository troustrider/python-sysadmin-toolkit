from network_models import Router, Server

r = Router("gw-01", "10.0.0.1", "AA:BB:CC:DD:EE:FF", "OSPF")
s = Server("web-01", "10.0.0.2", "AA:BB:CC:DD:EE:01", "Ubuntu 22.04", 2)

r.audit_device()
s.audit_device()