life-hack
=========

Gist for pre-commit

Git hook to catch pyflakes and pep8 issues before committing.
How it works?
copy file to '/usr/share/git-core/templates/hooks/' then,
it will automatically copy to .git/hooks whenever new repository is cloned.
Before committing changes this file will get all staged python files
and run pyflakes, pep8 on each file and exit commit process if there is any
violation.

Note: To skip this hook use git commit -m "########" --no-verify
