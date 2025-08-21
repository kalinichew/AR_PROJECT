@echo off
chcp 65001 >nul
title Magic Album AR - HTTPS Server

echo.
echo ========================================
echo    Magic Album AR - HTTPS Server
echo ========================================
echo.

echo 🚀 Запуск AR сервера...
start "AR Server" cmd /k "python server.py"

echo ⏳ Ожидание запуска сервера...
timeout /t 3 /nobreak >nul

echo 🔒 Создание HTTPS туннеля...
start "HTTPS Tunnel" cmd /k "ngrok http 8000"

echo.
echo 🌐 AR сервер запущен на http://localhost:8000
echo 🔒 HTTPS туннель создается...
echo 📱 Скопируйте HTTPS URL из ngrok терминала
echo.
echo 💡 Инструкции:
echo    1. В терминале ngrok найдите HTTPS URL
echo    2. Скопируйте его в браузер
echo    3. Нажмите "Start AR Experience"
echo    4. Разрешите доступ к камере
echo    5. Наведите камеру на target изображение
echo.
echo ⚠️  Для остановки закройте оба терминала
echo.
pause 