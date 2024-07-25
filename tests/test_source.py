from src.hypot.source import hypot, sqrt

def test_hypot():
    test_a = 3
    test_b = 4
    expected_out = 5
    
    output = hypot(test_a, test_b)
    
    assert output == expected_out
    
def test_sqrt():
    test_a = 4
    expected_out = 2
    
    output = sqrt(test_a)
    
    assert output == expected_out
