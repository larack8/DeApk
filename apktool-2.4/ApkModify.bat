@echo off
rem Author:	black-snowflake
rem Function:	Decode & Code Apk File
rem Date:	2012-7-15
rem Name:	Apk Modfily Tools
rem Publ:	bbs.91dongji.com



Rem Warning:	Please Don't Modfily This Application and The Script! Thanks!
Rem Notice:	Use Your Own Risk 
	
path %~dp0;%path%
color fc
if /i "%~x1" equ "" goto Code

:Dcode
title Apk������
:CheckFile
if /i "%~x1" neq ".apk" (
	echo.
	echo.===^>������ѡ��Apk�ļ����ԣ�
	echo.
	goto Exit
)
echo.
java -jar "%~dp0apktool_bsf.jar" d -f "%~1" "%~1"

:exit
echo.
echo.===^>Done
echo.
pause
exit

:Code
title Apk�ر���
echo.
java -jar "%~dp0apktool_bsf.jar" b -f "%~1"

goto exit