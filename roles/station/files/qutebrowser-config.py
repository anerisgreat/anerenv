# Basing this heavily on ii.com qutebrowser template

config.load_autoconfig(False)

#Using a lot from DTs config https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/qutebrowser/config.py
#Also using this https://github.com/miseran/tabs_are_windows/blob/main/config.py

c.tabs.show = 'never'
c.tabs.tabs_are_windows = True
c.window.title_format = 'qute: {private}{perc}{current_title}'

#Search engines from DT
c.url.searchengines = {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'am': 'https://www.amazon.com/s?k={}', #Amazon
    'aw': 'https://wiki.archlinux.org/?search={}', #Arch Wiki
    'go': 'https://www.google.com/search?q={}', #Google
    're': 'https://www.reddit.com/r/{}', 'wi': #Reddit
    'https://en.wikipedia.org/wiki/{}', #Wikipedia
    'yt': 'https://www.youtube.com/results?search_query={}', #Youtube
    'gh': 'https://github.com/search?q={}' #Qutebrowser
}

#Youtube stuff from DT. Added media-title to MPV and youtube-dl with exwm process so can track progress.
config.bind('M', 'hint links spawn mpv --title=\'${media-title}\' {hint-url}')
config.bind('Z', 'hint links spawn emacsclient -e "(start-process \\"youtube-dl {hint-url}\\" \\"youtube-dl {hint-url}\\" \\"youtube-dl\\" \\"-o\\" \\"~/Downloads/%(title)s.%(ext)s\\" \\"{hint-url}\\")"')

config.bind('xb', 'config-cycle statusbar.show always in-mode')
c.statusbar.show = 'in-mode'
