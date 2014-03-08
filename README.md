CSS True Format for Sublime Text
================================


Description
-----------

CSS True Format is an opinionated Sublime Text packge that formats CSS/SASS/SCSS/LESS code
using The One True Format&#8482;.
CSS True Format is only a formatter and does not support grammar checks.

**Example:**

* Expanded format:

    body {
        background-color: #fff;
        color: #333;
        font-size: 12px;
    }
    a {
        color: #06f;
    }
    a:hover {
        color: #09c;
    }

* True format:

        body { background-color: #fff; color: #333; font-size: 12px; }
        a { color: #06f; }
        a:hover { color: #09c; }


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
    ~/Library/Application Support/Sublime Text 3/Packages/


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


Acknowledgements
----------------

Thanks to **Mutian** ([http://mutian.info](http://mutian.info/)) and the **RIA Team** of [Weibo.com](http://weibo.com/) .
