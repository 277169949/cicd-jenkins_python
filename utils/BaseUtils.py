# coding=utf-8
import os


class BaseUtils:
    def __init__(self):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        os.chdir(dir_name)