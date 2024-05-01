################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset 10

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            if who in ["Hachiman", "Taishi", "Tobe", "Hayato", "Totsuka"]:
                window:
                    id "namebox"
                    style "namebox_blue"
                    text who id "who" xalign 0.5

            elif who in ["Komachi", "Magomachi", "Saki", "Yukino", "Yui", "Iroha", "Keika", "Hiratsuka", "Girl A", "Girl B", "Girl C", "Yumiko", "Ebina", "Kaori", "Meguri", "Haruno"]:
                window:
                    id "namebox"
                    style "namebox_pink"
                    text who id "who" xalign 0.5

            #else:
            #    window:
            #        id "namebox"
            #        style "namebox_grey"
            #        text who id "who" xalign 0.5

        # Might want to clean fancytext up and strip it down
        # The only effect we're going to use is slow_fade
        fancytext what id "what" slow_effect slow_fade slow_effect_delay 0.1

    fixed:
        imagebutton auto "gui/icons/play_%s.png":
            focus_mask "gui/icons/play_idle.png"
            yoffset 835
            xoffset 1775
            selected_idle "gui/icons/circle_idle.png"
            selected_hover "gui/icons/circle_hover.png"
            activate_sound gui.sound_confirm
            hover_sound gui.hover_sound
            action Preference("auto-forward", "toggle")

        if Skip().get_sensitive():
            imagebutton auto "gui/icons/skip_%s.png":
                focus_mask "gui/icons/skip_idle.png"
                yoffset 950
                xoffset 1775
                selected_idle "gui/icons/pause_idle.png"
                selected_hover "gui/icons/pause_hover.png"
                activate_sound gui.sound_confirm
                hover_sound gui.hover_sound
                action Skip()


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox_blue:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Fixed("gui/namebox_blue.png")
    padding gui.namebox_borders.padding

style namebox_pink:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Fixed("gui/namebox_pink.png")
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    hover_sound gui.hover_sound
    activate_sound gui.sound_start
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

# screen quick_menu():

#     ## Ensure this appears on top of other screens.
#     zorder 100

#     if quick_menu:

#         hbox:
#             style_prefix "quick"

#             xalign 0.5
#             yalign 1.0

#             textbutton _("Back") action Rollback()
#             textbutton _("History") action ShowMenu('history')
#             textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
#             textbutton _("Auto") action Preference("auto-forward", "toggle")
#             textbutton _("Save") action ShowMenu('save')
#             textbutton _("Q.Save") action QuickSave()
#             textbutton _("Q.Load") action QuickLoad()
#             textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
#     config.overlay_screens.append("quick_menu")

# default quick_menu = False

# style quick_button is default
# style quick_button_text is button_text

# style quick_button:
#     properties gui.button_properties("quick_button")

# style quick_button_text:
#     properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen add_button_main(i, name, act):
    fixed:
        ypos i * (gui.main_navigation_spacing + 96) - 300
        xpos 20

        $ click = gui.hover_sound
        $ confirm = gui.sound_confirm

        if name == "Start":
            $ confirm = gui.sound_start
        imagebutton auto "gui/button/menu_%s.png" xpos 0 ypos 0:
            focus_mask "gui/button/menu_idle.png"
            activate_sound confirm
            hover_sound click
            action act
        text name:
            xpos 250 ypos 55
            xalign 0.5 yalign 0.5
            size 60
            color "#000000" #!# Ideally figure out how to get a hover-color for this
screen add_button(name, act):

    style_prefix "main"

    textbutton name:
        xsize 295
        ysize 72

        background Frame("gui/button/button_idle.png")
        hover_background Frame("gui/button/button_hover.png")
        selected_background Frame("gui/button/button_hover.png")

        activate_sound gui.sound_confirm
        hover_sound gui.hover_sound

        action act

screen add_button_spec(name, act, xDim, yDim, xOff, yOff, URL = ["gui/button/button_idle.png","gui/button/button_hover.png","gui/button/button_hover.png"]):
    style_prefix "main"
    textbutton name:
        xsize xDim
        ysize yDim

        xoffset xOff
        yoffset yOff

        background Frame(URL[0])
        hover_background Frame(URL[1])
        selected_background Frame(URL[2])

        activate_sound gui.sound_confirm
        hover_sound gui.hover_sound

        action act

style main_button is button:
    ypadding 0

style main_button_text is button_text:
    yalign 0.6
    xoffset 21
    xalign 0.5
    yfill False

screen add_sub_button(name, clr, act):

    style_prefix "sub"

    textbutton name:
        xsize 150
        ysize 100

        #background Frame("gui/button/sub/" + clr + "_idle.png")
        #hover_background Frame("gui/button/sub/" + clr + "_hover.png")
        #selected_background Frame("gui/button/sub/" + clr + "_selected.png")

        activate_sound gui.sound_confirm

        action act

style sub_button is button:
    ypadding 0

style sub_button_text is button_text:
    yalign 0.25
    xalign 0.5
    yfill False

screen navigation():

    # The vbox object didn't really want to work with me
    # So i needed to give each button an index and calculate manually

    if main_menu:
        fixed:
            xpos gui.main_navigation_xpos
            ypos gui.main_navigation_ypos

            use add_button_main(0, _("New Game"), Start())
            use add_button_main(1, _("Continue"), ShowMenu("load"))
            use add_button_main(2, _("Memories"), ShowMenu("memories"))
            use add_button_main(3, _("Options"), ShowMenu("preferences"))

            if renpy.variant("pc"):
                use add_button_main(4, _("Quit"), Quit(confirm=not main_menu))

    else:
        vbox:
            xpos gui.navigation_xpos
            ypos gui.navigation_ypos

            use add_button(_("History"), ShowMenu("history"))
            use add_button(_("Save"), ShowMenu("save"))
            use add_button(_("Load"), ShowMenu("load"))
            use add_button(_("Settings"), ShowMenu("preferences"))

            if _in_replay:
                use add_button(_("End Replay"), EndReplay(confirm=True))


transform text_rotate(ang):
    rotate ang

transform text_rotate_center(ang):
    around (0.5, 0.5)
    rotate ang

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


screen prompt_update():
    fixed:
        add gui.game_menu_background
        text "{color=#000}Something went wrong when you upgraded to [persistent.version]! Try updating again!" xalign 0.5 yalign 0.5

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background


    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    if str(persistent.version) != str(config.version):
        use prompt_update
    else:
        ## This empty frame darkens the main menu.
        frame:
            pass
        use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add "gui/overlay/background_transparent.png"

    if not main_menu:
        fixed:
            add "gui/overlay/label.png":
                xpos -92
                ypos -92

            text _("Paused") at text_rotate_center(-7) ypos 16 xpos 16

    text title xpos 532 yalign 0.18:
        color "#bfd970"
        outlines [ (3, "#6d7070", 0, 0) ]

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

        if not main_menu:
            use navigation

        vbox:
            xpos gui.navigation_xpos
            yalign 1.0
            yoffset -45

            if main_menu:
                use add_button(_("Return"), Return())
            else:
                use add_button(_("Continue"), Return())

            if not main_menu:
                use add_button(_("Main Menu"), MainMenu())

                if renpy.variant("pc"):
                    use add_button(_("Quit"), Quit(confirm=not main_menu))

        if title in ["Options", "Help", "About"]:
            hbox:
                xalign 1.0
                xoffset -150
                yoffset 8
                spacing 25

                use add_sub_button(_("Options"), "blue", ShowMenu("preferences"))
                use add_sub_button(_("Help"), "orange", ShowMenu("help"))
                use add_sub_button(_("About"), "green", ShowMenu("about"))

        if main_menu:
            key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 220
    right_margin 200
    top_margin 74
    bottom_margin 20

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

screen ctc(arg=None):

    zorder 100

    add "ctc_blink" xalign 0.92 yalign 0.97

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            yoffset 52
            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style about_text:
    yoffset 14
    line_spacing 14
    color gui.insensitive_color


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

#!#
screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        activate_sound gui.sound_confirm
                        hover_sound gui.hover_sound

                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        null height 5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing
                yoffset -10

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
style options_button_text:
    color "#000000"
    selected_color "#00c4f4"
    hover_color "#00c4f4"

screen preferences():

    tag menu

    use game_menu(_("preferences"), scroll=None):
        add gui.game_menu_options at top:
            xoffset 868
            yoffset -254

        #option gui boxes | display
        if renpy.variant("pc") or renpy.variant("web"):
            add "gui/option_active_top.png" xoffset -551 yoffset -87
            add "gui/option_active_middle.png" xoffset -551 yoffset -67
            add "gui/option_active_middle.png" xoffset -551 yoffset -47
            add "gui/option_active_middle.png" xoffset -551 yoffset -27
            add "gui/option_active_bottom.png" xoffset -551 yoffset -7
        #Rollback
        add "gui/option_active_top.png" xoffset -551 yoffset 33
        add "gui/option_active_middle.png" xoffset -551 yoffset 53
        add "gui/option_active_middle.png" xoffset -551 yoffset 73
        add "gui/option_active_middle.png" xoffset -551 yoffset 93
        add "gui/option_active_bottom.png" xoffset -551 yoffset 113
        #Skip
        add "gui/option_active_top.png" xoffset -551 yoffset 153
        add "gui/option_active_middle.png" xoffset -551 yoffset 173
        add "gui/option_active_middle.png" xoffset -551 yoffset 193
        add "gui/option_active_middle.png" xoffset -551 yoffset 213
        add "gui/option_active_bottom.png" xoffset -551 yoffset 233
        #text speed | auto-forward time
        add "gui/option_active.png" xoffset -551 yoffset 273
        add "gui/option_active.png" xoffset -551 yoffset 333
        add "gui/option_active_middle.png" xoffset -551 yoffset 333
        #volumes
        add "gui/option_active.png" xoffset -551 yoffset 453
        add "gui/option_active.png" xoffset -551 yoffset 512
        add "gui/option_active_middle.png" xoffset -551 yoffset 503

        hbox:
            xpos -455
            ypos -72
            vbox:
                spacing 10.5
                if renpy.variant("pc") or renpy.variant("web"):
                    label _("Display") text_color "#000000" text_size 60

                label _("Rollback Side") text_color "#000000" yoffset 46 text_size 60
                label ""
                label _("Skip") text_color "#000000" yoffset 37 text_size 60

                label ""
                label ""

                label _("Text Speed") text_color "#000000" yoffset -6
                label _("Auto-Forward Time") text_color "#000000"

                label ""

                if config.has_music:
                    label _("Music Volume") text_color "#000000"
                if config.has_sound:
                    label _("Sound Volume") text_color "#000000"
                if config.has_sound:
                    label _("Voice Volume") text_color "#000000"

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            vbox:
                xoffset 250
                spacing 10.5

                vbox:
                    yoffset -4
                    spacing 2

                    style_prefix "check"

                    if renpy.variant("pc") or renpy.variant("web"):
                        hbox:
                            textbutton _("Window") action Preference("display", "window") text_size 60 text_style "options_button_text"
                            textbutton _("Fullscreen") action Preference("display", "fullscreen") text_size 60 text_style "options_button_text"

                    hbox:
                        textbutton _("Disable") action Preference("rollback side", "disable") text_size 60 yoffset 40 text_style "options_button_text"
                        textbutton _("Left") action Preference("rollback side", "left") text_size 60 yoffset 40 text_style "options_button_text"
                        textbutton _("Right") action Preference("rollback side", "right") text_size 60 yoffset 40 text_style "options_button_text"

                    hbox:
                        textbutton _("Unseen") action Preference("skip", "toggle") text_size 60 yoffset 80 text_style "options_button_text"
                        textbutton _("Choices") action Preference("after choices", "toggle") text_size 60 yoffset 80 text_style "options_button_text"
                        textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")) text_size 60 yoffset 80 text_style "options_button_text"

                vbox:
                    spacing 10.5

                    style_prefix "slider"

                    vbox:

                        vbox:
                            yoffset 137
                            spacing 31

                            bar value Preference("text speed")
                            bar value Preference("auto-forward time")

                        vbox:
                            yoffset 214
                            spacing 26

                            if config.has_music:
                                bar value Preference("music volume")

                            hbox:
                                if config.has_music or config.has_sound or config.has_voice:
                                    textbutton _("Mute All"):
                                        xoffset -250
                                        yoffset -11
                                        action Preference("all mute", "toggle")
                                        text_style "options_button_text"
                                if config.has_sound:
                                    bar value Preference("sound volume") xoffset -162 yoffset 1
                            if config.has_voice:
                                bar value Preference("voice volume") yoffset -23



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    # properties gui.button_properties("radio_button")
    # foreground "gui/button/radio_[prefix_]foreground.png"
    activate_sound gui.sound_confirm
    hover_sound gui.hover_sound

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_hbox:
    spacing gui.pref_button_spacing

style check_button:
    # properties gui.button_properties("check_button")
    # foreground "gui/button/check_[prefix_]foreground.png"
    activate_sound gui.sound_confirm
    hover_sound gui.hover_sound

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    hover_sound gui.hover_sound
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15
    hover_sound gui.hover_sound

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.

                        # if "color" in h.who_args:
                        #    text_color h.who_args["color"]

                        if h.who in ["Hachiman", "Taishi", "Tobe",
                            "Hayato", "Student Council Vice President",
                            "Male Staff", "Totsuka", "Announcer", "PE Teacher (Male)"]:
                            text_color "#2cb5fc"
                        elif h.who in ["Komachi", "Magomachi", "Saki",
                            "Hostess", "Yukino", "Yui",
                            "Iroha", "Keika", "Hiratsuka",
                            "Girl", "Girl A", "Girl B", "Girl C",
                            "Yumiko", "Ebina", "Kaori",
                            "Meguri", "Haruno", "Female Staff"]:
                            text_color "#dd5481"
                        else:
                            text_color "#999999"

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    color "#000000"
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

style help_text:
    color gui.insensitive_color


################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color gui.text_color
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    yoffset -2
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus. | #!# DO we want an NVL mode?
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants | #!# Maybe cut these? Not sure if we want to natively support mobile
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"

style game_menu_outer_frame:
    variant "small"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
