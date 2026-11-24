# One-Star Review of Something Essential

[![make.fun bounty](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/imusic-487/one-star-review-gravity/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/imusic-487/one-star-review-gravity/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

Entry for the [make.fun bounty "One-Star Review of Something Essential"](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629).

## The review

> One star. Gravity has never caught a single thing I have dropped. It just makes sure it lands screen-down.

106 characters, one line. A deadpan complaint filed in earnest against an
everyday essential: gravity has a perfect record of never catching anything,
and its one reliable feature is making sure whatever you drop lands
screen-down. The sting arrives in the last two words.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the review
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: UTF-8, 1–160 characters, a
single line, not only whitespace. The output is deterministic — every run
writes the exact same bytes, and the copy is verified byte for byte.
