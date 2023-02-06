#!/bin/bash

tar -czvf submissions/submission.tar.gz \
--exclude="*.gz" \
--exclude="*.ipynb" \
--exclude="*.sh" \
--exclude="*.log" \
--exclude=".ipynb_checkpoints" \
--exclude="__pycache__" \
--exclude="replays" \
--exclude="errorlogs" \
--exclude="img" \
--exclude="submissions" \
*