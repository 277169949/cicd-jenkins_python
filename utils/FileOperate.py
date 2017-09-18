#coding=utf-8
import os
class FileOperate:
    def readfile(self,filePath):
        filePath=os.path.abspath('.')+"\\"+filePath
        print filePath
        file = open(filePath )
        fileContent= open(filePath, 'rb').read()
        return fileContent

    def createfile(self, filePath,fileContent):

        filePath = os.path.abspath('.') + "\\" + filePath.replace('/', '\\')
        #如果路径不存在时创建目录
        file_path=os.path.split(filePath)[0]
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        file = open(filePath,'a')
        file.write(fileContent)
        file.close()

    if __name__ == '__main__':


        print os.path.split('F:\\PythonScript\\cicd-jenkins_python\\JobConfig\\template_ci\\aaaaaa.xml')[0]
#F:\\PythonScript\\cicd-jenkins_python\\JobConfig\\template_ci\\aaaaaa.xml