#!/bin/bash
# archive_expenses.sh
# Lab 3 
# Archives expense files into an "archives" directory and logs operations.

ARCHIVE_DIR="archives"
LOG_FILE="archive_log.txt"

# 1. Ensure archive directory exists
if [ ! -d "$ARCHIVE_DIR" ]; then
  mkdir "$ARCHIVE_DIR"
fi

# --------------------------------
# Usage:
# ./archive_expenses.sh YYYY-MM-DD   -> Archive file for that date
# ./archive_expenses.sh search YYYY-MM-DD -> Search archived file
# -------------------------------

# Archive mode
if [ $# -eq 1 ]; then
  FILE="expenses_$1.txt"
  if [ -f "$FILE" ]; then
    mv "$FILE" "$ARCHIVE_DIR/"
    echo "$(date '+%Y-%m-%d %H:%M:%S') Archived $FILE" >> "$LOG_FILE"
    echo "Archived $FILE successfully."
  else
    echo "Expense file for $1 not found."
  fi
fi

# Search mode
if [ $# -eq 2 ] && [ "$1" == "search" ]; then
  FILE="$ARCHIVE_DIR/expenses_$2.txt"
  if [ -f "$FILE" ]; then
    echo "Showing archived expenses for $2:"
    cat "$FILE"
  else
    echo "No archived file for $2"
  fi
fi
