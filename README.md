# Mech Gacha

Assemble your own mecha with parts from user-submitted core mechanics!

Use [this link](https://discord.com/api/oauth2/authorize?client_id=836012465732059146&permissions=26688&scope=bot) to invite the bot to your Discord server.

## Installing the server

First, run `pip install -r requirements.txt` to install the necessary libraries.

Make a file named `.env`, create a discord bot token, and add `TOKEN=<your discord token>`. Second, create a database file in `db_data/mechgacha.sqlite` (probably via running the `sqlite3` command). Then run `bot.py`.

Note that the `.env` file must be in the `mechgacha` directory, and `bot.py` must also be run from here. This is so that they can see the database.

Run `docker compose up -d` to deploy!
