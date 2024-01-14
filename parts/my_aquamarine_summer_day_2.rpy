
label my_aquamarine_summer_day_2:
    window hide

    $ renpy.pause(1.0, hard=True)

    $ new_chapter(2, u"Моё аквамариновое лето.\nДень второй")

    scene my_aquamarine_summer_backdrop_day_2 with fade
    $ renpy.pause(1.5, hard=True)
    $ persistent.sprite_time = "day"
    $ day_time()

    scene prolog_1 
    show unblink
    $ renpy.pause(1.0, hard=True)
    window show

    "Мне снилось, будто бы сейчас лето и я отдыхаю в пионерлагере. А нет, со мной это действительно произошло. Пробудился я от того, что яркие солнечные лучи били в глаза."

    window hide
    $ renpy.pause(1.0, hard=True)
    scene int_house_of_mt_day with dissolve
    play ambience ambience_int_cabin_day loop fadein 2.0
    play music lonesome_shepherd loop fadein 2.0
    $ renpy.pause(1.0, hard=True)
    window show

    "Будильник на столе показывал, что скоро полдень, завтрак благополучно проспал, зато выспался и чувствую себя превосходно."
    
    stop ambience fadeout 2.0
    window hide
    $ renpy.pause(1.0, hard=True)
    scene ext_house_of_mt_day with dissolve
    play ambience ambience_camp_center_day loop fadein 2.0
    play sound sfx_open_door_1
    $ renpy.pause(1.0, hard=True)
    window show
    
    "Одеваюсь и выхожу на улицу и тут к домику подходит Ольга Дмитриевна, одетая в спортивный костюм:"