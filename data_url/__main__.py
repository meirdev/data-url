import argparse

from . import data_url_file, data_url_text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file or text")
    parser.add_argument("-t", "--text", action="store_true", help="Input is text")

    args = parser.parse_args()

    if args.text:
        result = data_url_text(args.input)
    else:
        result = data_url_file(args.input)

    print(result)


if __name__ == "__main__":  # pragma: no cover
    main()
