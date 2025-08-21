@echo off
chcp 65001 >nul
title Magic Album AR Server

echo.
echo ========================================
echo    Magic Album AR - Локальный сервер
echo ========================================
echo.

echo 🚀 Запуск AR сервера...
echo 📁 Директория: %CD%
echo 🌐 Порт: 8000
echo.

echo ⚠️  ВАЖНО: Для работы с камерой нужен HTTPS!
echo 💡 Используйте ngrok для создания HTTPS туннеля
echo.

python server.py

if errorlevel 1 (
    echo.
    echo ❌ Ошибка запуска Python сервера
    echo 💡 Убедитесь, что Python установлен
    echo 💡 Попробуйте: python --version
    echo.
    pause
) 