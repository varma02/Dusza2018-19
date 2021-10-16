pip install wheel pyinstaller
pyinstaller --distpath "./build/" --workpath "./temp/" --onefile index.py
rmdir -r "./temp/" -ErrorAction SilentlyContinue
rmdir -r "./__pycache__/" -ErrorAction SilentlyContinue
rm "./index.spec" -ErrorAction SilentlyContinue