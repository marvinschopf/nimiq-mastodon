import requests


def quickstats():
    return requests.get("https://nimiq.mopsus.com/api/quick-stats").json()
