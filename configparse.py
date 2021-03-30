import configparser

config = configparser.ConfigParser()


def writing(style):
    try:
        config.add_section('style')
    except configparser.DuplicateSectionError as e:
        print(e)
    config['style']['active'] = style

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def read_style():
    config.read('config.ini')
    return config['style']['active']
