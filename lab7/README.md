# Lab 7: Fuzzing for Input Validation Bugs

## Files
- `processor.py`: fixed application
- `test_processor.py`: Hypothesis tests for all three functions
- `requirements.txt`: dependencies
- `screenshots/`: evidence images
- `Lab7_FuzzTesting_Evidence.pdf`: screenshot report

## Install and run
```bash
python -m pip install -r requirements.txt
python processor.py
python -m pytest test_processor.py
```

## Input handling
- `first_character_type` returns `invalid` for non-string values and `empty` for an empty string.
- `split_credentials` splits only on the first colon and returns `None` for malformed input or missing fields.
- `digit_ratio` returns `0.0` for non-string or empty input.

Hypothesis strategies generate strings, `None`, integers and lists.
