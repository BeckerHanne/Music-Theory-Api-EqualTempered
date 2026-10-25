
import pytest
from app.theory.scales import get_scale


# ---------------------------------------------------------------------------
# Major scales
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("tonic,expected", [
    ("C",  ["C",  "D",  "E",  "F",  "G",  "A",  "B"]),
    ("G",  ["G",  "A",  "B",  "C",  "D",  "E",  "F#"]),
    ("D",  ["D",  "E",  "F#", "G",  "A",  "B",  "C#"]),
    ("A",  ["A",  "B",  "C#", "D",  "E",  "F#", "G#"]),
    ("E",  ["E",  "F#", "G#", "A",  "B",  "C#", "D#"]),
    ("B",  ["B",  "C#", "D#", "E",  "F#", "G#", "A#"]),
    ("F#", ["F#", "G#", "A#", "B",  "C#", "D#", "E#"]),
    ("C#", ["C#", "D#", "E#", "F#", "G#", "A#", "B#"]),
    ("F",  ["F",  "G",  "A",  "Bb", "C",  "D",  "E"]),
    ("Bb", ["Bb", "C",  "D",  "Eb", "F",  "G",  "A"]),
    ("Eb", ["Eb", "F",  "G",  "Ab", "Bb", "C",  "D"]),
    ("Ab", ["Ab", "Bb", "C",  "Db", "Eb", "F",  "G"]),
    ("Db", ["Db", "Eb", "F",  "Gb", "Ab", "Bb", "C"]),
    ("Gb", ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"]),
    ("Cb", ["Cb", "Db", "Eb", "Fb", "Gb", "Ab", "Bb"]),
])
def test_major_scale(tonic, expected):
    assert get_scale(tonic, "major") == expected


# ---------------------------------------------------------------------------
# Natural minor scales
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("tonic,expected", [
    ("A",  ["A",  "B",  "C",  "D",  "E",  "F",  "G"]),
    ("E",  ["E",  "F#", "G",  "A",  "B",  "C",  "D"]),
    ("B",  ["B",  "C#", "D",  "E",  "F#", "G",  "A"]),
    ("F#", ["F#", "G#", "A",  "B",  "C#", "D",  "E"]),
    ("C#", ["C#", "D#", "E",  "F#", "G#", "A",  "B"]),
    ("G#", ["G#", "A#", "B",  "C#", "D#", "E",  "F#"]),
    ("D#", ["D#", "E#", "F#", "G#", "A#", "B",  "C#"]),
    ("A#", ["A#", "B#", "C#", "D#", "E#", "F#", "G#"]),
    ("D",  ["D",  "E",  "F",  "G",  "A",  "Bb", "C"]),
    ("G",  ["G",  "A",  "Bb", "C",  "D",  "Eb", "F"]),
    ("C",  ["C",  "D",  "Eb", "F",  "G",  "Ab", "Bb"]),
    ("F",  ["F",  "G",  "Ab", "Bb", "C",  "Db", "Eb"]),
    ("Bb", ["Bb", "C",  "Db", "Eb", "F",  "Gb", "Ab"]),
    ("Eb", ["Eb", "F",  "Gb", "Ab", "Bb", "Cb", "Db"]),
    ("Ab", ["Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"]),
])
def test_natural_minor_scale(tonic, expected):
    assert get_scale(tonic, "natural_minor") == expected


# ---------------------------------------------------------------------------
# Harmonic minor scales
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("tonic,expected", [
    ("A",  ["A",  "B",  "C",  "D",  "E",  "F",  "G#"]),
    ("E",  ["E",  "F#", "G",  "A",  "B",  "C",  "D#"]),
    ("B",  ["B",  "C#", "D",  "E",  "F#", "G",  "A#"]),
    ("F#", ["F#", "G#", "A",  "B",  "C#", "D",  "E#"]),
    ("C#", ["C#", "D#", "E",  "F#", "G#", "A",  "B#"]),
    ("G#", ["G#", "A#", "B",  "C#", "D#", "E",  "F##"]),  # double sharp
    ("D#", ["D#", "E#", "F#", "G#", "A#", "B",  "C##"]),  # double sharp
    ("D",  ["D",  "E",  "F",  "G",  "A",  "Bb", "C#"]),
    ("G",  ["G",  "A",  "Bb", "C",  "D",  "Eb", "F#"]),
    ("C",  ["C",  "D",  "Eb", "F",  "G",  "Ab", "B"]),
    ("F",  ["F",  "G",  "Ab", "Bb", "C",  "Db", "E"]),
    ("Bb", ["Bb", "C",  "Db", "Eb", "F",  "Gb", "A"]),
    ("Eb", ["Eb", "F",  "Gb", "Ab", "Bb", "Cb", "D"]),
])
def test_harmonic_minor_scale(tonic, expected):
    assert get_scale(tonic, "harmonic_minor") == expected


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_unsupported_mode_raises():
    with pytest.raises(ValueError, match="Unsupported mode"):
        get_scale("C", "lydian")

def test_invalid_tonic_major_raises():
    with pytest.raises(ValueError, match="Invalid tonic"):
        get_scale("X", "major")

def test_invalid_tonic_natural_minor_raises():
    with pytest.raises(ValueError, match="Invalid tonic"):
        get_scale("X", "natural_minor")

def test_invalid_tonic_harmonic_minor_raises():
    with pytest.raises(ValueError, match="Invalid tonic"):
        get_scale("X", "harmonic_minor")


# ---------------------------------------------------------------------------
# Coverage gaps — known missing keys
# ---------------------------------------------------------------------------

@pytest.mark.xfail(reason="A# harmonic minor not yet in HARMONIC_MINOR_SPELLINGS")
def test_harmonic_minor_a_sharp_missing():
    get_scale("A#", "harmonic_minor")