class NetworkDevice:
      def __init__(self, hostname: str, ip: str, mac: str) -> None:
          self.hostname = hostname
          self.ip = ip
          self.mac = mac

      def audit_device(self) -> None:
          print(f"[{self.hostname}] Generic audit — IP: {self.ip}, MAC: {self.mac}")

      def __repr__(self) -> str:
          return f"{self.__class__.__name__}(hostname={self.hostname}, ip={self.ip})"


class Router(NetworkDevice):
      def __init__(self, hostname: str, ip: str, mac: str, routing_protocol: str) -> None:
          super().__init__(hostname, ip, mac)
          self.routing_protocol = routing_protocol

      def audit_device(self) -> None:
          print(f"[ROUTER {self.hostname}] Verify {self.routing_protocol} route tables.")
          print(f"  → Ensure no default route points to untrusted next-hop.")
          print(f"  → Check ACLs on management interfaces.")


class Server(NetworkDevice):
      def __init__(self, hostname: str, ip: str, mac: str, os: str, ram_gb: int) -> None:
          super().__init__(hostname, ip, mac)
          self.os = os
          self.ram_gb = ram_gb

      def audit_device(self) -> None:
          print(f"[SERVER {self.hostname}] OS: {self.os}, RAM: {self.ram_gb}GB")
          print(f"  → Verify SSH key-only auth (no password login).")
          print(f"  → Check for unpatched CVEs on {self.os}.")
          if self.ram_gb < 4:
              print(f"  → WARNING: Low RAM — risk of OOM killer.")