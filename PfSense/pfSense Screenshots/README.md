# pfSense Lab Practice - Comprehensive Step-by-Step Guide

[cite_start]This document details the configuration steps required to complete the pfSense Hands-On Assessment[cite: 1].

---

## LAB 1: Networking & Interface Configuration
[cite_start]**Goal:** Standardize interface naming, configure internal networks, and manage interface behavior [cite: 16-19].

### [cite_start]Task 1: Identify Interfaces [cite: 21]
* **Navigate to:** `Interfaces` > `Assignments`.
* **Action:** Observe the list of physical network ports (e.g., `em0`, `em1`, `vtnet0`).
* **Verification:** Note which port corresponds to WAN and which to LAN.

### [cite_start]Task 2: Configure LAN IP [cite: 22]
* **Navigate to:** `Interfaces` > `LAN`.
* **Action:**
    1.  Set **IPv4 Configuration Type** to `Static IPv4`.
    2.  Scroll to **Static IPv4 Configuration**.
    3.  **IP Address:** Enter a private IP (e.g., `192.168.50.1`).
    4.  **Subnet Mask:** Select `/24`.
    5.  Click `Save` and `Apply Changes`.

### [cite_start]Task 3: Rename Interfaces [cite: 23]
* **Navigate to:** `Interfaces` > `LAN` (or WAN/OPT1).
* **Action:**
    1.  In the **Description** field, enter a meaningful name (e.g., `LAN-Core` or `WAN-Uplink`).
    2.  Click `Save`.
    3.  Repeat for all active interfaces.

### [cite_start]Task 4: Reboot and Confirm [cite: 24]
* **Navigate to:** `Diagnostics` > `Reboot`.
* **Action:** Click `Submit` to restart the system.
* **Verification:** Log back in and check `Status` > `Dashboard` to confirm names and IPs persisted.

### [cite_start]Task 5: Modify MTU [cite: 25]
* **Navigate to:** `Interfaces` > `[Interface Name]`.
* **Action:**
    1.  Locate the **MTU** (Maximum Transmission Unit) field.
    2.  Set value to `1400`.
    3.  Click `Save` and `Apply Changes`.
* **Observation:** Note if the interface resets or if connectivity drops briefly.

### [cite_start]Task 6: Disable Interface [cite: 28]
* **Navigate to:** `Interfaces` > `[Unused Interface]`.
* **Action:** Uncheck the **Enable Interface** box at the top. Click `Save`.
* **Observation:** Go to Dashboard; the interface status should show as down/gray.

---

## LAB 2: Firewall Rule Logic & Policy Enforcement
[cite_start]**Goal:** Enforce selective permissions and visibility for troubleshooting [cite: 31-33].

### [cite_start]Task 1: Permit Specific Host [cite: 35]
* **Navigate to:** `Firewall` > `Rules` > `LAN`.
* **Action:**
    1.  Click **Add** (Up Arrow).
    2.  **Action:** `Pass`.
    3.  **Source:** `Single Host or Alias` -> `192.168.50.10` (Target Client IP).
    4.  **Description:** "Allow Specific Host".
    5.  Click `Save` & `Apply Changes`.

### [cite_start]Task 2: Block ICMP [cite: 36]
* **Navigate to:** `Firewall` > `Rules` > `LAN`.
* **Action:**
    1.  Click **Add** (Up Arrow) to place at the **top**.
    2.  **Action:** `Block`.
    3.  **Protocol:** `ICMP`.
    4.  **Source:** `LAN net`.
    5.  **Description:** "Block ICMP".
    6.  Click `Save` & `Apply Changes`.

### [cite_start]Task 3: Time-Based Rule [cite: 37]
* **Step 1:** Go to `Firewall` > `Schedules`. Click `Add`.
    * **Name:** `WorkHours`. Select range (e.g., 09:00 - 17:00). Click `Save`.
* **Step 2:** Go to `Firewall` > `Rules` > `LAN`. Click `Add`.
    * **Action:** `Pass`.
    * **Source:** `LAN net`.
    * **Advanced Options:** Scroll to **Schedule**, select `WorkHours`.
    * Click `Save`.

### [cite_start]Task 4: Enable Logging [cite: 38]
* **Navigate to:** `Firewall` > `Rules` > `LAN`.
* **Action:** Edit the **Block ICMP** rule (from Task 2).
    1.  Check box: **"Log packets that are handled by this rule"**.
    2.  Click `Save` & `Apply Changes`.
* **Verification:** Check `Status` > `System Logs` > `Firewall`.

### [cite_start]Task 5: Capture Rule Match [cite: 39]
* **Navigate to:** `Status` > `System Logs` > `Firewall`.
* **Action:**
    1.  Generate blocked traffic (Ping pfSense from client).
    2.  Locate the red `X` entry in logs.
    3.  Click the entry to view which rule ID triggered the block.

---

## LAB 3: NAT & Port Forwarding
[cite_start]**Goal:** Configure outbound NAT and port forwarding for hosted applications [cite: 44-46].

### [cite_start]Task 1: Identify NAT Mode [cite: 48]
* **Navigate to:** `Firewall` > `NAT` > `Outbound`.
* **Action:** Observe current mode (Automatic/Hybrid/Manual).

### [cite_start]Task 2: Outbound NAT [cite: 49]
* **Navigate to:** `Firewall` > `NAT` > `Outbound`.
* **Action:**
    1.  Select **Hybrid Outbound NAT**. Click `Save`.
    2.  Click **Add**.
    3.  **Interface:** `WAN`.
    4.  **Source:** `Network` -> `10.0.0.0/24` (Custom Subnet).
    5.  **Translation:** `Interface Address`.
    6.  Click `Save`.

### [cite_start]Task 3: Port Forwarding [cite: 50]
* **Navigate to:** `Firewall` > `NAT` > `Port Forward`.
* **Action:**
    1.  Click **Add**.
    2.  **Interface:** `WAN`.
    3.  **Dest. Port Range:** `8080`.
    4.  **Redirect Target IP:** `192.168.50.5` (Internal Server).
    5.  **Redirect Target Port:** `80`.
    6.  Click `Save` & `Apply Changes`.

### [cite_start]Task 4: Disable NAT Reflection [cite: 52]
* **Navigate to:** Edit the Port Forward rule from Task 3.
* **Action:**
    1.  Scroll to **NAT Reflection**.
    2.  Select **Disable**.
    3.  Click `Save`.

### [cite_start]Task 5: Observe NAT States [cite: 54]
* **Navigate to:** `Diagnostics` > `States`.
* **Action:** Filter by port `8080` or the target IP to see active translation entries.

---

## LAB 4: DHCP Server & Client Policy
[cite_start]**Goal:** Automate addressing and enforce device control [cite: 61-64].

### [cite_start]Task 1: Enable DHCP [cite: 66]
* **Navigate to:** `Services` > `DHCP Server` > `LAN`.
* **Action:**
    1.  Check **Enable**.
    2.  **Range:** `192.168.50.100` to `192.168.50.200`.
    3.  Click `Save`.

### [cite_start]Task 2: Static Mapping [cite: 67]
* **Navigate to:** `Services` > `DHCP Server` > `LAN` (bottom of page).
* **Action:**
    1.  Click **Add**.
    2.  **MAC Address:** Enter client MAC (e.g., `aa:bb:cc:dd:ee:ff`).
    3.  **IP Address:** `192.168.50.50`.
    4.  Click `Save`.

### [cite_start]Task 3: Custom DNS [cite: 68]
* **Navigate to:** `Services` > `DHCP Server` > `LAN`.
* **Action:**
    1.  **DNS Servers:** Enter `8.8.8.8` and `1.1.1.1`.
    2.  Click `Save`.

### [cite_start]Task 4: Block Unknown Devices [cite: 69]
* **Navigate to:** `Services` > `DHCP Server` > `LAN`.
* **Action:**
    1.  Check **"Deny unknown clients"**.
    2.  Click `Save`.

### [cite_start]Task 5: Locate Leases [cite: 70]
* **Navigate to:** `Status` > `DHCP Leases`.
* **Action:** View table for Hostname, MAC, and IP status.

---

## LAB 5: DNS Resolver & DNS Control
[cite_start]**Goal:** Centralize DNS handling and restrict domain resolution [cite: 81-83].

### [cite_start]Task 1: Verify DNS Mode [cite: 85]
* **Navigate to:** `Services` > `DNS Resolver`.
* **Action:** Ensure **Enable** is checked. (Verify `Services` > `DNS Forwarder` is disabled).

### [cite_start]Task 2: Host Override [cite: 86]
* **Navigate to:** `Services` > `DNS Resolver` (bottom).
* **Action:**
    1.  Click **Add** under Host Overrides.
    2.  **Host:** `portal`. **Domain:** `local`.
    3.  **IP:** `192.168.50.10`.
    4.  Click `Save`.

### [cite_start]Task 3: Enable DNSSEC [cite: 87]
* **Navigate to:** `Services` > `DNS Resolver`.
* **Action:** Check **Enable DNSSEC Support**. Click `Save`.

### [cite_start]Task 4: Block Domain [cite: 88]
* **Navigate to:** `Services` > `DNS Resolver` > `Host Overrides`.
* **Action:**
    1.  Click **Add**.
    2.  **Host:** `facebook`. **Domain:** `com`.
    3.  **IP:** `127.0.0.1`.
    4.  Click `Save`.

### [cite_start]Task 5: Observe Query Flow [cite: 89]
* **Navigate to:** `Diagnostics` > `Packet Capture`.
* **Action:**
    1.  **Interface:** `LAN`. **Port:** `53`.
    2.  Click `Start`.
    3.  Run `nslookup google.com 192.168.50.1` (Force query to pfSense IP).
    4.  Click `Stop` and view "View Capture".

---

## LAB 6: Traffic Shaping & Rate Limiting
[cite_start]**Goal:** Optimize performance and control bandwidth [cite: 96-98].

### [cite_start]Task 1: Bandwidth Usage [cite: 100]
* **Navigate to:** `Status` > `Traffic Graph`.
* **Action:** Select `WAN` to view real-time speeds.

### [cite_start]Task 2: Bandwidth Limit [cite: 101]
* **Step 1:** `Firewall` > `Traffic Shaper` > `Limiters`.
    * Create **New Limiter**: Name `Limit-5Mbps`, Bandwidth `5 Mbit/s`. Save.
* **Step 2:** `Firewall` > `Rules` > `LAN`.
    * Edit a Pass rule.
    * **Advanced Options** > **In/Out Pipe**: Select `Limit-5Mbps`.
    * Click `Save`.

### [cite_start]Task 3: Prioritize Interactive Traffic [cite: 102]
* **Navigate to:** `Firewall` > `Traffic Shaper` > `Wizards`.
* **Action:**
    1.  Run **Traffic_Shaper_Wizard_Dedicated**.
    2.  Follow prompts.
    3.  Check **Prioritize Voice over IP traffic** when asked.
    4.  Finish Wizard.

### [cite_start]Task 4 & 5: Observe Congestion [cite: 103, 104]
* **Navigate to:** `Status` > `Queues`.
* **Action:** Initiate a heavy download and watch the "Drops" column in the queue list.

---

## LAB 7: VPN – Secure Remote Access
[cite_start]**Goal:** Establish secure remote access [cite: 110-112].

### [cite_start]Task 1: Identify VPN Types [cite: 114]
* **Navigate to:** Top Menu `VPN`.
* **Action:** Note options (IPsec, OpenVPN, L2TP).

### [cite_start]Task 2: Configure VPN [cite: 115]
* **Navigate to:** `VPN` > `OpenVPN` > `Wizards`.
* **Action:**
    1.  Select **Local User Access**.
    2.  Create new CA/Cert.
    3.  Follow default prompts.
    4.  Finish.

### [cite_start]Task 3: IP Pool [cite: 116]
* **Navigate to:** `VPN` > `OpenVPN` > `Servers`.
* **Action:** Edit server. Check **Tunnel Network** (e.g., `10.0.8.0/24`). This is the pool.

### [cite_start]Task 4: Restrict Clients [cite: 117]
* **Navigate to:** `Firewall` > `Rules` > `OpenVPN`.
* **Action:**
    1.  Add Rule: **Pass** specific Destination IP.
    2.  Add Rule: **Block** Any Destination (place at bottom).

### [cite_start]Task 5: Verify Status [cite: 117]
* **Navigate to:** `Status` > `OpenVPN`.
* **Action:** Check service status is "Up".

---

## LAB 8: Integrated Policy Exercise (Advanced)
[cite_start]**Goal:** Cohesive enterprise-style configuration [cite: 122-125].

### [cite_start]Task 1: Interface Separation [cite: 127]
* **Navigate to:** `Interfaces` > `Assignments`.
* **Action:** Ensure distinct interfaces exist for `WAN`, `LAN`, and `GUEST` (OPT1).

### [cite_start]Task 2: Restrict VPN (DNS+HTTP) [cite: 128]
* **Navigate to:** `Firewall` > `Rules` > `OpenVPN`.
* **Action:**
    1.  Pass UDP/TCP Port `53`.
    2.  Pass TCP Port `80`.
    3.  Block All else.

### [cite_start]Task 3: Guest Rate Limits [cite: 129]
* **Navigate to:** `Firewall` > `Rules` > `GUEST`.
* **Action:** Edit Pass rule -> **Advanced Options** -> **In/Out Pipe** -> Select Limiters (from Lab 6).

### [cite_start]Task 4: DHCP Allow-List [cite: 130]
* **Navigate to:** `Services` > `DHCP Server` > `GUEST`.
* **Action:**
    1.  Check **"Deny unknown clients"**.
    2.  Add trusted MACs to **Static Mappings**.

### [cite_start]Task 5: State Table [cite: 131]
* **Navigate to:** `Diagnostics` > `States`.
* **Action:** Filter by `GUEST` interface to view combined NAT/Traffic states.
