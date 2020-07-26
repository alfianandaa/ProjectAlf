# this module original created by @spechide
# port to userbot by @afdulfauzan

from telethon.tl import functions
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.create (b|g|c)(?: |$)(.*)")
async def telegraphs(grop):
    """ For .create command, Creating New Group & Channel """
    if grop.text[0].isalpha() or grop.text[0] in ("/", "#", "@", "!"):
        return
    if grop.fwd_from:
        return
    type_of_group = grop.pattern_match.group(1)
    group_name = grop.pattern_match.group(2)
    if type_of_group == "b":
        try:
            result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                users=["@sanaTWICEbot"],
                # Not enough users (to create a chat, for example)
                # Telegram, no longer allows creating a chat with ourselves
                title=group_name
            ))
            created_chat_id = result.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit("Your {} Group Created Successfully. Click [{}]({}) to join".format(group_name, group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))
    elif type_of_group in ["g", "c"]:
        try:
            r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                title=group_name,
                about="Welcome to this Channel",
                megagroup=False if type_of_group == "c" else True
            ))
            created_chat_id = r.chats[0].id
            result = await grop.client(functions.messages.ExportChatInviteRequest(
                peer=created_chat_id,
            ))
            await grop.edit("Your {} Group/Channel Created Successfully. Click [{}]({}) to join".format(group_name, group_name, result.link))
        except Exception as e:  # pylint:disable=C0103,W0703
            await grop.edit(str(e))

CMD_HELP.update({
    "create":
    "Create"
    "\nUsage: Create Channel, Group & Group With Bot."
    "\n\n`>.create g <group name>`"
    "\nUsage: Create a Private Group."
    "\n\n`>.create b <group name>`"
    "\nUsage: Create a Group with Bot."
    "\n\n`>.create c <channel name>`"
    "\nUsage: Create a Channel."
})
