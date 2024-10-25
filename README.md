# Git Resources

* [Stackoverflow - git terminology](http://stackoverflow.com/a/7076569/406)
* [Git in six hundred words by: Mary Rose Cook](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
* [A Hacker's guide to git](http://wildlyinaccurate.com/a-hackers-guide-to-git)
* [Think Like (a) Git](http://think-like-a-git.net/)
* [The simple git guide](https://rogerdudler.github.io/git-guide/)
* [Git Essentials - a webinar by Atlassian](https://www.youtube.com/watch?v=wcbzd84eWnk)
* http://think-like-a-git.net/sections/about-this-site.html
* [Git and Github Resources](http://haacked.com/archive/2014/12/03/git-and-github-resources/)
* [Aha! Moments When Learning Git](http://betterexplained.com/articles/aha-moments-when-learning-git/?utm_source=feedburner&utm_medium=twitter&utm_campaign=Feed%3A+hackernewsyc+%28Hacker+News+YC%29)
* [Visual Git Reference](https://marklodato.github.io/visual-git-guide/index-en.html)
* [Git from the inside out](https://codewords.recurse.com/issues/two/git-from-the-inside-out)
* [Explain Git with D3](http://www.wei-wang.com/ExplainGitWithD3)
* [The Git Parable](http://tom.preston-werner.com/2009/05/19/the-git-parable.html)

## Style Guide

* https://github.com/agis-/git-style-guide

## Commit Guidelines

* [conventional commits](https://www.conventionalcommits.org) - A specification for adding human and machine readable meaning to commit messages.
* [AngularJS project - commit guidelines](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#-git-commit-guidelines)

## Books

* [Pro Git (free)](http://git-scm.com/book/en/v2)
* [git internals PDF](https://github.com/pluralsight/git-internals-pdf)


## Videos / Talks

* [Git For Ages 4 And Up](https://www.youtube.com/watch?v=1ffBJ4sVUb4)
* [Daily Tech Git Videos](http://dailytechvideo.com/category/git/)

## Podcasts

* [gitminutes](http://episodes.gitminutes.com/)

## Cheat Sheets
* [git-tips](https://github.com/git-tips/tips)
* [Git Tower's Cheat Sheet](http://www.git-tower.com/blog/git-cheat-sheet/)
* [ndpsoftware's cheat sheet](http://ndpsoftware.com/git-cheatsheet.html)
* [tiimgreen's cheat sheet](https://github.com/tiimgreen/github-cheat-sheet)
  * [github cheatsheet](https://github.com/tiimgreen/github-cheat-sheet#github)
  * [git cheatsheet](https://github.com/tiimgreen/github-cheat-sheet#git)
* [github's education cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [another git cheat sheet](http://ktown.kde.org/~zrusin/git/git-cheat-sheet-medium.png)

# Setup / Configuration

## Aliases

- Commit Counts - `git config --global alias.count 'rev-list --count HEAD'`

# Git Tools

## GUIs

* [git fork](https://git-fork.com) - this is the gui I use and highly recommend.

### Others

* [Source Tree](http://www.sourcetreeapp.com/) - Windows / macOS
* [Git Extensions](http://sourceforge.net/projects/gitextensions/) - Windows / macOS / Linux
* [tortoisegit](https://code.google.com/p/tortoisegit/) - Windows
* [Git Tower](http://www.git-tower.com/) - macOS only
* [GitX](http://gitx.frim.nl/) - macOS only
* [SmartGit](http://www.syntevo.com/smartgit/) - macOS, Windows and Linux
* [Github for Windows](https://windows.github.com/)
* [Github for Mac](https://mac.github.com/)
* [gitup](http://gitup.co/) - Interesting live view, may help while learning git

## addons

* https://github.com/stevemao/awesome-git-addons
*

## .gitignore

* Creating .gitignore files
  * https://www.gitignore.io/ - create .gitignore files for different languages, IDEs, etc.

## Handling Large Files

### Remove Large Files

* https://rtyley.github.io/bfg-repo-cleaner/

### git-lfs

* [Git Large File Storage Website](https://git-lfs.github.com/)
* [git-lfs repo](https://github.com/github/git-lfs?utm_source=gitlfs_site&utm_medium=repo_link&utm_campaign=gitlfs)
* [Hacker News Discussion](https://news.ycombinator.com/item?id=9343021)


### git-bigstore

* https://github.com/lionheart/git-bigstore

### git-media

* https://github.com/alebedev/git-media

### git-annex

* https://git-annex.branchable.com/

# Git Processes / Workflows

## git flow
  * [A successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
  * [How to use a scalable Git branching model called Gitflow](http://buildamodule.com/video/change-management-and-version-control-deploying-releases-features-and-fixes-with-git-how-to-use-a-scalable-git-branching-model-called-gitflow)
  * [gitflow cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)
  * [Atlassian's gitflow tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

# Git Links / Tips / Snippets

* http://thelinell.com/2014/12/23/curated-git-links-of-2014/
*

# dvcs

Distributed Version Control - articles, links, general

* [Distributed Version Control is here to stay](https://www.joelonsoftware.com/2010/03/17/distributed-version-control-is-here-to-stay-baby/)

# Git Migration

* Migrate from SVN
  * Atlassian's Guide: https://www.atlassian.com/git/tutorials/migrating-overview
  * Remove Large Files
    * https://rtyley.github.io/bfg-repo-cleaner/
    *

# Git Repository Hosting Solutions


## Cloud Based



### Github

* https://github.com/

### Bitbucket

* https://bitbucket.org


### Gitlab

* [https://about.gitlab.com/gitlab-com/](https://about.gitlab.com/gitlab-com/)


# Git Merging

![](https://docs.google.com/drawings/d/1MNxHD5UG1JpilalijGZ2nJHEZ4Wzi_imTtMH-m-mViA/pub?w=960&amp;h=720)

# Empty Directories

Git will not track empty directories, there must be a file in the directory for Git to track it.

* [.gitkeep file](https://stackoverflow.com/a/7229996/406) - common pattern to save a directory
* See: https://git.wiki.kernel.org/index.php/Git_FAQ#Can_I_add_empty_directories.3F
