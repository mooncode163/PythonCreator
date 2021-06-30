#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path 

sys.path.append('../../') 
sys.path.append('./') 

from Project.Resource import mainResource
from Common.File.ZipUtil import ZipUtil

class AppCode(): 
# 删除子目录
    def DeleteSubDir(self,sourceDir):
        for file in os.listdir(sourceDir):
            sourceFile = os.path.join(sourceDir,  file)
            #目录嵌套
            if os.path.isdir(sourceFile):
                if file!="CodeZip":
                    shutil.rmtree(sourceFile)
    


    def GetDirScriptApps(self):
        return mainResource.GetRootProjectUnity()+"/myLaya/src/script/Apps" 

    def GetDirSourceCode(self):
        return self.GetDirScriptApps() + "/" + mainResource.getGameType()
    def GetDirSourceCodeMain(self):
        return self.GetDirScriptApps() + "/" + "Main"

    def GetFileSourceCodeZip(self):
        return self.GetDirScriptApps() + "/CodeZip/" + mainResource.getGameType() + ".zip"

    def GetFileSourceCodeZipMain(self):
        return self.GetDirScriptApps() + "/CodeZip/" + mainResource.getGameType() + "_Main.zip"

    # 备份游戏代码到CodeZip  压缩zip
    def SaveCode(self):
        dir_code = self.GetDirSourceCode()
        file_zip = self.GetFileSourceCodeZip()
        
        if not os.path.exists(dir_code):
            return

        print(dir_code)
        print(file_zip)
        
        # 压缩目录
        ZipUtil.zipDir(dir_code,file_zip)

    def SaveCodeMain(self):
        dir_code = self.GetDirSourceCodeMain()
        file_zip = self.GetFileSourceCodeZipMain()
        
        if not os.path.exists(dir_code):
            return

        print(dir_code)
        print(file_zip)
        
        # 压缩目录
        ZipUtil.zipDir(dir_code,file_zip)


    # 从CodeZip的zip文件里解压到assets目录
    
    def CopyCode(self):
        dir_code = self.GetDirScriptApps()
        if not os.path.exists(dir_code):
            return

        file_zip = self.GetFileSourceCodeZip()

        print(dir_code)
        print(file_zip)

        self.DeleteSubDir(dir_code)

        flag = os.path.exists(file_zip)
        if flag:
            ZipUtil.un_zip(file_zip,dir_code)


    def CopyCodeMain(self):
        dir_code = self.GetDirScriptApps()
        if not os.path.exists(dir_code):
            return

        file_zip = self.GetFileSourceCodeZipMain()

        print(dir_code)
        print(file_zip)

        # self.DeleteSubDir(dir_code)

        flag = os.path.exists(file_zip)
        if flag:
            ZipUtil.un_zip(file_zip,dir_code)

# 主函数的实现
    def Run(self,type):   
        gameName = mainResource.getGameName()
        gameType = mainResource.getGameType()
        
        if type == "save":
            self.SaveCode()
            self.SaveCodeMain()

        if type == "copy":
            self.CopyCode()
            self.CopyCodeMain()

mainAppCode = AppCode()
