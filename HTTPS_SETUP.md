# 🔒 Настройка HTTPS для AR приложения

## Почему нужен HTTPS?

**Камера устройства требует HTTPS соединения** для работы с WebRTC API. Без HTTPS приложение не сможет получить доступ к камере.

## 🚀 Быстрая настройка с ngrok

### 1. Установка ngrok

#### Windows
```bash
# Скачайте с https://ngrok.com/download
# Распакуйте в папку проекта
# Или используйте chocolatey:
choco install ngrok
```

#### macOS
```bash
# Homebrew
brew install ngrok

# Или скачайте с https://ngrok.com/download
```

#### Linux
```bash
# Скачайте с https://ngrok.com/download
# Или используйте snap:
sudo snap install ngrok
```

### 2. Регистрация на ngrok.com

1. Перейдите на [ngrok.com](https://ngrok.com)
2. Создайте бесплатный аккаунт
3. Получите ваш `authtoken`
4. Выполните команду:
```bash
ngrok config add-authtoken YOUR_TOKEN_HERE
```

### 3. Запуск с HTTPS

#### Вариант 1: Автоматический запуск
```bash
# Запустите сервер
python server.py

# В новом терминале запустите ngrok
ngrok http 8000
```

#### Вариант 2: Комбинированный скрипт
Создайте файл `start_https.bat` (Windows) или `start_https.sh` (Linux/macOS):

**Windows (start_https.bat):**
```batch
@echo off
start "AR Server" cmd /k "python server.py"
timeout /t 3
start "HTTPS Tunnel" cmd /k "ngrok http 8000"
echo.
echo 🌐 AR сервер запущен на http://localhost:8000
echo 🔒 HTTPS туннель создается...
echo 📱 Скопируйте HTTPS URL из ngrok терминала
echo.
pause
```

**Linux/macOS (start_https.sh):**
```bash
#!/bin/bash
echo "🚀 Запуск AR сервера..."
python server.py &
SERVER_PID=$!

echo "⏳ Ожидание запуска сервера..."
sleep 3

echo "🔒 Создание HTTPS туннеля..."
ngrok http 8000 &
NGROK_PID=$!

echo "🌐 AR сервер: http://localhost:8000"
echo "🔒 HTTPS туннель создается..."
echo "📱 Скопируйте HTTPS URL из ngrok терминала"

# Ожидание завершения
wait $SERVER_PID $NGROK_PID
```

## 🌐 Альтернативные способы получения HTTPS

### 1. Vercel (Бесплатно)
```bash
# Установка Vercel CLI
npm i -g vercel

# Развертывание
vercel
```

### 2. GitHub Pages
1. Создайте репозиторий
2. Загрузите файлы проекта
3. Включите GitHub Pages в настройках
4. Получите HTTPS URL

### 3. Netlify
1. Зарегистрируйтесь на netlify.com
2. Загрузите папку проекта
3. Получите HTTPS URL

## 🔧 Проверка HTTPS

После настройки HTTPS:

1. **Откройте HTTPS URL** в браузере
2. **Нажмите "Start AR Experience"**
3. **Разрешите доступ к камере**
4. **Наведите камеру на target изображение**

## 🚨 Устранение проблем

### Ошибка "Camera access denied"
- ✅ Убедитесь, что используете HTTPS
- ✅ Проверьте разрешения браузера
- ✅ Перезагрузите страницу

### ngrok не работает
- ✅ Проверьте авторизацию: `ngrok config check`
- ✅ Убедитесь, что порт 8000 свободен
- ✅ Проверьте файрвол

### Камера не инициализируется
- ✅ Используйте Chrome или Safari
- ✅ Проверьте консоль браузера (F12)
- ✅ Убедитесь, что камера не используется другими приложениями

## 📱 Тестирование на мобильных устройствах

1. **Запустите ngrok** на компьютере
2. **Скопируйте HTTPS URL** из ngrok терминала
3. **Откройте URL на мобильном устройстве**
4. **Разрешите доступ к камере**
5. **Наведите камеру на target изображение**

## 💡 Советы

- **Используйте Chrome** на Android для лучшей совместимости
- **Используйте Safari** на iOS (единственный поддерживаемый браузер)
- **Обеспечьте хорошее освещение** для лучшего распознавания
- **Держите камеру стабильно** при распознавании 