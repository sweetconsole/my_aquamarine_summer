
init:
    $ path_dir = "mods/my_aquamarine_summer/"

    # msuic
    $ black_hill_a_wild_river_to_take_you_home = path_dir + "sounds/music/black_hill_a_wild_river_to_take_you_home.ogg"
    $ borrtex_we_are_saved = path_dir + "sounds/music/borrtex_we_are_saved.ogg"
    $ carefree = path_dir + "sounds/music/carefree.ogg"
    $ catch_the_hedge = path_dir + "sounds/music/catch_the_hedge.ogg"
    $ everyday = path_dir + "sounds/music/everyday.ogg"
    $ fogive_me = path_dir + "sounds/music/fogive_me.ogg"
    $ jay_lounge_breath_of_fresh_air = path_dir + "sounds/music/jay_lounge_breath_of_fresh_air.ogg"
    $ kiss_you = path_dir + "sounds/music/kiss_you.ogg"
    $ last_hope = path_dir + "sounds/music/last_hope.ogg"
    $ lastlight_guitar = path_dir + "sounds/music/lastlight_guitar.ogg"
    $ laugh_throught_the_universe = path_dir + "sounds/music/laugh_throught_the_universe.ogg"
    $ lonesome_shepherd = path_dir + "sounds/music/lonesome_shepherd.ogg"
    $ marvin_kopp_every_day_like_the_last = path_dir + "sounds/music/marvin_kopp_every_day_like_the_last.ogg"
    $ soft_piano_music_senbonzakura = path_dir + "sounds/music/soft_piano_music_senbonzakura.ogg"

    # sounds
    $ sfx_girl_screech = path_dir + "sounds/sfx/sfx_girl_screech.ogg"
    $ sfx_phone_call = path_dir + "sounds/sfx/phone_call.ogg"
    $ sfx_alarm_clock = path_dir + "sounds/sfx/sfx_alarm_clock.ogg"
    $ sfx_creaking_floor = path_dir + "sounds/sfx/sfx_creaking_floor.ogg"

    # bg
    image ext_house_of_un_night = path_dir + "images/bg/ext_house_of_un_night.jpg"
    image ext_musclub_night = path_dir + "images/bg/ext_musclub_night.jpg"
    image ext_musclub_sunset = path_dir + "images/bg/ext_musclub_sunset.jpg"
    image int_dining_hall_distribution_table_sunset = im.MatrixColor( im.Composite((1920, 1080), (0,0), path_dir + "images/bg/int_dining_hall_distribution_table_sunset.jpg"), im.matrix.tint(0.94, 0.82, 1.0) )
    image int_dining_hall_people_sunset = path_dir + "images/bg/int_dining_hall_people_sunset.jpg"
    image int_musclub_sunset = path_dir + "images/bg/int_musclub_sunset.jpg"
    image int_music_club_mattresses_day = path_dir + "images/bg/int_music_club_mattresses_day.jpg"
    image int_music_club_mattresses_night_lights_on = path_dir + "images/bg/int_music_club_mattresses_night_lights_on.jpg"
    image int_music_club_mattresses_night = path_dir + "images/bg/int_music_club_mattresses_night.jpg"
    image int_music_club_mattresses_sunset = path_dir + "images/bg/int_music_club_mattresses_sunset.jpg"

    # cg
    image d1_food_without_cutlets = path_dir + "images/cg/d1_food_without_cutlets.jpg"
    image library_mz_sleep = path_dir + "images/cg/library_mz_sleep.jpg"
    image me_mi_guitar_musclub = path_dir + "images/cg/me_mi_guitar_musclub.jpg"
    image mi_piano_musclub = path_dir + "images/cg/mi_piano_musclub.jpg"
    image prologue_monitor_kino = path_dir + "images/cg/prologue_monitor_kino.jpg"
    image starry_sky = path_dir + "images/cg/starry_sky.jpg"
    image ul_un_grasshopper = path_dir + "images/cg/ul_un_grasshopper.jpg"
    image winter_balcony = path_dir + "images/cg/winter_balcony.jpg"

    # misc
    image my_aquamarine_summer_chair = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/misc/my_aquamarine_summer_chair.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/misc/my_aquamarine_summer_chair.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/misc/my_aquamarine_summer_chair.png") )

    image my_aquamarine_summer_clock = path_dir + "images/misc/my_aquamarine_summer_clock.png"
    image phone disable = path_dir + "images/misc/phone_disable.png"
    image phone enable = path_dir + "images/misc/phone_enable.png"

    image my_aquamarine_summer_backdrop_day_1 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_1.jpg"
    image my_aquamarine_summer_backdrop_day_2 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_2.jpg"
    image my_aquamarine_summer_backdrop_day_3 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_3.jpg"
    image my_aquamarine_summer_backdrop_day_4 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_4.jpg"
    image my_aquamarine_summer_backdrop_day_5 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_5.jpg"
    image my_aquamarine_summer_backdrop_day_6 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_6.jpg"
    image my_aquamarine_summer_backdrop_day_7 = path_dir + "images/days/my_aquamarine_summer_backdrop_day_7.jpg"

    # chairs
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

    # cook
    image ck normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_normal.png") )

    image ck sad = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/ck/ck_sad.png") )

    # mt Sport
    image mt sport normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mt/mt_sport_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mt/mt_sport_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True, im.Composite((900, 1080), (0,0), path_dir + "images/sprites/mt/mt_sport_normal.png") )


