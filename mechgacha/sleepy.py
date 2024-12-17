import db
from datetime import datetime

async def wakeup(client):
    db.create_table_if_not_made("stats")
    if (last_time := db.get_data("time", "stats")) is None:
        db.create_new_entry("time", datetime.now().isoformat(), "stats")
    if (channel_id := db.get_data("channel", "stats")) is None:
        db.create_new_entry("channel", 0, "stats")
        return

    if (channel := client.get_channel(channel_id)) is None:
        logging.warning("Failed to fetch channel for funny joke")
        return

    number_of_messages_starting_with_prefix = 0
    async for message in channel.history(after=datetime.fromisoformat(last_time)):
        if message.content.startswith(prefix):
            number_of_messages_starting_with_prefix += 1
    if number_of_messages_starting_with_prefix == 0:
        return
    if number_of_messages_starting_with_prefix > 1:
        await channel.send(f"yall meowed {number_of_messages_starting_with_prefix} times while i was napping")

    await channel.send(f"yawwwn. okay i'm up")


