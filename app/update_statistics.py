import client
import mopsus
import nimiqx
import format_hashrate

if __name__ == "__main__":
    formatted_price_usd = "{:,} USD".format(nimiqx.price("USD"))
    formatted_price_eur = "{:,} EUR".format(nimiqx.price("EUR"))
    mopsus_stats = mopsus.quickstats()
    client.mastodon.status_post(
        "Price: {price_usd} | {price_eur}\nGlobal hashrate: {hashrate}\nCurrent supply: {current_supply}\nBlock reward: {block_reward}".format(
            price_usd=formatted_price_usd,
            price_eur=formatted_price_eur,
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
