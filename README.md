# sonybraviacontrol
Basic control for turning on a Sony Bravia TV and changing HDMI

## Requires
* Linux
* Python 2.7
* arp installed (normally installed by default)
* curl
* pip
* wakeonlan python module
* Sony Bravia Smart TV
* Device on same network at TV
* TV's MAC address (can be found in tv settings or checking your router)

## Installation
* `git clone https://github.com/Charliedean/sonybraviacontrol.git `
* `pip install wakeonlan`
* Edit tvwake.py with your TV MAC address and hdmi choice
* python ./tvwake.py
