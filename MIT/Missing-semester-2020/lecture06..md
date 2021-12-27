## Lecture 06. Version Control(git)

---

> If you don’t have any past experience with Git, either try reading the first couple chapters of [Pro Git](https://git-scm.com/book/en/v2) or go through a tutorial like [Learn Git Branching](https://learngitbranching.js.org/). As you’re working through it, relate Git commands to the data model.

:)

> Clone the [repository for the class website](https://github.com/missing-semester/missing-semester)
>
> 1. Explore the version history by visualizing it as a graph.
> 2. Who was the last person to modify `README.md`? (Hint: use `git log` with an argument).
> 3. What was the commit message associated with the last modification to the `collections:` line of `_config.yml`? (Hint: use `git blame` and `git show`).

```bash
> git clone git@github.com:missing-semester/missing-semester.git
> cd missing-semester

# step 1.
> git log --oneline --all --graph --color          

# step 2.
> git log -1 README.md			# -1 means showing last related commit
# then we know Anish Athalye is the last person modify README.md

# step 3.
> git blame _config.yml | grep -E "collections:"
# then we know the commit's sha-1 value is a88b4eac
# we can use `git show` command to get commit message
> git show -q a88b4eac			# -q means --quiet, it will suppress diff output
```

> One common mistake when learning Git is to commit large files that should not be managed by Git or adding sensitive information. Try adding a file to a repository, making some commits and then deleting that file from history (you may want to look at [this](https://help.github.com/articles/removing-sensitive-data-from-a-repository/)).

I made a new repo and made some commits. Finally I found the correct command to delete a file from all history :hugs:

Ths command we are going to use is `git filter-repo`. If you haven't installed it, you may just run `brew install git filter-repo `(for mac users). Then use this "magic" command do finish this exercise.

```bash
> git filter-repo --invert-paths --force --path <file>
```

The reason why I use `--force` is that `git filter-repo` refuses to overwrite my repo. It says my repo doesn't look like a fresh clone.

The mechanism behind this command is: `--invert-paths` will only select files matching none of options which we specify by `--path`. So it will keep everything except `<file>`, and overwrite this commit history.

> Clone some repository from GitHub, and modify one of its existing files. What happens when you do `git stash`? What do you see when running `git log --all --oneline`? Run `git stash pop` to undo what you did with `git stash`. In what scenario might this be useful?

I tried to modify `README.md` is the repo for the class website. 

Then I ran `git stash`. The output is: `Saved working directory and index state WIP on master: c2f9535 Merge pull request #172 from chapmanjacobd/patch-1`

```
*   96cca4b (refs/stash) WIP on master: c2f9535 Merge pull request #172 from chapmanjacobd/patch-1
|\
| * a95c46f index on master: c2f9535 Merge pull request #172 from chapmanjacobd/patch-1
|/
*   c2f9535 (HEAD -> master, origin/master, origin/HEAD) Merge pull request #172 from chapmanjacobd/patch-1
```

Then I ran `git stash pop`. My modification has come back.

The scenario of using `git stash` is that: For exmaple, say I have beening working on my project in `master` branch for quite a long time. Now I want to switch to another branch, but my working directory is in a mess. I don't want to make a dirty commit to temporarily save my work. Here comes the `git stash`. **I can use this command to temporarily save my half-finished work.** :hugs:

> Like many command line tools, Git provides a configuration file (or dotfile) called `~/.gitconfig`. Create an alias in `~/.gitconfig` so that when you run `git graph`, you get the output of `git log --all --graph --decorate --oneline`. Information about git aliases can be found [here](https://git-scm.com/docs/git-config#Documentation/git-config.txt-alias).

```bash
> git config --global --add alias.graph 'log --all --graph --decorate --oneline'
> git graph
```

> You can define global ignore patterns in `~/.gitignore_global` after running `git config --global core.excludesfile ~/.gitignore_global`. Do this, and set up your global gitignore file to ignore OS-specific or editor-specific temporary files, like `.DS_Store`.

```bash
> git config --global core.excludesfile ~/.gitignore_global
> echo ".DS_Store" >> ~/.test
```

> Fork the [repository for the class website](https://github.com/missing-semester/missing-semester), find a typo or some other improvement you can make, and submit a pull request on GitHub (you may want to look at [this](https://github.com/firstcontributions/first-contributions)).

I followed first-contributions in [this](https://github.com/firstcontributions/first-contributions).:happy:

