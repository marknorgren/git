# Git Resources

* [Stackoverflow - git terminology](http://stackoverflow.com/a/7076569/406)
* [Git in six hundred words by: Mary Rose Cook](http://maryrosecook.com/blog/post/git-in-six-hundred-words)
* [A Hacker's guide to git](http://wildlyinaccurate.com/a-hackers-guide-to-git)
* [Think Like (a) Git](http://think-like-a-git.net/)
* [The simple git guide](https://rogerdudler.github.io/git-guide/)
* [Git Essentials - a webinar by Atlassian](https://www.youtube.com/watch?v=wcbzd84eWnk)
* http://think-like-a-git.net/sections/about-this-site.html

* [Git and Github Resources](http://haacked.com/archive/2014/12/03/git-and-github-resources/)

# Books

* [Pro Git (free)](http://git-scm.com/book/en/v2)

# Podcasts

* [gitminutes](http://episodes.gitminutes.com/)

# Cheat Sheets
* [Git Tower's Cheat Sheet](http://www.git-tower.com/blog/git-cheat-sheet/)
* [ndpsoftware's cheat sheet](http://ndpsoftware.com/git-cheatsheet.html)
* [tiimgreen's cheat sheet](https://github.com/tiimgreen/github-cheat-sheet)
* [github's education cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [another git cheat sheet](http://ktown.kde.org/~zrusin/git/git-cheat-sheet-medium.png)


# Git Tools (GUIs)

* [Source Tree](http://www.sourcetreeapp.com/) - Windows / Mac OS X (this is what I use on a Mac OS X)
* [Git Extensions](http://sourceforge.net/projects/gitextensions/) - Windows / Mac OS X / Linux
* [tortoisegit](https://code.google.com/p/tortoisegit/) - Windows
* [Git Tower](http://www.git-tower.com/) - Mac OS X only
* [GitX](http://gitx.frim.nl/) - Mac OS X only 
* [SmartGit](http://www.syntevo.com/smartgit/) - Mac OS X, Windows and Linux
* [Github for Windows](https://windows.github.com/)
* [Github for Mac](https://mac.github.com/)


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

* [Distributed Version Control is here to stay](http://www.joelonsoftware.com/items/2010/03/17.html)

# Git Migration

* Migrate from SVN
  * Atlassian's Guide: https://www.atlassian.com/git/tutorials/migrating-overview

# Git Repository Hosting Solutions
==================================

Comparison of different Git repository management solutions


## Cloud Based

* Both Github and Bitbucket have a respository limit of about 1GB.
  * https://blog.bitbucket.org/2014/05/30/repository-size-limits/
  * https://help.github.com/articles/what-is-my-disk-quota/#rule-of-thumb-1gb-per-repository-100mb-per-file


### Github 

* https://github.com/
* Unlimited Collaborators
* Unlimited Public Repositories
* From [https://github.com/pricing](https://github.com/pricing)
* Security Info: https://help.github.com/articles/github-security
  * See: https://help.github.com/articles/github-security/#employee-access

Github offers Personal Plans and Organizational Plans. According to their website:

* **Personal Plans** - For individuals looking to share their own projects and collaborate with others.
* **Organizational Plans** -  Organizations are best suited for businesses managing teams and varying permissions.

| Github Personal Plans 	|||||||				
|:-----------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|**Cost** 			| Free	        | $7 / mo  		| $12 / mo 		| $22 / mo 		| $50 / mo 		| *Not Offered*	|
|**Users** 			| Unlimited		| Unlimited		| Unlimited		| Unlimited		| Unlimited		| Unlimited		| 
|**Private Repos** 	| 0 			| 5 			| 10 			| 20 			| 50 			| Unlimited		|



| Github Organization plans 	|||||||				
|:-----------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|**Cost** 			| Free	        | $25 / mo  	| $50 / mo 		| $100 / mo 	| $200 / mo 	| *Not Offered*	|
|**Users** 			| Unlimited		| Unlimited		| Unlimited		| Unlimited		| Unlimited		| Unlimited		| 
|**Private Repos** 	| 0 			| 10 			| 20 			| 50 			| 125 			| Unlimited		|



### Bitbucket 

* https://bitbucket.org
* Unlimited Private Repos
* From [https://bitbucket.org/plans](https://bitbucket.org/plans) 
* Security: https://confluence.atlassian.com/pages/viewpage.action?pageId=282175543

#### Repo Size Limits

* Soft Limit of 1GB, hard limit of 2GB
  * https://blog.bitbucket.org/2014/05/30/repository-size-limits/

| Bitbucket plans 	|||||||
|:-----------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|**Cost** 			| Free	        | $10 / mo  	| $25 / mo 		| $50 / mo 		| $100 / mo 	| $200 /mo		|
|**Users** 			| 5 			| 10			| 25			| 50			| 100			| Unlimited		| 
|**Private Repos** 	| Unlimited 	| Unlimited		| Unlimited 	| Unlimited		| Unlimited 	| Unlimited		|

### Gitlab 

* [https://about.gitlab.com/gitlab-com/](https://about.gitlab.com/gitlab-com/)


## Self hosted 

### Github Enterprise

* [https://enterprise.github.com/](https://enterprise.github.com/)

| Github Enterprise plans 	|||||||
|:-----------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|**Cost** 			| $5,000 / yr   | $10,000 / yr	| $15,000 / yr	| $20,000 / yr  | $25,000 / yr 	| $28,500 / yr	|
|**Users** 			| 20 			| 40			| 60			| 80			| 100			| 120   		| 
|**Private Repos** 	| Unlimited 	| Unlimited		| Unlimited 	| Unlimited		| Unlimited 	| Unlimited		|

### Atlassian's Stash

* [https://www.atlassian.com/software/stash](https://www.atlassian.com/software/stash)

| Atlassian Stash plans 	|||||||
|:-----------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|:-------------:|
|**Initial Cost**   | $10		    | $1,800		| $3,300     	| $6,000        | Coming Soon? 	| $16,000   	|
|**Maintenance**   | $10 / yr      | $900 / yr	    | $1,650 / yr	| $3,000 / yr   | Coming Soon? 	| $8,000 / yr	|
|**Users** 			| 10 			| 25			| 50			| 100    		| 250			| 500   		| 
|**Private Repos** 	| Unlimited 	| Unlimited		| Unlimited 	| Unlimited		| Unlimited 	| Unlimited		|

* Atlassian Stash plans come with 1 year software maintenance for free.
* [Atlassian Stash FAQs](https://www.atlassian.com/licensing/stash/)

### Gitlab

https://about.gitlab.com/


# Git Merging

![](https://docs.google.com/drawings/d/1MNxHD5UG1JpilalijGZ2nJHEZ4Wzi_imTtMH-m-mViA/pub?w=960&amp;h=720)
