# -* - coding: UTF-8 -* -
import ConfigParser
import os


class ConfigParserUtils:
    conf = ConfigParser.ConfigParser()

    def __init__(self):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        os.chdir(dir_name)

    @classmethod
    def get_config_value_by_key(cls, section, file_path, key):
        file_path = '../' + file_path
        cls.conf.read(file_path)
        # 获取指定的section， 指定的option的值
        key_value = cls.conf.get(section, key)
        return key_value

    @classmethod  # 获取所有的section
    def get_all_sections_from_config_file(cls, file_path):
        file_path = '../' + file_path
        cls.conf.read(file_path)
        sections = cls.conf.sections()
        return sections

    @classmethod  # 更新指定section, option的值
    def update_value_by_section_and_key(cls, file_path, section_name, key, key_value):
        file_path = '../' + file_path
        cls.conf.read(file_path)
        cls.conf.set(section_name, key, key_value)
        cls.conf.write(open(file_path, 'w'))
        # print 'Config file update succeeded.'


if __name__ == '__main__':
    ConfigParserUtils.update_value_by_section_and_key('config/jenkins_config.ini', 'test', 'port', '12345')
