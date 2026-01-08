# SDN LAB 

Environment: Ubuntu / Linux VM  
Tools: Mininet, RYU Controller, Open vSwitch, Wireshark  
Python Version: Python 3  

---


# SYSTEM PREREQUISITES (VERIFY ONCE)

```bash
python3 --version
mn --version
ovs-vsctl --version
ryu-manager --version
```

If Mininet was used earlier:
```bash
sudo mn -c
```

---

# TERMINAL USAGE CONVENTION (MANDATORY)

Throughout this lab, **multiple terminals are required**.

| Terminal | Purpose |
|--------|--------|
| Terminal 1 | RYU Controller |
| Terminal 2 | Mininet |
| Terminal 3 | REST API / Scripts |
| Terminal 4 | Wireshark / Packet Observation |

---

# =========================================================
# TASK 1: TOPOLOGY DISCOVERY USING RYU
# =========================================================

## OBJECTIVE
Discover switches and links dynamically using RYU’s topology discovery mechanism.

---

## FILE USED
`topo_learner.py`

---

## SOURCE CODE: topo_learner.py

```python
from ryu.base import app_manager
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.topology import event, switches
from ryu.topology.api import get_switch, get_link

class TopoLearner(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    _CONTEXTS = {
        'topology_api_app': switches.Switches,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.topology_api_app = kwargs['topology_api_app']

    @set_ev_cls(event.EventSwitchEnter)
    def get_topology_data(self, ev):
        switch_list = get_switch(self.topology_api_app, None)
        link_list = get_link(self.topology_api_app, None)

        print("Switches:", [sw.dp.id for sw in switch_list])
        print("Links:", [(lnk.src.dpid, lnk.dst.dpid) for lnk in link_list])
```

---

## TERMINAL 1 – START RYU

```bash
cd ~/ryu/ryu/app
ryu-manager topo_learner.py --observe-links
```

Explanation:
- `--observe-links` enables LLDP
- Controller listens on port 6653

---

## TERMINAL 2 – START MININET

```bash
sudo mn --topo tree,depth=2,fanout=2 --controller=remote
```

---

## OPTIONAL MININET COMMANDS

```bash
mininet> net
mininet> dump
mininet> pingall
```

---

## EXPECTED OUTPUT (TERMINAL 1)

```
Switches: [1, 2, 3, 4]
Links: [(1,2), (2,1), (2,3), (3,2), ...]
```

---

## CLEANUP

```bash
sudo mn -c
```

---

# =========================================================
# TASK 2: REST API FOR RYU (FLOW PROGRAMMING)
# =========================================================

## OBJECTIVE
Install OpenFlow rules using RYU REST APIs.

---

## TERMINAL 1 – START RYU WITH REST

```bash
ryu-manager ryu.app.ofctl_rest ryu.app.simple_switch_rest_13
```

---

## TERMINAL 2 – START MININET

```bash
sudo mn --mac --switch ovsk --controller remote --arp
```

---

## TERMINAL 2 – COLLECT TOPOLOGY INFO

```bash
mininet> sh ovs-ofctl show s1
mininet> h1 ifconfig
mininet> h2 ifconfig
```

---

## TERMINAL 3 – ADD FLOW USING REST

```bash
curl -X POST -d '{
  "dpid": 1,
  "priority": 123,
  "match": {
    "in_port": 1,
    "eth_src": "00:00:00:00:00:01",
    "eth_dst": "00:00:00:00:00:02"
  },
  "actions": [
    { "type": "OUTPUT", "port": 2 }
  ]
}' http://localhost:8080/stats/flowentry/add
```

---

## VERIFY FLOW INSTALLATION

```bash
sudo ovs-ofctl dump-flows s1
```

---

## TEST CONNECTIVITY

```bash
mininet> h1 ping h2 -c 5
```

---

## WIRESHARK OBSERVATION (CONTROL PLANE)

### TERMINAL 4

```bash
sudo wireshark -i lo -k
```

Wireshark display filter (inside GUI):
```
openflow
```

Observe:
- OFPT_HELLO
- OFPT_PACKET_IN
- OFPT_FLOW_MOD

---

## CLEANUP

```bash
sudo mn -c
```

---

# =========================================================
# TASK 3: CUSTOM TOPOLOGY USING PYTHON (HIGH-LEVEL API)
# =========================================================

## OBJECTIVE
Create a reusable topology using the Topo class.

---

## FILE: myfirsttopo.py

```python
from mininet.topo import Topo

class MyFirstTopo(Topo):
    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h3)
        self.addLink(s2, h4)

topos = {'myfirsttopo': (lambda: MyFirstTopo())}
```

---

## RUN CUSTOM TOPOLOGY

```bash
sudo mn --custom myfirsttopo.py --topo myfirsttopo
```

---

## VERIFY

```bash
mininet> net
mininet> pingall
```

---

## AUTOMATED TEST

```bash
sudo mn --custom myfirsttopo.py --topo myfirsttopo --test pingall
```

---

## CLEANUP

```bash
sudo mn -c
```

---

# =========================================================
# TASK 4: MININET PYTHON CLASSES (LOW-LEVEL API)
# =========================================================

## OBJECTIVE
Manually create network using low-level Mininet classes.

---

## FILE: myfirsttopo_lowlevel.py

```python
#!/usr/bin/python3
from mininet.node import Host, OVSSwitch, RemoteController
from mininet.link import Link
from mininet.log import setLogLevel
import time

setLogLevel('info')

h1 = Host('h1')
h2 = Host('h2')
h3 = Host('h3')
h4 = Host('h4')

s1 = OVSSwitch('s1', inNamespace=False)
s2 = OVSSwitch('s2', inNamespace=False)

c0 = RemoteController('c0', ip='127.0.0.1', port=6653)

Link(h1, s1)
Link(h2, s1)
Link(s1, s2)
Link(s2, h3)
Link(s2, h4)

h1.setIP('10.0.0.1/24')
h2.setIP('10.0.0.2/24')
h3.setIP('10.0.0.3/24')
h4.setIP('10.0.0.4/24')

c0.start()
s1.start([c0])
s2.start([c0])

time.sleep(2)

print(h1.IP())
print(h2.IP())
print(h3.IP())
print(h4.IP())

print("Pinging...")
print(h1.cmd('ping -c 3 10.0.0.2'))
print(h1.cmd('ping -c 3 10.0.0.3'))

s1.stop()
s2.stop()
c0.stop()
```

---

## TERMINAL 1 – START RYU

```bash
ryu-manager ryu.app.simple_switch_13
```

---

## TERMINAL 2 – RUN SCRIPT

```bash
sudo python3 myfirsttopo_lowlevel.py
```

---

## FINAL CLEANUP (MANDATORY)

```bash
sudo mn -c
```

---

# COMMON ERRORS & FIXES

| Error | Fix |
|-----|----|
| ovs-controller not found | Use RemoteController |
| Port 6653 busy | Stop other RYU instances |
| python not found | Use python3 |
| Wireshark not opening | Ensure GUI / use Windows Wireshark |

---

# FINAL SUMMARY

- Topology discovery via LLDP
- Flow programming via REST APIs
- Custom topology using Topo class
- Manual network creation using low-level API
- Control plane vs data plane observed using Wireshark

---


