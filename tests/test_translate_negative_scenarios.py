import pytest

from utils.core import get_translation


# I am assuming the status 400 is returned when an input is missing or is incorrect, like the locale.
@pytest.mark.parametrize("query, locale, expected_status", [
    ("", "es-ES", 400),  # empty query
    ("apple", "", 400),  # empty locale
    ("apple", "xx-XX", 400),  # locale invalid
    (None, "es-ES", 400),  # missing query
    ("apple", None, 400),  # miss locale
])
def test_invalid_inputs(query, locale, expected_status):
    query = query or ""
    locale = locale or ""
    response = get_translation(query, locale)
    assert response.status_code == expected_status, f"Expected {expected_status}, Actual: {response.status_code}"
