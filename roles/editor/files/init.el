(setq vc-follow-symlinks t)
(setq custom-file (expand-file-name "custom.el" user-emacs-directory))
(load custom-file)
(require 'org)
; Taken out of definition for org-babel-load-file, want to force.
(setq conf-file (expand-file-name "config.org" user-emacs-directory))
(let* ((conf-file (expand-file-name "config.org" user-emacs-directory))
       (tangled-conf-file (concat (file-name-sans-extension conf-file) ".el")))
  (org-babel-tangle-file conf-file tangled-conf-file "emacs-lisp")
  (load-file tangled-conf-file))

