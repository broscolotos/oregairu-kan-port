## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Oregairu Kan")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.01"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "oregairukanpc"
define build.include_update = True


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/bgm/BGM52.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(0.1)
define config.exit_transition = Dissolve(0.1)


## Between screens of the game menu.

define config.intra_transition = Dissolve(0.1)


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_splash_transition = Dissolve(0.5)
define config.end_game_transition = Fade(2.0, 1.0, 1.0, color="#000000")


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 25


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 10

## Stops skipping of unseen text for dists
# config.allow_skipping = False
init -1:
    $ config.skipping = None

## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "oregairuzokupc"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

# define config.window_icon = "add_assets/window_icon.png"
define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Use to seperate patched content into a seperate file

    build.archive("bgm", "all")
    build.archive("sfx", "all")
    build.archive("voice", "all")
    build.archive("bg", "all")
    build.archive("chara", "all")
    build.archive("minigame", "all")
    build.archive("texts", "all")
    build.archive("Scripts", "all")
    build.archive("GUI", "all")
    build.archive("Movies", "all")
    build.archive("TL", "all")
    build.archive("Screens", "all")
    build.archive("Init", "all")
    build.archive("Options", "all")
    build.archive("Version", "all")
    # build.archive("add_assets", "all")

    ## Classify files as None to exclude them from the built distributions.


    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.txt', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('scripts/', None)
    build.classify('**/saves/**', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/audio/bgm/**.ogg', 'bgm')
    build.classify('game/audio/sfx/**.ogg', 'sfx')
    build.classify('game/audio/voice/**.ogg', 'voice')
    build.classify('game/images/bg/**', 'bg')
    build.classify('game/images/chara/**', 'chara')
    build.classify('game/images/minigame/**', 'minigame')
    build.classify('game/images/texts/**', 'texts')
    build.classify('game/fancytext**', 'texts')
    build.classify('game/gui**', 'GUI')
    build.classify('game/movies/**', 'Movies')
    build.classify('game/tl/**', 'TL')
    build.classify('game/custom_screens**', 'Screens')
    build.classify('game/screens**', 'Screens')
    build.classify('game/init**', 'Init')
    build.classify('game/options**', 'Options')
    build.classify('game/version**', 'Version')
    build.classify('game/scripts/**', 'Scripts')
    build.classify('game/utilities**', 'Scripts')
    build.classify('game/script**', 'Scripts')
    # build.classify('game/add_assets/**', 'add_assets')


    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

init -2:
    # ---------- CTC blinking arrow -------------------
    image ctc_blink:
        xpos 1020
        ypos 763 # This actually doesn't matter, but it doesn't work right without it. Go figure...?
        alpha 1.0 # visible
        "gui/ctc/ctc1.png"
        0.5
        "gui/ctc/ctc2.png"
        0.5
        "gui/ctc/ctc3.png"
        0.5
        repeat
