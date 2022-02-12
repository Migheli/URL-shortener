Обрезка ссылок с помощью Битли
Проект позволяет, используя терминал среды разработки python:
1. Создавать короткие ссылки (битлинки) с помощью популярного сервиса bitly.
2. Получать информацию о количестве кликов по битлинку, созданному в проекте.

В случае, если пользователь вводит в качестве ссылки полный URL, программа возвращает битлинк. 
Если введен битлинк, возвращается количество кликов по данному битлинку.
Распознавание ввода происходит автоматически. 
Ввод производится в терминале среды разработки, сама ссылка указывается в качестве аргумента в терминале.

Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
pip install -r requirements.txt
Ключ для доступа к API bitlink можно получить, следуя этой инструкции:
1. Регистрируемся в сервисе битли: https://bitly.com/
2. В профиле переходим в Settings - Developers Settings - API - Access Token.
3. Вводим корректный пароль от битли и жмем Generate Token. Токен готов!
4. Читаем документацию битли: https://dev.bitly.com/
Токен представляет собой набор из 40 различных символов (цифры и буквы латинского алфавита). 
ВАЖНО! Никогда не публикуйте и не разглашайте Ваш токен, с помощью токена возможен доступ к Вашим данным на битли. Токен должен быть записан в переменную окружения BITLY_TOKEN в файле dot.env: BITLY_TOKEN='your_access_token'

Файл dot.env должен быть расположен в одной директории с main.py.
ВАЖНО! При использовании PyCharm обязательно необходимо предварительно разрешить среде разработки работу с переменными окружения.
Плагин для PyCharm и инструкция по его установке здесь: https://plugins.jetbrains.com/plugin/7861-envfile 
Также в PyCharm необходимо в меню Project главного окна сделать щелчок ПКМ по папке проекта и выбрать следующие пункты - Mark Directory as - Mark as sources route

Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.