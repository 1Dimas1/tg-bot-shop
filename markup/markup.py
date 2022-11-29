from telebot.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from settings import config
from data_base.dbalchemy import DBManager


class Keyboards:
    """
    The Keyboards class is for creating and marking up the bot's interface
    """

    def __init__(self):
        self.markup = None
        self.BD = DBManager()

    def set_btn(self, name, step=0, quantity=0):
        """
        Creates and returns a button by input parameters
        """
        if name == 'AMOUNT_ORDERS':
            config.KEYBOARD['AMOUNT_ORDERS'] = "{} {} {}".format(step+1, 'from', str(
                self.BD.count_rows_order()
            ))

        if name == 'AMOUNT_PRODUCTS':
            config.KEYBOARD['AMOUNT_PRODUCTS'] = "{}".format(quantity)

        return KeyboardButton(config.KEYBOARD[name])

    @staticmethod
    def set_inline_btn(name):
        """
        Creates and returns an inline button by input parameters
        """

        return InlineKeyboardButton(str(name), callback_data=str(name.id))

    def start_menu(self):
        """
        Creates button markup in the main menu and returns the markup
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('CHOOSE_GOODS')
        itm_btn_2 = self.set_btn('INFO')
        itm_btn_3 = self.set_btn('SETTINGS')
        # menu button  layout
        self.markup.row(itm_btn_1)
        self.markup.row(itm_btn_2, itm_btn_3)
        return self.markup

    def info_menu(self):
        """
        Creates a button layout in the 'INFO' menu and returns the markup
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # menu button  layout
        self.markup.row(itm_btn_1)
        return self.markup

    def settings_menu(self):
        """
        Creates a button layout in the 'SETTINGS' menu and returns the markup
        """
        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('<<')
        # menu button  layout
        self.markup.row(itm_btn_1)
        return self.markup

    @staticmethod
    def remove_menu():
        """
        Deletes previous keyboard markup
        """
        return ReplyKeyboardRemove()

    def category_menu(self):
        """
        Creates a button layout in the 'CHOOSE GOODS' menu and returns the markup
        """
        self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
        self.markup.add(self.set_btn('SEMIPRODUCT'))
        self.markup.add(self.set_btn('GROCERY'))
        self.markup.add(self.set_btn('ICE_CREAM'))
        self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
        return self.markup

    def set_select_category(self, category):
        """
        Creates an inline button layout inside chosen product category and returns the markup
        """
        self.markup = InlineKeyboardMarkup(row_width=2)
        for item in self.BD.select_all_product_category(category):
            self.markup.add(self.set_inline_btn(item))

        return self.markup

    def orders_menu(self, step, quantity):
        """
        Creates and returns button markup in the order menu
        """

        self.markup = ReplyKeyboardMarkup(True, True)
        itm_btn_1 = self.set_btn('X', step, quantity)
        itm_btn_2 = self.set_btn('DOWN', step, quantity)
        itm_btn_3 = self.set_btn('AMOUNT_PRODUCTS', step, quantity)
        itm_btn_4 = self.set_btn('UP', step, quantity)

        itm_btn_5 = self.set_btn('BACK_STEP', step, quantity)
        itm_btn_6 = self.set_btn('AMOUNT_ORDERS', step, quantity)
        itm_btn_7 = self.set_btn('NEXT_STEP', step, quantity)
        itm_btn_8 = self.set_btn('APPLY', step, quantity)
        itm_btn_9 = self.set_btn('<<', step, quantity)

        self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
        self.markup.row(itm_btn_5, itm_btn_6, itm_btn_7)
        self.markup.row(itm_btn_9, itm_btn_8)

        return self.markup
