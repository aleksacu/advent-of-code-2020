#!/usr/bin/env bash

# Meant to be ran from the root of the repo

set -eou pipefail

mkdir "day$1"

cd riir

mkdir "day$1"

cat <<EOF > "day$1/main.rs"
fn main() {
    let input = include_str!("./input.txt").lines().collect::<Vec<&str>>();
}
EOF

cat <<EOF >> Cargo.toml

[[bin]]
name = "day$1"
path = "day$1/main.rs"
EOF
