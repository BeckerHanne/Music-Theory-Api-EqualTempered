# Music Theory API

This REST API aims to encode music theory in separate retrievable endpoints. The data encoded stands currently as it exists within the modern equal temperament tradition (and what is generally known as the common practice period). 

It aims to:
- retrieve and present music theory questions programmatically (scales, intervals, chords, Roman Numerals) output as clean, well-documented JSON

It does not — and at this stage cannot — capture the full complexity of Western music's historical and improvisatory traditions, where much of the profound musical knowledge was ironically not written down, but instead passed along through a combination of oral and improvised tradition.

Historical tuning system support (Pythagorean, quarter-comma meantone, 17th century temperaments) is planned for a future version.

## Endpoints (v1)

| Endpoint | Description | Status |
|---|---|---|
| `GET /scales/{tonic}/{mode}` | Returns notes and scale degrees | Active
| `GET /chords/triads/{root}/{quality}` | Returns triad notes and intervals above bass | Active |
| `GET /chords/seventh/{root}/{quality}` | Returns seventh chord notes and intervals above bass | Active |
| `GET /key/{tonic}/{mode}/diatonic-chords` | Returns all diatonic chords with Roman numerals | In progress
| `GET /analyze` | Returns Roman numeral analysis of a chord in context | In progress
| `GET /intervals/{note1}/{note2}` | Returns interval name and quality | Active

## Running the API

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python run.py
```

Swagger UI available at `http://127.0.0.1:3000/api/docs`

## Running test suite

```bash
# Run all tests
python -m pytest app/theory_tests/ -v

# Run a specific test file
python -m pytest app/theory_tests/test_scales.py -v
python -m pytest app/theory_tests/test_intervals.py -v
python -m pytest app/theory_tests/test_chords.py -v
```

## Stack

- Python / Flask
- OpenAPI / Swagger


## Author

Hanné Becker — Computational Musicologist & Research Software Developer

