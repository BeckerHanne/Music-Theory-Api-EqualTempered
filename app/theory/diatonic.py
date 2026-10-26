# Get the diatonic triads and seventh chords for a given tonic and scale degree.

from app.theory.scales import get_scale
from app.theory.chords import get_triad, get_seventh

DIATONIC_TRIADS = {
    "major": [
        {"degree": "I",    "quality": "maj"},
        {"degree": "ii",   "quality": "min"},
        {"degree": "iii",  "quality": "min"},
        {"degree": "IV",   "quality": "maj"},
        {"degree": "V",    "quality": "maj"},
        {"degree": "vi",   "quality": "min"},
        {"degree": "vii°", "quality": "dim"},
    ],
    "harmonic_minor": [
        {"degree": "i",    "quality": "min"},
        {"degree": "ii°",  "quality": "dim"},
        {"degree": "III+", "quality": "aug"},
        {"degree": "iv",   "quality": "min"},
        {"degree": "V",    "quality": "maj"},
        {"degree": "#VI",   "quality": "maj"},
        {"degree": "#vii°", "quality": "dim"},
    ],
}

DIATONIC_SEVENTHS = {
    "major": [
        {"degree": "Imaj7",  "quality": "major7th"},
        {"degree": "ii7",    "quality": "minor7th"},
        {"degree": "iii7",   "quality": "minor7th"},
        {"degree": "IVmaj7", "quality": "major7th"},
        {"degree": "V7",     "quality": "dominant7th"},
        {"degree": "vi7",    "quality": "minor7th"},
        {"degree": "vii∅7",  "quality": "half_diminished7th"},
    ],
    "harmonic_minor": [
        {"degree": "imaj7",    "quality": "minor_major7th"},
        {"degree": "ii∅7",     "quality": "half_diminished7th"},
        {"degree": "III+maj7", "quality": "aug_maj7"},
        {"degree": "iv7",      "quality": "minor7th"},
        {"degree": "V7",       "quality": "dominant7th"},
        {"degree": "#VImaj7",   "quality": "major7th"},
        {"degree": "#vii°7",   "quality": "diminished7th"},
    ],
}

def get_diatonic_chords(tonic: str, mode: str) -> dict:
    if mode not in DIATONIC_TRIADS:
        raise ValueError(f"Unsupported mode: {mode}. Supported modes: major, harmonic_minor")

    scale_notes = get_scale(tonic, mode)

    triads = []
    for i, entry in enumerate(DIATONIC_TRIADS[mode]):
        root = scale_notes[i]
        chord = get_triad(root, entry["quality"])
        triads.append({
            "degree": entry["degree"],
            "root": root,
            "quality": chord["quality"],
            "notes": chord["notes"],
        })

    sevenths = []
    for i, entry in enumerate(DIATONIC_SEVENTHS[mode]):
        root = scale_notes[i]
        chord = get_seventh(root, entry["quality"])
        sevenths.append({
            "degree": entry["degree"],
            "root": root,
            "quality": chord["quality"],
            "notes": chord["notes"],
        })

    return {
        "tonic": tonic,
        "mode": mode,
        "triads": triads,
        "seventh_chords": sevenths,
    }

if __name__ == "__main__":
    import json
    print(json.dumps(get_diatonic_chords("C", "major"), indent=2))
    print(json.dumps(get_diatonic_chords("A", "harmonic_minor"), indent=2))