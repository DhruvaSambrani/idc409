# Regex

- [Full regex syntax](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)
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

