import configparser

from Settings.Config import eleLocationPath


class IniToFile:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(eleLocationPath)

    def getSection(self,section_name):
        """
        获取节下面所有键值
        :param section_name:
        :return:
        """
        option_dict=dict(self.cf.items(section_name))
        return option_dict

    def getOptionValue(self,section_name,option_name):
        """
        获取某个节中键的值
        :param section_name:
        :param option_name:
        :return:
        """
        return self.cf.get(section_name,option_name)