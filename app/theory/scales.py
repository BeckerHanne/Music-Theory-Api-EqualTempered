MAJOR_SCALE_SPELLINGS = {
    'C':  ['C',  'D',  'E',  'F',  'G',  'A',  'B'],
    'G':  ['G',  'A',  'B',  'C',  'D',  'E',  'F#'],
    'D':  ['D',  'E',  'F#', 'G',  'A',  'B',  'C#'],
    'A':  ['A',  'B',  'C#', 'D',  'E',  'F#', 'G#'],
    'E':  ['E',  'F#', 'G#', 'A',  'B',  'C#', 'D#'],
    'B':  ['B',  'C#', 'D#', 'E',  'F#', 'G#', 'A#'],
    'F#': ['F#', 'G#', 'A#', 'B',  'C#', 'D#', 'E#'],
    'C#': ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#'],
    'F':  ['F',  'G',  'A',  'Bb', 'C',  'D',  'E'],
    'Bb': ['Bb', 'C',  'D',  'Eb', 'F',  'G',  'A'],
    'Eb': ['Eb', 'F',  'G',  'Ab', 'Bb', 'C',  'D'],
    'Ab': ['Ab', 'Bb', 'C',  'Db', 'Eb', 'F',  'G'],
    'Db': ['Db', 'Eb', 'F',  'Gb', 'Ab', 'Bb', 'C'],
    'Gb': ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F'],
    'Cb': ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb'],
}

NATURAL_MINOR_SPELLINGS = {
    'A':  ['A',  'B',  'C',  'D',  'E',  'F',  'G'],
    'E':  ['E',  'F#', 'G',  'A',  'B',  'C',  'D'],
    'B':  ['B',  'C#', 'D',  'E',  'F#', 'G',  'A'],
    'F#': ['F#', 'G#', 'A',  'B',  'C#', 'D',  'E'],
    'C#': ['C#', 'D#', 'E',  'F#', 'G#', 'A',  'B'],
    'G#': ['G#', 'A#', 'B',  'C#', 'D#', 'E',  'F#'],
    'D#': ['D#', 'E#', 'F#', 'G#', 'A#', 'B',  'C#'],
    'A#': ['A#', 'B#', 'C#', 'D#', 'E#', 'F#', 'G#'],
    'D':  ['D',  'E',  'F',  'G',  'A',  'Bb', 'C'],
    'G':  ['G',  'A',  'Bb', 'C',  'D',  'Eb', 'F'],
    'C':  ['C',  'D',  'Eb', 'F',  'G',  'Ab', 'Bb'],
    'F':  ['F',  'G',  'Ab', 'Bb', 'C',  'Db', 'Eb'],
    'Bb': ['Bb', 'C',  'Db', 'Eb', 'F',  'Gb', 'Ab'],
    'Eb': ['Eb', 'F',  'Gb', 'Ab', 'Bb', 'Cb', 'Db'],
    'Ab': ['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'Gb'],
}

HARMONIC_MINOR_SPELLINGS = {
    'A':  ['A',  'B',  'C',  'D',  'E',  'F',  'G#'],
    'E':  ['E',  'F#', 'G',  'A',  'B',  'C',  'D#'],
    'B':  ['B',  'C#', 'D',  'E',  'F#', 'G',  'A#'],
    'F#': ['F#', 'G#', 'A',  'B',  'C#', 'D',  'E#'],
    'C#': ['C#', 'D#', 'E',  'F#', 'G#', 'A',  'B#'],
    'G#': ['G#', 'A#', 'B',  'C#', 'D#', 'E',  'F##'],
    'D#': ['D#', 'E#', 'F#', 'G#', 'A#', 'B',  'C##'],
    'D':  ['D',  'E',  'F',  'G',  'A',  'Bb', 'C#'],
    'G':  ['G',  'A',  'Bb', 'C',  'D',  'Eb', 'F#'],
    'C':  ['C',  'D',  'Eb', 'F',  'G',  'Ab', 'B'],
    'F':  ['F',  'G',  'Ab', 'Bb', 'C',  'Db', 'E'],
    'Bb': ['Bb', 'C',  'Db', 'Eb', 'F',  'Gb', 'A'],
    'Eb': ['Eb', 'F',  'Gb', 'Ab', 'Bb', 'Cb', 'D'],
    'Ab': ['Ab', 'Bb', 'Cb', 'Db', 'Eb', 'Fb', 'G'],
}

def get_scale(tonic: str, mode: str) -> list[str]:
    if mode == 'major':
        if tonic not in MAJOR_SCALE_SPELLINGS:
            raise ValueError(f"Invalid tonic for major scale: {tonic}")
        return MAJOR_SCALE_SPELLINGS[tonic]
    elif mode == 'natural_minor':
        if tonic not in NATURAL_MINOR_SPELLINGS:
            raise ValueError(f"Invalid tonic for natural minor scale: {tonic}")
        return NATURAL_MINOR_SPELLINGS[tonic]
    elif mode == 'harmonic_minor':
        if tonic not in HARMONIC_MINOR_SPELLINGS:
            raise ValueError(f"Invalid tonic for harmonic minor scale: {tonic}")
        return HARMONIC_MINOR_SPELLINGS[tonic]
    else:
        raise ValueError(f"Unsupported mode: {mode}")

if __name__ == "__main__":
    print(get_scale('C', 'major'))
    print(get_scale('A', 'natural_minor'))
    print(get_scale('D', 'harmonic_minor'))