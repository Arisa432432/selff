'========================================
' 여러 파이썬 스크립트를 백그라운드 실행
'========================================

Set WshShell = CreateObject("WScript.Shell")

' 실행할 파이썬 스크립트 목록
Dim files
files = Array("main.py", "main (2).py", "main (3).py")

' 각 스크립트를 백그라운드에서 실행
For Each f In files
    WshShell.Run "python """ & f & """", 0
Next

' 객체 해제
Set WshShell = Nothing