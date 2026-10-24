# Music Theory API

This REST API aims to encode music theory in separate retrievable endpoints. The data encoded stands currently as it exists within the modern equal temperament tradition (and what is generally known as the common practice period). 

It aims to:
- retrieve and present music theory questions programmatically (scales, intervals, chords, Roman Numerals) output as clean, well-documented JSON

It does not — and at this stage cannot — capture the full complexity of Western music's historical and improvisatory traditions, where much of the profound musical knowledge was ironically not written down, but instead passed along through a combination of oral and improvised tradition.

Historical tuning system support (Pythagorean, quarter-comma meantone, 17th century temperaments) is planned for a future version.

## Endpoints (v1)

| Endpoint | Description |
|---|---|
| `GET /scales/{tonic}/{mode}` | Returns notes and scale degrees |
| `GET /chords/{root}/{quality}` | Returns chord tones and intervals |
| `GET /key/{tonic}/{mode}/diatonic-chords` | Returns all diatonic chords with Roman numerals |
| `GET /analyze` | Returns Roman numeral analysis of a chord in context |
| `GET /intervals/{note1}/{note2}` | Returns interval name and quality |

## Stack

- Python / Flask
- PostgreSQL
- OpenAPI / Swagger


## Author

Hanné Becker — Computational Musicologist & Research Software Developer

