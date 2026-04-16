import json

from rest_framework.parsers import BaseParser
from rest_framework.exceptions import ParseError


class PlainTextJSONParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        raw = stream.read()
        if not raw:
            return {}

        if isinstance(raw, bytes):
            text = raw.decode('utf-8')
        else:
            text = str(raw)

        text = text.strip()
        if not text:
            return {}

        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise ParseError(f'Invalid plain text JSON: {exc.msg}')
