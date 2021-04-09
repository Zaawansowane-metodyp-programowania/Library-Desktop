import configparser

config = configparser.ConfigParser()


def writing(style):
    """
    Służy do zapisania informacji na temat aktualnie wybranego tematu graficznego.
    :param style: str
    """
    try:
        config.add_section('style')
    except configparser.DuplicateSectionError as e:
        print(e)
    config['style']['active'] = style

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def read_style():
    """
    Odczytuje zapisane informacje z pliku config.ini, w którym znajdują się dane na temat wybranego
    tematu graficznego.
    :rtype: str
    """
    config.read('config.ini')
    return config['style']['active']
