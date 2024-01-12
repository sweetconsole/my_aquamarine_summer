
label my_aquamarine_summer_day_1:
    window hide

    $ renpy.pause(1.0, hard=True)

    $ backdrop = "days"
    $ new_chapter(1, u"Моё аквамариновое лето.\nДень первый")
    $ persistent.sprite_time = "day"
    $ day_time()

    show bg int_bus
    play ambience ambience_camp_entrance_day loop fadein 2

    show unblink

    $ renpy.pause(1, hard=True)

    window show

    "Проснулся я от того, что стало жарко. Водитель, должно быть, печку на полную включил. Хм, вроде ненадолго вздремнул, а по ощущениям будто бы пару часов проспал. В глаза ударил дневной свет."
    "Встаю с места, оглядываюсь и понимаю: что-то не так. За окном светло, как будто бы день сейчас. В салоне я один, и, похоже, водителя нет на месте."
    "Что за чертовщина? {w}Я ехал на встречу с одногруппниками, был декабрьский вечер. {w}А сейчас летний день."
    "Я подошёл к водительскому сидению. Да, никого нет. Посмотрел в зеркало и ахнул: на меня смотрело лицо семнадцатилетнего подростка. Свежее, без трёхнедельной щетины, без мешков под глазами. Мало того, что я оказался непонятно где, так ещё и помолодел."

    "Надо бы успокоиться, разобраться в ситуации. Посмотрим, что есть в бардачке. Открываю бардачок и достаю пачку сигарет. В жизни курю очень редко, только когда нервничаю сильно, и это тот случай."

    scene ext_camp_entrance_day with dissolve

    "Я вышел из автобуса с трофейными сигаретами, и первое что мне бросилось в глаза- кирпичная ограда, металлические ворота, по бокам которых статуи пионеров, и возвышающаяся над воротами надпись - «пионерлагерь Совёнок»."
    "Становится всё интереснее, и статуи, и ворота выглядят как новые, не потрёпанные временем, как это часто бывало в заброшенных местах, да и не только. В своё время лазил по заброшкам, насмотрелся на эти артефакты ушедшей эпохи. Впрочем обшарпанные статуи я и в одном городском парке видел, не пощадило время скульптуры."
    "В голове пронеслось: может я ещё и в другое время переместился, как в фантастических рассказах? Я уже ничему не удивлюсь, летнего пейзажа и омоложения лет на восемь вполне хватило."

    scene ext_bus with dissolve

    "Я оглянулся в сторону автобуса и увидел новенький Икарус{w}, хм, садился я в старенький ЛИАЗ. {w}Интересно, сколько сейчас времени?"

    show phone disable with dissolve
    $ renpy.pause(0.5, hard=True)
    show phone enable with dissolve

    "Достаю смартфон: так, уже два часа дня. И связь не ловит, замечательно, хотя, чего я ожидал? Если я сейчас в совке, то до сотовых вышек ещё далеко. {w}Да и кому мне звонить?"

    show phone disable with dissolve
    $ renpy.pause(0.5, hard=True)
    hide phone with dissolve

    "Убираю смартфон обратно в карман пальто, затем достаю зажигалку и затягиваюсь трофейной сигаретой. Я закашлялся, лёгкие жгло. Я редко курил, так сейчас ещё и организм помолодел."

    scene ext_camp_entrance_day with dissolve
    play sound sfx_carousel_squeak

    "Выкидываю сигарету и, как оказалось, вовремя. Одновременно с этим слышу, как скрипнули ворота."

    show sl pioneer smile with dissolve

    "Выходит девушка, красивая, голубоглазая, с длинными светлыми косами, на вид семнадцать, одета в пионерскую форму. И обращается ко мне:"

    sl "Привет, ты наверное новенький?"