CSS True Format for Sublime Text
================================


Description
-----------

CSS True Format is an opinionated Sublime Text packge that formats CSS/SASS/SCSS/LESS code
using The One True Format&#8482;.
CSS True Format is only a formatter and does not support grammar checks.

**Example:**

* Original format:
    body {Background:#FF0000 url("../img/homepage/noize.png");}


    .languages {position: absolute; right: 0%; top: 0px; width:20rem;}
    .languages span,.languages a {line-height:2rem;}
    .languages span +em {position:absolute; Padding:0.5rem 0rem; right:0; Color:#4FC270;}
    .languages ul {display:none; margin:0; padding:0px 5px 0; z-index:1;}

    .languages:hover span { display:none }
    .languages:hover ul {display: block; width:20rem}
    .languages li {float:right; list-style:none}
    .languages a {padding:1rem; display: block }
    .languages a:hover {color:#54cc76}




    header .pure-menu {padding:.7rem 2rem 1.4rem;}
    header .pure-menu-open {background-color:transparent;}
    header .stuck>.pure-menu {max-width:1056px; padding:.25rem 0 1rem;}
    header .nav-wrapper {box-shadow:2px 2px 4px rgba(0, 0, 0, 0.08); margin-bottom:1.5rem;}
    header .nav-wrapper.stuck {background-color:rgba(245, 245, 245, 0.92);box-shadow:2px 2px 4px rgba(0, 0, 0, 0.15);left:0;position:fixed;right:0;top:0; z-index:2;}


* True format:
    body {background:#ff0000 url('../img/homepage/noize.png');}


    .languages {position:absolute; right:0; top:0; width:20rem;}
    .languages span,
    .languages a {line-height:2rem;}
    .languages span + em {color:#4fc270; padding:.5rem 0; position:absolute; right:0;}
    .languages ul {display:none; margin:0; padding:0 5px 0; z-index:1;}

    .languages:hover span {display:none;}
    .languages:hover ul {display:block; width:20rem;}
    .languages li {float:right; list-style:none;}
    .languages a {display:block; padding:1rem;}
    .languages a:hover {color:#54cc76;}


    header .pure-menu {padding:.7rem 2rem 1.4rem;}
    header .pure-menu-open {background-color:transparent;}
    header .stuck > .pure-menu {max-width:1056px; padding:.25rem 0 1rem;}
    header .nav-wrapper {box-shadow:2px 2px 4px rgba(0, 0, 0, 0.08); margin-bottom:1.5rem;}
    header .nav-wrapper.stuck {
        background-color:rgba(245, 245, 245, 0.92);
        box-shadow:2px 2px 4px rgba(0, 0, 0, 0.15);
        left:0;
        position:fixed;
        right:0;
        top:0;
        z-index:2;
    }


Installation
------------

**OPTION 1 - with Package Control (recommended)**

The easiest way to install this package is through Package Control.

1. Install [Package Control](https://sublime.wbond.net/installation), follow instructions on the website.

2. Open command panel: `Ctrl+Shift+P` (Linux/Windows) or `Cmd+Shift+P` (OS X) and select **Package Control: Install Package**.

3. When packages list appears, type `CSSTrueFormat` and select it.


**OPTION 2 - with Git**

Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/drdla/CSS-True-Format.git "CSS True Format"

On OS X you can find your packages inside directory
    ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/


Usage
-----

Select the code, or place cursor in the document, and execute commands in one of the following ways:

* Context Menu: **CSS True Format**.

* Command Panel: Open command panel: `Ctrl+Shift+P` (Linux/Windows) or `Cmd+Shift+P` (OS X) and select **Format CSS**.


Shortcuts
---------

By default CSS True Format provides no keyboard shortcuts to avoid conflicts, but you can view the included `Example.sublime-keymaps` file to get an idea how to set up your own.


Author
------

Created by Dominik Rodler.


Testing
-------

Run::

    python runtests.py

Acknowledgements
----------------

Thanks to **Mutian** ([http://mutian.info](http://mutian.info/)) and the **RIA Team** of [Weibo.com](http://weibo.com/) .
