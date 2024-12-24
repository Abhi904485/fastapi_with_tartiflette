from typing import Optional, Any, Dict

from tartiflette import Resolver
from tartiflette.execution.types import ResolveInfo

from database import session
from models import Todo


@Resolver("Query.todos")
async def resolve_query_todos(parent: Optional[Any], args: Dict[str, Any], ctx: Dict[str, Any], info: "ResolveInfo") -> Any:
    return session.query(Todo).all()


@Resolver("Query.todo")
async def resolve_query_todo(parent: Optional[Any], args: Dict[str, Any], ctx: Dict[str, Any], info: "ResolveInfo") -> \
        Optional[Dict[str, Any]]:
    todo = session.query(Todo).get(args['id'])
    if todo:
        return todo
    return None
