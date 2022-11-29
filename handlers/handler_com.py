from handlers.handler import Handler


class HandlerCommands(Handler):
    """
    The class processes incoming commands /start and /help
    """
    def __init__(self, bot):
        super().__init__(bot)

    def pressed_btn_start(self, message):
        """
        handles incoming /start commands
        """
        self.bot.send_message(message.chat.id,
                              f'{message.from_user.first_name},'
                              f' Hi! Looking forward to further tasks.',
                              reply_markup=self.keyboards.start_menu())

    def handle(self):
        # message handler (decorator),
        # which handles incoming /start commands.
        @self.bot.message_handler(commands=['start'])
        def handle(message):
            if message.text == '/start':
                self.pressed_btn_start(message)
