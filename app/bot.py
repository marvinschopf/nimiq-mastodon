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
import time
import html2text
import nimiqx
import currencies
from padatious import IntentContainer

h = html2text.HTML2Text()
h.ignore_links = True

container = IntentContainer("intent_cache")

container.add_intent("price_currency", ["price {currency}", "price in {currency}"])

if __name__ == "__main__":
    print("Bot started")
    while True:
        print("Check started...")
        notifications = client.mastodon.notifications()
        client.mastodon.notifications_clear()
        for notification in notifications:
            if notification.type == "mention":
                message = (
                    h.handle(notification.status.content)
                    .replace("@nimiq ", "")
                    .replace("@ nimiq ", "")
                )
                intent = container.calc_intent(message)
                if intent.conf > 0.85:
                    if intent.name == "price_currency":
                        if intent.matches and intent.matches["currency"]:
                            currency = intent.matches["currency"]
                            continueWith = True
                            try:
                                currencies.Currency(currency.upper())
                            except currencies.exceptions.CurrencyDoesNotExist:
                                continueWith = False
                                print("Unknown currency...")
                            if continueWith:
                                price = nimiqx.price(currency=currency.upper())
                                print("Okay, replying...")
                                client.mastodon.status_post(
                                    "@{reply_to} {price}".format(
                                        reply_to=notification.account.username,
                                        price=currencies.Currency(
                                            currency.upper()
                                        ).get_money_with_currency_format(price),
                                    ),
                                    in_reply_to_id=notification.status.id,
                                    visibility="unlisted",
                                )
                                print("Reply sent.")
                        else:
                            print("Currency not found in intent...")
                    else:
                        print("Unsure about intent...")
                else:
                    print("Confidence not high enough...")
            else:
                print("Notification is no mention, skipping...")
        time.sleep(5)
