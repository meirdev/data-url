from unittest import mock

import pytest

from data_url import data_url_file, data_url_text

STRING = "Hello World!"
STRING_BASE64 = "SGVsbG8gV29ybGQh"


def test_data_url_file(fs):
    fs.create_file("foo.txt", contents=STRING.encode())

    assert data_url_file("foo.txt") == f"data:text/plain;base64,{STRING_BASE64}"


def test_data_url_text():
    assert data_url_text(STRING) == f"data:text/plain;base64,{STRING_BASE64}"


def test_unknown_mime_type(fs):
    fs.create_file("foo.hahaha", contents="")

    with pytest.raises(ValueError):
        data_url_file("foo.hahaha")
