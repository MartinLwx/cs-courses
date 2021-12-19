---
title: "the HWs of MIT. Missing-semester(2020)"
date: 2021-12-18T10:11:22+08:00
draft: false
tags: ["Course"]
author: "MartinLwx"
description: "the solutions for exercises in MIT. Missing-semester"
---

## Lecture 1. Shell

---

> Create a new directory called `missing` under `/tmp`

```bash
> mkdir -p /tmp/missing
```

📒 `-p` means *Create intermediate directories as required*

> Use `touch` to create a new file called `semester` in `missing`.

```bash
> cd ~/tmp/missing
> touch semester
```

> Write the following into that file, one line at a time:
>
> ```bash
> #!/bin/sh
> curl --head --silent https://missing.csail.mit.edu
> ```

⚠️ Make sure you are in the `tmp/missing` directory start from now.

```bash
> echo "#\!/bin/sh" >> semester
> echo "curl --head --silent https://missing.csail.mit.edu" >> semester
```

⚠️ Warning：`!` has a special meaning even within double-quoted(`"`) strings, so when we use `echo "..."` to append a string to a file, remember to use `\` to escape `!`

>  Try to execute the file

```bash
> ./semeseter
# ... permission denied

> ls -l
# you can see the permission bits are  -rw-r--r--
# It suggests that we don't have execute(x) permission

## Solution 1.
# run command below to, u means user, x means execute
> chmod u+x semester
> ./semester
# You should see the outputs like: 
# HTTP/2 200
# server: GitHub.com
# ...

## Solution 2.
> sh ./semester
```

📒 use `chmod` to change the file permission, see `man chmod` for more information. I will suggest the `tldr` tool, which is quite handy, you may check `tldr chmod` by yourself:hugs:

> Use `|` and `>` to write the “last modified” date output by `semester` into a file called `last-modified.txt` in your home directory.

```bash
# Solution 1.
> date -r semester > last-modified.txt

# Solution 2.
> ls -l semester  | awk '{print $6,$7,$8}' > last-modified.txt
```

> Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from `/sys`

I am a macOS user, so I will just skip this exercise:)
