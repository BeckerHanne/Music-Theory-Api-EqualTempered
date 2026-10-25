
import pytest
from app.theory.chords import get_triad, get_seventh

# ---------------------------------------------------------------------------
# Triads — root position
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,expected_notes", [
    ("C",  "maj", ["C",  "E",  "G"]),
    ("G",  "maj", ["G",  "B",  "D"]),
    ("F",  "maj", ["F",  "A",  "C"]),
    ("Bb", "maj", ["Bb", "D",  "F"]),
    ("F#", "maj", ["F#", "A#", "C#"]),
    ("Cb", "maj", ["Cb", "Eb", "Gb"]),
    ("C",  "min", ["C",  "Eb", "G"]),
    ("G#", "min", ["G#", "B",  "D#"]),
    ("Ab", "min", ["Ab", "Cb", "Eb"]),
    ("C",  "dim", ["C",  "Eb", "Gb"]),
    ("B",  "dim", ["B",  "D",  "F"]),
    ("Eb", "dim", ["Eb", "Gb", "Bbb"]),
    ("C",  "aug", ["C",  "E",  "G#"]),
    ("B",  "aug", ["B",  "D#", "F##"]),
    ("Ab", "aug", ["Ab", "C",  "E"]),
])
def test_triad_root_position_notes(root, quality, expected_notes):
    result = get_triad(root, quality, inversion=0)
    assert result["notes"] == expected_notes
    assert result["bass"] == expected_notes[0]
    assert result["inversion"] == "root position"
    assert result["basso_continuo"] == "5/3"


# ---------------------------------------------------------------------------
# Triads — inversions
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,inversion,expected_notes,expected_bass,expected_bc", [
    ("C", "maj", 1, ["E",  "G", "C"], "E",  "6/3"),
    ("C", "maj", 2, ["G",  "C", "E"], "G",  "6/4"),
    ("C", "min", 1, ["Eb", "G", "C"], "Eb", "6/3"),
    ("C", "min", 2, ["G",  "C", "Eb"],"G",  "6/4"),
    ("C", "dim", 1, ["Eb", "Gb","C"], "Eb", "6/3"),
    ("C", "aug", 1, ["E",  "G#","C"], "E",  "6/3"),
])
def test_triad_inversions(root, quality, inversion, expected_notes, expected_bass, expected_bc):
    result = get_triad(root, quality, inversion=inversion)
    assert result["notes"] == expected_notes
    assert result["bass"] == expected_bass
    assert result["basso_continuo"] == expected_bc


# ---------------------------------------------------------------------------
# Triads — intervals above bass
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,inversion,expected_intervals", [
    ("C", "maj", 0, ["major third", "perfect fifth"]),
    ("C", "maj", 1, ["minor third", "minor sixth"]),
    ("C", "maj", 2, ["perfect fourth", "major sixth"]),
    ("C", "min", 0, ["minor third", "perfect fifth"]),
    ("C", "min", 1, ["major third", "major sixth"]),
    ("C", "min", 2, ["perfect fourth", "minor sixth"]),
    ("C", "dim", 0, ["minor third", "diminished fifth"]),
    ("C", "aug", 0, ["major third", "augmented fifth"]),
])
def test_triad_intervals_above_bass(root, quality, inversion, expected_intervals):
    result = get_triad(root, quality, inversion=inversion)
    assert result["intervals_above_bass"] == expected_intervals


# ---------------------------------------------------------------------------
# Seventh chords — root position
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,expected_notes", [
    ("G",  "dominant7th",        ["G",  "B",  "D",  "F"]),
    ("C",  "dominant7th",        ["C",  "E",  "G",  "Bb"]),
    ("C",  "major7th",           ["C",  "E",  "G",  "B"]),
    ("F#", "major7th",           ["F#", "A#", "C#", "E#"]),
    ("C",  "minor7th",           ["C",  "Eb", "G",  "Bb"]),
    ("A#", "minor7th",           ["A#", "C#", "E#", "G#"]),
    ("C",  "half_diminished7th", ["C",  "Eb", "Gb", "Bb"]),
    ("B",  "half_diminished7th", ["B",  "D",  "F",  "A"]),
    ("C",  "diminished7th",      ["C",  "Eb", "Gb", "Bbb"]),
    ("F#", "diminished7th",      ["F#", "A",  "C",  "Eb"]),
    ("C",  "minor_major7th",     ["C",  "Eb", "G",  "B"]),
    ("G#", "minor_major7th",     ["G#", "B",  "D#", "F##"]),
])
def test_seventh_root_position_notes(root, quality, expected_notes):
    result = get_seventh(root, quality, inversion=0)
    assert result["notes"] == expected_notes
    assert result["bass"] == expected_notes[0]
    assert result["inversion"] == "root position"
    assert result["basso_continuo"] == "7/5/3"


# ---------------------------------------------------------------------------
# Seventh chords — inversions
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,inversion,expected_bass,expected_bc", [
    ("G", "dominant7th", 0, "G", "7/5/3"),
    ("G", "dominant7th", 1, "B", "6/5/3"),
    ("G", "dominant7th", 2, "D", "6/4/3"),
    ("G", "dominant7th", 3, "F", "6/4/2"),
    ("C", "major7th",    1, "E", "6/5/3"),
    ("C", "major7th",    2, "G", "6/4/3"),
    ("C", "major7th",    3, "B", "6/4/2"),
])
def test_seventh_inversions(root, quality, inversion, expected_bass, expected_bc):
    result = get_seventh(root, quality, inversion=inversion)
    assert result["bass"] == expected_bass
    assert result["basso_continuo"] == expected_bc


# ---------------------------------------------------------------------------
# Seventh chords — intervals above bass
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,inversion,expected_intervals", [
    ("G", "dominant7th", 0, ["major third", "perfect fifth", "minor seventh"]),
    ("G", "dominant7th", 1, ["minor third", "diminished fifth", "minor sixth"]),
    ("G", "dominant7th", 2, ["minor third", "perfect fourth", "major sixth"]),
    ("G", "dominant7th", 3, ["major second", "augmented fourth", "major sixth"]),
    ("C", "diminished7th", 0, ["minor third", "diminished fifth", "diminished seventh"]),
    ("C", "half_diminished7th", 0, ["minor third", "diminished fifth", "minor seventh"]),
])
def test_seventh_intervals_above_bass(root, quality, inversion, expected_intervals):
    result = get_seventh(root, quality, inversion=inversion)
    assert result["intervals_above_bass"] == expected_intervals


# ---------------------------------------------------------------------------
# Quality names
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("root,quality,expected_name", [
    ("C", "maj",              "C major"),
    ("C", "min",              "C minor"),
    ("C", "dim",              "C diminished"),
    ("C", "aug",              "C augmented"),
    ("C", "dominant7th",      "C dominant seventh"),
    ("C", "major7th",         "C major seventh"),
    ("C", "minor7th",         "C minor seventh"),
    ("C", "half_diminished7th","C half-diminished seventh"),
    ("C", "diminished7th",    "C diminished seventh"),
    ("C", "minor_major7th",   "C minor-major seventh"),
])
def test_quality_names(root, quality, expected_name):
    if quality in ("maj", "min", "dim", "aug"):
        result = get_triad(root, quality)
    else:
        result = get_seventh(root, quality)
    assert result["name"] == expected_name


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------

def test_invalid_triad_root_raises():
    with pytest.raises(ValueError, match="Invalid root or quality"):
        get_triad("X", "maj")

def test_invalid_triad_quality_raises():
    with pytest.raises(ValueError, match="Invalid root or quality"):
        get_triad("C", "invalid")

def test_invalid_triad_inversion_raises():
    with pytest.raises(ValueError, match="Invalid inversion"):
        get_triad("C", "maj", inversion=3)

def test_invalid_seventh_inversion_raises():
    with pytest.raises(ValueError, match="Invalid inversion"):
        get_seventh("C", "dominant7th", inversion=4)