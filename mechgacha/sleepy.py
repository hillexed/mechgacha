import db
from datetime import datetime
import logging
import random

MIN_NUM_OF_MISSED_COMMANDS_TO_COMMENT_ON = 5 # 10
PROBABILITY = 0.02

async def wakeup_command(client, prefix):
    db.create_table_if_not_made("stats")
    if (last_time := db.get_data("last_time", "stats")) is None:
        db.create_new_entry("last_time", datetime.now().isoformat(), "stats")
    if (channel_id := db.get_data("last_channel", "stats")) is None:
        db.create_new_entry("last_channel", 0, "stats")
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
    if number_of_messages_starting_with_prefix > MIN_NUM_OF_MISSED_COMMANDS_TO_COMMENT_ON:
        rolled = random.random()
        logging.info(f"rolled {rolled}, against probability {PROBABILITY} of saying funny message")
        if rolled < PROBABILITY:
            await channel.send(f"wow yall sent {number_of_messages_starting_with_prefix} messages while i was napping")

