
LETTER_ORDER = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

NOTE_TO_SEMITONE = {
    'C': 0, 'D': 2, 'E': 4, 'F': 5,
    'G': 7, 'A': 9, 'B': 11
}

ACCIDENTAL_OFFSET = {
    '':   0,
    '#':  1,
    '##': 2,
    'b':  -1,
    'bb': -2,
}

def parse_note(note: str) -> tuple[str, str]:
    """Split a note string into (letter, accidental). E.g. 'F#' -> ('F', '#')"""
    letter = note[0].upper()
    accidental = note[1:]
    if letter not in LETTER_ORDER:
        raise ValueError(f"Invalid note: {note}")
    if accidental not in ACCIDENTAL_OFFSET:
        raise ValueError(f"Invalid accidental: {accidental}")
    return letter, accidental

def semitone_value(note: str) -> int:
    letter, accidental = parse_note(note)
    return NOTE_TO_SEMITONE[letter] + ACCIDENTAL_OFFSET[accidental]

def get_interval(note1: str, note2: str) -> dict:
    letter1, _ = parse_note(note1)
    letter2, _ = parse_note(note2)

    semitones = (semitone_value(note2) - semitone_value(note1)) % 12
    diatonic = (LETTER_ORDER.index(letter2) - LETTER_ORDER.index(letter1)) % 7 + 1

    quality = determine_quality(diatonic, semitones)
    interval_name = f"{quality} {degree_name(diatonic)}"
    inversion_diatonic = 9 - diatonic
    inversion_semitones = 12 - semitones
    inversion_quality = determine_quality(inversion_diatonic, inversion_semitones)
    inversion_name = f"{inversion_quality} {degree_name(inversion_diatonic)}"

    return {
        "note1": note1,
        "note2": note2,
        "name": interval_name,
        "diatonic_interval": diatonic,
        "semitones": semitones,
        "quality": quality,
        "inversion": inversion_name,
    }

def determine_quality(diatonic: int, semitones: int) -> str:
    # Expected semitones for a perfect/major interval of each diatonic degree
    perfect = {1: 0, 4: 5, 5: 7, 8: 12}
    major   = {2: 2, 3: 4, 6: 9, 7: 11}

    if diatonic in perfect:
        diff = semitones - perfect[diatonic]
        return {-2: "diminished", -1: "diminished", 0: "perfect", 1: "augmented"}.get(diff, "unknown")
    else:
        diff = semitones - major[diatonic]
        return {-2: "diminished", -1: "minor", 0: "major", 1: "augmented"}.get(diff, "unknown")

def degree_name(diatonic: int) -> str:
    return {
        1: "unison", 2: "second", 3: "third", 4: "fourth",
        5: "fifth",  6: "sixth",  7: "seventh", 8: "octave"
    }[diatonic]

#if __name__ == "__main__":
#    print(get_interval("C", "G"))   # perfect fifth
#    print(get_interval("A", "C"))   # minor third
#    print(get_interval("C", "A"))   # major sixth
#    print(get_interval("C", "F#"))  # augmented fourth
#    print(get_interval("C", "Gb"))  # diminished fifth