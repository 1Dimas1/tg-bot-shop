def _convert(list_convert):
    """
    Converts list from [(5,),(8,),...] to [5,8,...]
    """
    return [itm[0] for itm in list_convert]


def get_total_cost(bd):
    """
    Returns total order cost
    """
    all_product_id = bd.select_all_product_id()
    all_price = [bd.select_single_product_price(item) for item in all_product_id]
    all_quantity = [bd.select_order_quantity(item) for item in all_product_id]
    return total_cost(all_quantity, all_price)


def get_total_quantity(bd):
    """
    Returns the total amount of the ordered item
    """
    all_product_id = bd.select_all_product_id()
    all_quantity = [bd.select_order_quantity(itm) for itm in all_product_id]
    return total_quantity(all_quantity)


def total_cost(list_quantity, list_price):

    order_total_cost = 0

    for ind, item in enumerate(list_price):
        order_total_cost += list_quantity[ind]*list_price[ind]

        return order_total_cost


def total_quantity(list_quantity):

    order_total_quantity = 0

    for item in list_quantity:
        order_total_quantity += item

        return order_total_quantity
