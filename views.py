from typing import Dict, List, Optional, Iterable

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from models import BatchRequestSchema
from utils import build_query

main_bp = Blueprint('main', __name__)

FILE_NAME = 'data/apache_logs.txt'


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    try:
        params: Dict[str, List[Dict[str, str]]] = BatchRequestSchema().load(data=request.json)
    except ValidationError as error:
        return Response(response=error.messages, status=400)

    result: Optional[Iterable[str]] = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=FILE_NAME,
            data=result,
        )

    return jsonify(result)
