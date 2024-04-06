from MainProcess import valueget

def test_valueget():
    assert valueget().status_code == 400
