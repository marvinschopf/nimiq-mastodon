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


def format_hashrate(hashrate):
    if hashrate >= 1000 and hashrate < 1000000:
        return "{:,.2f} kH/s".format(hashrate / 1000)
    elif hashrate >= 1000000 and hashrate < 1000000000:
        return "{:,.2f} MH/s".format(hashrate / 1000000)
    elif hashrate >= 1000000000:
        return "{:,.2f} GH/s".format(hashrate / 1000000000)
    else:
        return "{:,.2f} H/s".format(hashrate)
