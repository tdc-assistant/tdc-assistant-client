from datetime import datetime
from typing import Any, Dict, Optional
from dateutil import parser

from graphql import GraphQLScalarType, ValueNode
from graphql.utilities import value_from_ast_untyped


def serialize_datetime(value: Any) -> str:
    return value.isoformat()


def parse_datetime_value(value: Any) -> datetime:
    return parser.isoparse(value)


def parse_datetime_literal(
    value_node: ValueNode, variables: Optional[Dict[str, Any]] = None
) -> datetime:
    ast_value = value_from_ast_untyped(value_node, variables)
    return parse_datetime_value(ast_value)


DatetimeScalar = GraphQLScalarType(
    name="DateTime",
    serialize=serialize_datetime,
    parse_value=parse_datetime_value,
    parse_literal=parse_datetime_literal,
)
