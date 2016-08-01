#!/usr/bin/env bash

# remove all pycache
rm -rf __pycache__
rm -rf ./*/__pycache__

# remove all read emails
python3 ./scripts/delete_mails.py
