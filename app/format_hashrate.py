def format_hashrate(hashrate):
    if hashrate >= 1000 and hashrate < 1000000:
        return "{:,.2f} KH/s".format(hashrate / 1000)
    elif hashrate >= 1000000 and hashrate < 1000000000:
        return "{:,.2f} MH/s".format(hashrate / 1000000)
    elif hashrate >= 1000000000:
        return "{:,.2f} GH/s".format(hashrate / 1000000000)
    else:
        return "{:,.2f} H/s".format(hashrate)
