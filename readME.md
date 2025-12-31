To create virtual Environment:
PS C:\Users\02bin\OneDrive\Documents\Python\fastapi> py -3 -m venv venv
Control Shift P to open command pallete or View
Select Python: Select Interpreter and chose this path:
venv/Scripts/python.exe
Then activate it in the terminal
CMD:
    PS C:\Users\02bin\OneDrive\Documents\Python\fastapi> venv/Scripts/activate.bat
Powershell:
    PS C:\Users\02bin\OneDrive\Documents\Python\fastapi> .\venv\Scripts\Activate.ps1

Then install fastapi with:
    pip install fastapi[all]

    (check all insatllations with pip freeze)

run server:
    uvicorn app.main:app --reload

To view documentation:
    http://127.0.0.1:8000/docs
    or
    http://127.0.0.1:8000/redoc