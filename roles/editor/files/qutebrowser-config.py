# Basing this heavily on ii.com qutebrowser template

#Using a lot from DTs config https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/qutebrowser/config.py

c.tabs.show = 'multiple'

config.load_autoconfig(False)

config.bind('<Shift-o>', 'set-cmd-text -s :open -w ')

#Search engines from DT
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'am': 'https://www.amazon.com/s?k={}', 'aw': 'https://wiki.archlinux.org/?search={}', 'go': 'https://www.google.com/search?q={}', 're': 'https://www.reddit.com/r/{}', 'wi': 'https://en.wikipedia.org/wiki/{}', 'yt': 'https://www.youtube.com/results?search_query={}'}

#Youtube stuff from DT
config.bind('M', 'hint links spawn mpv --title=\'${media-title}\' {hint-url}')
config.bind('Z', 'hint links spawn emacsclient -e "(start-process \\"youtube-dl {hint-url}\\" \\"youtube-dl {hint-url}\\" \\"youtube-dl\\" \\"{hint-url}\\")"')
