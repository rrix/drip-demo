# module for moving actions between states
import aiohttp

import agent.models as models
import agent.entities as entities

import common.enums as enums

def push_forward(action: entities.Action):
    if action.state == enums.ActionState.pending:
        return push_pending(action)
    elif action.state == enums.ActionState.opened:
        return push_open(action)
    elif action.state == enums.ActionState.closed:
        pass
        # nothing to do: push_closed(action)

async def push_pending(action: entities.Action):
    base = action.business.api_base
    request_url = "{base}/excercise/".format(
        base=base
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(request_url) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
