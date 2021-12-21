## Lecture 03. Editors (Vim)

> Complete `vimtutor`. Note: it looks best in a [80x24](https://en.wikipedia.org/wiki/VT100) (80 columns by 24 lines) terminal window.

It is a tutorial for beginners of vim. **I will just put some notes which are not mentioned in course here**.

- `U` command: When we press `u` in normal mode, we can undo the last command. What `U` does is fixing a whole line.
- `Ctrl + G`: show your location in the file and the file status. Type the linenumber you want to go, then press `G`, then you are there. 
  - To search for a phrase in the backward direction, use  `?`  instead of  `/` .

- Type  `:!`  followed by an external command to execute that command.

- Select text to write
  - Use visual mode to select text
  - type `:w <type_filename_here` 
  - You can also type `:!ls` to verify this

- To insert the contents of a file, type  `:r` FILENAME
  - Furthermore, You can also read the output of an external command.  For example, `:r !ls`  reads the output of the ls command

- Type a capital  `R`  to replace more than one character.

> Download our [basic vimrc](https://missing.csail.mit.edu/2020/files/vimrc) and save it to `~/.vimrc`. Read through the well-commented file (using Vim!), and observe how Vim looks and behaves slightly differently with the new config.

I would recommend making your own configuration.

> Install and configure a plugin: [ctrlp.vim](https://github.com/ctrlpvim/ctrlp.vim)
>
> 1. Create the plugins directory with `mkdir -p ~/.vim/pack/vendor/start`
> 2. Download the plugin: `cd ~/.vim/pack/vendor/start; git clone https://github.com/ctrlpvim/ctrlp.vim`
> 3. Read the [documentation](https://github.com/ctrlpvim/ctrlp.vim/blob/master/readme.md) for the plugin. Try using CtrlP to locate a file by navigating to a project directory, opening Vim, and using the Vim command-line to start `:CtrlP`.
> 4. Customize CtrlP by adding [configuration](https://github.com/ctrlpvim/ctrlp.vim/blob/master/readme.md#basic-options) to your `~/.vimrc` to open CtrlP by pressing Ctrl-P.

PASS

> To practice using Vim, re-do the [Demo](https://missing.csail.mit.edu/2020/editors/#demo) from lecture on your own machine.

PASS

> Use Vim for *all* your text editing for the next month. Whenever something seems inefficient, or when you think “there must be a better way”, try Googling it, there probably is. If you get stuck, come to office hours or send us an email.

> Configure your other tools to use Vim bindings (see instructions above).

I have already enable *vim mode* in my Vscode and zsh. :muscle:

> Further customize your `~/.vimrc` and install more plugins.

I have made my own configuration

> (Advanced) Convert XML to JSON ([example file](https://missing.csail.mit.edu/2020/files/example-data.xml)) using Vim macros. Try to do this on your own, but you can look at the [macros](https://missing.csail.mit.edu/2020/editors/#macros) section above if you get stuck.

The steps:

1. Press `Gdd` && `ggdd` to delete the first line and the last line
2. Macro to format a single element (register `e`)
   - Go to line with `<name>`
   - `qe^r"f>s": "<ESC>f<C"<ESC>q`
3. Macro to format a person
   - Go to line with `<person>`
   - `qpS{<ESC>j@eA,<ESC>j@ejS},<ESC>q`
4. Macro to format a person and go to the next person
   - Go to line with `<person>`
   - `qq@pjq`
5. Execute macro until end of file
   - `999@q`
6. Manually remove last `,` and add `[` and `]` delimiters

The solution above is provided by the official course site.