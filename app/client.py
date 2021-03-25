import os
from dotenv import load_dotenv

load_dotenv()

from mastodon import Mastodon

mastodon = Mastodon(
    access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
    api_base_url=os.getenv("MASTODON_API_BASE_URL"),
)
