@echo  apk_build_all
@set filepath = %~dp0 

cd ../../../../../../Common/PythonLaya/ProjectConfig/Script
python ProjectManager.py %~dp0 ApkBuild all


@Pause
