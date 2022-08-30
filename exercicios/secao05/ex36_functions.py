def real_br_money_mask(my_value):
    """
    Transforma um valor float em um str formatado para a moeda real.
    :param my_value: valor em float
    :return: str formatada
    """
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')
