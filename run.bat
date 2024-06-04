set VENV_FOLDER=.venv

if not exist %VENV_FOLDER% (
    echo Creating virtual environment...
    python -m venv %VENV_FOLDER%
    echo Virtual environment created.
)

call %VENV_FOLDER%\Scripts\activate

pip install -r requirements.txt

python app.py

deactivate
pause
