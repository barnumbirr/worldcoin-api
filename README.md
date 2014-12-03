<h1><img src="https://raw.github.com/c0ding/worldcoin-api/master/doc/worldcoin.png" height=55 alt="worldcoin" title="worldcoin"> worldcoin-api</h1>

[![PyPi Version](http://img.shields.io/pypi/v/worldcoin.svg)](https://pypi.python.org/pypi/worldcoin/)   [![Downloads](http://img.shields.io/pypi/dm/worldcoin.svg)](https://pypi.python.org/pypi/worldcoin/)

worldcoin is an APACHE licensed library written in Python designed to provide a simple to use API for the Worldcoin cryptocurrency.

## More about Worldcoin:

WorldCoin is designed to be the digital currency of the future. At the forefront is it's' blazing fast speed. Your transaction will be fully confirmed in about 60 seconds or less.

The major goal is to become the cryptocurrency of choice for merchants and consumers for their everyday transaction, whether it be a cup of coffee or a bigger ticket item. Speed and security makes all of this possible. Blazing fast speeds make WorldCoin the best way to pay for everyday transactions. Transactions are fully confirmed in about 60 seconds. Transfer money to your friends and family instantly with just a few clicks. WorldCoin is also based on sound money principals which makes it the smart choice for wealth preservation. It is designed to appreciate in value over time, unlike paper currency. This is due to the fact that only 265 million coins will ever be produced. These advantages are what makes Worldcoin the leading choice for users.

## Installation:

From source use

    $ python setup.py install

or install from PyPi

    $ pip install worldcoin

## API Documentation:

This API can currently retrieve the following stats from [worldcoinexplorer.com](http://www.worldcoinexplorer.com/) and [CryptoCoin](http://www.cryptocoincharts.info):

### Network:

  - Difficulty:

```
>>> import worldcoin
>>> worldcoin.get_difficulty()
19.12163587
```

  - Hashrate:

```
>>> worldcoin.get_hashrate()
1643421348
```

  - Block count:

```
>>> worldcoin.block_count()
1205465
```

  - Total coins:

```
>>> worldcoin.total_coins()
52455474.3611
```

  - Block reward:

```
>>> worldcoin.reward()
46.86741576
```

### Blocks:

  - Block hash:
    [PARAMETER] is optional, should be a block hash or height.
    [DEFAULT] equals to last block.

```
>>> worldcoin.block_hash(PARAMETER)
{
    "PreviousBlock": "", 
    "Hash": "1a48c2bf97e0df6d4f03cd5cb0896ef43b04987048fbeb5ab2dc013335e40731", 
    "Transactions": [
        "0fc36e386282295512aa63d9f5047d9dc305c983394803474cfaa2f99d7e1bd0"
    ], 
    "NextBlock": "b439caa3baf7e8f6532783ef630ff18293f237da42d3cc8975620d3e3ca96bb3", 
    "Height": 1, 
    "Time": 1368504801
}
```

### Transactions:

  - Transaction:
    [PARAMETER] is required and should be a transaction hash.

```
>>> worldcoin.transaction(PARAMETER)
{
    "Inputs": [], 
    "Hash": "0fc36e386282295512aa63d9f5047d9dc305c983394803474cfaa2f99d7e1bd0", 
    "Outputs": [
        {
            "Index": 0, 
            "Amount": 32.0, 
            "Address": "WYJ142WhSViiCJuUB2JbpbNiCFAuk9B47z"
        }
    ], 
    "Block": "1a48c2bf97e0df6d4f03cd5cb0896ef43b04987048fbeb5ab2dc013335e40731", 
    "Time": 1368504801
}
```

### Addresses:

  - Address:
    [PARAMETER] is required and should be an address hash.

```
>>> worldcoin.address(PARAMETER)
{
    "RichListRank": 45011, 
    "TotalSent": 32.0, 
    "Balance": 0.0, 
    "Hash": "WYJ142WhSViiCJuUB2JbpbNiCFAuk9B47z", 
    "TotalReceived": 32.0
}
```

  - Address/private key generation :

```
>>> worldcoin.generate_address()
{
    "address": "WmZs8FY7TWpqhNM917zYVLV2QM5RFpvdTC", 
    "private_key": "WsSBJ5tfLcoNbNKy8Y1NoQWisub4gDz13DEa8h4ppV6VVWHn28Gx" 
}
```

### Exchanges:

  - BTC:

```
>>> worldcoin.to_btc()
{
    "latest_trade": "2014-04-18 11:23:30", 
    "volume_btc": "58.24", 
    "price": "0.00009061", 
    "price_before_24h": "0.00008404", 
    "volume_first": "624421.07441386", 
    "best_market": "cryptsy", 
    "volume_second": "58.2372003281511", 
    "id": "wdc/btc"
}
```

  - LTC:

```
>>> worldcoin.to_ltc()
{
    "latest_trade": "2014-04-22 21:18:55", 
    "volume_btc": "2.13", 
    "price": "0.00335412", 
    "price_before_24h": "0.00340005", 
    "volume_first": "25139.6915261745", 
    "best_market": "cryptsy", 
    "volume_second": "84.9153636898845", 
    "id": "wdc/ltc"
}
```

  - USD:

```
>>> worldcoin.to_usd()
{
    "latest_trade": "2014-04-18 14:41:33", 
    "volume_btc": "0.04", 
    "price": "0.05500000", 
    "price_before_24h": "0.05799300", 
    "volume_first": "391.214920043945", 
    "best_market": "crypto-trade", 
    "volume_second": "21.4769533276558", 
    "id": "wdc/usd"
}
```

## License:

```
  Apache v2.0 License
  Copyright 2014 Martin Simon

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## Useful links:

* [Worldcoin Alliance](http://www.worldcoinalliance.net/)
* [Worldcoin Forum](http://worldcoinforum.org/)
* [Worldcoin Wiki](http://www.wdcwiki.org/wiki/Main_Page)
* [worldcoinexplorer.com](http://www.worldcoinexplorer.com/)

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
