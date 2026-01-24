@echo off
echo ==========================================
echo Demarrage de Yann's Note Flask App
echo ==========================================
echo.

if not exist venv (
    echo Environnement virtuel non trouve!
    echo Veuillez executer setup.bat d'abord
    pause
    exit /b 1
)

echo Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo Lancement de l'application...
echo.
echo L'application sera disponible sur: http://localhost:5000
echo.
echo Appuyez sur Ctrl+C pour arreter le serveur
echo.

python app.py

pause
