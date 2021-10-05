# Regex

- [Full regex syntax](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)
- [IHateRegex - Also shows the finite state automaton for the regex](https://ihateregex.io/expr/ip/)
- [Regex tester](https://regex101.com/)
- [Regexr](https://regexr.com)
- [regular-expression.info](https://regular-expression.info)

# Examples

Syntax used is - `s/regextomatch/regextoreplace/`

- Match strings of even length - `^\w{2}+$`
- Match strings of odd length - `^\w{2}*\w$`
- Match strings of length k mod n - `^\w{n}*\w{k}`
- Replace trailing `a`s - `s/(\w+?)a*$/\1/` - an additional `?` is necessary after the `\w+` to make the query "non-greedy", otherwise it would match the LARGEST substring of `\w?`
- Palindrome of length 4 - `s/(\w)(\w)(\w)(\w)\4\3\2\1`
- Palindrome of arbitrarily large length - Impossible without lookbacks, see pumping lemma for finite state automatons - [idc621](https://sejdm.github.io/idc621)
- Email id - `s/^([[:alnum:]]|\.)*@[[:alpha:]]+?(\.[[:alpha:]]+)+$`
    - `([[:alnum:]]|\.|_)+` matches alphanum or `.` or `_` 1 or more times
        - `[[:alnum:]]` matches all alpha and num
        - `|` is OR
    - `[[:alpha:]]+?` matches only alphabet 1 or more times, but non-greedily
    - `(\.[[:alpha:]]*)` matches `.` followed by alphabets 1 or more times
- IP adresses - 
- dates
- Proper nouns
- citations

# My examples

- Get all headings from a markdown file
- Get the link from all links from a markdown file
- Get the different parts of a [gemini](https://gemini.circumlunar.space/docs/gemtext.gmi) file
- Odd/Even binary integers
- Choose any 2 of the above examples(each of them constitute a "language"), and match strings of BOTH examples (languages). This is called a Union
- From the previous example, show that ANY finite set of strings definitely has a finite regex which matches it
- From the previous example, show that ANY finite UNIONs of finite languages has a finite regex which matches it
- From the previous example, show that ANY finite UNION of languages which have a regex has a finite regex which matches it
- From this, prove that the set of all palindromes of length less than any finite n has a regex
- Given that computers have only finite memory, all evaluate-able programs must have a regex
- Try to define a regex for a valid mathematical expression made of +, -, *, / and digits
- Try to define a regex for a valid mathematical expression made of +, -, *, /, digits and parentheses

## Regex Flags

These extra options basically modify the behaviour of the regex parser. Naturally, the associated FSA will generally be different.

- `s` - dotall. `.` also matches `\n`
- `g` - global. continue looking after the first match
- `m` - multiline. For a set of lines, consider `^/$` to match the start/end of each line, not as a single block of text
- `i` - case insensitive search

