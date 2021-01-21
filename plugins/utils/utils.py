import plugins as plugins
import pkgutil

"""
    This module is dedicated to united all utilities for this project.
"""


def camel_case_to_joined_lower(string):
    """Receives a string in CamelCase and returns it in joined_lower

    :param string: string in camel case
    :type string: string

    :return: string in joined lower
    :rtype: string

    """
    to_joined_lower = ('_' + char if char.isupper() and i != 0 else char for i, char in enumerate(string))
    return ''.join(to_joined_lower).lower()


def joined_lower_to_camel_case(string):
    """Receives a string in joined_lower and returns it in CamelCase

    :param string: string in joined lower
    :type string

    :return string in camel case
    :rtype string
    """
    return ''.join([w.title() for w in string.split('_')])


def get_plugins_modules():
    """In the plugins folder, search for all plugins models

    :return list of plugins models
    :rtype list of strings """
    base_package = plugins.__name__
    plugin_modules = []
    for importer, modname, ispkg in pkgutil.iter_modules(plugins.__path__):
        if not ispkg:
            plugin_modules.append("{}.{}".format(base_package, modname))
    return plugin_modules


def get_module_plugin_name(class_name):
    """
        Given the name of the plugin class, it takes the name of its module

    :param class_name: class name of the plugin
    :type class_name: string

    :return: module name of the plugin
    :rtype: string
    """
    base_package = plugins.__name__
    plugin_name = camel_case_to_joined_lower(class_name)
    for importer, modname, ispkg in pkgutil.iter_modules(plugins.__path__):
        if not ispkg and plugin_name == modname:
            return f"{base_package}.{modname}"
