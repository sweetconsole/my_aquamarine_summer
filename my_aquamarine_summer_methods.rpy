

init 3 python:
    def mas_timeskip_transition():
        return ImageDissolve(path_dir + "images/transitions/timeskip.png", 2.0, ramplen=0, reverse=False, alpha=True)

    def my_aquamarine_summer_timeskip():
        renpy.scene()
        renpy.show("bg black")
        renpy.with_statement(dissolve)
        renpy.play(path_dir + "sounds/sfx/sfx_clock_transition_sound.ogg", channel="sound")
        renpy.show("my_aquamarine_summer_clock", at_list=[truecenter])
        renpy.with_statement(mas_timeskip_transition())
        renpy.hide("my_aquamarine_summer_clock")
        renpy.with_statement(mas_timeskip_transition())
        renpy.music.stop(channel="sound", fadeout=2.0)