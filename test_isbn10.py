import pytest
from src.isbn import is_valid_isbn10, normalize_isbn

def test_valid_isbn10_digits():
    assert is_valid_isbn10("0306406152") is True

def test_valid_isbn10_with_X():
    assert is_valid_isbn10("0-8044-2957-X") is True

def test_invalid_isbn10_checksum():
    assert is_valid_isbn10("0306406153") is False

def test_invalid_isbn10_length_short():
    assert is_valid_isbn10("03064061") is False

def test_invalid_isbn10_length_long():
    assert is_valid_isbn10("03064061523") is False

def test_invalid_isbn10_character():
    assert is_valid_isbn10("03064A6152") is False

def test_invalid_isbn10_X_not_last():
    assert is_valid_isbn10("X306406152") is False

def test_empty_string():
    assert is_valid_isbn10("") is False