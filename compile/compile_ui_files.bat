@echo off
echo Compiling UI Files

cd..

pyside2-uic compile\ui_designer_files\main_window.ui > src\ui\main_window.py
pyside2-uic compile\ui_designer_files\project_window.ui > src\ui\project_window.py

cd .\build

echo Compiling UI Files Complete
