# advent-of-code-2020

[![license](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](.pre-commit-config.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/aleksacu/advent-of-code-2020/main.svg)](https://results.pre-commit.ci/latest/github/aleksacu/advent-of-code-2020/main)

Solutions to advent of code puzzles in various programming languages

Main solutions are mostly going to be written in go, but sometimes in other languages
as well. All the solutions are going to be rewritten in rust (`riir` directory).

At least some of the solutions are hopefully going to be streamed live on [aleksacu](https://twitch.tv/aleksacu)
twitch channel

## Stages of Advent of Code

![aoc-stages](aoc-stages.png)

I reached stage 2 on day 3. Hopefully I don't reach stage 3.

## Getting started

In some cases you need to change directory, either because of the input path or
because the compiler requires it.

### Go

```shell script
cd day01
go run main.go
```

### Rust

```shell script
cd riir
cargo run --bin day01
```

### Python

```shell script
python day03/main.py
```

## Solutions

| Day                                        | Languages                                           |
| ------------------------------------------ | --------------------------------------------------- |
| [1](https://adventofcode.com/2020/day/1)   | [go](day01/main.go), [rust](riir/day01/main.rs)     |
| [2](https://adventofcode.com/2020/day/2)   | [go](day02/main.go), [rust](riir/day02/main.rs)     |
| [3](https://adventofcode.com/2020/day/3)   | [python](day03/main.py), [rust](riir/day03/main.rs) |
| [4](https://adventofcode.com/2020/day/4)   | [python](day04/main.py), [rust](riir/day04/main.rs) |
| [5](https://adventofcode.com/2020/day/5)   | [python](day05/main.py), [rust](riir/day05/main.rs) |
| [6](https://adventofcode.com/2020/day/6)   | [python](day06/main.py), [rust](riir/day06/main.rs) |
| [7](https://adventofcode.com/2020/day/7)   | [python](day07/main.py)                             |
| [8](https://adventofcode.com/2020/day/8)   | [python](day08/main.py)                             |
| [9](https://adventofcode.com/2020/day/9)   | [python](day09/main.py)                             |
| [10](https://adventofcode.com/2020/day/10) | [python](day10/main.py)                             |
