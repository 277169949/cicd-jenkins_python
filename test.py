# coding=utf-8
from JenkinsUtils import JenkinsUtils
from utils.ConfigParserUtils import ConfigParserUtils


if __name__ == '__main__':
    a = JenkinsUtils()
    config_parse = ConfigParserUtils()
    print config_parse.get_config_value_by_key('jenkins_config_local', 'config/jenkins_config.ini', 'jenkins_api_url')
