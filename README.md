# Tower_defence_Golear_Karpenko
[![build status](
  http://img.shields.io/travis/Disadvantaged/Tower_defence_Golear_Karpenko/master.svg?style=flat)](
 https://travis-ci.org/Disadvantaged/Tower_defence_Golear_Karpenko)


Tower defence
(Пишем вдвоем)

О чем проект: есть карта с дорогой. По бокам от дороги можно ставить башни. По дороге идут противники. Их цель - добраться до базы, наша цель - не пустить их. Для этого ставятся башни разных типов(имеющие разные "способности"). 

Что по идее надо: графический интерфейс, использование фабричного метода проектирования для создания башен

Запуск проекта после установки выполняется командой
    tower_defence
Также можно запустить его с помощью
    python3 -m Tower_defence_Golear_Karpenko

Как играть:
Play - новая игра. На счету есть определенная сумма.
Можем покупать башни разной стоимости.
Каждый дошедший до финиша враг - -200 к счету.

Новая волна: +500 к текущему счету. Башни остаются с предыдущей волны, но можно ставить новые.
Всего волн 3. Если в какой-то момент счет становится отрицательным - игрок проиграл.
Если прошли 3 волны и мы выжили (положительный счет) - победа.

Башни различаются стоимостью, дальностью, скоростью стрельбы и уроном. Убивают врагов в определенном радиусе, стреляя с определенной частотой (каждый выстрел отбирает часть жизни противника). 
