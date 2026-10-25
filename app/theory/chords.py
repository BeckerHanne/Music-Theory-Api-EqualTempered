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

#if __name__ == "__main__":
#    print(get_triad("C", "min", 0))  # root position
#    print(get_triad("C", "min", 1))  # first inversion
#    print(get_triad("C", "min", 2))  # second inversion
#    print(get_triad("B", "aug", 0))  # double sharp