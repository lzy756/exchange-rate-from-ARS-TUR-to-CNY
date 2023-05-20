@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo hello

REM 读取原来的ProxyServer的值
for /f "tokens=2*" %%A in ('reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer') do (
   set "originalValue=%%B"
)

REM 输出原值
echo %originalValue%

REM 检查原值是否已经以"http://"开头，如果没有，则添加
set "newValue=%originalValue%"
if not "!originalValue:~0,7!"=="http://" set "newValue=http://!originalValue!"

REM 输出要修改的值
echo %newValue%

REM 修改注册表项
reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /t REG_SZ /d "%newValue%" /f

endlocal

