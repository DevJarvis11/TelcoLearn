
# VNF Firewall Setup: pfSense Virtualization Lab Manual

## Objective

Deploy pfSense as a virtualized VNF in VirtualBox and validate networking modes: NAT, Bridged, Host-Only. Perform packet flow tests using ping, traceroute, and tcpdump.

## Setup Steps

### 1\. Download pfSense ISO Installer

  * Visit <https://www.pfsense.org/download/>.
  * Select Architecture: `AMD64`.
  * Select Installer Type: `ISO Installer`.
  * Select Console: `VGA`.
  * Save the file (e.g., `netgate-installer-amd64.iso`).

### 2\. Create pfSense VM in VirtualBox

  * Open VirtualBox and click **New**.
  * **Name**: `pfSense-VNF`.
  * **Type**: `BSD`.
  * **Version**: `FreeBSD (64-bit)`.
  * **RAM**: 2GB.
  * **CPU**: 2 vCPUs.
  * **Disk**: 20GB dynamically allocated.

### 3\. Attach pfSense ISO

  * Go to VM **Settings** → **Storage** → **Controller: IDE** → **Empty**.
  * Choose Disk → Select `netgate-installer-amd64.iso`.

### 4\. Configure Network Interfaces

  * **Adapter 1 (WAN)**:
      * Enabled.
      * Attached to: `NAT` (initial setup).
  * **Adapter 2 (LAN)**:
      * Enabled.
      * Attached to: `Host-only Adapter`.
      * Name: `vboxnet0`.

### 5\. Install pfSense

  * Boot the VM.
  * Select **Install**.
  * Accept defaults.
  * Reboot after installation.
      * The pfSense console menu will appear.
      * LAN default IP: `192.168.1.1`.

### 6\. Access Web GUI

From the host PC browser:

  * Navigate to `https://192.168.1.1`.
  * **Username**: `admin`.
  * **Password**: `pfsense`.

### 7\. Configure WAN/LAN

  * Verify WAN receives a DHCP IP.
  * LAN network: `192.168.1.0/24`.

## Networking Experiments

### NAT Mode Test

1.  Keep Adapter 1 = `NAT`.
2.  From the pfSense shell, run: `ping 8.8.8.8`.
      * *Expected*: Successful replies.

### Bridged Mode Test

1.  Change Adapter 1 → `Bridged Adapter`.
2.  Reboot pfSense.
3.  WAN should receive an IP from your physical router.
4.  Test ping again.

### Host-Only Mode Test

1.  From the Host PC, run: `ping 192.168.1.1`.
      * *Expected*: pfSense reachable.

### Packet Flow Validation

Run these inside the pfSense shell:

  * **Ping test**:
      * `ping 192.168.1.1`
      * `ping 8.8.8.8`
  * **Traceroute**:
      * `traceroute 8.8.8.8`
  * **tcpdump**:
      * `tcpdump -i em0`
      * `tcpdump -i em1`


