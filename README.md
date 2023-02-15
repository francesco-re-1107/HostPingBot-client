# HostPingBot-client
 
This is a simple client for **Push** watchdogs in [HostPingBot](https://github.com/francesco-re-1107/HostPingBot) Telegram bot.

## Run with Docker
 
```bash
docker pull hostpingbotclient

docker run -d --restart unless-stopped \
 -e TOKEN=your_token \
 -e INTERVAL=60 \
 -e TIMEOUT=10 \
 -e RETRY_AFTER=10 \
 --name hpb-client \
 hostpingbotclient
```

## Parameters

| Parameter | Function | Default |
| --- | --- | :---: |
| TOKEN | Given from the bot, must be a UUID | (mandatory) |
| INTERVAL | Interval in seconds between two requests | 60 |
| TIMEOUT | Timeout in seconds to wait for a response | 10 |
| RETRY_AFTER | Time in seconds to wait before retrying (if failed) | 10 |

