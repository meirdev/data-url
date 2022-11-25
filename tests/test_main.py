from unittest import mock

from data_url.__main__ import main

STRING = "Hello World!"
STRING_BASE64 = "SGVsbG8gV29ybGQh"


def test_main_file(capsys, fs):
    fs.create_file("foo.txt", contents=b"Hello World!")

    with mock.patch("sys.argv", ["data_url", "foo.txt"]):
        main()

        captured = capsys.readouterr()

        assert captured.out.strip() == f"data:text/plain;base64,{STRING_BASE64}"


def test_main_text(capsys):
    with mock.patch("sys.argv", ["data_url", "-t", STRING]):
        main()

        captured = capsys.readouterr()

        assert captured.out.strip() == f"data:text/plain;base64,{STRING_BASE64}"
