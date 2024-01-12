from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=0)

def separatorl(fg="light", bg="dark"):
    return widget.Sep(**base(fg, bg), linewidth=0, padding=15)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3,
        margin=0,
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text=" ", # Icon: nf-oct-triangle_left
        fontsize=120,
        padding=-45,
    )


def powerlineright(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=130,
        padding=0
    )

def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light',bg='color2'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
         powerlineright('color2', 'dark'),
        separator(),
        widget.WindowName(**base(fg='color7'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color5', 'dark'),

    widget.CPU(**base(bg='color5'),format='  {load_percent}%'),

    widget.DF(
        **base(bg='color5'),
        visible_on_warn=False,
        format=' |   {uf}{m}'),

    widget.Memory(
        **base(bg='color5'),
        format=' |  {MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}'),

    separatorl('color4', 'color5'),

    powerline('color4', 'color5'),

    icon(bg="color4", text='󰀂 '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='enp0s3'),


    separatorl('color3', 'color4'),

    powerline('color3', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color3'),custom_icon_paths=["/home/fx/.config/qtile/layout-icons/gruvbox-dark0/"], scale=0.45),

    widget.CurrentLayout(**base(bg='color3'), padding=5),


    separatorl('color2', 'color3'),

    powerline('color7', 'color3'),

    icon(bg="color7", fontsize=17, text='󰃰 '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color7'), format='%d/%m/%Y - %H:%M '),

    
    separatorl('color1', 'color7'),

    powerline('color1', 'color7'),

    icon(bg="color1", text=' '),
    
    # widget.Volume(**base(bg='color1')),

    widget.PulseVolume(
        **base(bg='color1'),
        check_mute_string=['on'],
        ),

    separatorl('color6', 'color1'),

    powerline('color6', 'color1'),


    widget.Systray(background=colors['color6'], padding=10),


    # separatorl('color6', 'color6'),


    # icon(fg="light",bg="color6", text='  '), # Icon: nf-fa-download
    
    # widget.CheckUpdates(
    #     **base(bg='color6'),
    #     colour_have_updates=colors['light'],
    #     colour_no_updates=colors['light'],
    #     no_update_string='0',
    #     display_format='{updates}',
    #     update_interval=1800,
    #     custom_command='checkupdates',
    #     distro='Ubuntu'
    # ),

    separatorl('color6', 'color6'),



]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),

    # widget.Clock(**base(bg='color1')),

]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
