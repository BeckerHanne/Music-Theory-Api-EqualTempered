
import pytest
from app.theory.intervals import get_interval, parse_note, semitone_value

# ---------------------------------------------------------------------------
# parse_note
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("note,expected", [
    ("C",  ("C", "")),
    ("F#", ("F", "#")),
    ("Bb", ("B", "b")),
    ("C##",("C", "##")),
    ("Ab", ("A", "b")),
])
def test_parse_note(note, expected):
    assert parse_note(note) == expected

def test_parse_note_invalid_letter():
    with pytest.raises(ValueError, match="Invalid note"):
        parse_note("X")

def test_parse_note_invalid_accidental():
    with pytest.raises(ValueError, match="Invalid accidental"):
        parse_note("Cx")  # x not in ACCIDENTAL_OFFSET


# ---------------------------------------------------------------------------
# semitone_value
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("note,expected", [
    ("C",   0),
    ("C#",  1),
    ("Db",  1),
    ("D",   2),
    ("E",   4),
    ("F",   5),
    ("F#",  6),
    ("Gb",  6),
    ("G",   7),
    ("A",   9),
    ("Bb", 10),
    ("B",  11),
    ("Cb", 11),
    ("B#",  0),  # wraps — same semitone as C
])
def test_semitone_value(note, expected):
    assert semitone_value(note) % 12 == expected


# ---------------------------------------------------------------------------
# Perfect intervals
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("note1,note2,diatonic,semitones,quality,name,inversion", [
    ("C", "C",  1,  0, "perfect", "perfect unison",   "perfect octave"),
    ("C", "F",  4,  5, "perfect", "perfect fourth",   "perfect fifth"),
    ("C", "G",  5,  7, "perfect", "perfect fifth",    "perfect fourth"),
    ("A", "D",  4,  5, "perfect", "perfect fourth",   "perfect fifth"),
    ("G", "D",  5,  7, "perfect", "perfect fifth",    "perfect fourth"),
])
def test_perfect_intervals(note1, note2, diatonic, semitones, quality, name, inversion):
    result = get_interval(note1, note2)
    assert result["diatonic_interval"] == diatonic
    assert result["semitones"] == semitones
    assert result["quality"] == quality
    assert result["name"] == name
    assert result["inversion"] == inversion


# ---------------------------------------------------------------------------
# Major and minor intervals
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("note1,note2,diatonic,semitones,quality,name,inversion", [
    ("C", "D",  2,  2, "major",  "major second",   "minor seventh"),
    ("C", "E",  3,  4, "major",  "major third",    "minor sixth"),
    ("C", "A",  6,  9, "major",  "major sixth",    "minor third"),
    ("C", "B",  7, 11, "major",  "major seventh",  "minor second"),
    ("A", "C",  3,  3, "minor",  "minor third",    "major sixth"),
    ("A", "G",  7, 10, "minor",  "minor seventh",  "major second"),
    ("D", "F",  3,  3, "minor",  "minor third",    "major sixth"),
    ("E", "G",  3,  3, "minor",  "minor third",    "major sixth"),
    ("B", "D",  3,  3, "minor",  "minor third",    "major sixth"),
])
def test_major_minor_intervals(note1, note2, diatonic, semitones, quality, name, inversion):
    result = get_interval(note1, note2)
    assert result["diatonic_interval"] == diatonic
    assert result["semitones"] == semitones
    assert result["quality"] == quality
    assert result["name"] == name
    assert result["inversion"] == inversion


# ---------------------------------------------------------------------------
# Augmented and diminished intervals
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("note1,note2,diatonic,semitones,quality,name,inversion", [
    ("C", "F#", 4, 6, "augmented",  "augmented fourth",  "diminished fifth"),
    ("C", "Gb", 5, 6, "diminished", "diminished fifth",  "augmented fourth"),
    ("C", "G#", 5, 8, "augmented",  "augmented fifth",   "diminished fourth"),
    ("B", "F",  5, 6, "diminished", "diminished fifth",  "augmented fourth"),
    ("F", "B",  4, 6, "augmented",  "augmented fourth",  "diminished fifth"),
    ("G", "Ab", 2, 1, "minor",      "minor second",      "major seventh"),  # not augmented — diatonic second
    ("C", "Db", 2, 1, "minor",      "minor second",      "major seventh"),
])
def test_augmented_diminished_intervals(note1, note2, diatonic, semitones, quality, name, inversion):
    result = get_interval(note1, note2)
    assert result["diatonic_interval"] == diatonic
    assert result["semitones"] == semitones
    assert result["quality"] == quality
    assert result["name"] == name
    assert result["inversion"] == inversion


# ---------------------------------------------------------------------------
# Enharmonic pairs — same semitones, different diatonic spelling
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("note1,note2,expected_name", [
    ("C", "F#", "augmented fourth"),
    ("C", "Gb", "diminished fifth"),
    ("C", "D#", "augmented second"),
    ("C", "Eb", "minor third"),
    ("C", "A#", "augmented sixth"),
    ("C", "Bb", "minor seventh"),
])
def test_enharmonic_pairs(note1, note2, expected_name):
    assert get_interval(note1, note2)["name"] == expected_name


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_invalid_note1_raises():
    with pytest.raises(ValueError):
        get_interval("X", "C")

def test_invalid_note2_raises():
    with pytest.raises(ValueError):
        get_interval("C", "X")