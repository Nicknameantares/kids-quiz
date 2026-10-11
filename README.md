# Своя игра: Хогвартс

Детская викторина по Гарри Поттеру для показа на телевизоре, с кнопками на телефонах.
Сайт: https://nicknameantares.github.io/kids-quiz/

- `src/quiz.src.html` — исходник: главная страница, вход команды, выбор раундов и сама игра (вопросы в массиве `POOL`).
- `vendor/` — mqtt.js и qrcode-generator, встраиваются в страницу при сборке.
- `python3 build.py` собирает `index.html` (его и показывает GitHub Pages).
