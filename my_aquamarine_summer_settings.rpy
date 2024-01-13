
init:
    $ path_dir = "mods/my_aquamarine_summer/"

    # MUSIC
    $ soft_piano_music_senbonzakura = path_dir + "sounds/music/soft_piano_music_senbonzakura.ogg"

    # SOUNDS
    $ sfx_phone_call = path_dir + "sounds/sfx/phone_call.ogg"
    $ sfx_alarm_clock = path_dir + "sounds/sfx/sfx_alarm_clock.ogg"
    $ sfx_creaking_floor = path_dir + "sounds/sfx/sfx_creaking_floor.ogg"

    # BG
    image ext_house_of_un_night = path_dir + "images/bg/ext_house_of_un_night.jpg"
    image ext_musclub_night = path_dir + "images/bg/ext_musclub_night.jpg"
    image ext_musclub_sunset = path_dir + "images/bg/ext_musclub_sunset.jpg"
    image int_dining_hall_distribution_table_sunset = im.MatrixColor( im.Composite((1920, 1080), (0,0), path_dir + "images/bg/int_dining_hall_distribution_table_sunset.jpg"), im.matrix.tint(0.94, 0.82, 1.0) )
    image int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"
    image int_musclub_sunset = path_dir + "images/bg/int_musclub_sunset.jpg"

    # CG
    image d1_food_without_cutlets = path_dir + "images/cg/d1_food_without_cutlets.jpg"
    image me_mi_guitar_musclub = path_dir + "images/cg/me_mi_guitar_musclub.jpg"
    image mi_piano_musclub = path_dir + "images/cg/mi_piano_musclub.jpg"
    image prologue_monitor_kino = path_dir + "images/cg/prologue_monitor_kino.jpg"
    image starry_sky = path_dir + "images/cg/starry_sky.jpg"
    image winter_balcony = path_dir + "images/cg/winter_balcony.jpg"

    # MISC
    image my_aquamarine_summer_chair = path_dir + "images/misc/chair.png"
    image my_aquamarine_summer_clock = path_dir + "images/misc/clock.png"
    image phone disable = path_dir + "images/misc/phone_disable.png"
    image phone enable = path_dir + "images/misc/phone_enable.png"

    image my_aquamarine_summer_backdrop_day_1 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_1.jpg"
    image my_aquamarine_summer_backdrop_day_2 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_2.jpg"
    image my_aquamarine_summer_backdrop_day_3 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_3.jpg"
    image my_aquamarine_summer_backdrop_day_4 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_4.jpg"
    image my_aquamarine_summer_backdrop_day_5 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_5.jpg"
    image my_aquamarine_summer_backdrop_day_6 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_6.jpg"
    image my_aquamarine_summer_backdrop_day_7 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_7.jpg"

    # CHAIRS
    image my_aquamarine_summer_chair_left:
        "my_aquamarine_summer_chair"
        left
        yalign 0.0

    image my_aquamarine_summer_chair_center:
        "my_aquamarine_summer_chair"
        center
        yalign 0.0

    image my_aquamarine_summer_chair_right:
        "my_aquamarine_summer_chair"
        right
        yalign 0.0

    # Cook
    image ck normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png") )

    image ck sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png") )

