import pytest

from sensors import CPULoad

@pytest.fixture
def sensor():
	return CPULoad

class TestFormatCPULoad:
	@pytest.fixture
	def subject(self, sensor):
		return sensor.format

	def test_format(self, subject):
		assert subject(0.05) == "5.0%"

	def test_format_multiple_decimal_places(self, subject):
		assert subject(0.031415926) == "3.1%"

	def test_format_multiple_decimal_places_int(self, subject) -> None:
		assert subject(1) == "100.0%"
