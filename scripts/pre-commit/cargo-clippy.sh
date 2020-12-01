#!/usr/bin/env bash

# Meant to be ran from pre-commit -- assumes it is ran from the root of the repo

set -e

cd riir
cargo clippy -- -D warnings
