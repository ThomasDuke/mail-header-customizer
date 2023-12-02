$pythonUrl = "https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe"
$pythonInstaller = "python-3.12.0-amd64.exe"
Invoke-WebRequest -Uri $pythonUrl -OutFile $pythonInstaller

Start-Process -Wait -FilePath $pythonInstaller -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1"

Remove-Item -Path $pythonInstaller

$pipUrl = "https://bootstrap.pypa.io/get-pip.py"
Invoke-WebRequest -Uri $pipUrl -OutFile "get-pip.py"

python get-pip.py

Remove-Item -Path "get-pip.py"

pip install -r requirements.txt