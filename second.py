# THIS FILE CONTAINS NOTES FROM PYLADIES GIT WORKSHOP 1 (2016-03-15)

print ("This file contains notes from the PyLadies Git Workshop 1 from Wednesday, March 15th.")
print ("")

# checking the status 
git_status = "use git_status to check the status of the git directory "
git_log = "use 'git log' check the history of the repository " # hit 'q' to exit the log
git_diff = "use 'git diff' to get information about the differences from now and before the last commit"

# establish a repository
git_init = "'git init' establishes a new repository from a folder that exists on the computer"
git_clone = "'git clone' adds a repository from online that is not local "

# adding a file / edits that is on the local computer
git_add = "must 'git add' before committing to let git know you are ready to commit"
git_reset = "'git reset' will undo the add command (nevermind!)"
git_commit = "when doing a 'git commit' include -m and a description in quotes "
# "-a" is the same as adding "." and will commit all the files in the repository

# adding a file that is on the remote repository
git_pull = "use 'git pull' to add files from online that are in a reposity that is also local "

commands = [git_status,git_log,git_diff,git_init,git_clone,git_add,git_reset,git_commit,git_pull]

for c in commands:
	print (c)
	print ("")

# RESEARCH VIM 
# FOR QUESTIONS: georgia.reh@gmail	@georgiareh

# FOLLOWING TEXT IS THE COMMAND LINE ENTRIES 
"""Last login: Tue Mar 15 18:12:10 on ttys000
foa:~ Alexa$ cd gitpractice
foa:gitpractice Alexa$ hello.py
-bash: hello.py: command not found
foa:gitpractice Alexa$ git init
Reinitialized existing Git repository in /Users/Alexa/gitpractice/.git/
foa:gitpractice Alexa$ hello.py
-bash: hello.py: command not found
foa:gitpractice Alexa$ python hello.py
hello!
foa:gitpractice Alexa$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp
	hello.py

nothing added to commit but untracked files present (use "git add" to track)
foa:gitpractice Alexa$ git add hello.py
foa:gitpractice Alexa$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

foa:gitpractice Alexa$ git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

foa:gitpractice Alexa$ git commit -m "added a new file"
[master (root-commit) 789f89f] added a new file
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
foa:gitpractice Alexa$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

nothing added to commit but untracked files present (use "git add" to track)
foa:gitpractice Alexa$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp
	second.py

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ git commit -m "another file for practice"
On branch master
Changes not staged for commit:
	modified:   hello.py

Untracked files:
	.hello.py.swp
	second.py

no changes added to commit
foa:gitpractice Alexa$ git diff
diff --git a/hello.py b/hello.py
index 70cddf5..0dba7dd 100644
--- a/hello.py
+++ b/hello.py
@@ -1 +1 @@
-print "hello!"
\ No newline at end of file
+print ("goodbye!")
\ No newline at end of file
foa:gitpractice Alexa$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp
	second.py

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ git commit -m "another try"
On branch master
Changes not staged for commit:
	modified:   hello.py

Untracked files:
	.hello.py.swp
	second.py

no changes added to commit
foa:gitpractice Alexa$ git add second.py
foa:gitpractice Alexa$ git commit -m "a second file for git practice"
[master 38216d6] a second file for git practice
 1 file changed, 5 insertions(+)
 create mode 100644 second.py
foa:gitpractice Alexa$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ python second.py
this is another file for gitpractice
use this to check the status of the git directory
foa:gitpractice Alexa$ git diff
diff --git a/hello.py b/hello.py
index 70cddf5..0dba7dd 100644
--- a/hello.py
+++ b/hello.py
@@ -1 +1 @@
-print "hello!"
\ No newline at end of file
+print ("goodbye!")
\ No newline at end of file
foa:gitpractice Alexa$ git log
commit 38216d6cc8cd8885afe4982a78fe518755059434
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:28:15 2016 -0700

    a second file for git practice

commit 789f89fae291728ece240ed8edfe902d7a848813
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:21:36 2016 -0700

    added a new file
foa:gitpractice Alexa$ git diff 38216d6cc8cd8885afe4982a78fe518755059434
diff --git a/hello.py b/hello.py
index 70cddf5..0dba7dd 100644
--- a/hello.py
+++ b/hello.py
@@ -1 +1 @@
-print "hello!"
\ No newline at end of file
+print ("goodbye!")
\ No newline at end of file
foa:gitpractice Alexa$ git commit -m "another edit that i will not like"
On branch master
Changes not staged for commit:
	modified:   hello.py
	modified:   second.py

Untracked files:
	.hello.py.swp

no changes added to commit
foa:gitpractice Alexa$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   hello.py
	modified:   second.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ git diff
diff --git a/hello.py b/hello.py
index 70cddf5..0dba7dd 100644
--- a/hello.py
+++ b/hello.py
@@ -1 +1 @@
-print "hello!"
\ No newline at end of file
+print ("goodbye!")
\ No newline at end of file
diff --git a/second.py b/second.py
index dcc17ab..1635994 100644
--- a/second.py
+++ b/second.py
@@ -2,4 +2,6 @@ print ("this is another file for gitpractice")
 
 git_status = "use this to check the status of the git directory"
 
-print (git_status)
\ No newline at end of file
+print (git_status)
+
+print ("this is an edit...")
\ No newline at end of file
foa:gitpractice Alexa$ python second.py
this is another file for gitpractice
use this to check the status of the git directory
this is an edit...
foa:gitpractice Alexa$ git log
commit 38216d6cc8cd8885afe4982a78fe518755059434
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:28:15 2016 -0700

    a second file for git practice

commit 789f89fae291728ece240ed8edfe902d7a848813
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:21:36 2016 -0700

    added a new file
foa:gitpractice Alexa$ git reset--card
git: 'reset--card' is not a git command. See 'git --help'.
foa:gitpractice Alexa$ git reset --card
error: unknown option `card'
usage: git reset [--mixed | --soft | --hard | --merge | --keep] [-q] [<commit>]
   or: git reset [-q] <tree-ish> [--] <paths>...
   or: git reset --patch [<tree-ish>] [--] [<paths>...]

    -q, --quiet           be quiet, only report errors
    --mixed               reset HEAD and index
    --soft                reset only HEAD
    --hard                reset HEAD, index and working tree
    --merge               reset HEAD, index and working tree
    --keep                reset HEAD but keep local changes
    -p, --patch           select hunks interactively
    -N, --intent-to-add   record only the fact that removed paths will be added later

foa:gitpractice Alexa$ git reset --hard
HEAD is now at 38216d6 a second file for git practice
foa:gitpractice Alexa$ git help
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Find by binary search the change that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Forward-port local commits to the updated upstream head
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
foa:gitpractice Alexa$ git remote add origin https://github.com/alexatodd/gitpractice-.git
fatal: remote origin already exists.
foa:gitpractice Alexa$ git push -u origin master
Username for 'https://github.com': alexatodd
Password for 'https://alexatodd@github.com': 
Branch master set up to track remote branch master from origin.
Everything up-to-date
foa:gitpractice Alexa$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   second.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   second.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ git commit -m "edited git_status variable"
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
	modified:   second.py

Untracked files:
	.hello.py.swp

no changes added to commit
foa:gitpractice Alexa$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Everything up-to-date
foa:gitpractice Alexa$ git push -u master
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

fatal: 'master' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
foa:gitpractice Alexa$ git remote show origin
* remote origin
  Fetch URL: https://github.com/alexatodd/gitpractice.git
  Push  URL: https://github.com/alexatodd/gitpractice.git
  HEAD branch: master
  Remote branch:
    master tracked
  Local branch configured for 'git pull':
    master merges with remote master
  Local ref configured for 'git push':
    master pushes to master (up to date)
foa:gitpractice Alexa$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   second.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

no changes added to commit (use "git add" and/or "git commit -a")
foa:gitpractice Alexa$ git log
commit 38216d6cc8cd8885afe4982a78fe518755059434
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:28:15 2016 -0700

    a second file for git practice

commit 789f89fae291728ece240ed8edfe902d7a848813
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:21:36 2016 -0700

    added a new file
foa:gitpractice Alexa$ git diff
diff --git a/second.py b/second.py
index dcc17ab..262cac2 100644
--- a/second.py
+++ b/second.py
@@ -1,5 +1,6 @@
 print ("this is another file for gitpractice")
 
-git_status = "use this to check the status of the git directory"
+git_status = "use git_status to check the status of the git directory"
+
+print (git_status)
 
-print (git_status)
\ No newline at end of file
foa:gitpractice Alexa$ git add
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?
foa:gitpractice Alexa$ git add second.py
foa:gitpractice Alexa$ git commit -m "edits to the variable git_status"
[master 9691b52] edits to the variable git_status
 1 file changed, 3 insertions(+), 2 deletions(-)
foa:gitpractice Alexa$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.hello.py.swp

nothing added to commit but untracked files present (use "git add" to track)
foa:gitpractice Alexa$ git push
warning: push.default is unset; its implicit value has changed in
Git 2.0 from 'matching' to 'simple'. To squelch this message
and maintain the traditional behavior, use:

  git config --global push.default matching

To squelch this message and adopt the new behavior now, use:

  git config --global push.default simple

When push.default is set to 'matching', git will push local branches
to the remote branches that already exist with the same name.

Since Git 2.0, Git defaults to the more conservative 'simple'
behavior, which only pushes the current branch to the corresponding
remote branch that 'git pull' uses to update the current branch.

See 'git help config' and search for 'push.default' for further information.
(the 'simple' mode was introduced in Git 1.7.11. Use the similar mode
'current' instead of 'simple' if you sometimes use older versions of Git)

Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 328 bytes | 0 bytes/s, done.
Total 3 (delta 1), reused 0 (delta 0)
To https://github.com/alexatodd/gitpractice.git
   38216d6..9691b52  master -> master
foa:gitpractice Alexa$ cd ..
foa:~ Alexa$ rm -rf gitpractice
foa:~ Alexa$ git clone https://github.com/alexatodd/gitpractice.git
Cloning into 'gitpractice'...
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 1), reused 9 (delta 1), pack-reused 0
Unpacking objects: 100% (9/9), done.
Checking connectivity... done.
foa:~ Alexa$ ls
Applications		Google Drive		Sites
Bitrix24		Library			VirtualBox VMs
Cloud Drive		Movies			Windows 7.iso
Desktop			Music			emaildb.sqlite
Documents		Pictures		gitpractice
Downloads		Public			~$Calendar012512.csv
Dropbox			Records
GitHub			Running
foa:~ Alexa$ cd gitpractice
foa:gitpractice Alexa$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
foa:gitpractice Alexa$ git log
commit 9691b52e877ed4c7f4e29684682eb3ee1fa0c8dc
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:58:49 2016 -0700

    edits to the variable git_status

commit 38216d6cc8cd8885afe4982a78fe518755059434
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:28:15 2016 -0700

    a second file for git practice

commit 789f89fae291728ece240ed8edfe902d7a848813
Author: anorthfox <alexatodd@gmail.com>
Date:   Tue Mar 15 18:21:36 2016 -0700

    added a new file
foa:gitpractice Alexa$ """


