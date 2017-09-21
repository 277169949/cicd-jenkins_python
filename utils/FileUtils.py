# coding=utf-8
import os


class FileUtils:
    def __init__(self):
        dir_name = os.path.dirname(os.path.abspath(__file__))
        os.chdir(dir_name)

    @classmethod
    def read_file(cls, file_path):
        file_path = '../' + file_path
        file_content = open(file_path, 'rb').read()
        return file_content

    @classmethod
    def create_file(cls, file_path, file_content):
        file_path = '../'+file_path
        file_path = file_path.replace('/', '\\')
        # 如果路径不存在时创建目录
        file_path = os.path.split(file_path)[0]
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        f = open(file_path, 'a')
        f.write(file_content)
        f.close()


if __name__ == '__main__':
    a = FileUtils()
    print a.read_file('README.md')
