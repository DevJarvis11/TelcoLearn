# pfSense Lab Practice - Comprehensive Step-by-Step Guide

This document details the configuration steps required to complete the pfSense Hands-On Assessment.

---

## LAB 1: Networking & Interface Configuration
**Goal:** Standardize interface naming, configure internal networks, and manage interface behavior.

### Task 1: Identify Interfaces
* **Navigate to:** `Interfaces` > `Assignments`.
* **Action:** Observe the list of physical network ports (e.g., `em0`, `em1`, `vtnet0`).
* **Verification:** Note which port corresponds to WAN and which to LAN.
* **Screenshot:** Capture the interface assignment list.

### Task 2: Configure LAN IP
* **Navigate to:** `Interfaces` > `LAN`.
* **Action:**
    1.  Set **IPv4 Configuration Type** to `Static IPv4`.
    2.  Scroll to **Static IPv4 Configuration**.
    3.  **IP Address:** Enter a private IP (e.g., `192.168.50.1`).
    4.  **Subnet Mask:** Select `/24`.
    5.  Click `Save` and `Apply Changes`.
* **Screenshot:** Capture the Static IPv4 configuration section.

### Task 3: Rename Interfaces
* **Navigate to:** `Interfaces` > `LAN` (or WAN/OPT1).
* **Action:**
    1.  In the **Description** field, enter a meaningful name (e.g., `LAN-Core` or `WAN-Uplink`).
    2.  Click `Save`.
    3.  Repeat for all active interfaces.
* **Screenshot:** Go back to Assignments and capture the new names.

### Task 4: Reboot and Confirm
* **Navigate to:** `Diagnostics` > `Reboot`.
* **Action:** Click `Submit` to restart the system.
* **Verification:** Log back in and check `Status` > `Dashboard` to confirm names and IPs persisted.

### Task 5: Modify MTU
* **Navigate to:** `Interfaces` > `[Interface Name]`.
* **Action:**
    1.  Locate the **MTU** (Maximum Transmission Unit) field.
    2.  Set value to `1400`.
    3.  Click `Save` and `Apply Changes`.
* **Observation:** Note if the interface resets or if connectivity drops briefly.
* **Screenshot:** Capture the interface settings showing the new MTU.

### Task 6: Disable Interface
* **Navigate to:** `Interfaces` > `[Unused Interface]`.
* **Action:** Uncheck the **Enable Interface** box at the top. Click `Save`.
* **Observation:** Go to Dashboard; the interface status should show as down/gray.
* **Screenshot:** Capture the dashboard widget showing the disabled interface.

---

## LAB 2: Firewall Rule Logic & Policy Enforcement
**Goal:** Enforce selective permissions and visibility for troubleshooting.

### Task 1: Permit Specific Host
* **Navigate to:** `Firewall` > `Rules` > `LAN`.
* **Action:**
    1.  Click **Add** (Up Arrow).
    2.  **Action:** `Pass`.
    3.  **Source:** `Single Host or Alias` -> `192.168.50.10` (Target Client IP).
    4.  **Description:** "Allow Specific Host".
    5.  Click `Save` & `Apply Changes`.
* **Screenshot:** Capture the rule list showing the pass rule.

### Task 2: Block ICMP
* **Navigate to:** `Firewall` > `Rules` > `LAN`.
* **Action:**
    1.  Click **Add** (Up Arrow) to place at the **top**.
    2.  **Action:** `Block`.
    3.  **Protocol:** `ICMP`.
    4.  **Source:** `LAN net`.
    5.  **Description:** "Block ICMP".
    6.  Click `Save` & `Apply Changes`.
* **Screenshot:** Capture the rule list showing the block rule at the top.

### Task 3: Time-Based Rule
* **Step 1:** Go to `Firewall` > `Schedules`. Click `Add`.
    * **Name:** `WorkHours`. Select range (e.g., 09:00 - 17:00). Click `Save`.
* **Step 2:** Go to `Firewall` > `Rules` > `LAN`. Click `Add`.
    * **Action:** `Pass`.
    * **Source:** `LAN net`.
    * **Advanced Options:** Scroll to **Schedule**, select `WorkHours`.
    * Click `Save`.
* **Screenshot:** Capture the rule list showing the schedule icon.

### Task 4: Enable Logging
* **Navigate to:** `Firewall` > `Rules` > `LAN`.
* **Action:** Edit the **Block ICMP** rule (from Task 2).
    1.  Check box: **"Log packets that are handled by this rule"**.
    2.  Click `Save` & `Apply Changes`.
* **Verification:** Check `Status` > `System Logs` > `Firewall`.

### Task 5: Capture Rule Match
* **Navigate to:** `Status` > `System Logs` > `Firewall`.
* **Action:**
    1.  Generate blocked traffic (Ping pfSense from client).
    2.  Locate the red `X` entry in logs.
    3.  Click the entry to view which rule ID triggered the block.
* **Screenshot:** Capture the log entry details.

---

## LAB 3: NAT & Port Forwarding
**Goal:** Configure outbound NAT and port forwarding for hosted applications.

### Task 1: Identify NAT Mode
* **Navigate to:** `Firewall` > `NAT` > `Outbound`.
* **Action:** Observe current mode (Automatic/Hybrid/Manual).
* **Screenshot:** Capture the NAT mode selection.

### Task 2: Outbound NAT
* **Navigate to:** `Firewall` > `NAT` > `Outbound`.
* **Action:**
    1.  Select **Hybrid Outbound NAT**. Click `Save`.
    2.  Click **Add**.
    3.  **Interface:** `WAN`.
    4.  **Source:** `Network` -> `10.0.0.0/24` (Custom Subnet).
    5.  **Translation:** `Interface Address`.
    6.  Click `Save`.
* **Screenshot:** Capture the mappings list showing the custom rule.

### Task 3: Port Forwarding
* **Navigate to:** `Firewall` > `NAT` > `Port Forward`.
* **Action:**
    1.  Click **Add**.
    2.  **Interface:** `WAN`.
    3.  **Dest. Port Range:** `8080`.
    4.  **Redirect Target IP:** `192.168.50.5` (Internal Server).
    5.  **Redirect Target Port:** `80`.
    6.  Click `Save` & `Apply Changes`.
* **Screenshot:** Capture the port forward list.

### Task 4: Disable NAT Reflection
* **Navigate to:** Edit the Port Forward rule from Task 3.
* **Action:**
    1.  Scroll to **NAT Reflection**.
    2.  Select **Disable**.
    3.  Click `Save`.
* **Screenshot:** Capture the rule edit page showing reflection disabled.

### Task 5: Observe NAT States
* **Navigate to:** `Diagnostics` > `States`.
* **Action:** Filter by port `8080` or the target IP to see active translation entries.
* **Screenshot:** Capture the state table.

---

## LAB 4: DHCP Server & Client Policy
**Goal:** Automate addressing and enforce device control.

### Task 1: Enable DHCP
* **Navigate to:** `Services` > `DHCP Server` > `LAN`.
* **Action:**
    1.  Check **Enable**.
    2.  **Range:** `192.168.50.100` to `192.168.50.200`.
    3.  Click `Save`.
* **Screenshot:** Capture the DHCP pool settings.

### Task 2: Static Mapping
* **Navigate to:** `Services` > `DHCP Server` > `LAN` (bottom of page).
* **Action:**
    1.  Click **Add**.
    2.  **MAC Address:** Enter client MAC (e.g., `aa:bb:cc:dd:ee:ff`).
    3.  **IP Address:** `192.168.50.50`.
    4.  Click `Save`.
* **Screenshot:** Capture the static mapping table.

### Task 3: Custom DNS
* **Navigate to:** `Services` > `DHCP Server` > `LAN`.
* **Action:**
    1.  **DNS Servers:** Enter `8.8.8.8` and `1.1.1.1`.
    2.  Click `Save`.
* **Screenshot:** Capture the DNS server fields.

### Task 4: Block Unknown Devices
* **Navigate to:** `Services` > `DHCP Server` > `LAN`.
* **Action:**
    1.  Check **"Deny unknown clients"**.
    2.  Click `Save`.
* **Screenshot:** Capture the checkbox.

### Task 5: Locate Leases
* **Navigate to:** `Status` > `DHCP Leases`.
* **Action:** View table for Hostname, MAC, and IP status.
* **Screenshot:** Capture the active lease table.

---

## LAB 5: DNS Resolver & DNS Control
**Goal:** Centralize DNS handling and restrict domain resolution.

### Task 1: Verify DNS Mode
* **Navigate to:** `Services` > `DNS Resolver`.
* **Action:** Ensure **Enable** is checked. (Verify `Services` > `DNS Forwarder` is disabled).
* **Screenshot:** Capture the enabled setting.

### Task 2: Host Override
* **Navigate to:** `Services` > `DNS Resolver` (bottom).
* **Action:**
    1.  Click **Add** under Host Overrides.
    2.  **Host:** `portal`. **Domain:** `local`.
    3.  **IP:** `192.168.50.10`.
    4.  Click `Save`.
* **Screenshot:** Capture the host override entry.

### Task 3: Enable DNSSEC
* **Navigate to:** `Services` > `DNS Resolver`.
* **Action:** Check **Enable DNSSEC Support**. Click `Save`.
* **Screenshot:** Capture the DNSSEC checkbox.

### Task 4: Block Domain
* **Navigate to:** `Services` > `DNS Resolver` > `Host Overrides`.
* **Action:**
    1.  Click **Add**.
    2.  **Host:** `facebook`. **Domain:** `com`.
    3.  **IP:** `127.0.0.1`.
    4.  Click `Save`.
* **Screenshot:** Capture the override showing the blocked domain.

### Task 5: Observe Query Flow
* **Navigate to:** `Diagnostics` > `Packet Capture`.
* **Action:**
    1.  **Interface:** `LAN`. **Port:** `53`.
    2.  Click `Start`.
    3.  Run `nslookup google.com 192.168.50.1` (Force query to pfSense IP).
    4.  Click `Stop` and view "View Capture".
* **Screenshot:** Capture the output showing Query and Response packets.

---

## LAB 6: Traffic Shaping & Rate Limiting
**Goal:** Optimize performance and control bandwidth.

### Task 1: Bandwidth Usage
* **Navigate to:** `Status` > `Traffic Graph`.
* **Action:** Select `WAN` to view real-time speeds.
* **Screenshot:** Capture the traffic graph.

### Task 2: Bandwidth Limit
* **Step 1:** `Firewall` > `Traffic Shaper` > `Limiters`.
    * Create **New Limiter**: Name `Limit-5Mbps`, Bandwidth `5 Mbit/s`. Save.
* **Step 2:** `Firewall` > `Rules` > `LAN`.
    * Edit a Pass rule.
    * **Advanced Options** > **In/Out Pipe**: Select `Limit-5Mbps`.
    * Click `Save`.
* **Screenshot:** Capture the limiter settings and rule configuration.

### Task 3: Prioritize Interactive Traffic
* **Navigate to:** `Firewall` > `Traffic Shaper` > `Wizards`.
* **Action:**
    1.  Run **Traffic_Shaper_Wizard_Dedicated**.
    2.  Follow prompts.
    3.  Check **Prioritize Voice over IP traffic** when asked.
    4.  Finish Wizard.
* **Screenshot:** Capture the queue list created by the wizard.

### Task 4 & 5: Observe Congestion
* **Navigate to:** `Status` > `Queues`.
* **Action:** Initiate a heavy download and watch the "Drops" column in the queue list.
* **Screenshot:** Capture the queue status showing drops/activity.

---

## LAB 7: VPN – Secure Remote Access
**Goal:** Establish secure remote access.

### Task 1: Identify VPN Types
* **Navigate to:** Top Menu `VPN`.
* **Action:** Note options (IPsec, OpenVPN, L2TP).
* **Screenshot:** Capture the VPN menu.

### Task 2: Configure VPN
* **Navigate to:** `VPN` > `OpenVPN` > `Wizards`.
* **Action:**
    1.  Select **Local User Access**.
    2.  Create new CA/Cert.
    3.  Follow default prompts.
    4.  Finish.
* **Screenshot:** Capture the created server.

### Task 3: IP Pool
* **Navigate to:** `VPN` > `OpenVPN` > `Servers`.
* **Action:** Edit server. Check **Tunnel Network** (e.g., `10.0.8.0/24`). This is the pool.
* **Screenshot:** Capture the tunnel network setting.

### Task 4: Restrict Clients
* **Navigate to:** `Firewall` > `Rules` > `OpenVPN`.
* **Action:**
    1.  Add Rule: **Pass** specific Destination IP.
    2.  Add Rule: **Block** Any Destination (place at bottom).
* **Screenshot:** Capture the restricted rule set.

### Task 5: Verify Status
* **Navigate to:** `Status` > `OpenVPN`.
* **Action:** Check service status is "Up".
* **Screenshot:** Capture the status page.

---

## LAB 8: Integrated Policy Exercise (Advanced)
**Goal:** Cohesive enterprise-style configuration.

### Task 1: Interface Separation
* **Navigate to:** `Interfaces` > `Assignments`.
* **Action:** Ensure distinct interfaces exist for `WAN`, `LAN`, and `GUEST` (OPT1).
* **Screenshot:** Capture the interface list.

### Task 2: Restrict VPN (DNS+HTTP)
* **Navigate to:** `Firewall` > `Rules` > `OpenVPN`.
* **Action:**
    1.  Pass UDP/TCP Port `53`.
    2.  Pass TCP Port `80`.
    3.  Block All else.
* **Screenshot:** Capture the rule list.

### Task 3: Guest Rate Limits
* **Navigate to:** `Firewall` > `Rules` > `GUEST`.
* **Action:** Edit Pass rule -> **Advanced Options** -> **In/Out Pipe** -> Select Limiters (from Lab 6).
* **Screenshot:** Capture the rule showing pipe settings.

### Task 4: DHCP Allow-List
* **Navigate to:** `Services` > `DHCP Server` > `GUEST`.
* **Action:**
    1.  Check **"Deny unknown clients"**.
    2.  Add trusted MACs to **Static Mappings**.
* **Screenshot:** Capture the deny setting and mapping table.

### Task 5: State Table
* **Navigate to:** `Diagnostics` > `States`.
* **Action:** Filter by `GUEST` interface to view combined NAT/Traffic states.
* **Screenshot:** Capture the state table entries.
