import pytest
from src.isbn import normalize_isbn, detect_isbn

def test_idempotent_normalization():
    raw = "978-0-306-40615-7"
    once = normalize_isbn(raw)
    twice = normalize_isbn(once)
    assert once == twice

def test_equivalent_format_detection():
    raw1 = "9780306406157"
    raw2 = "978-0-306-40615-7"
    assert detect_isbn(raw1) == detect_isbn(raw2)

def test_detect_isbn10():
    assert detect_isbn("0-8044-2957-X") == "ISBN-10"

def test_detect_isbn13():
    assert detect_isbn("9780306406157") == "ISBN-13"

def test_detect_invalid():
    assert detect_isbn("123456789") == "INVALID"