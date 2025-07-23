"""Test cases for the package sort function."""

import pytest
from package_sort import sort

class TestPackageSorting:
    """Test cases for the package sorting function."""

    def test_standard_package_small_light(self):
        """Test a small and light package should go to STANDARD."""
        assert sort(10, 10, 10, 5) == "STANDARD"

    def test_standard_package_near_limits(self):
        """Test a package just below both limits should go to STANDARD."""
        assert sort(99, 99, 99, 19) == "STANDARD"

    def test_special_package_bulky_by_volume(self):
        """Test a package that is bulky by volume but not heavy should go to SPECIAL."""
        assert sort(100, 100, 100, 10) == "SPECIAL"

    def test_special_package_bulky_by_dimension(self):
        """Test a package that is bulky by dimension but not heavy should go to SPECIAL."""
        assert sort(150, 50, 50, 10) == "SPECIAL"
        assert sort(50, 150, 50, 10) == "SPECIAL"
        assert sort(50, 50, 150, 10) == "SPECIAL"

    def test_special_package_heavy_only(self):
        """Test a package that is heavy but not bulky should go to SPECIAL."""
        assert sort(50, 50, 50, 20) == "SPECIAL"
        assert sort(50, 50, 50, 30) == "SPECIAL"

    def test_rejected_package_heavy_and_bulky_by_volume(self):
        """Test a package that is both heavy and bulky by volume should be REJECTED."""
        assert sort(100, 100, 100, 20) == "REJECTED"

    def test_rejected_package_heavy_and_bulky_by_dimension(self):
        """Test a package that is both heavy and bulky by dimension should be REJECTED."""
        assert sort(150, 50, 50, 25) == "REJECTED"
        assert sort(200, 30, 30, 20) == "REJECTED"

    def test_edge_cases_exact_limits(self):
        """Test packages at exact limit values."""
        assert sort(100, 100, 100, 19) == "SPECIAL"

        assert sort(50, 50, 50, 20) == "SPECIAL"

        assert sort(150, 50, 50, 19) == "SPECIAL"

        assert sort(100, 100, 100, 20) == "REJECTED"
        assert sort(150, 50, 50, 20) == "REJECTED"

    def test_very_large_package(self):
        """Test a very large package."""
        assert sort(200, 200, 200, 50) == "REJECTED"

    def test_different_dimension_combinations(self):
        """Test various dimension combinations that result in bulky packages."""
        assert sort(200, 10, 10, 5) == "SPECIAL"

        assert sort(10, 200, 10, 5) == "SPECIAL"
        assert sort(10, 10, 200, 5) == "SPECIAL"

    def test_volume_calculation_accuracy(self):
        """Test that volume calculation is accurate for edge cases."""
        assert sort(99.99, 100, 100, 10) == "STANDARD"

        assert sort(100, 100, 100, 10) == "SPECIAL"

    def test_floating_point_values(self):
        """Test the function handles floating point values correctly."""
        assert sort(99.5, 99.5, 99.5, 19.5) == "STANDARD"
        assert sort(150.1, 50.5, 50.5, 19.9) == "SPECIAL"
        assert sort(150.0, 50.0, 50.0, 20.0) == "REJECTED"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
