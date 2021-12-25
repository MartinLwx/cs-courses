## Lecture 04. Data Wrangling

---

> Take this [short interactive regex tutorial](https://regexone.com/).

Just click this link to finish this regex tutorial.

> Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending. What are the three most common last two letters of those words? `sed`’s `y` command, or the `tr` program, may help you with case insensitivity. How many of those two-letter combinations are there? And for a challenge: which combinations do not occur?

The answers of questions in exercise are :arrow_down:

> **Q: Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending.**

Answer: `tr 'A-Z' 'a-z' < /usr/share/dict/words | grep -E '.*a.*a.*a.*[^s]$' | wc -l`, :point_right: `5290`

1. Use `tr 'A-Z' 'a-z' < /usr/share/dict/words` to make text case-insensitive

2. Use `grep -E 'grep -E '.*a.*a.*a.*[^s]$'` to find the words that contain at least three `a` and don't have a `'s` ending

   - The combination of `.*` means any character repeats any times.

   - `[s]` will match the `s` character. We add a `^` in `[]`, which mean we want to match any single character excepet `s` 

3. Use `wc -l` to count the number of lines in output.

> **Q: What are the three most common last two letters of those words?**

A: `tr 'A-Z' 'a-z' < /usr/share/dict/words | grep -E '.*a.*a.*a.*[^s]$' | grep -E -o '.{2}$' | sort | uniq -c | sort | tail -n 1`, :point_right: `1039 al` and `763 an` and `637 ae`

1. Use `grep -E -o '.{2}$'` to get last 2 letters of these words
   - `-o` means *Prints only the matching part of the lines.* In this case, what we want is the last 2 letters, so we type `.{2}$`
2. Use `sort | uniq -c` to get the two-letter combinations count
   - This can ensure the combinations are uniq.
3. Use `sort | tail -n 3` to sort previous results according to their frequency counts

> **Q: How many of those two-letter combinations are there?**

A: `tr 'A-Z' 'a-z' < /usr/share/dict/words | grep -E '.*a.*a.*a.*[^s]$' | grep -E -o '.{2}$' | sort | uniq -c | wc -l`, :point_right: `140`

> **Q: And for a challenge: which combinations do not occur?**

```bash
diff <(echo {a..z}{a..z} | tr " " "\n") \
		 <(tr 'A-Z' 'a-z' < /usr/share/dict/words | grep -E '.*a.*a.*a.*[^s]$' | grep -E -o '.{2}$' | sort | uniq -c | sort | awk '{print $2}' | sort) \
		 | grep -E "<" \
		 | wc -l
# output: 536
```

1. Use `echo {a..z}{a..z}` to get all two-letter combinations. However, in order to compare 2 sets of combinations(this one && Our previous results), we need to use `\n` as delimiter of each combination. We can use `tr " " "\n"`.
2. In the previous question, we can get every different combinations and their frequency counts. Each row looks like `<frequency count> combination`. In order to get the combinations, we can use `awk {print $2}`, `$2` means the second field in each row. After that, we need to 
3. Then we need a tool to compare the 2 sets of combinations. Here comes the `diff` command. `diff` will compare 2 files line by line. We also need [Process substation](https://tldp.org/LDP/abs/html/process-sub.html) to pass the 2 sets of combinations as arguments of `diff`

> To do in-place substitution it is quite tempting to do something like `sed s/REGEX/SUBSTITUTION/ input.txt > input.txt`. However this is a bad idea, why? Is this particular to `sed`? Use `man sed` to find out how to accomplish this.

This exercie remind me of the `shellcheck` tool. So I just type `sed s/REGEX/SUBSTITUTION/ input.txt > input.txt` in a `test.sh` file and run `shellcheck test.sh`. Then I knew [THIS IS A BAD IDEA](https://github.com/koalaman/shellcheck/wiki/SC2094). 📒 We should not read and write the same file in the same pipeline. After checking `man sed` carefully, I found 2 flags helpful--`-i` and `-I`. Both of them can edit file in-place. More information, you may check

> Find your average, median, and max system boot time over the last ten boots. Use
>
> ```bash
> journalctl
> ```
>
> on Linux and
>
> ```bash
> log show
> ```
>
> on macOS, and look for log timestamps near the beginning and end of each boot. On Linux, they may look something like:
>
> ```bash
> Logs begin at ...
> ```
>
> and
>
> ```bash
> systemd[577]: Startup finished in ...
> ```
>
> On macOS, [look for](https://eclecticlight.co/2018/03/21/macos-unified-log-3-finding-your-way/):
>
> ```bash
> === system boot:
> ```
>
> and
>
> ```bash
> Previous shutdown cause: 5
> ```

I am a macos user. I barely shutdown my Macbook Pro. So when I ran `log show | grep -E "log show | grep -E "system boot"`, it kept running like it will never stop :crying_cat_face:. So I decided to skip this exercise.

> Look for boot messages that are *not* shared between your past three reboots (see `journalctl`’s `-b` flag). Break this task down into multiple steps. First, find a way to get just the logs from the past three boots. There may be an applicable flag on the tool you use to extract the boot logs, or you can use `sed '0,/STRING/d'` to remove all lines previous to one that matches `STRING`. Next, remove any parts of the line that *always* varies (like the timestamp). Then, de-duplicate the input lines and keep a count of each one (`uniq` is your friend). And finally, eliminate any line whose count is 3 (since it *was* shared among all the boots).

PASS :crying_cat_face:

> Find an online data set like [this one](https://stats.wikimedia.org/EN/TablesWikipediaZZ.htm), [this one](https://ucr.fbi.gov/crime-in-the-u.s/2016/crime-in-the-u.s.-2016/topic-pages/tables/table-1), or maybe one [from here](https://www.springboard.com/blog/free-public-data-sets-data-science-project/). Fetch it using `curl` and extract out just two columns of numerical data. If you’re fetching HTML data, [`pup`](https://github.com/EricChiang/pup) might be helpful. For JSON data, try [`jq`](https://stedolan.github.io/jq/). Find the min and max of one column in a single command, and the difference of the sum of each column in another.

PASS :crying_cat_face:

## References

---

1. [[Accessing last x characters of a string in Bash]](https://stackoverflow.com/questions/19858600/accessing-last-x-characters-of-a-string-in-bash)

2. [Process substitution](https://tldp.org/LDP/abs/html/process-sub.html)
