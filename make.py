import PyInstaller.__main__

scriptname = 'coldCardExe.py'

PyInstaller.__main__.run([
    scriptname,
    #'--name=%s' % package_name,
    '--onefile',
])
