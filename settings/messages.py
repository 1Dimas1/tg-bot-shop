from .config import KEYBOARD, VERSION, AUTHOR

# response to the user when visiting the block "INFO"
my_store = """

<b>Welcome to MyStore !!!</b>

This application is designed
specifically for retail representatives,
as well as for storekeepers,
commercial organizations engaged
in wholesale and retail trade.

Sales representatives using MyStore
application can easily accept orders
from customers in a convenient and intuitive way. 
MyStore will help to create an order
and conveniently address it to the storekeeper
of the company for further order acquisition. 

"""
# response to the user when visiting the block "SETTINGS"
settings = """
<b>General application guidance:</b>

<i>Guidance:</i>

-<b>({}) - </b><i>backward</i>
-<b>({}) - </b><i>forward</i>
-<b>({}) - </b><i>add</i>
-<b>({}) - </b><i>reduce</i>
-<b>({}) - </b><i>next</i>
-<b>({}) - </b><i>previous</i>

<i>Special buttons:</i>

-<b>({}) - </b><i>delete</i>
-<b>({}) - </b><i>order</i>
-<b>({}) - </b><i>place an order</i>

<i>General Information:</i>

-<b>program version: - </b><i>({})</i>
-<b>developer: - </b><i>({})</i>


<b>{}My Store</b>

""".format(
    KEYBOARD['<<'],
    KEYBOARD['>>'],
    KEYBOARD['UP'],
    KEYBOARD['DOWN'],
    KEYBOARD['NEXT_STEP'],
    KEYBOARD['BACK_STEP'],
    KEYBOARD['X'],
    KEYBOARD['ORDER'],
    KEYBOARD['APPLY'],
    VERSION,
    AUTHOR,
    KEYBOARD['COPY'],
)
# ответ пользователю при добавлении товара в заказ
product_order = """
Chosen product:

{}
{}
Price: {} UAH

added to order!!!

Remaining in stock {} items. 
"""
# ответ пользователю при посещении блока с заказом
order = """

<i>Name:</i> <b>{}</b>

<i>Trade mark:</i> <b>{}</b>

<i>Price:</i> <b>{} uah per 1 item</b>

<i>Number of items:</i> <b>{} items</b> 
"""

order_number = """

<b>Order item № </b> <i>{}</i>

"""

no_orders = """
<b>You have no orders yet !!!</b>
"""

apply = """
<b>Your order has been placed !!!</b>

<i>The total cost of the order is:</i> <b>{} uah</b>

<i>The total quantity of items is:</i> <b>{} items</b>

<b>THE ORDER HAS BEEN SENT TO
 THE WAREHOUSE FOR PICKING !!!</b>
"""

MESSAGES = {
    'my_store': my_store,
    'product_order': product_order,
    'order': order,
    'order_number': order_number,
    'no_orders': no_orders,
    'apply': apply,
    'settings': settings
}
