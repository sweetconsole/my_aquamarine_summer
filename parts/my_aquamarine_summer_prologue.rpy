
label my_aquamarine_summer_prologue:
    $ new_chapter(0, u"Моё аквамариновое лето.\nПролог")
    $ prolog_time()

    scene prologue_monitor_kino
    show unblink
    play music black_hill_a_wild_river_to_take_you_home loop fadein 2.0
    play sound2 sfx_computer_noise loop fadein 2.0
    pause(1.5)
    window show

    "Обычный вечер пятницы. Я сидел за компьютером и смотрел фильм. Зачёты сданы, можно и передохнуть маленько, хотя такой отдых не особо отличается от моего времяпровождения. Дом-учёба-дом, и всё за монитором."
    "Коротко о себе: Семён Персунов, двадцать пять лет от роду, студент. Работа есть, не сказал бы, что платят много, но на жизнь хватает. {w}Да и предки, если что, окажут помощь. В личной жизни всё спокойно, точнее она отсутствует. После нескольких неудач на любовном фронте замкнулся и не пытался с тех пор заводить отношения."
    "Зачем в очередной раз разочаровываться, портить себе нервы? И вроде я не такой страшила, чтобы девушки сторонились, но и на Ален Делона не тяну."
    "Впрочем, я отвлёкся."

    play sound sfx_phone_call

    "Где-то на середине фильма раздался звонок мобильника. Я взял трубку и услышал:"

    show phone disable with dissolve
    $ renpy.pause(0.5, hard=True)
    show phone enable with dissolve

    gln "Здорово, Перс!"

    "Перс. Не в восторге от этого прозвища, впрочем, привык со школы. {w}Звонил мой лучший друг Глеб. Интересно, что ему нужно."

    me "И тебе не хворать, братишка."

    gl "Ты сейчас не сильно занят?"

    me "Нет, вечер свободный."
    "Впрочем, как и всегда."

    gl "Отлично! Приедешь к восьми на техноложку? {w}Там группа наша собирается, зачёты сданы и это надо отметить."

    me "Я там нужен?"

    gl "Обижаешь, мы же друзья. {w}Да и потом, надо ведь иногда выходить из своей сычевальни."

    "С одной стороны он прав, иногда надо выходить в люди. А с другой - кого я там не видел, всё равно после новогодних праздников на экзаменах встретимся. Не особо хотелось идти, тем не менее я ответил:"

    me "Хорошо, буду."

    gl "Отлично, увидимся на месте. Бывай!"

    show phone disable with dissolve
    $ renpy.pause(0.5, hard=True)
    hide phone with dissolve

    "А правда, что я теряю? Схожу, проветрюсь. Почти семь вечера. "

    window hide
    scene winter_balcony with fade
    window show

    "Я быстро оделся, взял телефон, наушники, зарядку на всякий случай, накинул пальто и вышел из дома."

    stop sound2 fadeout 2.0
    window hide
    play music borrtex_we_are_saved loop fadein 2.0
    show intro_1 with dissolve
    $ renpy.pause(0.5, hard=True)
    show intro_2 with dissolve
    $ renpy.pause(2.0, hard=True)
    show intro_3 with dissolve
    $ renpy.pause(2.0, hard=True)
    show intro_4 with dissolve
    $ renpy.pause(2.0, hard=True)
    show intro_5 with dissolve
    $ renpy.pause(0.5, hard=True)
    show intro_6 with dissolve
    $ renpy.pause(2.0, hard=True)
    show intro_8 with dissolve
    play sound sfx_inhale
    $ renpy.pause(2.5, hard=True)
    show bus_stop with dissolve
    window show

    "Пять минут и я стою на остановке и жду автобус."

    play sound sfx_ikarus_arrive
    scene anim intro_9 with dissolve

    "И вот подъезжает старый ЛИАЗ и распахивает двери. "

    scene anim intro_11 with dissolve

    "Я даже не посмотрел на номер и вошёл в салон, спросил у водителя, доеду ли до нужной остановки, после чего устроился у окна. Ехать полчаса, можно вздремнуть. "

    scene bg intro_xx with dissolve
    play sound sfx_bus_interior_moving fadein 2.0

    "Я надел наушники, включил музыку и закрыл глаза."

    stop music fadeout 2.0
    stop sound fadeout 2.0
    window hide
    show blink

    jump my_aquamarine_summer_day_1