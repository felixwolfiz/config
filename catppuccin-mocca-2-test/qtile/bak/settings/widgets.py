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
        text="", # Icon: nf-oct-triangle_left
        fontsize=130,
        padding=10,
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
        widget.WindowName(**base(fg='color5'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color5', 'dark'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color5'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color4', 'color5'),

    icon(bg="color4", text='󰲐 '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='enp0s3'),


    powerline('color3', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color2', 'color3'),

    icon(bg="color2", fontsize=17, text='󰃰 '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    
    powerline('color1', 'color2'),

    icon(bg="color1", text=' '),
    
    widget.Volume(**base(bg='color1')),

    powerline('color6', 'color1'),

    widget.Systray(background=colors['color6'], padding=2),

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
