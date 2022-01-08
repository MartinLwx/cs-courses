## Lecture 07. Debugging and profiling

---

### debugging

> Use `journalctl` on Linux or `log show` on macOS to get the super user accesses and commands in the last day. If there aren’t any you can execute some harmless commands such as `sudo ls` and check again.

When I run `log show --last 1d`, it keeps running for along time. I don't know how long it make take, so I will just execute harmless `sudo ls` to check the log.

```bash
> sudo ls
> log show --last 10s | grep -E "sudo"
# you should see the last line of output says 
# you once run ls in super user access
```

> Do [this](https://github.com/spiside/pdb-tutorial) hands on `pdb` tutorial to familiarize yourself with the commands. For a more in depth tutorial read [this](https://realpython.com/python-debugging-pdb).

I have finished this tutorial. Actually, I fork this repo and add [chinese translation](https://github.com/MartinLwx/pdb-tutorial/tree/master).

> Install [`shellcheck`](https://www.shellcheck.net/) and try checking the following script. What is wrong with the code? Fix it. Install a linter plugin in your editor so you can get your warnings automatically.
>
> ```bash
> #!/bin/sh
> ## Example: a typical script with several problems
> for f in $(ls *.m3u)
> do
>   grep -qi hq.*mp3 $f \
>     && echo -e 'Playlist $f contains a HQ file in mp3 format'
> done
> ```

**ERROR**

1. [SC2045](https://github.com/koalaman/shellcheck/wiki/SC2045). In line 3, it says *Iterating over ls output is fragile. Use globs.*

**WARNINGS**

1. [SC2062](https://github.com/koalaman/shellcheck/wiki/SC2062). In line 5, it says *Quote the grep pattern so the shell won't interpret it.*

2. [SC3037](https://github.com/koalaman/shellcheck/wiki/SC3037). In line 6, it says *In POSIX sh, echo flags are undefined.* I think we can use `bash` instead of `sh`

**INFO**

1. [SC2016](https://github.com/koalaman/shellcheck/wiki/SC2016). In line 6, it says *Expressions don't expand in single quotes, use double quotes for that.*

2. [SC2086](). In line 5, it says *Double quote to prevent globbing and word splitting.*

3. [SC3010](https://github.com/koalaman/shellcheck/wiki/SC3010). After following the guide of [SC2045](https://github.com/koalaman/shellcheck/wiki/SC2045), I added a line(`[[ -e $f ]] || break`) below `do`. [SC3010](https://github.com/koalaman/shellcheck/wiki/SC3010) says  *In POSIX sh, [[ ]] is undefined.* Then I change shebang to `#!/bin/bash`

So the final version of `sh` file is :arrow_down:

```bash
#!/bin/bash
## Example: a typical script with several problems
for f in  *.m3u
do
    [[ -e "$f" ]] || break    # handle the case of no *.m3u files
    grep -qi "hq.*mp3" "$f" \
    && echo -e "Playlist $f contains a HQ file in mp3 format"
done
```

> (Advanced) Read about [reversible debugging](https://undo.io/resources/reverse-debugging-whitepaper/) and get a simple example working using [`rr`](https://rr-project.org/) or [`RevPDB`](https://morepypy.blogspot.com/2016/07/reverse-debugging-for-python.html).

PASS :)

### Profiling

> [Here](https://missing.csail.mit.edu/static/files/sorts.py) are some sorting algorithm implementations. Use [`cProfile`](https://docs.python.org/3/library/profile.html) and [`line_profiler`](https://github.com/pyutils/line_profiler) to compare the runtime of insertion sort and quicksort. What is the bottleneck of each algorithm? Use then `memory_profiler` to check the memory consumption, why is insertion sort better? Check now the inplace version of quicksort. Challenge: Use `perf` to look at the cycle counts and cache hits and misses of each algorithm.

🤔We can type `python -m cProfile -s tottime sorts.py 1000` in the terminal to get the runtime of insertion sort and quicksort. `1000` means that we will run this `sorts.py` 1000 times. Check [documentations](https://docs.python.org/3/library/profile.html) for more details. 

```
     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     ...
     1000     0.045    0.000    0.045    0.000 sorts.py:12(insertionsort)
33218/1000    0.044    0.000    0.068    0.000 sorts.py:25(quicksort)
		 ...
```

🤔If you want to use `line_profiler` to compare the runtime of insertion sort and quicksort, you need to add `@profile` decorator above insertion sort and quicksort(You should install `line_profiler` fist by `pip install line_profiler`). The code will be like :arrow_down:

```python
@profile
def insertionsort(array):
  ...
  
@profile
def quicksort(array):
	...
```

Then type `kernprof -v -l sorts.py` in your terminal. The output will look like: :arrow_down:

```
Wrote profile results to sorts.py.lprof
Timer unit: 1e-06 s

Total time: 0.382157 s
File: sorts.py
Function: insertionsort at line 11

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    11                                           @profile
    12                                           def insertionsort(array):
    13
    14     25881      10925.0      0.4      2.9      for i in range(len(array)):
    15     24881      10814.0      0.4      2.8          j = i-1
    16     24881      11411.0      0.5      3.0          v = array[i]
    17    221660     133321.0      0.6     34.9          while j >= 0 and v < array[j]:
    18    196779     113095.0      0.6     29.6              array[j+1] = array[j]
    19    196779      88824.0      0.5     23.2              j -= 1
    20     24881      13333.0      0.5      3.5          array[j+1] = v
    21      1000        434.0      0.4      0.1      return array

Total time: 0.162542 s
File: sorts.py
Function: quicksort at line 24

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    24                                           @profile
    25                                           def quicksort(array):
    26     33150      24083.0      0.7     14.8      if len(array) <= 1:
    27     17075       9918.0      0.6      6.1          return array
    28     16075      10775.0      0.7      6.6      pivot = array[0]
    29     16075      46333.0      2.9     28.5      left = [i for i in array[1:] if i < pivot]
    30     16075      46896.0      2.9     28.9      right = [i for i in array[1:] if i >= pivot]
    31     16075      24537.0      1.5     15.1      return quicksort(left) + [pivot] + quicksort(right)
```

**So we can easily find that the bottleneck(rows which have high `% Time`)**. More details can be found on [this](https://github.com/pyutils/line_profiler)

🤔Now we come to the `memory_profiler` part. If you haven't installed it, you may run `pip install -U memory_profiler`. The usage of `memory_profiler` is quite similar to the `line_profiler`. Both of them need to add `@profile` first, then you can run ``. The output will be like :arrow_down:

```
Filename: sorts.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    11   38.176 MiB   38.176 MiB        1000   @profile
    12                                         def insertionsort(array):
    13
    14   38.176 MiB    0.000 MiB       25694       for i in range(len(array)):
    15   38.176 MiB    0.000 MiB       24694           j = i-1
    16   38.176 MiB    0.000 MiB       24694           v = array[i]
    17   38.176 MiB    0.000 MiB      223188           while j >= 0 and v < array[j]:
    18   38.176 MiB    0.000 MiB      198494               array[j+1] = array[j]
    19   38.176 MiB    0.000 MiB      198494               j -= 1
    20   38.176 MiB    0.000 MiB       24694           array[j+1] = v
    21   38.176 MiB    0.000 MiB        1000       return array


Filename: sorts.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24   38.172 MiB   38.148 MiB       33522   @profile
    25                                         def quicksort(array):
    26   38.172 MiB    0.000 MiB       33522       if len(array) <= 1:
    27   38.172 MiB    0.000 MiB       17261           return array
    28   38.172 MiB    0.000 MiB       16261       pivot = array[0]
    29   38.172 MiB    0.004 MiB      156337       left = [i for i in array[1:] if i < pivot]
    30   38.172 MiB    0.000 MiB      156337       right = [i for i in array[1:] if i >= pivot]
    31   38.172 MiB    0.020 MiB       16261       return quicksort(left) + [pivot] + quicksort(right)
```

It is weird, insertion sort is no better than quicksort in memory usage :crying_cat_face:

🤔If we use the inlace version of quicksort, we can find that it uses slightly less memory.

🤔In Mac, there is no `perf`, so I will just skip this.

> Here’s some (arguably convoluted) Python code for computing Fibonacci numbers using a function for each number.
>
> ```python
> #!/usr/bin/env python
> def fib0(): return 0
> 
> def fib1(): return 1
> 
> s = """def fib{}(): return fib{}() + fib{}()"""
> 
> if __name__ == '__main__':
> 
>     for n in range(2, 10):
>         exec(s.format(n, n-1, n-2))
>     # from functools import lru_cache
>     # for n in range(10):
>     #     exec("fib{} = lru_cache(1)(fib{})".format(n, n))
>     print(eval("fib9()"))
> ```
>
> Put the code into a file and make it executable. Install prerequisites: [`pycallgraph`](http://pycallgraph.slowchop.com/en/master/) and [`graphviz`](http://graphviz.org/). (If you can run `dot`, you already have GraphViz.) Run the code as is with `pycallgraph graphviz -- ./fib.py`and check the `pycallgraph.png` file. How many times is `fib0` called?. We can do better than that by memoizing the functions. Uncomment the commented lines and regenerate the images. How many times are we calling each `fibN` function now?

First, we need to install prerequisites :arrow_down:

```bash
> pip install pycallgraph
> brew install graphviz
```

Then we can run commands followed :arrow_down:

```bash
> pycallgraph graphviz -- ./fib.py
```

Open `pycallgraph.png`(in the same working dir). We can know that `fib0` was called 21 times.

> A common issue is that a port you want to listen on is already taken by another process. Let’s learn how to discover that process pid. First execute `python -m http.server 4444` to start a minimal web server listening on port `4444`. On a separate terminal run `lsof | grep LISTEN` to print all listening processes and ports. Find that process pid and terminate it by running `kill <PID>`.

```bash
> python -m http.server 4444
> lsof | grep LISTEN
> kill <PID>             # <PID> can be found in the output of last command
```

> Limiting processes resources can be another handy tool in your toolbox. Try running `stress -c 3` and visualize the CPU consumption with `htop`. Now, execute `taskset --cpu-list 0,2 stress -c 3` and visualize it. Is `stress` taking three CPUs? Why not? Read [`man taskset`](https://www.man7.org/linux/man-pages/man1/taskset.1.html). Challenge: achieve the same using [`cgroups`](https://www.man7.org/linux/man-pages/man7/cgroups.7.html). Try limiting the memory consumption of `stress -m`.

After I ran `stress -c 3`, the `htop` shows I am taking 3 CPUs.

In Mac, there is no `taskset` or `cgroups`.

> (Advanced) The command `curl ipinfo.io` performs a HTTP request and fetches information about your public IP. Open [Wireshark](https://www.wireshark.org/) and try to sniff the request and reply packets that `curl` sent and received. (Hint: Use the `http` filter to just watch HTTP packets).

PASS :)

