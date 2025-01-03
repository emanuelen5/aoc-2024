#!/usr/bin/env bash

set -x
force=false

while getopts "f" flag; do
    case "$flag" in
    f)
        force=true
        ;;
    *)
        echo "Unknown flag $OPTARG" >&2
        exit 1
        ;;
    esac
done

# Shift parsed options to access positional arguments
shift $((OPTIND - 1))

day=$1

branch="day/$day"
if ! git branch "$branch" && ! $force; then
    echo "Branch '$branch' does already exist. Clean up first and delete it to be able to initialize" >&2
    exit 1
fi
git checkout "$branch"

dir="day$day"
if [ -d "$dir" ] && ! $force; then
    echo "Directory '$dir' already created" >&2
    exit 1
elif ! [ -d "$dir" ]; then
    cp -r template/ "$dir"
    mv "$dir/test.py" "$dir/test_day$day.py"
fi

if which code; then
    code "$dir/data/input.txt" "$dir/data/test_input.txt"
fi

function trim_trailing_newlines() {
    awk '/./ { last = $0; print last } END { if (length(last)) print last }'
}

echo "Paste test content (Ctrl+D to finish):"
cat | trim_trailing_newlines >"$dir/data/test_input.txt"

year=2024
if which aocd; then
    aocd "$year" "$day" >"$dir/data/input.txt"
else
    echo "Paste real content (Ctrl+D to finish):"
    cat | trim_trailing_newlines >"$dir/data/input.txt"
fi

git add "$dir"
git commit -m "Create $dir from template"
