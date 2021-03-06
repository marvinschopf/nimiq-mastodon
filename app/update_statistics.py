#!/usr/bin/env python3
"""
nimiq-mastodon
Copyright (C) 2021 Marvin Schopf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import client
import mopsus
import nimiqx
import format_hashrate
import currencies

if __name__ == "__main__":
    mopsus_stats = mopsus.quickstats()
    client.mastodon.status_post(
        "Price: {price_usd} | {price_eur}\nGlobal hashrate: {hashrate}\nCurrent supply: {current_supply}\nBlock reward: {block_reward}".format(
            price_usd=currencies.Currency("USD").get_money_with_currency_format(
                nimiqx.price("USD")
            ),
            price_eur=currencies.Currency("EUR").get_money_with_currency_format(
                nimiqx.price("EUR")
            ),
            hashrate=format_hashrate.format_hashrate(
                mopsus_stats["estimated_global_hashrate"]
            ),
            current_supply=str(mopsus_stats["current_supply"]),
            block_reward=str(mopsus_stats["block_reward"]),
        )
        + "\n\n#nimiq #crypto #cryptocurrency #coin",
        visibility="unlisted",
    )
    print("Statistics tooted")
