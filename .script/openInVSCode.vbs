Set objShell = CreateObject("WScript.Shell")

' Check if VS Code is installed
Dim codePath
codePath = objShell.RegRead("HKEY_CLASSES_ROOT\Applications\Code.exe\shell\open\command\")

If IsEmpty(codePath) Then
    MsgBox "Visual Studio Code is not installed. Please install VS Code to open .mwText files.", vbExclamation, "Error"
Else
    ' Read the saved file path
    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objFile = objFSO.OpenTextFile("last_saved_path.txt", 1)
    fileToOpen = objFile.ReadLine
    objFile.Close

    objShell.Run "code " & Chr(34) & fileToOpen & Chr(34)
End If
