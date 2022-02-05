from telegram.ext import run_async

from Demon import dispatcher
from Demom.modules.disable import DisableAbleCommandHandler
from Demon.modules.helper_funcs.alternate import send_message
from Demon.modules.helper_funcs.chat_status import user_admin


@run_async
@user_admin
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [ADD_CCHAT_HANDLER]
