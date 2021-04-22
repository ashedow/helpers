# Iptables

One of the utility firewall developed for Linux systems is iptables.

## How iptables Work

Network traffic is made up of packets. 
Data is broken up into smaller pieces (called packets), sent over a network, then put back together. Iptables identifies the packets received and then uses a set of rules to decide what to do with them.

Iptables filters packets based on:
- **Tables**: Tables are files that join similar actions. A table consists of several chains.
- **Chains**: A chain is a string of rules. When a packet is received, iptables finds the appropriate table, then runs it through the chain of rules until it finds a match.
- **Rules**: A rule is a statement that tells the system what to do with a packet. Rules can block one type of packet, or forward another type of packet. The outcome, where a packet is sent, is called a target.
- **Targets**: A target is a decision of what to do with a packet. Typically, this is to accept it, drop it, or reject it (which sends an error back to the sender).

### Tables and Chains

Linux firewall iptables has four default tables.

#### 1. Filter

The Filter table is the most frequently used one. 
It acts as a bouncer, deciding who gets in and out of your network. It has the following default chains:
- **Input** – the rules in this chain control the packets received by the server.
- **Output** – this chain controls the packets for outbound traffic.
- **Forward** – this set of rules controls the packets that are routed through the server.

#### 2. Network Address Translation (NAT)

This table contains NAT (Network Address Translation) rules for routing packets to networks that cannot be accessed directly. 
When the destination or source of the packet has to be altered, the NAT table is used. 
It includes the following chains:
- **Prerouting** – this chain assigns packets as soon as the server receives them.
- **Output** – works the same as the output chain we described in the filter table.
- **Postrouting** – the rules in this chain allow making changes to packets after they leave the output chain.

#### 3. Mangle

The Mangle table adjusts the IP header properties of packets. The table has all the following chains we described above:
- **Prerouting**
- **Postrouting**
- **Output**
- **Input**
- **Forward**

#### 4. Raw

The Raw table is used to exempt packets from connection tracking. The raw table has two of the chains we previously mentioned:
- **Prerouting**
- **Output**

![Diagram with iptables and chains tables contain](iptables-diagram.png)

#### 5. Security (Optional)

Some versions of Linux also use a **Security** table to manage special access rules. This table includes 
- **input**
- **output**
- **forward** 

chains, much like the filter table.

### Targets

A target is what happens *after a packet matches a rule criteria*. 
Non-terminating targets keep matching the packets against rules in a chain even when the packet matches a rule.

With terminating targets, a packet is evaluated immediately and is not matched against another chain. The terminating targets in Linux iptables are:
- **Accept** – this rule accepts the packets to come through the iptables firewall.
- **Drop** – the dropped package is not matched against any further chain. When Linux iptables drop an incoming connection to your server, the person trying to connect does not receive an error. It appears as if they are trying to connect to a non-existing machine.
- **Return** – this rule sends the packet back to the originating chain so you can match it against other rules.
- **Reject** – the iptables firewall rejects a packet and sends an error to the connecting device.

## Basic Syntax for iptables Commands and Options

General looks like
```bash
sudo iptables [option] CHAIN_rule [-j target]
```
A list of some common iptables options:
* `–A ––append` – Add a rule to a chain (at the end).
* `–C ––check` – Look for a rule that matches the chain’s requirements.
* `–D ––delete` – Remove specified rules from a chain.
* `–F ––flush` – Remove all rules.
* `–I ––insert` – Add a rule to a chain at a given position.
* `–L ––list` – Show all rules in a chain.
* `–N ––new–chain` – Create a new chain.
* `–v ––verbose` – Show more information when using a list option.
* `–X ––delete–chain` – Delete the provided chain.

> Iptables is case-sensitive, so make sure you’re using the correct options.

Current iptables Status
```bash
iptables -L
```

Enable Loopback Traffic
```bash
sudo iptables –A INPUT –i lo –j ACCEPT
```

**Allow Traffic on Specific Ports:**
To allow HTTP web traffic, enter the following command:
```
sudo iptables –A INPUT –p tcp ––dport 80 –j ACCEPT
```

To allow only incoming SSH (Secure Shell) traffic, enter the following:
```
sudo iptables –A INPUT –p tcp ––dport 22 –j ACCEPT
```

To allow HTTPS internet traffic, enter the following command:
```
sudo iptables –A INPUT –p tcp ––dport 443 –j ACCEPT
```

* `–p` – Check for the specified protocol (tcp).
* `––dport` – Specify the destination port.
* `–j` jump – Take the specified action.

**Control Traffic by IP Address**

ACCEPT traffic from a specific IP address.
```
sudo iptables –A INPUT –s 192.168.0.27 –j ACCEPT
```

DROP traffic from an IP address:
```
sudo iptables –A INPUT –s 192.168.0.27 –j DROP
```

REJECT traffic from a range of IP addresses, but the command is more complex:
```
sudo iptables –A INPUT –m iprange ––src–range 192.168.0.1–192.168.0.255 -j REJECT
```

* `–m` – Match the specified option.
* `–iprange` – Tell the system to expect a range of IP addresses instead of a single one.
* `––src-range` – Identifies the range of IP addresses.

Dropping Unwanted Traffic
```
sudo iptables –A INPUT –j DROP
```

Delete a Rule
You can use the –F option to clear all iptables firewall rules. A more precise method is to delete the line number of a rule.

First, list all rules by entering the following:
```
sudo iptables –L ––line–numbers
sudo iptables –D INPUT <Number>
```

Save rules
`sudo /sbin/iptables–save` or `sudo /sbin/service iptables save`
