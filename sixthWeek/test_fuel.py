from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/4") == "25%"
    assert convert("2/100") == "2%"
    assert convert("98/100") == "98%"

def test_fuel_empty():
    assert convert("0/100") == "E"
    assert convert("1/100") == "E"

def test_fuel_full():
    assert convert("99/100") == "F"
    assert convert("100/100") == "F"

def test_gauge_output():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"

def test_gauge_out_of_range():
    assert gauge(-1) is None
    assert gauge(101) is None