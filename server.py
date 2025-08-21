#!/usr/bin/env python3
"""
Простой HTTP сервер для тестирования AR приложения
Запускает локальный сервер на порту 8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

# Настройки сервера
PORT = 8000
DIRECTORY = Path(__file__).parent

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Добавляем CORS заголовки для AR приложения
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Красивое логирование запросов
        print(f"🌐 {format % args}")

def main():
    """Запуск сервера"""
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 AR сервер запущен на http://localhost:{PORT}")
        print(f"📁 Рабочая директория: {DIRECTORY}")
        print(f"📱 Откройте http://localhost:{PORT} в браузере")
        print(f"⚠️  Для работы с камерой используйте HTTPS (ngrok)")
        print(f"🔄 Нажмите Ctrl+C для остановки сервера")
        print("-" * 50)
        
        try:
            # Автоматически открываем браузер
            webbrowser.open(f'http://localhost:{PORT}')
            
            # Запускаем сервер
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Сервер остановлен")
        except Exception as e:
            print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main() 