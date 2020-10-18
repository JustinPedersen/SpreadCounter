@echo off

echo "Compiling .ui files"
call compile_ui_files.bat

echo
echo "Compiling SpreadCounter executable"

cd ..
python -m PyInstaller --noconfirm --log-level=WARN --name SpreadCounter --onefile --icon "src/icons/icon.ico" --hidden-import PySide2.QtXml --add-data "%cd%\src\icons\no_image.png;.\icons" --noconsole src/main.py


echo
echo "Cleanup"


md .\build\spread_counter_build

move .\SpreadCounter.spec .\build\spread_counter_build
move .\dist .\build\spread_counter_build
move .\build\SpreadCounter .\build\spread_counter_build

cd .\compile
