# Package Sorting System

A Python implementation of a package sorting algorithm for Thoughtful's robotic automation factory. This system classifies packages into different handling stacks based on their dimensions and mass.

## Overview

The robotic arm uses this function to determine which stack a package should be dispatched to based on two criteria:

- **Volume and dimensions** (to determine if a package is bulky)
- **Mass** (to determine if a package is heavy)

## Requirements

- Python 3.6+
- pytest (for running tests)

## Installation

1. Clone or download this repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```bash
project/
├── package_sort.py
├── test_package_sort.py
└── README.md
```

## Usage

```python
from package_sort import sort

# Example: Standard package (small and light)
result = sort(width=50, height=50, length=50, mass=10)
print(result)  # Output: "STANDARD"

# Example: Special package (bulky but not heavy)
result = sort(width=150, height=50, length=50, mass=10)
print(result)  # Output: "SPECIAL"

# Example: Rejected package (both bulky and heavy)
result = sort(width=150, height=100, length=100, mass=25)
print(result)  # Output: "REJECTED"
```

## Sorting Rules

### Package Classifications

1. **Bulky**: A package is considered bulky if:
   - Its volume (Width × Height × Length) ≥ 1,000,000 cm³, OR
   - Any single dimension ≥ 150 cm

2. **Heavy**: A package is considered heavy if:
   - Its mass ≥ 20 kg

### Stack Assignments

- **STANDARD**: Packages that are neither bulky nor heavy
- **SPECIAL**: Packages that are either bulky OR heavy (but not both)
- **REJECTED**: Packages that are both bulky AND heavy

## Function Signature

```python
def sort(width, height, length, mass):
    """
    Sort packages into appropriate stacks based on their dimensions and mass.
    
    Args:
        width: Package width in centimeters
        height: Package height in centimeters
        length: Package length in centimeters
        mass: Package mass in kilograms
    
    Returns:
        str: The stack where the package should go ("STANDARD", "SPECIAL", or "REJECTED")
    """
```

## Running Tests

Run all tests with verbose output:

```bash
pytest test_package_sort.py -v
```

Run all tests in the current directory:

```bash
pytest
```

Run a specific test:

```bash
pytest test_package_sort.py::TestPackageSorting::test_standard_package_small_light
```

## Test Coverage

The test suite includes comprehensive coverage of:

- Standard packages (small and light)
- Edge cases at exact thresholds
- Bulky packages (by volume or by dimension)
- Heavy packages
- Rejected packages (both bulky and heavy)
- Various dimension combinations
- Floating-point precision handling

## Examples

| Width (cm) | Height (cm) | Length (cm) | Mass (kg) | Volume (cm³) | Result |
|------------|-------------|-------------|-----------|--------------|---------|
| 50 | 50 | 50 | 10 | 125,000 | STANDARD |
| 100 | 100 | 100 | 10 | 1,000,000 | SPECIAL (bulky by volume) |
| 150 | 50 | 50 | 10 | 375,000 | SPECIAL (bulky by dimension) |
| 50 | 50 | 50 | 20 | 125,000 | SPECIAL (heavy) |
| 150 | 50 | 50 | 20 | 375,000 | REJECTED (bulky and heavy) |
| 100 | 100 | 100 | 20 | 1,000,000 | REJECTED (bulky and heavy) |

## License

This project is part of a technical assessment.
