import pytest
import pandas as pd
import tempfile
import os
from log_parser import parse_auth_log
from inventory_manager import filter_vulnerable

SAMPLE_LOG = """Jan 10 06:55:48 server sshd[1234]: Failed password for root from 192.168.1.100 port 22 ssh2
Jan 10 06:55:50 server sshd[1235]: Failed password for admin from 10.0.0.5 port 22 ssh2
Jan 10 06:55:52 server sshd[1236]: Failed password for root from 192.168.1.100 port 22 ssh2
Jan 10 06:56:01 server sshd[1237]: Accepted password for karim from 192.168.1.50 port 22 ssh2
Jan 10 06:56:10 server sshd[1238]: Failed password for invalid user deploy from 172.16.0.99 port 22 ssh2
Jan 10 06:56:15 server sshd[1239]: Failed password for root from 192.168.1.100 port 22 ssh2
Jan 10 06:57:01 server sshd[1240]: Failed password for admin from 10.0.0.5 port 22 ssh2
"""


def test_parse_auth_log_counts():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False) as f:
        f.write(SAMPLE_LOG)
        tmp_path = f.name

    try:
        result = parse_auth_log(tmp_path)
        assert result["counts"]["192.168.1.100"] == 3
        assert result["counts"]["10.0.0.5"] == 2
        assert result["counts"]["172.16.0.99"] == 1
        assert result["total_attempts"] == 6
        assert len(result["unique_ips"]) == 3
        assert "192.168.1.50" not in result["unique_ips"]
    finally:
        os.unlink(tmp_path)


def test_filter_vulnerable_windows():
    df = pd.DataFrame([
        {"hostname": "srv1", "os": "Windows Server 2019", "ram_gb": 16},
        {"hostname": "srv2", "os": "Ubuntu 22.04", "ram_gb": 8},
        {"hostname": "srv3", "os": "Debian 11", "ram_gb": 2},
    ])
    result = filter_vulnerable(df)
    assert len(result) == 2
    assert "srv1" in result["hostname"].values
    assert "srv3" in result["hostname"].values
    assert "srv2" not in result["hostname"].values
