(TeX-add-style-hook
 "template_poster"
 (lambda ()
   (setq TeX-command-extra-options
         "-shell-escape")
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("tikzposter" "25pt" "a0paper" "portrait")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T1") ("cite" "compress") ("contour" "outline") ("hyperref" "hidelinks")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "tikzposter"
    "tikzposter10"
    "fontenc"
    "sfmath"
    "amsmath"
    "lipsum"
    "cite"
    "circuitikz"
    "svg"
    "contour"
    "xcolor"
    "hyperref")
   (TeX-add-symbols
    '("C" ["argument"] 1)
    '("section" 2)
    '("thebibliography" 1)
    "CORE"
    "PLANCK"
    "prd"
    "prr"
    "mnras"
    "jcap"
    "jmap"
    "joss"
    "pasa"
    "aap"
    "prl"
    "arxiv"
    "oldbibliography")
   (LaTeX-add-labels
    "eq:noise_g")
   (LaTeX-add-bibliographies)
   (LaTeX-add-xcolor-definecolors
    "myred"
    "myblue"
    "mygreen"
    "mydarkblue"
    "lightgray"
    "varcolor"
    "myorange"
    "C0"
    "C1"
    "C2"
    "C3"
    "C4"
    "C5"
    "C6"
    "C7"
    "C8"
    "C9"
    "backgroundcolor"
    "framecolor"
    "titlefgcolor"
    "titlebgcolor"
    "blocktitlebgcolor"
    "blocktitlefgcolor"
    "blockbodybgcolor"
    "blockbodyfgcolor"
    "innerblocktitlebgcolor"
    "innerblocktitlefgcolor"
    "innerblockbodybgcolor"
    "notefgcolor"
    "notebgcolor"
    "notefrcolor"))
 :latex)

