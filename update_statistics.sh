#!/usr/bin/env bash
cd /opt/nimiq-mastodon/bot
source venv/bin/activate
python3 app/update_statistics.py
deactivate