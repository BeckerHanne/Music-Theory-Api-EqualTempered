
import pytest
from app.theory.diatonic import get_diatonic_chords

# ---------------------------------------------------------------------------
# C major — triads
# ---------------------------------------------------------------------------

def test_c_major_triad_degrees():
    result = get_diatonic_chords("C", "major")
    degrees = [c["degree"] for c in result["triads"]]
    assert degrees == ["I", "ii", "iii", "IV", "V", "vi", "vii°"]

def test_c_major_triad_roots():
    result = get_diatonic_chords("C", "major")
    roots = [c["root"] for c in result["triads"]]
    assert roots == ["C", "D", "E", "F", "G", "A", "B"]

def test_c_major_triad_qualities():
    result = get_diatonic_chords("C", "major")
    qualities = [c["quality"] for c in result["triads"]]
    assert qualities == ["major", "minor", "minor", "major", "major", "minor", "diminished"]

@pytest.mark.parametrize("degree,expected_notes", [
    ("I",    ["C", "E", "G"]),
    ("ii",   ["D", "F", "A"]),
    ("iii",  ["E", "G", "B"]),
    ("IV",   ["F", "A", "C"]),
    ("V",    ["G", "B", "D"]),
    ("vi",   ["A", "C", "E"]),
    ("vii°", ["B", "D", "F"]),
])
def test_c_major_triad_notes(degree, expected_notes):
    result = get_diatonic_chords("C", "major")
    chord = next(c for c in result["triads"] if c["degree"] == degree)
    assert chord["notes"] == expected_notes


# ---------------------------------------------------------------------------
# C major — seventh chords
# ---------------------------------------------------------------------------

def test_c_major_seventh_degrees():
    result = get_diatonic_chords("C", "major")
    degrees = [c["degree"] for c in result["seventh_chords"]]
    assert degrees == ["Imaj7", "ii7", "iii7", "IVmaj7", "V7", "vi7", "vii∅7"]

def test_c_major_seventh_qualities():
    result = get_diatonic_chords("C", "major")
    qualities = [c["quality"] for c in result["seventh_chords"]]
    assert qualities == [
        "major seventh", "minor seventh", "minor seventh", "major seventh",
        "dominant seventh", "minor seventh", "half-diminished seventh"
    ]

@pytest.mark.parametrize("degree,expected_notes", [
    ("Imaj7",  ["C", "E", "G",  "B"]),
    ("ii7",    ["D", "F", "A",  "C"]),
    ("iii7",   ["E", "G", "B",  "D"]),
    ("IVmaj7", ["F", "A", "C",  "E"]),
    ("V7",     ["G", "B", "D",  "F"]),
    ("vi7",    ["A", "C", "E",  "G"]),
    ("vii∅7",  ["B", "D", "F",  "A"]),
])
def test_c_major_seventh_notes(degree, expected_notes):
    result = get_diatonic_chords("C", "major")
    chord = next(c for c in result["seventh_chords"] if c["degree"] == degree)
    assert chord["notes"] == expected_notes


# ---------------------------------------------------------------------------
# A harmonic minor — triads
# ---------------------------------------------------------------------------

def test_a_harmonic_minor_triad_degrees():
    result = get_diatonic_chords("A", "harmonic_minor")
    degrees = [c["degree"] for c in result["triads"]]
    assert degrees == ["i", "ii°", "III+", "iv", "V", "#VI", "#vii°"]

def test_a_harmonic_minor_triad_qualities():
    result = get_diatonic_chords("A", "harmonic_minor")
    qualities = [c["quality"] for c in result["triads"]]
    assert qualities == ["minor", "diminished", "augmented", "minor", "major", "major", "diminished"]

@pytest.mark.parametrize("degree,expected_notes", [
    ("i",     ["A", "C",  "E"]),
    ("ii°",   ["B", "D",  "F"]),
    ("III+",  ["C", "E",  "G#"]),
    ("iv",    ["D", "F",  "A"]),
    ("V",     ["E", "G#", "B"]),
    ("#VI",   ["F", "A",  "C"]),
    ("#vii°", ["G#","B",  "D"]),
])
def test_a_harmonic_minor_triad_notes(degree, expected_notes):
    result = get_diatonic_chords("A", "harmonic_minor")
    chord = next(c for c in result["triads"] if c["degree"] == degree)
    assert chord["notes"] == expected_notes


# ---------------------------------------------------------------------------
# A harmonic minor — seventh chords
# ---------------------------------------------------------------------------

def test_a_harmonic_minor_seventh_degrees():
    result = get_diatonic_chords("A", "harmonic_minor")
    degrees = [c["degree"] for c in result["seventh_chords"]]
    assert degrees == ["imaj7", "ii∅7", "III+maj7", "iv7", "V7", "#VImaj7", "#vii°7"]

def test_a_harmonic_minor_seventh_qualities():
    result = get_diatonic_chords("A", "harmonic_minor")
    qualities = [c["quality"] for c in result["seventh_chords"]]
    assert qualities == [
        "minor-major seventh", "half-diminished seventh", "augmented major seventh",
        "minor seventh", "dominant seventh", "major seventh", "diminished seventh"
    ]

@pytest.mark.parametrize("degree,expected_notes", [
    ("imaj7",    ["A", "C",  "E",  "G#"]),
    ("ii∅7",     ["B", "D",  "F",  "A"]),
    ("III+maj7", ["C", "E",  "G#", "B"]),
    ("iv7",      ["D", "F",  "A",  "C"]),
    ("V7",       ["E", "G#", "B",  "D"]),
    ("#VImaj7",  ["F", "A",  "C",  "E"]),
    ("#vii°7",   ["G#","B",  "D",  "F"]),
])
def test_a_harmonic_minor_seventh_notes(degree, expected_notes):
    result = get_diatonic_chords("A", "harmonic_minor")
    chord = next(c for c in result["seventh_chords"] if c["degree"] == degree)
    assert chord["notes"] == expected_notes


# ---------------------------------------------------------------------------
# Sharp key — F# major
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("degree,expected_notes", [
    ("I",    ["F#", "A#", "C#"]),
    ("ii",   ["G#", "B",  "D#"]),
    ("V",    ["C#", "E#", "G#"]),
    ("vii°", ["E#", "G#", "B"]),
])
def test_fsharp_major_triad_notes(degree, expected_notes):
    result = get_diatonic_chords("F#", "major")
    chord = next(c for c in result["triads"] if c["degree"] == degree)
    assert chord["notes"] == expected_notes


# ---------------------------------------------------------------------------
# Flat key — Bb major
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("degree,expected_notes", [
    ("I",    ["Bb", "D",  "F"]),
    ("ii",   ["C",  "Eb", "G"]),
    ("V",    ["F",  "A",  "C"]),
    ("vii°", ["A",  "C",  "Eb"]),
])
def test_bb_major_triad_notes(degree, expected_notes):
    result = get_diatonic_chords("Bb", "major")
    chord = next(c for c in result["triads"] if c["degree"] == degree)
    assert chord["notes"] == expected_notes


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_unsupported_mode_raises():
    with pytest.raises(ValueError, match="Unsupported mode"):
        get_diatonic_chords("C", "natural_minor")

def test_invalid_tonic_raises():
    with pytest.raises(ValueError):
        get_diatonic_chords("X", "major")