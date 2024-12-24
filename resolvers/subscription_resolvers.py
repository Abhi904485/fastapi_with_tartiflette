import asyncio
from typing import Any, AsyncGenerator, Dict, Optional

from tartiflette import Subscription
from tartiflette.execution.types import ResolveInfo

from database import session
from models import Todo


@Subscription("Subscription.launchAndWaitTodoTimer")
async def subscribe_subscription_launch_and_wait_cooking_timer(
        parent: Optional[Any],
        args: Dict[str, Any],
        ctx: Dict[str, Any],
        info: "ResolveInfo",
) -> AsyncGenerator[Dict[str, Any], None]:
    todo: Todo = session.query(Todo).get(args['id'])
    for i in range(todo.todo_time):
        yield {
            "launchAndWaitTodoTimer": {
                "remainingTime": todo.todo_time - i,
                "status": "IN_PROGRESS",
            }
        }
        await asyncio.sleep(1)

    yield {
        "launchAndWaitTodoTimer": {"remainingTime": 0, "status": "DONE"}
    }
