# Basing this heavily on ii.com qutebrowser template

config.load_autoconfig(True)

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
    'gh': 'https://github.com/search?q={}', #Qutebrowser
    'wa' : 'https://www.wolframalpha.com/input/?i={}' #Wolfram alpha
}

#Youtube stuff from DT. Added media-title to MPV and youtube-dl with exwm process so can track progress.
config.bind('M', 'hint links spawn mpv --title=\'${media-title}\' {hint-url}')
config.bind('Z', 'hint links spawn emacsclient -e "(start-process \\"youtube-dl {hint-url}\\" \\"youtube-dl {hint-url}\\" \\"youtube-dl\\" \\"-o\\" \\"~/downloads/%(title)s.%(ext)s\\" \\"{hint-url}\\")"')

config.bind('xb', 'config-cycle statusbar.show always in-mode')
c.statusbar.show = 'in-mode'

#Only confirm if downloads
c.confirm_quit = ['downloads']

c.downloads.location.directory = '~/downloads'
c.downloads.location.prompt = False

c.editor.command = ['emacsclient', '-e', '(find-file "{}")']

monospace = "10pt 'LiberationMono'"
c.fonts.completion.category = f"bold{monospace}"
c.fonts.completion.entry = monospace
c.fonts.debug_console = monospace
c.fonts.downloads = monospace
c.fonts.keyhint = monospace
c.fonts.messages.error = monospace
c.fonts.messages.info = monospace
c.fonts.messages.warning = monospace
c.fonts.prompts = monospace
c.fonts.statusbar = monospace
c.fonts.hints = "bold 13px 'LiberationMono'"


