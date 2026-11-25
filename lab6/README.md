# L6_L7_39 — Password Policy Checker

## Lab 6: Code and Branch Coverage

The original `password_policy.py` application is tested with two separate pytest suites.

### Files

| File | Purpose |
|---|---|
| `password_policy.py` | Application under test |
| `CodeCoverageTest_0039_application.py` | Line/code coverage tests |
| `BranchCoverageTest_0039_application.py` | Branch coverage tests |
| `.coveragerc` | Coverage configuration |
| `requirements.txt` | Test dependencies |
| `screenshots/code_coverage.png` | Code coverage terminal output |
| `screenshots/branch_coverage.png` | Branch coverage terminal output |

### Install

Run from the `lab6` directory:

```bash
python -m pip install -r requirements.txt
```

### Code coverage

```bash
coverage erase
coverage run --rcfile=.coveragerc -m pytest -q CodeCoverageTest_0039_application.py
coverage report --rcfile=.coveragerc -m
```

### Branch coverage

```bash
coverage erase
coverage run --branch --rcfile=.coveragerc -m pytest -q BranchCoverageTest_0039_application.py
coverage report --rcfile=.coveragerc -m
```

### Verified results

Both suites pass 16 tests. The measured coverage for `password_policy.py` is 100% line coverage and 100% branch coverage, covering all 36 branches with zero partial branches.

Lab 6 requires separate code-coverage and branch-coverage test files, terminal-output screenshots for both runs, and at least two commits: one for the code-coverage test/evidence and one for the branch-coverage test/evidence.
