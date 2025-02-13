import inventory
import equip
from gacha_tables import all_parts_list
import asyncio

open_trade_offers = [] # [(requesting_user, target_user, item1)]

async def trade_command(message, message_body, client):
    global open_trade_offers

    this_user_id = message.author.id

    # when you @ someone, the message is actually of the form <@123>
    if "<@" not in message_body or ">" not in message_body:
        return await message.channel.send("To use this command, use `m!trade <@user> <your item you'd like to trade>`. Make sure to @-mention the user who you would like to trade with as part of the command. If you don't have a trade partner in mind, ask around!")

    # extract @ed user
    this_targeted_id = message_body[message_body.index("<@")+2:message_body.index(">")]
    try:
        this_targeted_id = int(this_targeted_id)
    except:
        return await message.channel.send("Something went wrong figuring out which user you meant to trade with...")

    if this_targeted_id == this_user_id:
        return await message.channel.send("Congratulations! You successfully traded with yourself!")

    # figure out which item you offered to trade
    words = message_body.strip().split(" ")

    if len(words) < 2:
        return await message.channel.send("To trade one of your items, use m!trade <another user> <item title>")
    offered_item_name = " ".join(words[1:])

    your_inventory = inventory.compute_inventory(this_user_id)
  
    # compute id of the item whose title the user gave
    offered_item_index = equip.select_item_index_by_name_or_position(offered_item_name, your_inventory)

    if offered_item_index == -1:
        return await message.channel.send("I'm not sure what item that is. To trade one of your items, use m!trade <another user> <item title>")
    offered_item_id = all_parts_list[your_inventory[offered_item_index]].id

    # check if we're completing an existing trade offer
    for offer in open_trade_offers:
        prev_user_id, prev_target_id, prev_offered_id = offer
        if this_user_id == prev_target_id and this_targeted_id == prev_user_id:
            # print("Match!")
            # we have a match!
            user_1_id = this_targeted_id
            item_1_id = prev_offered_id

            user_2_id = this_user_id
            item_2_id = offered_item_id

            offer_msg = f"{message.author.display_name} wants to trade:\n{inventory.format_item(item_1_id)}\n for \n{inventory.format_item(item_2_id)}\nSound good? Both parties, use :thumbsup: to agree to the trade!"
            reactmessage = await message.channel.send(offer_msg)
            await reactmessage.add_reaction('👍')
            await reactmessage.add_reaction('👎')

            # wait for both users to approve the trade
            approvals_required = [user_1_id, user_2_id]

            def check(reaction, user):
                return reaction.message == reactmessage and user.id in approvals_required and str(reaction.emoji) in ('👍', '👎')

            try:
                for i in range(2):
                    reaction, user = await client.wait_for('reaction_add', timeout=5 * 60.0, check=check)
                    if str(reaction.emoji) == '👍':
                        approvals_required.remove(user.id)
                    else:
                        await message.channel.send(f'The trade has been cancelled.')
                        return

                # if we get here, we've got two successful approvals!

            except asyncio.TimeoutError:
                await message.channel.send('The time limit has expired for this trade offer')
                try:    
                    await reactmessage.clear_reactions()
                except discord.errors.Forbidden:
                    pass
                return

            
            # print("Trade confirmed!")
            inventory.trade(user_1_id, item_1_id, user_2_id, item_2_id)

            await message.channel.send("The trade is complete!")

            if offer in open_trade_offers:
                open_trade_offers.remove(offer)
            return

    # this is a new trade offer

    offer = (this_user_id, this_targeted_id, offered_item_id)
    open_trade_offers.append(offer)

    traded_item = all_parts_list[offered_item_id]

    other_user = await client.fetch_user(this_targeted_id)

    stars_string = "☆☆☆" if stars == 0 else "★" * traded_item.stars
    await message.channel.send(f"You have offered to trade this item to {other_user.display_name}: \n **{traded_item.name} {stars_string}**\n{traded_item.description}\n\nTo complete the trade, {other_user.display_name} must offer to trade an item to you!")

    # trade offer expires in 2 minutes
    await asyncio.sleep(60 * 2)
    if offer in open_trade_offers:
        open_trade_offers.remove(offer)
