"""Sort packages into appropriate stacks based on their dimensions and mass."""

def sort(width: float, height: float, length: float, mass: float) -> str:
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
    # Calculate volume
    volume = width * height * length

    # Check if package is bulky
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Check if package is heavy
    is_heavy = mass >= 20

    # Determine the appropriate stack
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
