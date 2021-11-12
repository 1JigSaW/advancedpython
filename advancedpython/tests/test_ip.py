import pytest

import socket

from unittest import mock

from sensors import IPAddresses

@pytest.fixture
def sensor():
	return IPAddresses

class TestFormatterIPAddresses:
	@pytest.fixture
	def subject(self, sensor):
		return sensor.format

	def test_format_ipv4(self, subject):
		ip = [("AF_INET", "192.168.56.1")]
		assert subject(ip) == '192.168.56.1 (IPv4)'

	def test_format_ipv6(self, subject):
		ip = [("AF_INET6", "fe80::c512:a3fe:a373:ac9a")]
		assert subject(ip) == 'fe80::c512:a3fe:a373:ac9a (IPv6)'

	def test_format_mixed_list(self, subject):
		ip = [("AF_INET", "192.168.0.14"), ("AF_INET6", "fe80::693f:ebc:2594:d632")]
		assert subject(ip) == "192.168.0.14 (IPv4)\nfe80::693f:ebc:2594:d632 (IPv6)"

