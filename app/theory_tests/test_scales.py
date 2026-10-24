from app.theory import get_scale

def test_c_major():
    assert get_scale('C', 'major') == ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def test_a_natural_minor():
    assert get_scale('A', 'natural_minor') == ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def test_d_harmonic_minor():
    assert get_scale('D', 'harmonic_minor') == ['D', 'E', 'F', 'G', 'A', 'Bb', 'C#']