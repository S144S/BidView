from pages import home

home_layouts = home.Home()


def main_navigator(pathname):
    """
    The main navigator callback.

    :param pathname: the current pathname
    :return: the layout of the current page
    """
    if pathname == "/analysis":
        return None
    else:
        return home_layouts.layout()
