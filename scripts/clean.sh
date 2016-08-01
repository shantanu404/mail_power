#!/usr/bin/env bash

# remove all pycache
find . | grep -E "(__pycache__$)" | xargs rm -rf

# remove all read emails
python3 ./scripts/delete_mails.py
