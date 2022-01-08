## Lecture 08. Metaprogramming

---

> Most makefiles provide a target called `clean`. This isn’t intended to produce a file called `clean`, but instead to clean up any files that can be re-built by make. Think of it as a way to “undo” all of the build steps. Implement a `clean` target for the `paper.pdf` `Makefile` above. You will have to make the target [phony](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html). You may find the [`git ls-files`](https://git-scm.com/docs/git-ls-files)subcommand useful. A number of other very common make targets are listed [here](https://www.gnu.org/software/make/manual/html_node/Standard-Targets.html#Standard-Targets).

If you check the files in the folder after we run `make`, you will find that the new files are `paper.aux`, `paper.log`, `paper.pdf` and `paper.png`. These files are what we want to `clean`. In order to do this, we can modify `Makefile` like this :arrow_down:

```makefile
paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@

.PHONY: clean
cleanall: cleanaux cleanlog cleanpdf cleanpng

cleanaux:
	rm *.aux

cleanlog:
	rm *.log

cleanpdf:
	rm *.pdf

cleanpng:
	rm *.png
```

> Take a look at the various ways to specify version requirements for dependencies in [Rust’s build system](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html). Most package repositories support similar syntax. For each one (caret, tilde, wildcard, comparison, and multiple), try to come up with a use-case in which that particular kind of requirement makes sense.

1. Caret requirements: It is used to update minor version and patch version.
2. Tilde requirements: It is used to match the most recent patch version by freezing major version and minor version.
3. Wildcard requirements: It is used to specify major version and accept any minor version and patch version.
4. Both of comparison requirements and multiple requirements are used to give more control over packages. We may used them to overcome conflicts.

> Git can act as a simple CI system all by itself. In `.git/hooks` inside any git repository, you will find (currently inactive) files that are run as scripts when a particular action happens. Write a [`pre-commit`](https://git-scm.com/docs/githooks#_pre_commit) hook that runs `make paper.pdf` and refuses the commit if the `make` command fails. This should prevent any commit from having an unbuildable version of the paper.

After reading this tutorial above, You will find how git hooks work. So the solution will be :arrow_down:

1. Write a `pre-commit` hook in whatever languages you like. Here is my scipt.

   ```bash
   #!/usr/bin/env bash
   if ! make paper.pdf;
   then 
       echo "==> Running make command fail :("
       exit 1
   else
       echo "==> Running make command successfully :)"
       exit 0
   fi
   ```

2. Change the file mode of hook you just wrote, make it executable. Type `chmod u+x pre-commit` in your terminal.

3. mv the hook to `.git/hooks`. Type `mv pre-commit .git/hooks/pre-commit`

Now it time to test if your hook works as you expected :hugs: :arrow_down:

```bash
> git add .
> git commit -m "Try to commit"
```

> Set up a simple auto-published page using [GitHub Pages](https://pages.github.com/). Add a [GitHub Action](https://github.com/features/actions) to the repository to run `shellcheck` on any shell files in that repository (here is [one way to do it](https://github.com/marketplace/actions/shellcheck)). Check that it works!

This blog is host by Github Pages:hugs:



1. First, create a `yml` file in your `.github/workflows/`. My `yml` file looks like:

   ```yaml
   on: [push]
   
   name: 'Trigger: Push action'
   
   jobs:
     shellcheck:
       name: Shellcheck
       runs-on: ubuntu-latest
       steps:
       - uses: actions/checkout@v2
       - name: Run ShellCheck
         uses: ludeeus/action-shellcheck@master
   ```

2. `git add` && `git commit -m ""` && `git push`. Add your workflow to your remote repo.

3. Now we can create a simple `.sh` file. I deliberately didn't add `shebang` in `sh` file. 

   ```sh
   date
   ```

   If you run `shellcheck` in your local machine, you should get a warning says: `SC2148 (error): Tips depend on target shell and yours is unknown. Add a shebang or a 'shell' directive.`

4. `git add` && `git commit -m ""` && `git push`. Check if your workflow works by clicking `Actions` in your repo. You will see it didn't pass the test. The output is:

   ```
   Run ludeeus/action-shellcheck@master
   Run problem_matcher_file="/home/runner/work/_actions/ludeeus/action-shellcheck/master/.github/problem-matcher-gcc.json"
   Run if [[ "Linux" == "macOS" ]]; then
   Run "/home/runner/work/_actions/ludeeus/action-shellcheck/master/shellcheck" --version
   ShellCheck - shell script analysis tool
   version: 0.8.0
   license: GNU General Public License, version 3
   website: https://www.shellcheck.net
   Run declare -a options
   Run declare -a excludes
   Run declare -a files
   Run declare -a filepaths
   Run statuscode=0
   Error: ./another.sh:1:1: error: Tips depend on target shell and yours is unknown. Add a shebang or a 'shell' directive. [SC2148]
   Error: ./sample.sh:1:1: error: Tips depend on target shell and yours is unknown. Add a shebang or a 'shell' directive. [SC2148]
   Run echo "Files: ./another.sh ./sample.sh"
   Files: ./another.sh ./sample.sh
   Excluded: ! -path *./.git/* ! -path *.go ! -path */mvnw
   Options: --format=gcc
   Status code: 1
   Error: Process completed with exit code 1.
   ```


> [Build your own](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/building-actions) GitHub action to run [`proselint`](http://proselint.com/) or [`write-good`](https://github.com/btford/write-good) on all the`.md` files in the repository. Enable it in your repository, and check that it works by filing a pull request with a typo in it.

I should learn some basics of `docker`, then I may return to this exercise :(



