from app.theory.intervals import get_interval

TRIAD_SPELLINGS = {
    ("C",  "maj"): ["C",  "E",  "G"],
    ("G",  "maj"): ["G",  "B",  "D"],
    ("D",  "maj"): ["D",  "F#", "A"],
    ("A",  "maj"): ["A",  "C#", "E"],
    ("E",  "maj"): ["E",  "G#", "B"],
    ("B",  "maj"): ["B",  "D#", "F#"],
    ("F#", "maj"): ["F#", "A#", "C#"],
    ("C#", "maj"): ["C#", "E#", "G#"],
    ("F",  "maj"): ["F",  "A",  "C"],
    ("Bb", "maj"): ["Bb", "D",  "F"],
    ("Eb", "maj"): ["Eb", "G",  "Bb"],
    ("Ab", "maj"): ["Ab", "C",  "Eb"],
    ("Db", "maj"): ["Db", "F",  "Ab"],
    ("Gb", "maj"): ["Gb", "Bb", "Db"],
    ("Cb", "maj"): ["Cb", "Eb", "Gb"],

    ("C",  "min"): ["C",  "Eb", "G"],
    ("G",  "min"): ["G",  "Bb", "D"],
    ("D",  "min"): ["D",  "F",  "A"],
    ("A",  "min"): ["A",  "C",  "E"],
    ("E",  "min"): ["E",  "G",  "B"],
    ("B",  "min"): ["B",  "D",  "F#"],
    ("F#", "min"): ["F#", "A",  "C#"],
    ("C#", "min"): ["C#", "E",  "G#"],
    ("G#", "min"): ["G#", "B",  "D#"],
    ("D#", "min"): ["D#", "F#", "A#"],
    ("A#", "min"): ["A#", "C#", "E#"],
    ("F",  "min"): ["F",  "Ab", "C"],
    ("Bb", "min"): ["Bb", "Db", "F"],
    ("Eb", "min"): ["Eb", "Gb", "Bb"],
    ("Ab", "min"): ["Ab", "Cb", "Eb"],

    ("C",  "dim"): ["C",  "Eb", "Gb"],
    ("G",  "dim"): ["G",  "Bb", "Db"],
    ("D",  "dim"): ["D",  "F",  "Ab"],
    ("A",  "dim"): ["A",  "C",  "Eb"],
    ("E",  "dim"): ["E",  "G",  "Bb"],
    ("B",  "dim"): ["B",  "D",  "F"],
    ("F#", "dim"): ["F#", "A",  "C"],
    ("C#", "dim"): ["C#", "E",  "G"],
    ("G#", "dim"): ["G#", "B",  "D"],
    ("D#", "dim"): ["D#", "F#", "A"],
    ("A#", "dim"): ["A#", "C#", "E"],
    ("F",  "dim"): ["F",  "Ab", "Cb"],
    ("Bb", "dim"): ["Bb", "Db", "Fb"],
    ("Eb", "dim"): ["Eb", "Gb", "Bbb"],

    ("C",  "aug"): ["C",  "E",  "G#"],
    ("G",  "aug"): ["G",  "B",  "D#"],
    ("D",  "aug"): ["D",  "F#", "A#"],
    ("A",  "aug"): ["A",  "C#", "E#"],
    ("E",  "aug"): ["E",  "G#", "B#"],
    ("B",  "aug"): ["B",  "D#", "F##"],
    ("F#", "aug"): ["F#", "A#", "C##"],
    ("F",  "aug"): ["F",  "A",  "C#"],
    ("Bb", "aug"): ["Bb", "D",  "F#"],
    ("Eb", "aug"): ["Eb", "G",  "B"],
    ("Ab", "aug"): ["Ab", "C",  "E"],
    ("Db", "aug"): ["Db", "F",  "A"],
    ("Gb", "aug"): ["Gb", "Bb", "D"],
}

INVERSION_NAMES = {
    0: "root position",
    1: "first inversion",
    2: "second inversion",
}

BASSO_CONTINUO_TRIADS = {
    0: "5/3",
    1: "6/3",
    2: "6/4",
}

QUALITY_NAMES = {
    "maj": "major",
    "min": "minor",
    "dim": "diminished",
    "aug": "augmented",
}

def get_triad(root: str, quality: str, inversion: int = 0) -> dict:
    key = (root, quality)
    if key not in TRIAD_SPELLINGS:
        raise ValueError(f"Invalid root or quality: {root} {quality}")
    if inversion not in INVERSION_NAMES:
        raise ValueError(f"Invalid inversion for triad: {inversion}. Must be 0, 1, or 2.")

    notes = TRIAD_SPELLINGS[key].copy()
    # rotate notes for inversion
    for _ in range(inversion):
        notes.append(notes.pop(0))

    bass = notes[0]
    intervals_above_bass = [
        get_interval(bass, note)["name"]
        for note in notes[1:]
    ]

    return {
        "root": root,
        "quality": QUALITY_NAMES[quality],
        "name": f"{root} {QUALITY_NAMES[quality]}",
        "inversion": INVERSION_NAMES[inversion],
        "bass": bass,
        "notes": notes,
        "intervals_above_bass": intervals_above_bass,
        "basso_continuo": BASSO_CONTINUO_TRIADS[inversion],
    }

SEVENTH_SPELLINGS = {
    # Dominant sevenths
    ("C",  "dominant7th"): ["C",  "E",  "G",  "Bb"],
    ("G",  "dominant7th"): ["G",  "B",  "D",  "F"],
    ("D",  "dominant7th"): ["D",  "F#", "A",  "C"],
    ("A",  "dominant7th"): ["A",  "C#", "E",  "G"],
    ("E",  "dominant7th"): ["E",  "G#", "B",  "D"],
    ("B",  "dominant7th"): ["B",  "D#", "F#", "A"],
    ("F#", "dominant7th"): ["F#", "A#", "C#", "E"],
    ("C#", "dominant7th"): ["C#", "E#", "G#", "B"],
    ("F",  "dominant7th"): ["F",  "A",  "C",  "Eb"],
    ("Bb", "dominant7th"): ["Bb", "D",  "F",  "Ab"],
    ("Eb", "dominant7th"): ["Eb", "G",  "Bb", "Db"],
    ("Ab", "dominant7th"): ["Ab", "C",  "Eb", "Gb"],
    ("Db", "dominant7th"): ["Db", "F",  "Ab", "Cb"],
    ("Gb", "dominant7th"): ["Gb", "Bb", "Db", "Fb"],

    # Major sevenths
    ("C",  "major7th"): ["C",  "E",  "G",  "B"],
    ("G",  "major7th"): ["G",  "B",  "D",  "F#"],
    ("D",  "major7th"): ["D",  "F#", "A",  "C#"],
    ("A",  "major7th"): ["A",  "C#", "E",  "G#"],
    ("E",  "major7th"): ["E",  "G#", "B",  "D#"],
    ("B",  "major7th"): ["B",  "D#", "F#", "A#"],
    ("F#", "major7th"): ["F#", "A#", "C#", "E#"],
    ("C#", "major7th"): ["C#", "E#", "G#", "B#"],
    ("F",  "major7th"): ["F",  "A",  "C",  "E"],
    ("Bb", "major7th"): ["Bb", "D",  "F",  "A"],
    ("Eb", "major7th"): ["Eb", "G",  "Bb", "D"],
    ("Ab", "major7th"): ["Ab", "C",  "Eb", "G"],
    ("Db", "major7th"): ["Db", "F",  "Ab", "C"],
    ("Gb", "major7th"): ["Gb", "Bb", "Db", "F"],
    ("Cb", "major7th"): ["Cb", "Eb", "Gb", "Bb"],

    # Minor sevenths
    ("C",  "minor7th"): ["C",  "Eb", "G",  "Bb"],
    ("G",  "minor7th"): ["G",  "Bb", "D",  "F"],
    ("D",  "minor7th"): ["D",  "F",  "A",  "C"],
    ("A",  "minor7th"): ["A",  "C",  "E",  "G"],
    ("E",  "minor7th"): ["E",  "G",  "B",  "D"],
    ("B",  "minor7th"): ["B",  "D",  "F#", "A"],
    ("F#", "minor7th"): ["F#", "A",  "C#", "E"],
    ("C#", "minor7th"): ["C#", "E",  "G#", "B"],
    ("G#", "minor7th"): ["G#", "B",  "D#", "F#"],
    ("D#", "minor7th"): ["D#", "F#", "A#", "C#"],
    ("A#", "minor7th"): ["A#", "C#", "E#", "G#"],
    ("F",  "minor7th"): ["F",  "Ab", "C",  "Eb"],
    ("Bb", "minor7th"): ["Bb", "Db", "F",  "Ab"],
    ("Eb", "minor7th"): ["Eb", "Gb", "Bb", "Db"],
    ("Ab", "minor7th"): ["Ab", "Cb", "Eb", "Gb"],

    # Half-diminished sevenths
    ("C",  "half_diminished7th"): ["C",  "Eb", "Gb", "Bb"],
    ("G",  "half_diminished7th"): ["G",  "Bb", "Db", "F"],
    ("D",  "half_diminished7th"): ["D",  "F",  "Ab", "C"],
    ("A",  "half_diminished7th"): ["A",  "C",  "Eb", "G"],
    ("E",  "half_diminished7th"): ["E",  "G",  "Bb", "D"],
    ("B",  "half_diminished7th"): ["B",  "D",  "F",  "A"],
    ("F#", "half_diminished7th"): ["F#", "A",  "C",  "E"],
    ("C#", "half_diminished7th"): ["C#", "E",  "G",  "B"],
    ("G#", "half_diminished7th"): ["G#", "B",  "D",  "F#"],
    ("F",  "half_diminished7th"): ["F",  "Ab", "Cb", "Eb"],
    ("Bb", "half_diminished7th"): ["Bb", "Db", "Fb", "Ab"],
    ("Eb", "half_diminished7th"): ["Eb", "Gb", "Bbb","Db"],

    # Diminished sevenths
    ("C",  "diminished7th"): ["C",  "Eb", "Gb", "Bbb"],
    ("G",  "diminished7th"): ["G",  "Bb", "Db", "Fb"],
    ("D",  "diminished7th"): ["D",  "F",  "Ab", "Cb"],
    ("A",  "diminished7th"): ["A",  "C",  "Eb", "Gb"],
    ("E",  "diminished7th"): ["E",  "G",  "Bb", "Db"],
    ("B",  "diminished7th"): ["B",  "D",  "F",  "Ab"],
    ("F#", "diminished7th"): ["F#", "A",  "C",  "Eb"],
    ("C#", "diminished7th"): ["C#", "E",  "G",  "Bb"],
    ("G#", "diminished7th"): ["G#", "B",  "D",  "F"],
    ("D#", "diminished7th"): ["D#", "F#", "A",  "C"],
    ("A#", "diminished7th"): ["A#", "C#", "E",  "G"],
    ("F",  "diminished7th"): ["F",  "Ab", "Cb", "Ebb"],
    ("Bb", "diminished7th"): ["Bb", "Db", "Fb", "Abb"],

    # Minor-major sevenths
    ("C",  "minor_major7th"): ["C",  "Eb", "G",  "B"],
    ("G",  "minor_major7th"): ["G",  "Bb", "D",  "F#"],
    ("D",  "minor_major7th"): ["D",  "F",  "A",  "C#"],
    ("A",  "minor_major7th"): ["A",  "C",  "E",  "G#"],
    ("E",  "minor_major7th"): ["E",  "G",  "B",  "D#"],
    ("B",  "minor_major7th"): ["B",  "D",  "F#", "A#"],
    ("F#", "minor_major7th"): ["F#", "A",  "C#", "E#"],
    ("C#", "minor_major7th"): ["C#", "E",  "G#", "B#"],
    ("G#", "minor_major7th"): ["G#", "B",  "D#", "F##"],
    ("F",  "minor_major7th"): ["F",  "Ab", "C",  "E"],
    ("Bb", "minor_major7th"): ["Bb", "Db", "F",  "A"],
    ("Eb", "minor_major7th"): ["Eb", "Gb", "Bb", "D"],
    ("Ab", "minor_major7th"): ["Ab", "Cb", "Eb", "G"],
}

SEVENTH_QUALITY_NAMES = {
    "dominant7th":        "dominant seventh",
    "major7th":           "major seventh",
    "minor7th":           "minor seventh",
    "half_diminished7th": "half-diminished seventh",
    "diminished7th":      "diminished seventh",
    "minor_major7th":     "minor-major seventh",
}

INVERSION_NAMES_SEVENTH = {
    0: "root position",
    1: "first inversion",
    2: "second inversion",
    3: "third inversion",
}

BASSO_CONTINUO_SEVENTH = {
    0: "7/5/3",
    1: "6/5/3",
    2: "6/4/3",
    3: "6/4/2",
}

def get_seventh(root: str, quality: str, inversion: int = 0) -> dict:
    key = (root, quality)
    if key not in SEVENTH_SPELLINGS:
        raise ValueError(f"Invalid root or quality: {root} {quality}")
    if inversion not in INVERSION_NAMES_SEVENTH:
        raise ValueError(f"Invalid inversion for seventh chord: {inversion}. Must be 0, 1, 2, or 3.")

    notes = SEVENTH_SPELLINGS[key].copy()
    for _ in range(inversion):
        notes.append(notes.pop(0))

    bass = notes[0]
    intervals_above_bass = [
        get_interval(bass, note)["name"]
        for note in notes[1:]
    ]

    return {
        "root": root,
        "quality": SEVENTH_QUALITY_NAMES[quality],
        "name": f"{root} {SEVENTH_QUALITY_NAMES[quality]}",
        "inversion": INVERSION_NAMES_SEVENTH[inversion],
        "bass": bass,
        "notes": notes,
        "intervals_above_bass": intervals_above_bass,
        "basso_continuo": BASSO_CONTINUO_SEVENTH[inversion],
    }

#if __name__ == "__main__":
#    print(get_triad("C", "min", 0))  # root position
#    print(get_triad("C", "min", 1))  # first inversion
#    print(get_triad("C", "min", 2))  # second inversion
#    print(get_triad("B", "aug", 0))  # double sharp

#if __name__ == "__main__":
#    print(get_seventh("G", "dominant7th", 0))   # root position
#    print(get_seventh("G", "dominant7th", 1))   # first inversion
#    print(get_seventh("G", "dominant7th", 2))   # second inversion
#    print(get_seventh("G", "dominant7th", 3))   # third inversion
#    print(get_seventh("G#", "minor_major7th", 0))  # double sharp