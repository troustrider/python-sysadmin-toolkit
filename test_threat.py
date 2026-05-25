from log_parser import parse_auth_log
from threat_intel import print_threat_table

data = parse_auth_log("auth.log")
print_threat_table(data["counts"])