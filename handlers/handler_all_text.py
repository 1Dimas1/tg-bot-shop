from settings.messages import MESSAGES
from settings import config
from handlers.handler import Handler
from settings import utility

class HandlerAllText(Handler):
    """
    The class handles incoming text messages from pressing buttons
    """

    def __init__(self, bot):
        super().__init__(bot)
        # step in the order
        self.step = 0

    def pressed_btn_category(self, message):
        """
        handles incoming text messages
        from clicking on the 'CHOOSE GOOD' button
        """
        self.bot.send_message(message.chat.id, 'Product category list',
                              reply_markup=self.keyboards.remove_menu())
        self.bot.send_message(message.chat.id, 'Make a choice',
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_product(self, message, product):
        """
        handles incoming text messages
        from clicking on the 'CHOOSE GOODS' menu buttons
        """
        self.bot.send_message(message.chat.id, 'Category' + config.KEYBOARD[product],
                              reply_markup=self.keyboards.set_select_category(config.CATEGORY[product]))
        self.bot.send_message(message.chat.id, 'Ok',
                              reply_markup=self.keyboards.category_menu())

    def pressed_btn_info(self, message):
        """
        handles incoming text messages
        from clicking on the 'INFO' button
        """
        self.bot.send_message(message.chat.id, MESSAGES['my_store'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.info_menu())

    def pressed_btn_settings(self, message):
        """
        handles incoming text messages
        from clicking on the 'SETTINGS' button
        """
        self.bot.send_message(message.chat.id, MESSAGES['settings'],
                              parse_mode="HTML",
                              reply_markup=self.keyboards.settings_menu())

    def pressed_btn_back(self, message):
        """
        handles incoming text messages
        from clicking on the '<<' button
        """
        self.bot.send_message(message.chat.id, "You've moved back",
                              reply_markup=self.keyboards.start_menu())

    def pressed_btn_order(self, message):
        """
        handles incoming text messages
        from clicking on the 'ORDER' button
        """
        self.step = 0
        count = self.BD.select_all_product_id()
        quantity = self.BD.select_order_quantity(count[self.step])
        self.send_message_order(count[self.step], quantity, message)

    def send_message_order(self, product_id, quantity, message):
        """
        sends a response to the user when different actions are performed
        """
        self.bot.send_message(message.chat.id, MESSAGES['order_number'].format(
            self.step + 1), parse_mode="HTML")
        self.bot.send_message(message.chat.id,
                              MESSAGES['order'].
                              format(self.BD.select_single_product_name(
                                  product_id),
                                  self.BD.select_single_product_title(
                                      product_id),
                                  self.BD.select_single_product_price(
                                      product_id),
                                  self.BD.select_order_quantity(
                                      product_id)),
                              parse_mode="HTML",
                              reply_markup=self.keyboards.orders_menu(
                                  self.step, quantity))

    def pressed_btn_up(self, message):
        """
        handles incoming text messages
        from clicking on the 'UP' button
        """
        count = self.BD.select_all_product_id()
        quantity_order = self.BD.select_order_quantity(count[self.step])
        quantity_product = self.BD.select_single_product_quantity(count[self.step])
        if quantity_product > 0:
            quantity_order += 1
            quantity_product -= 1
            self.BD.update_order_value(count[self.step], 'quantity', quantity_order)
            self.BD.update_product_value(count[self.step], 'quantity', quantity_product)
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_down(self, message):
        """
        handles incoming text messages
        from clicking on the 'DOWN' button
        """
        count = self.BD.select_all_product_id()
        quantity_order = self.BD.select_order_quantity(count[self.step])
        quantity_product = self.BD.select_single_product_quantity(count[self.step])
        if quantity_product > 0:
            quantity_order -= 1
            quantity_product += 1
            self.BD.update_order_value(count[self.step], 'quantity', quantity_order)
            self.BD.update_product_value(count[self.step], 'quantity', quantity_product)
        self.send_message_order(count[self.step], quantity_order, message)

    def pressed_btn_x(self, message):
        """
        handles incoming text messages
        from clicking on the 'X' button
        """
        count = self.BD.select_all_product_id()
        if count.__len__() > 0:
            quantity_order = self.BD.select_order_quantity(count[self.step])
            quantity_product = self.BD.select_single_product_quantity(count[self.step])
            quantity_product += quantity_order
            self.BD.delete_order(count[self.step])
            self.BD.update_product_value(count[self.step], 'quantity', quantity_product)
            self.step -= 1

        count = self.BD.select_all_product_id()
        if count.__len__() > 0:
            quantity_order = self.BD.select_order_quantity(count[self.step])
            self.send_message_order(count[self.step], quantity_order, message)
        else:
            self.bot.send_message(message.chat.id, MESSAGES['no_orders'],
                                  parse_mode='HTML',
                                  reply_markup=self.keyboards.category_menu())

    def pressed_btn_back_step(self, message):
        """
        handles incoming text messages
        from clicking on the 'BACK_STEP' button
        """
        if self.step > 0:
            self.step -= 1
        count = self.BD.select_all_product_id()
        quantity = self.BD.select_order_quantity(count[self.step])
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_next_step(self, message):
        """
        handles incoming text messages
        from clicking on the 'NEXT_STEP' button
        """
        if self.step < self.BD.count_rows_order()-1:
            self.step += 1
        count = self.BD.select_all_product_id()
        quantity = self.BD.select_order_quantity(count[self.step])
        self.send_message_order(count[self.step], quantity, message)

    def pressed_btn_apply(self, message):
        """
        handles incoming text messages
        from clicking on the 'APPLY' button
        """
        self.bot.send_message(message.chat.id,
                              MESSAGES['apply'].format(
                                  utility.get_total_cost(self.BD),
                                  utility.get_total_quantity(self.BD)
                              ),
                              parse_mode="HTML",
                              reply_markup=self.keyboards.category_menu())
        self.BD.delete_all_order()

    def handle(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle(message):

            # ********** MENU ********** #

            if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                self.pressed_btn_category(message)

            if message.text == config.KEYBOARD['INFO']:
                self.pressed_btn_info(message)

            if message.text == config.KEYBOARD['SETTINGS']:
                self.pressed_btn_settings(message)

            if message.text == config.KEYBOARD['<<']:
                self.pressed_btn_back(message)

            if message.text == config.KEYBOARD['ORDER']:
                if self.BD.count_rows_order() > 0:
                    self.pressed_btn_order(message)
                else:
                    self.bot.send_message(message.chat.id,
                                          MESSAGES['no_orders'],
                                          parse_mode='HTML',
                                          reply_markup=self.keyboards.category_menu())

            # ********** CHOOSE GOODS MENU ********** #

            if message.text == config.KEYBOARD['SEMIPRODUCT']:
                self.pressed_btn_product(message, 'SEMIPRODUCT')

            if message.text == config.KEYBOARD['GROCERY']:
                self.pressed_btn_product(message, 'GROCERY')

            if message.text == config.KEYBOARD['ICE_CREAM']:
                self.pressed_btn_product(message, 'ICE_CREAM')

            # ********** ORDER MENU ********** #

            if message.text == config.KEYBOARD['UP']:
                self.pressed_btn_up(message)

            if message.text == config.KEYBOARD['DOWN']:
                self.pressed_btn_down(message)

            if message.text == config.KEYBOARD['X']:
                self.pressed_btn_x(message)

            if message.text == config.KEYBOARD['BACK_STEP']:
                self.pressed_btn_back_step(message)

            if message.text == config.KEYBOARD['NEXT_STEP']:
                self.pressed_btn_next_step(message)

            if message.text == config.KEYBOARD['APPLY']:
                self.pressed_btn_apply(message)

            else:
                self.bot.send_message(message.chat.id, message.text)


