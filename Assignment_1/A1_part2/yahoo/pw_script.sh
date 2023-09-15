#! /bin/bash

# select first 100 user entries and output to temp file original_lines.txt
tail -n 453509 password.file | head -n 100 > original_lines.txt
# isolate plain text passwords and output to temp file pws.txt
cut -d ':' -f3 original_lines.txt > pws.txt
# paste files together, remove \r to avoid extra newlines
paste -d ' ' original_lines.txt pws.txt | tr -d '\r' > yahoo_submission.txt
# remove temp files
rm original_lines.txt pws.txt
