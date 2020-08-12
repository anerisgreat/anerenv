(setq vc-follow-symlinks t)
(setq custom-file (expand-file-name "custom.el" user-emacs-directory))
(require 'org)
(org-babel-load-file (expand-file-name "config.org" user-emacs-directory))
