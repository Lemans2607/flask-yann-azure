@echo off
echo ==========================================
echo Installation de Yann's Note Flask App
echo ==========================================
echo.

echo Etape 1: Creation de l'environnement virtuel...
python -m venv venv
if %errorlevel% neq 0 (
    echo Erreur lors de la creation de l'environnement virtuel
    echo Essayez avec: py -m venv venv
    pause
    exit /b 1
)

echo.
echo Etape 2: Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo.
echo Etape 3: Mise a jour de pip...
python -m pip install --upgrade pip

echo.
echo Etape 4: Installation de Flask et Flask-SQLAlchemy...
pip install Flask Flask-SQLAlchemy

if %errorlevel% neq 0 (
    echo Erreur lors de l'installation des packages
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Installation terminee avec succes!
echo ==========================================
echo.
echo Pour demarrer l'application:
echo 1. Activez l'environnement: venv\Scripts\activate
echo 2. Lancez l'app: python app.py
echo.
echo Ou utilisez simplement: run.bat
echo.
pause
