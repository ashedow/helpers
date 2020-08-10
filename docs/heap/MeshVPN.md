# Mesh VPN

> https://stubarea51.net/2020/03/10/remote-workers-rapid-and-cost-effective-vpn-scale-with-zerotier-opnsense-and-frrouting/

Mesh VPNs are a relatively recent concept in overlay networking that allow for connectivity directly between any two points in the mesh without hairpinning through central points like a traditional VPN concentrator.
> Check podcast (networkcollective.com)[https://networkcollective.com/2020/02/cr-end-of-wan/]

## What Mesh VPN solutions are available?

There are a few and this isn’t an exhaustive list, but the three I hear the most chatter about are (ZeroTier)[https://www.zerotier.com/], (Nebula)[https://github.com/slackhq/nebula] and (TailScale)[https://www.tailscale.com/]

### ZeroTier

ZeroTier first got on my radar when Ethan Banks over at the Packet Pushers did a priority queue show with the founder Adam Ierymenko on the Mesh VPN solution he developed.
ZeroTier’s mission is “Global Area Networking” using a unique mix of a centralized controller and certificate based authentication of endpoints.
it’s super easy to deploy as well and can be functional between two computers, phones, etc in a matter of minutes.

**Managing L2 scale**

Normally, a large /16 subnet stretched across the globe would have networkers like me cringing as it’s a solution that’s often frowned upon and with good reason.

However, ZeroTier solves this in a very interesting way by managing all of the components that normally blow up L2 overlays like broadcast and multicast.

ARP is a good example – it is converted into unicast and sent to the appropriate destination as described in ZTs manual below:

Broadcast is also carried as multicast to reduce overhead. Hosts can choose to participate or block multicast based on what the host is used for.

This is how ZT scales to very large numbers in the same subnet.

And if that isn’t good enough, they also run a public network called ‘earth’ that’s one large /7, just to make sure that tens of thousands of people on one subnet won’t blow things up.

**Operating system support**

One of the great benefits of using ZeroTier is that it runs on practically everything including Windows, Linux, iPhone, iPad and Mac.

**ZT Controller – managing endpoints**

Once you’ve created an overlay network, ZeroTier makes it incredibly easy to manage and authorize endpoints.

Below is a screenshot of endpoints in production. Notice the last entry has IPv6 available for internet access, so ZeroTier will use that to transport the IPv4 overlay network – which is a huge benefit…the underlay IP version doesn’t matter.

This is not true in almost every other enterprise VPN solution i’ve come across – IPv4 must encapsulate in IPv4 and IPv6 must Encapsulate in IPv6.

**Security policy**

ZeroTier has the ability to push flow rules to endpoints that can permit / deny or change the flow of traffic.

There are a number of ways to leverage this along with rules at the OPNSense firewall to create a security policy that is modular, effective and functional.

**Using OPNSense as a firewall**

If you’ve never used it, (OPNSense)[https://opnsense.org/] is a open source firewall package.

It can be deployed from an ISO into a VM or as a bootstrap install in the cloud (I’ve successfully used AWS and Digital Ocean)

**Mesh VPN and Routing**

One of the intial challenges when using Mesh VPNs was to interconnect with routers and provide security policy beyond just the controller.

OPNSense has a number of packages and plugins – what initially drew me to it was the support for ZeroTier out of the box.

Installation was painless and the ZeroTier adapter was running and reachable within minutes.

**Security rules**

Here is a brief example of a security rule in OPNSense defining access coming from a ZeroTier remote worker subnet to a group of RDP Servers

That’s pretty much all you need to get started with connecting remote workers into the firewall.

Should you decide to force Internet access through the firewall, a NAT policy can be setup and ZeroTier can inject (or remove) a default route to the host if so desired.

The last piece to the puzzle – dynamic routing – is covered in the next section.

**FRRouting for dynamic routing**

The final piece to glue together the Mesh VPN connectivity through the firewall is a way to dynamically advertise the VPN subnets into a router or another firewall.

(FRRouting)[https://frrouting.org/] or Free Range Routing is an open source routing stack that was forked from Quagga a few years ago.

It’s a very solid and capable way to turn any linux box into a feature rich routing platform.

A quick look at the protocols supported shows a wealth of options

The plugin for OPNSense is installed in the same way as ZeroTier and is equally painless. Once intalled, a tab for routing shows up in the left hand menu.

**OSPF**

OSPF Configuration and creating neighbor adjacencies is very straightforward. In this network, OSPF is used to advertise loopbacks for iBGP to the DC core switch.

Here is an example from the OPNSense UI

**BGP**

BGP is also very easy to configure. In this example from the OPNSense UI, several ZT networks are advertised into the DC core route reflector via iBGP.

**Active routes**

All routes for FRRouting, including Kernel routes can be viewed from the routing diagnostics tab in OPNSense.

Here is a view of the ZeroTier 100.125.x.x routes coming from the OPNSense FW and FRRouting into the DC Core route reflector.

**Running configuration**

FRRouting has a running config that’s consistent with an industry standard CLI configuration.

The UI plugin will update the running config based on the web configuration, but features that aren’t supported in the UI can still be added by editing the running config.


