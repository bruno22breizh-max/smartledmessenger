async def handle_send(call):
    message = call.data["message"]
    coordinator.last_message = message
