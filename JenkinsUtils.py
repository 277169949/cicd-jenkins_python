#coding=utf-8
import jenkins
import JenkinsUtils
from utils.FileOperate import FileOperate


class JenkinsUtils:
    baseurl = 'http://localhost:8080/jenkins'
    username = 'lieber'
    password = '123456'
    server = jenkins.Jenkins(baseurl, username=username, password=password)

    @classmethod
    def getjob_fullname_byview(self ,view_name):
        '''
        返回某个视图下的所有job  fullname名字（JOB__NAME）
        :param view_name:
        :return:返回某个视图下的所有job名字
        '''
        url = JenkinsUtils.baseurl+'/view/'+view_name
        server = jenkins.Jenkins(url, username=JenkinsUtils.username, password=JenkinsUtils.password)
        joblists = server.get_jobs(view_name)
        jobfullnameList = []
        for job in joblists:
            jobfullnameList.append(job['fullname'])
        return jobfullnameList

    @classmethod
    def getjob_name_byview(self ,view_name):
        '''
        返回某个视图下的所有job JOB_BASE_NAME
        :param view_name:
        :return:返回某个视图下的所有job名字
        '''
        url = JenkinsUtils.baseurl+'/view/'+view_name
        server = jenkins.Jenkins(url, username=JenkinsUtils.username, password=JenkinsUtils.password)
        joblists = server.get_jobs(view_name)
        jobnameList = []
        for job in joblists:
            jobnameList.append(job['name'])
        return jobnameList

    def job_save_config_byview(self,view_name):
        '''
        传入视视图字，返回该视图下所有的job的配置信息 （不包括文件夹类型）
        :param view_name:
        :return:
        '''
        opt=JenkinsUtils()
        jobnameList=opt.getjob_fullname_byview(view_name)
        server = jenkins.Jenkins(JenkinsUtils.baseurl, username=JenkinsUtils.username, password=JenkinsUtils.password)
        for job in jobnameList:
            f = FileOperate()
            filepath= 'JobConfig\\'+job+".xml"
            filecontent =server.get_job_config(job)
            f.createfile(filepath,filecontent)


    def createjob(self,jobname,config_file_path):
        server = jenkins.Jenkins(JenkinsUtils.baseurl, username=JenkinsUtils.username, password=JenkinsUtils.password)
        f = FileOperate()
        config_xml = f.readfile(config_file_path)
        server.create_job(jobname, config_xml)

    def createView(self,name):
        server = jenkins.Jenkins(JenkinsUtils.baseurl, username=JenkinsUtils.username, password=JenkinsUtils.password)
        f = FileOperate()
        conig_xml = f.readfile("ConfigXML\\viewtemplate.xml")
        server.create_view(name,conig_xml)

    def batchCreateJob(self):
        self.createjob("template_deploy", "ConfigXML\\folder_job_config.xml")

if __name__ == '__main__':
    opt=JenkinsUtils()
    print opt.job_save_config_byview('template')







