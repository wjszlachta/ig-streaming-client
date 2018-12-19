# IG streaming API client

Small Python library to connect to [IG](https://www.ig.com/) streaming API (more information and API reference is available on [IG Labs](https://labs.ig.com/) website).

## Installation

To use most recent release:

```bash
pip install ig-streaming-client
```

To use current master branch:

```bash
pip install git+https://github.com/wjszlachta/ig-streaming-client.git
```

## Usage

For demo account:

```python
import time

from ig_streaming_client import IgStreamingSession
from lightstreamer_client import LightstreamerSubscription

api_key = '...'
account_id = '...'
rest_api_username = '...'
rest_api_password = '...'

session = IgStreamingSession(api_key, account_id, rest_api_username, rest_api_password)

subscription = LightstreamerSubscription('MERGE',
                                         ['MARKET:CS.D.BITCOIN.TODAY.IP'],
                                         ['UPDATE_TIME', 'BID', 'OFFER'])
subscription.addlistener(lambda item: print(item))
session.subscribe(subscription)

time.sleep(30)

session.log_out()
```

For live account:

```python
import time

from ig_rest_client import IG_REST_TRADING_API_LIVE_URL
from ig_streaming_client import IgStreamingSession
from lightstreamer_client import LightstreamerSubscription

api_key = '...'
account_id = '...'
rest_api_username = '...'
rest_api_password = '...'

session = IgStreamingSession(api_key, account_id, rest_api_username, rest_api_password, rest_api_url=IG_REST_TRADING_API_LIVE_URL)

subscription = LightstreamerSubscription('MERGE',
                                         ['MARKET:CS.D.BITCOIN.TODAY.IP'],
                                         ['UPDATE_TIME', 'BID', 'OFFER'])
subscription.addlistener(lambda item: print(item))
session.subscribe(subscription)

time.sleep(30)

session.log_out()
```
