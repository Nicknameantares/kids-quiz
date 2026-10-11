# Своя игра: Хогвартс

Детская викторина по Гарри Поттеру для показа на телевизоре, с кнопками на телефонах.
Сайт: https://nicknameantares.github.io/kids-quiz/

- `src/quiz.src.html` — исходник страницы (вопросы в массиве `ROUNDS`).
- `vendor/` — mqtt.js и qrcode-generator, встраиваются в страницу при сборке.
- `python3 build.py` собирает `index.html` (его и показывает GitHub Pages).
