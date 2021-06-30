#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys
import subprocess
 
 
sys.path.append('../../') 
sys.path.append('./')  
from Config.Config import mainConfig
from Common import Source
from Config.AdConfig import mainAdConfig  
from Project.Resource import mainResource
from Common.File.FileUtil import FileUtil 
from Common.Platform import Platform

# https://docs.cocos.com/creator/3.0/manual/en/editor/publish/publish-in-command-line.html
class UnityBuild(): 
# 主函数的实现
    @staticmethod
    def Run(stros):  
        # 0f6 2f1
        UNITYPATH=""
        if Platform.isWindowsSystem():
            UNITYPATH="E:/Unity/"+Source.UNITY_VERSION_WIN+"/Editor/Unity.exe"
            UNITYPATH= "CocosCreator.exe"
        else:
            # UNITYPATH="/Applications/Unity/Hub/Editor/"+Source.UNITY_VERSION_MAC+"/Unity.app/Contents/MacOS/Unity" 
            UNITYPATH="/Applications/CocosCreator/Creator/3.0.0/CocosCreator.app/Contents/MacOS/CocosCreator"
            #  --project projectPath--build "platform=web-desktop;debug=true"


        
        PROJECT_PATH= mainResource.GetRootProjectUnity()

        
        methond = ""
        if stros == Source.ANDROID:
            methond = "BuildPlayer.PerformAndroidBuild"
        if stros == Source.IOS:
            methond = "BuildPlayer.PerformiPhoneBuild"
        if stros == Source.ScreenShot:
            methond = "BuildPlayer.ScreenshotBuild"

            

        print("unity_build  start stros=",stros)
        # cmd = UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  "+methond
        cmd = UNITYPATH+" --project"+ PROJECT_PATH+"--build"+ "\"platform=web-desktop;debug=true\""
        # ps = subprocess.Popen(cmd)
        # ps.wait()#让程序阻塞
        os.system(cmd)
        print("unity_build  end")

        if stros == Source.ScreenShot:
            if Platform.isWindowsSystem():
                cmd =  mainResource.GetDirProduct()+"/bin/game.exe"
            if Platform.isMacSystem():
                cmd =  "open "+mainResource.GetDirProduct()+"/bin/game.app"

            os.system(cmd)


# PROJECT_PATH="F:\sourcecode\unity\product\kidsgame\kidsgameUnity"

# companyName="moonma"
# productName="kidsgame"
# platform="0"
# outPath="F:\sourcecode\unity\product\kidsgame\project_android_output_cmd"
# arg0="参数谁便定义"
# E:\Program Files\Unity_All\2019.1.2f1\2019.1.2f1\Editor\Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  ProjectBuild.BuildAndroid -buildTarget Android -exportPackage project_android_output_cmd kidsgame
# subprocess.call(UNITYPATH+" -quit "+" -batchmode "+" -projectPath "+PROJECT_PATH+" -executeMethod  ProjectBuild.BuildAndroid "+companyName+" "+productName+" "+platform+" "+outPath+" "+arg0)

# Unity.exe -quit -batchmode -projectPath F:\sourcecode\unity\product\kidsgame\kidsgameUnity -executeMethod  BuildPlayer.PerformAndroidUCBuild
#  os.system("adb connect "+myaddr)

