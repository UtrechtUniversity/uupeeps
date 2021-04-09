import uupeeps


def test_peeps():

	uupeeps.get_employees_url(5)


def test_employee():

	assert uupeeps.get_employee_info("ALLamprecht")["Guid"] == "30936d707a9546e6b768c707473c4366"
