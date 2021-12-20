## lecture 02. Shell Tools and Scripting

---

> write an `ls` command that lists files in the following manner
>
> - Includes all files, including hidden files
> - Sizes are listed in human readable format (e.g. 454M instead of 454279954)
> - Files are ordered by recency
> - Output is colorized
>
> A sample output would look like this
>
> ```bash
>  -rw-r--r--   1 user group 1.1M Jan 14 09:53 baz
>  drwxr-xr-x   5 user group  160 Jan 14 09:53 .
>  -rw-r--r--   1 user group  514 Jan 14 06:42 bar
>  -rw-r--r--   1 user group 106M Jan 13 12:12 foo
>  drwx------+ 47 user group 1.5K Jan 12 18:08 ..
> ```

Interpretation

- Usually, the filename of hidden files are begin with `.`, we can use `-a` flag to include them.
- If you want to list sizes in human readable format, use `-lh`
- According to the `man ls`，`-t` means the output are sort by descending time modified (most recently modified first)
- In order to enable colorized output, use `-G`

So the solution is:arrow_down:

```bash
> ls -a -lh -t -G
```

> Write bash functions `marco` and `polo` that do the following. Whenever you execute `marco` the current working directory should be saved in some manner, then when you execute `polo`, no matter what directory you are in, `polo` should `cd` you back to the directory where you executed `marco`. For ease of debugging you can write the code in a file `marco.sh` and (re)load the definitions to your shell by executing `source marco.sh`.

The `marco.sh`:arrow_down:

I store the output of `pwd` in `~/pwd.txt` file.

```bash
#!/bin/bash
marco() {
    touch ~/pwd.txt
    pwd >> ~/pwd.txt
}
```

The `poli.sh`:arrow_down:

Just use `cat ~/pwd.txt` to get the origin working directory.

```bash
#!/bin/bash
poli() {
    destination=$(cat ~/pwd.txt)
    cd "$destination" || exit
}
```

Quick test⬇️

```bash
> source marco.sh
> source poli.sh
> marco
> cd ..            # you can cd wherever you want
> poli             # now you will go back to origin working directory
```

📒 I highly recommend the `shellcheck` tool. Use it to check your `*.sh` file after you have finished your code.

> Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.
>
> ```bash
> #!/usr/bin/env bash
> 
> n=$(( RANDOM % 100 ))
> 
> if [[ n -eq 42 ]]; then
>  echo "Something went wrong"
>  >&2 echo "The error was using magic numbers"
>  exit 1
> fi
> 
> echo "Everything went according to plan"
> ```

The meaning of this script is judge if a random number(`n`) equal 42 or not. The random number ranges from 0 to 99, so we may need to run many many time until we get a `42`. In order to debug this `*.sh` file, we can measure how many times we run this `*.sh`. Apparently, we can use *do-while* loop, which corresponds to `until-loop` in bash. I found this [Link](https://www.tutorialkart.com/bash-shell-scripting/bash-until-loop-statement/) helpful. The solution is(`test.sh`)⬇️

```bash
#!/bin/bash
count=0

# run random.sh until it goes wrong
until [[ "$?" -ne 0 ]];do								# $? will return the exit status of the most recently executed command
count=$((count + 1))
bash ./random.sh &> result.txt					# & means we run the random.sh in the background.
done

echo "Error dectected: $count runs"
cat result.txt
```

Quick test⬇️

```bash
> bash test.sh
```

> As we covered in the lecture `find`’s `-exec` can be very powerful for performing operations over the files we are searching for. However, what if we want to do something with **all** the files, like creating a zip file? As you have seen so far commands will take input from both arguments and STDIN. When piping commands, we are connecting STDOUT to STDIN, but some commands like `tar` take inputs from arguments. To bridge this disconnect there’s the [`xargs`](https://www.man7.org/linux/man-pages/man1/xargs.1.html) command which will execute a command using STDIN as arguments. For example `ls | xargs rm` will delete the files in the current directory.
>
> Your task is to write a command that recursively finds all HTML files in the folder and makes a zip with them. Note that your command should work even if the files have spaces (hint: check `-d` flag for `xargs`).
>
> 
>
> If you’re on macOS, note that the default BSD `find` is different from the one included in [GNU coreutils](https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands). You can use `-print0` on `find` and the `-0`flag on `xargs`. As a macOS user, you should be aware that command-line utilities shipped with macOS may differ from the GNU counterparts; you can install the GNU versions if you like by [using brew](https://formulae.brew.sh/formula/coreutils).

The steps:

1. Find all html files recursively. we can use `find . -name '*.html'`
2. `tar` all the html files, we can use `tar <tar_file_name> file1 file2 ...`
3. Use pipeline `|` to combine step1. and step2.

Because I am a macOS user, so I need to use `-print0` in `find` and `-0` in `xargs`

- `-print0` in `find` will print the pathname of files to standard output, each one followed by an ASCII NUL character
- `-0` in `xargs` will change `xargs` to expect NUL character as separators

```bash
> find . -name '*.html' -print0 | xargs -0 tar czf html_files.tar.gz
```

📒 I would recommend use `fd` instead of `find`. In `fd`, `-X` means *execute command once, with all search results as arguments*, we can use a placeholder `{}` to capture all results returned by `fd`. The nicer solution is like⬇️

```bash
> fd -e html -X tar czf html_files.tar.gz {}
```

> (Advanced) Write a command or script to recursively find the most recently modified file in a directory. More generally, can you list all files by recency?

```bash
> find . -type f -print0 | xargs -0 ls -trlh | tail -n 1
```

Again, use `fd` will make this easier.⬇️

```bash
> fd -t f -X ls -trlh {} | tail -n 1
```

