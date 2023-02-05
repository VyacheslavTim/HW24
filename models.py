from typing import Any, Dict
from marshmallow import Schema, fields, validates, ValidationError

VALID_CMD_COMMANDS = ('filter', 'unique', 'limit', 'map', 'sort', 'regex')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates
    def check_all_cmd_valid(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> None:
        if values['cmd'] not in VALID_CMD_COMMANDS:
            raise ValidationError('"cmd" contains invalid value')


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema())

