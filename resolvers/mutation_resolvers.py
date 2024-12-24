from typing import Any, Dict, Optional

from tartiflette import Resolver
from tartiflette.execution.types import ResolveInfo

from database import session
from models import Todo


@Resolver("Mutation.updateTodo")
async def resolve_mutation_update_todo(
        parent: Optional[Any],
        args: Dict[str, Any],
        ctx: Dict[str, Any],
        info: "ResolveInfo",
) -> Dict[str, Any]:
    todo_id = args["todo"]["id"]
    title = args["todo"].get("title")
    description = args["todo"].get("description")
    session.query(Todo).filter(Todo.id == todo_id).update({"title": title, "description": description})
    session.commit()
    return session.query(Todo).get(todo_id)
