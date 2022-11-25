import base64
import mimetypes
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover
    from _typeshed import StrPath


def guess_mime_type(path: "StrPath") -> str:
    mime_type, _ = mimetypes.guess_type(path)
    if mime_type is None:
        raise ValueError(f"Could not guess MIME type of {path}")
    return mime_type


def get_data_url(mime_type: str, data: bytes) -> str:
    return f"data:{mime_type};base64,{data.decode()}"


def data_url_file(url: "StrPath") -> str:
    mime_type = guess_mime_type(url)

    with open(url, "rb") as f:
        data = base64.b64encode(f.read())

    return get_data_url(mime_type, data)


def data_url_text(text: str) -> str:
    data = base64.b64encode(text.encode())

    return get_data_url("text/plain", data)
