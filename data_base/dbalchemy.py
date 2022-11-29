from os import path
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base.dbcore import Base

from settings import config
from models.product import Product
from models.order import Order
from settings import utility


class Singleton(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """
    Manager class for working with the database
    """

    def __init__(self):
        """
        Session initialization and database connection
        """
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    def select_all_product_category(self, category):
        """
        Returns all category products
        """
        result = self._session.query(Product).filter_by(category_id=category).all()
        self.close()
        return result

    def close(self):
        """
        Closes a session
        """
        self._session.close()

    # Order handling

    def _add_orders(self, quantity, product_id, user_id):
        """
        Order filling method
        """
        all_id_product = self.select_all_product_id()

        if product_id in all_id_product:
            quantity_order = self.select_order_quantity(product_id)
            quantity_order += 1
            self.update_order_value(product_id, 'quantity', quantity_order)

            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)
            return
        else:
            order = Order(quantity=quantity, product_id=product_id,
                          user_id=user_id, data=datetime.now())
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)

        self._session.add(order)
        self._session.commit()
        self.close()

    def select_all_product_id(self):
        """
        Returns all product id in the order
        """
        result = self._session.query(Order.product_id).all()
        self.close()
        return utility._convert(result)

    def select_order_quantity(self, product_id):
        """
        Returns the number of specified product in the order by product id
        """
        result = self._session.query(Order.quantity).filter_by(
            product_id=product_id).one()
        self.close()
        return result.quantity

    def update_order_value(self, product_id, name, value):
        """
        Updates specified value of the specified order item
        by product id
        """
        self._session.query(Order).filter_by(
            product_id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_quantity(self, rownum):
        """
        Returns the number of items in stock by product id - rownum
        This id is determined when selecting a product by inline bot buttons.
        """
        result = self._session.query(
            Product.quantity).filter_by(id=rownum).one()
        self.close()
        return result.quantity

    def update_product_value(self, rownum, name, value):
        """
        Updates specified value of a product in stock
        by product id - rownum
        """
        self._session.query(Product).filter_by(
            id=rownum).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_name(self, rownum):
        """
        Returns the name of a product
        by product id - rownum
        """
        result = self._session.query(Product.name).filter_by(id=rownum).one()
        self.close()
        return result.name

    def select_single_product_title(self, rownum):
        """
        Returns the trademark of a product
        by product id - rownum
        """
        result = self._session.query(Product.title).filter_by(id=rownum).one()
        self.close()
        return result.title

    def select_single_product_price(self, rownum):
        """
        Returns the price of a product
        by product id - rownum
        """
        result = self._session.query(Product.price).filter_by(id=rownum).one()
        self.close()
        return result.price

    def count_rows_order(self):
        """
        Returns the number of items in the order
        """
        result = self._session.query(Order).count()
        self.close()
        return result

    def delete_order(self, product_id):
        """
        Deletes selected order items
        """
        self._session.query(Order).filter_by(product_id=product_id).delete()
        self._session.commit()
        self.close()

    def delete_all_order(self):
        """
        Deletes all order items
        """

        all_orders_id = self.select_all_orders_id()

        for item in all_orders_id:
            self._session.query(Order).filter_by(id=item).delete()
            self._session.commit()
        self.close()

    def select_all_orders_id(self):
        """
        Returns all orders id
        """
        result = self._session.query(Order.id).all()
        self.close()
        return utility._convert(result)


