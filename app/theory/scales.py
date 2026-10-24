CHROMATIC_SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F',
                   'F#', 'G', 'G#', 'A', 'A#', 'B']

SCALE_INTERVALS = {
    'major':          [0, 2, 4, 5, 7, 9, 11],
    'natural_minor':  [0, 2, 3, 5, 7, 8, 10],
    'harmonic_minor': [0, 2, 3, 5, 7, 8, 11],
}

def get_scale(tonic: str, mode: str) -> list[str]:
    if tonic not in CHROMATIC_SCALE:
        raise ValueError(f"Invalid tonic: {tonic}")
    if mode not in SCALE_INTERVALS:
        raise ValueError(f"Unsupported mode: {mode}")
    root = CHROMATIC_SCALE.index(tonic)
    intervals = SCALE_INTERVALS[mode]
    return [CHROMATIC_SCALE[(root + i) % 12] for i in intervals]