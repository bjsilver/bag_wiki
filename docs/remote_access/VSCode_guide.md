# Guide to VS Code
by Ben Bradley, 29/03/2025
(last updated 06/10/2025)

## 🏁 Introduction

_This document is intended as a guide to modern programming for researchers and students within the School of Earth and Environment, primarily using Python and VS Code._

Throughout, I draw upon the expertise shared in the following sources:
- [The BAG Wiki](https://bjsilver.github.io/bag_wiki/), particularly the [Guide to VS Code](https://bjsilver.github.io/bag_wiki/docs/remote_access/vscode.html)
- [The Good Research Code Handbook](https://goodresearch.dev/index.html)

### Contents
- ❓ What is VS Code and Python?
- 🏗️ How do I set this up?

### Python

Python is one of the most successful programming languages, and for a reason! It values *readability* above all else, making it very user-friendly.
It is open-source and primarily relies on importing libraries others have created to solve problems efficiently. This means you can lean on the
work of others, who have likely solved the problem far more efficiently and cleanly than you could!

Many people start using Python via the Python-provided Integrated Development Environment (IDE) or directly through the terminal. These are excellent
places to get to grips with Python when first learning the language, as they allow you to focus on the basic coding you'll encounter in tutorials.
Complications arise when you want to do more than the basics, though.

### Environment Managers

Python relies on libraries for most interesting things anyone might actually want to do. Perhaps you've found yourself in the following situation before?

- discover a cool thing you want to try out in Python
- find you need a specific library
- `import library` doesn't work!
- google the error message
- find that you need to install the library using a command called `pip`
- your computer doesn't recognise the command `pip`
- other people say to use `conda install` but this doesn't work either
- some random guy from StackOverflow says everything will work if you use `pip3`
- give up

You need a **package manager**! Setting this up means you can easily and dependably install any libraries you may need.

Once you start installing lots of libraries, you'll eventually find that some conflict with others. If you get unlucky,
you'll install a library and find that your code no longer runs! To avoid this, you need a **virtual environent manager**:
something that resolves package dependencies and installs libraries in virtual environments that can easily be deleted and
refreshed if something goes wrong.

Some popular examples of joint package and virtual environment managers are _Anaconda_, _Miniconda_, and _Miniforge_, which
we'll look at later. Without one of these, your Python environment can become a messy hellscape :(

### VS Code
But if you're doing lots of coding, you don't just want your code to *run*. Is it clear, efficient, well-documented, backed-up,
shareable? This is where more complete IDEs like VS Code come in!

Visual Studio Code (VS Code) offers many attractive features, such as:
- Multi-language support
- Variable auto-completion syntax highlighting
- Robust terminal interfaces **AND** intuitive feature-rich graphical interfaces
- Seamless version control with Git and GitHub
- Jupyter Notebooks!
- Easy ways to explore netcdfs, tables, plots, and files
- Installable extensions like auto-generated documentation, AI coding suggestions, and more!

Hopefully this convinces you that VS Code is worth the effort to set up and use for day-to-day coding tasks. We'll explore
_how_ to set this up in the following section.

(For more information, visit the [BAG wiki guide to VS Code](https://bjsilver.github.io/bag_wiki/docs/remote_access/vscode.html))


## ⚠️ IMPORTANT: A Note on VS Code Compatibility

At the moment, the university is transitioning their "general compute" resource for the faculty of environment from the old foe-linux
machines that run on CentOS to modern machines run with RedHat9. The old machines have outdated software, requiring a downgrade to
version 1.98 of VS Code to enable use. The new machines are, as of 06/10/2025, not fully configured and still have some problems.

New and existing users therefore have a choice of two paths, both of which are descibed in this guide:
1) Downgrade VS Code and make use of the more reliable old machines, with some potential hiccups from VS Code and its extensions to navigate
2) Install the latest version of VS Code and be prepared to report some problems as the system is set up (contact Steve Arnold for this).

It is currently recommended to choose option 1, but all researchers will eventually need to migrate to the new system.
