# AWS Cloud Practitioner Exam

> Note
> * don't forgot about pricing and Shared Responsibility Model
> * you should know about the basis of AWS products. The key feature thad usually mentioned in the begining paragraphs. Literally.

## The 5 Pillars of the AWS Well-Architected Framework

1- Operational Excellence: The operational excellence pillar includes the ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures.
2- Security: The security pillar includes the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies.
3- Reliability: The reliability pillar includes the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as  misconfigurations or transient network issues.
4- Performance Efficiency: The performance efficiency pillar includes the ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve.
5- Cost Optimization: The cost optimization pillar includes the ability to avoid or eliminate unneeded cost or sub-optimal resources.

Additional information:

Creating a software system is a lot like constructing a building. If the foundation is not solid, structural problems can undermine the integrity and function of the building. When architecting technology solutions on Amazon Web Services (AWS), if you neglect the five pillars of operational excellence, security, reliability, performance efficiency, and cost optimization, it can become challenging to build a system that delivers on your expectations and requirements. Incorporating these pillars into your architecture helps produce stable and efficient systems. This allows you to focus on the other aspects of design, such as functional requirements. The AWS Well-Architected Framework helps cloud architects build the most secure, high-performing, resilient, and efficient infrastructure possible for their applications.     



## AWS Networking (Overview)

**Region** - geo location of you network
**AZ** - data center of you AWS resources
**VPC** - logically isolated section of the AWS Cloud where you can launch AWS resources
**Internet Gateway** **IGW** - Enable access to the Internet
**Route tables** - determine ehere network traffic from you subnets are directed
**NACLs** - Acts as a firewalls at the subnet level
**Security Groups** - Acts as firewall at instance level
**Subnets** - a logical partition of an IP network into multiple, smaller network segments

## Database (Overview)
DynamoDB - Nosql key/value
DocumentDB - NoSQL Document db that is MongoDB compatible
RDS - Relational DB service  support multyply engines
    Aurora MySQL (5x faster) PSQL (3x faster) fully managed
    Aurora serverless - only runs when you nedd it lile for Lambda
Neptune - managet Graph DB
Redshift - Columnar DB, petabyte wirehouse
ElastiCache - Redis or Memchched DB

## Provisioning (Overview)
The allocation or creation of resources and services to customer

Elastic Beanstalk - service for deploying and scaling web app an service
OpsWork - configuration management service that provides managed instance Chef and Puppet
CloudFormation - infrastructure as code JSON YAML
AWS QuickStart - pre-made packages that can launch and configure you AWS compute ets
AWS Marketplace - catalogue software

## Computing (Overview)
EC2 - elastic compute Cloud:
    ECS - Elastic cloud container . Docker as a service
    Fargate - microservices where you don't think about the infrastruvture. Play per task
    EKS - Kubernetis as a service easy to deploy, manage and scale containerized app using Kube
    Lambda - severless function
    Elastic Beanstalk - orcestrates various AWS services including EC@, S#, Simple Notification Service, CloudWatch, autoscaling, elastic load balancers
    AWS Batch - plans, shedules and executes you batch computing workloads across the full range of AWS compute services and futures such as AWS ES2 and Spot instances

## Cloud Services (Overview)
CloudFormation - infrastructure as a code
CloudTrail - logs all api calls between aws services
CloudFront - Content distribution Network. It create  a cached copy of you website and copies to servers located near 
CloudWatch - collection of multiply services
    CloudWatch logs - performance data, CPU, Memory, network, app logs ed Rails Nginx, Lambda
    CloudWatch Metrics - time oriented set of data points
    CloudWatch Events - trigger an event based on condition eg ever hour take snapshot
    CloudWatch Alarms - triggers notifications based om metrics
    CloudWatch dashboard - create visualisation based om metrics
CloudSearch - search engine, you have an ecommerce website and you whant to add seachbar

## Connect Services (Overview)
DirectConnect - Dedicated Fiber Optic Connections fron DataCenter to AWS
Amazon Connect - call center
MediaConnect - New versio of Elastic transcoder, converts videos to different video  types

## Storage (Overview)
S3 - Simple Storage Service - object store
S3 Glacier - low cost storage for archiving and long term backup
Storage Gateway - hybrid cloud storage with local chacing
    File gateway
    Volume gateway
    Tape Gateway
EBS - Elastic block storage - hard drive in the cloud you attach to EC2 (SSD, IOPS SSD, Throughput HHD, Cold HHD)
EFS - Elastic file storage - file storage mountable to multiple EC2 instances at the same time
Snowball - physically migrate lots of data via the comuter sutcase 50-80Tb
    Snowball Edge - better version - 100Tb
    Snowmobile - shipping container, pulled by a semi-trailer truck - 100PB

## Business Centric Services (Overview)
Amazon Connect - Call center - coud based call center service you can setup in just a few clicks - based on the same proven system used by Amazon customer service teams
WorkSpaces - Virtual Remote desctop - Secure managed service for providing either Win Linux desctops in just a feu min, wich quickly scales up to thouthends of desctops
WorkDocks - a content creation and collaboration service - early create, edit and share content (AWS Sharepoint)
Chime - AWS platform for online meetings, video conferencing and business calling wich elastic scales
WorkMail - managed business email contact and calendar service that support existing desctopmobile app (IMAP)
Pinpoint - marketing campaign management system you can use for sending targeting email, SMS, Push, voice messages
SES - Simple Email Service - cloud-based email sending service, designed for marketers and app developers to send marketing, notification and emails
QuickSight - business Interlligence (Bi) service. Connect multiple datasource and quickly visualize data in the form of graphs with little to no programming knoledge

## Enterprise integration (Overview)
Direct Connect - dedicated Gigabit network connection from you permises to AWS/
VPN - establish a secure connection to you AWS
    Site-to-site VPN - Connecting you on-permise to you AWS net
    Client VPN - Connecting a client (laptop) to you AWS net
Storage Gateway - a hybrid storage service that enables you on premises app to use AWS cloud storage. Use for backup, archiving, disaster recovery, cloud data processing, storage tiering and migration
Archive Directory - AWS Directory service for Microsoft Active Directory also known as AWS Managed Microsoft AD - enables you directory-aware workloads  and AWS resources to use managed Active Directory in AWS 

## Logging (OwerView)
CloudTrail - logs all API calls AWS service. 
    Detect developer misconfiguration
    detect malicious actors
    Automate responses
CloudWatch - collection of multiply services
    CloudWatch logs - performance data, CPU, Memory, network, app logs ed Rails Nginx, Lambda
    CloudWatch Metrics - time oriented set of data points
    CloudWatch Events - trigger an event based on condition eg ever hour take snapshot
    CloudWatch Alarms - triggers notifications based om metrics
    CloudWatch dashboard - create visualisation based om metrics

## MediaConnect vs Elastic Transcoder
Both transcodes videos

Elastic Transcoder:
old way
videos to streams format

MediaConnect:
new way
videos to streams format overlays images
insert videos clips
extracts captions data
robust UI

## SNS vs SQS vs SES
SNS - pub/sub HTTPS. you need topic
SQS - rabbitMQ, garanteed delivery, aws sdk
SES simple email service/ can html email|template, monitor

## Artifact vs Inspector vs Trusted Adviser
Both security tools perform audit

Inspector:
generate PDF
audits a single EC2
Generated a report from a long list of security checks 699

Artifact
generate PDF
Generates security report based on global compliance framework
Service organisation control
Payment Card Industry

Trusted Adviser
Doesn't  generate out a PDF
Gives you a holistic view of recomendations across multiply services and best practices

## ALB NLB CLB

* Application Load Balancer - 
layer 7 
Can attach WAF 
Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers. Operating at the individual request level (Layer 7), Application Load Balancer routes traffic to targets within Amazon Virtual Private Cloud (Amazon VPC) based on the content of the request.

* Network Load Balancer - layer 4 Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP) and Transport Layer Security (TLS) traffic where extreme performance is required. Operating at the connection level (Layer 4), Network Load Balancer routes traffic to targets within Amazon Virtual Private Cloud (Amazon VPC) and is capable of handling millions of requests per second while maintaining ultra-low latencies. Network Load Balancer is also optimized to handle sudden and volatile traffic patterns.

* Classic Load Balancer - layer 4 and 7/ does not use Target Groups Classic Load Balancer provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. Classic Load Balancer is intended for applications that were built within the EC2-Classic network.

## Payment options
You can choose between three payment options when you purchase a Standard or Convertible Reserved Instance:

1- No Upfront:
          No upfront payment is required. You are billed a discounted hourly rate  for every hour within the term, regardless of whether the Reserved Instance is being used. No Upfront Reserved Instances are based on a contractual obligation to pay monthly for the entire term of the reservation. A successful billing history is required before you can purchase No Upfront Reserved Instances.

2- Partial Upfront:
           A portion of the cost must be paid up front and the remaining hours in the term are billed at a discounted hourly rate, regardless of whether you’re using the Reserved Instance.

3- All Upfront:
           With the All Upfront option, you pay for the entire Reserved Instance term with one upfront payment. This option provides you with the largest discount compared to On-Demand instance pricing.

## Regions
geographically distinct
Each has at least 2 AZ
new feature always in US East
US-East-1 north virginia - only one with all you billing information

Each AWS Region contains multiple distinct locations, or Availability Zones. Each Availability Zone is engineered to be independent from failures in other Availability Zones. An Availability Zone is a data center, and in some cases, an Availability Zone consists of multiple data centers. Availability Zones within a Region provide inexpensive, low-latency network connectivity to other zones in the same Region. This allows you to replicate data across data centers in a synchronous manner so that failover can be automated and appear transparent to your users.

## AZ

**Multi-AZ**distribution you instances across multiple AZs allows failover configuration for handling requests when one goes down
<10ms latency between AZs

## Edge locations

has a Direct connection to AWS network
These location serve requests to **CloudFront** and **Route 53**. request going to either of these services will be routed to the nearest edge location automatically

S3 Transfer Acceleration traffic and API Gateway endpoint traffic also use Edge Network
Allows **low latency** no matter where the end user is geographicaly located

## GovCloud 

Allows customers to host sensitive **Controlled Unclassified Informatio** and other types of regulated workloads

Gov cloud special Regions are only operated by employees who are US citizens on US soil
Only accessible to US entities and root account holders

## Cloud computing 

1. Trade capital expense for variable expense – Instead of having to invest heavily in data centers and servers before you know how you’re going to use them, you can pay only when you consume computing resources, and pay only for how much you consume.

2. Benefit from massive economies of scale – By using cloud computing, you can achieve a lower variable cost than you can get on your own. Because usage from hundreds of thousands of customers is aggregated in the cloud, providers such as AWS can achieve higher economies of scale, which translates into lower pay as-you-go prices.

3. Stop guessing capacity – Eliminate guessing on your infrastructure capacity needs. When you make a capacity decision prior to deploying an application, you often end up either sitting on expensive idle resources or dealing with limited capacity. With cloud computing, these problems go away. You can access as much or as little capacity as you need, and scale up and down as required with only a few minutes’ notice.

4. Increase speed and agility – In a cloud computing environment, new IT resources are only a click away, which means that you reduce the time to make those resources available to your developers from weeks to just minutes. This results in a dramatic increase in agility for the organization, since the cost and time it takes to experiment and develop is significantly lower.

5. Stop spending money running and maintaining data centers – Focus on projects that differentiate your business, not the infrastructure. Cloud computing lets you focus on your own customers, rather than on the heavy lifting of racking, stacking, and powering servers.

6. Go global in minutes – Easily deploy your application in multiple regions around the world with just a few clicks. This means you can provide lower latency and a better experience for your customers at minimal cost.


## Common AWS Terms
AWS IoT: AWS IoT is a managed cloud service that lets connected devices easily and securely interact with cloud applic­ations and other devices.

Certif­icate Manager: AWS Certif­icate Manager lets you easily provision, manage, and deploy Secure Sockets Layer/­Tra­nsport Layer Security (SSL/TLS) certif­icates for use with AWS services.

CloudS­earch: AWS CloudS­earch is a fully managed search service for websites and apps.

Data Pipeline: AWS Data Pipeline is a lightw­eight orches­tration service for periodic, data-d­riven workflows.

EC2 Container Service: Amazon ECS allows you to easily run and manage Docker containers across a cluster of Amazon EC2 instances.

Elasti­Cache: Amazon Elasti­Cache improves applic­ation perfor­mance by allowing you to retrieve inform­ation from an in-memory caching system.

Elasti­csearch Service: Amazon Elasti­csearch Service is a managed service that makes it easy to deploy, operate, and scale Elasti­cse­arch, a popular open-s­ource search and analytics engine.

Elastic Transcoder: Amazon Elastic Transcoder lets you convert your media files in the cloud easily, at low cost, and at scale

Inspector: Amazon Inspector enables you to analyze the behavior of the applic­ations you run in AWS and helps you to identify potential security issues.

Machine Learning: Amazon Machine Learning is a service that enables you to easily build smart applic­ations.

SES: Amazon Simple Email Service (SES) enables you to send and receive email.

SNS: Amazon Simple Notifi­cation Service (SNS) lets you publish messages to subscr­ibers or other applic­ations.

Storage Gateway: AWS Storage Gateway securely integrates on-pre­mises IT enviro­nments with cloud storage for backup and disaster recovery.

SQS: Amazon Simple Queue Service (SQS) offers a reliable, highly scalable, hosted queue for storing messages.

SWF: Amazon Simple Workflow (SWF) coordi­nates all of the processing steps within an applic­ation.

CAF: Cloud Adoption Framework. AWS Professional Services created the AWS Cloud Adoption Framework (AWS CAF) to help organizations design and travel an accelerated path to successful cloud adoption. The guidance and best practices provided by the framework help you build a comprehensive approach to cloud computing across your organization, and throughout your IT lifecycle.


## VPC (Compute)
> https://aws.amazon.com/vpc/
Amazon Virtual Private Cloud (VPC) lets you launch AWS resources in a private, isolated cloud.

You have complete control over your virtual networking environment, including selection of your own IP address range, creation of subnets, and configuration of route tables and network gateways. You can use both IPv4 and IPv6 in your VPC for secure and easy access to resources and applications.
You can create a public-facing subnet for your web servers that have access to the internet. You can also place your backend systems, such as databases or application servers, in a private-facing subnet with no internet access.
Main ways to connect to your virtual cloud:
 * VPN connect
 * double Direct Connect

* Secure
* Simple
* Customizable

## Subnet (Networking)
A subnet is a range of IP addresses in your VPC.

• Divides	VPC
• Public	subnets	can	access	internet
• Private	subnets	cannot	(by	default)
• VPC	can	have	multiple	subnets

## Direct Connect (Networking)
> https://aws.amazon.com/directconnect/

AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS.

Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office, or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than Internet-based connections.
AWS Direct Connect lets you establish a dedicated network connection between your network and one of the AWS Direct Connect locations. Using industry standard 802.1q VLANs, this dedicated connection can be partitioned into multiple virtual interfaces. 

 * REDUCES YOUR BANDWIDTH COSTS
 * CONSISTENT NETWORK PERFORMANCE
 * COMPATIBLE WITH ALL AWS SERVICES
 * PRIVATE CONNECTIVITY TO YOUR AMAZON VPC
 * Elastic
 * simple

## EC2 (Compute)
> https://aws.amazon.com/ec2/

Main product. Amazon Elastic Compute Cloud (EC2) provides resizable compute capacity in the cloud.
Virtual server that provides secure, resizable (different sizes, memory, cpu, OS) compute capacity in the cloud.

Different types of instance.
    * On-Demand instances, you pay for compute capacity by the hour with no long-term commitments. You can increase or decrease your compute capacity depending on the demands of your application and only pay the specified hourly rate for the instances you use.
        On-demand instances are significantly less cost-effective than spot instances.
    * Reserved instance - cheaper price. shortest reservation length is one year. 
        Reserved instances are recommended for Customers that can commit to using EC2 over a 1 or 3-year term to reduce their total computing costs. Even if the project will last for more than a year, the cost-benefit for acquiring Reserved Instances is not as great as the cost-benefit from using Spot Instances. The Spot option provides the largest discount (up to 90%).
    * Spot instance (can up and down).  pay the Spot price that's in effect for the time period your instances are running.
        Spot instances provide a discount (up to 90%) off the On-Demand price. The Spot price is determined by long-term trends in supply and demand for EC2 spare capacity. If the Spot price exceeds the maximum price you specify for a given instance or if capacity is no longer available, your instance will automatically be interrupted.
         Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if you don't mind if your applications get interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks. 
    * Dedicated instance (phythical) - can be used if you require your instance be physically isolated at the host hardware level from instances that belong to other AWS accounts.
        > https://aws.amazon.com/ec2/dedicated-hosts/
        Dedicated instances are used when you need your instances to be physically isolated at the host hardware level from instances that belong to other AWS accounts. Dedicated instances are significantly more expensive than Spot Instances

SSM - simple systems manager
set connection
system manager
session manager

### pricing
EC2 instance pricing varies depending on many variables:
- The buying option (On-demand, Reserved, Spot, Dedicated)
- Selected AMI
- Selected instance type
- Region
- Data Transfer in/out
- Storage capacity.

### AMI
> https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html

Amazon Mashine Images
You may create image as a base image

## ACM

AWS Certificate manager tls

### Auto scaling (Load balancing/scaling)
> https://aws.amazon.com/autoscaling/

May create **Auto Scaling Group** to AMI by creating launch configuration
Min and max server is runing, set subnet etc

## Elastic Load Balancing (Load	balancing/scaling)
> https://aws.amazon.com/elasticloadbalancing/

Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions. It can handle the varying load of your application traffic in a single Availability Zone or across multiple Availability Zones.

Tree types of balancing:
* Application Load Balancer - Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers. Operating at the individual request level (Layer 7), Application Load Balancer routes traffic to targets within Amazon Virtual Private Cloud (Amazon VPC) based on the content of the request.

* Network Load Balancer - Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP) and Transport Layer Security (TLS) traffic where extreme performance is required. Operating at the connection level (Layer 4), Network Load Balancer routes traffic to targets within Amazon Virtual Private Cloud (Amazon VPC) and is capable of handling millions of requests per second while maintaining ultra-low latencies. Network Load Balancer is also optimized to handle sudden and volatile traffic patterns.

* Classic Load Balancer - Classic Load Balancer provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. Classic Load Balancer is intended for applications that were built within the EC2-Classic network.

* Highly available
* Secure
* Elastic
* Flexible
* Robust monitoring & auditing
* Hybrid load balancing

## EBS (Storage)
> https://aws.amazon.com/ebs/

Amazon EBS is a block-level storage that provides storage volumes for use with Amazon EC2 and Amazon RDS instances.
Block starage for extend you VPS server instead of install you own database on ES2 instance.

## SWF
Amazon Simple Workflow Service (SWF) 

## ECR

Amazon Elastic Container Registry (ECR) is a Docker container registry that allows developers to store, manage, and deploy Docker container images.

## EFS (Storage)
> https://aws.amazon.com/efs/

Amazon Elastic File System (Amazon EFS) is a file storage service for Amazon Elastic Compute Cloud (Amazon EC2) instances.
Amazon EFS is a file-level storage technology that provides massively parallel shared access to thousands of Amazon EC2 instances, enabling your applications to achieve high levels of aggregate throughput and IOPS with consistently low latencies.

## Amazon Instance Store

An instance store provides temporary block-level storage for your EC2 instances. Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content.

## Elastic Beanstalk (Deploying)
> https://aws.amazon.com/elasticbeanstalk/

AWS Elastic Beanstalk is an applic­ation container for deploying and managing applic­ations.

Service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.

You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.

Benefits:
 * Fast and simple to begin
 * Developer productivity
 * Impossible to outgrow
 * Complete resource control

## OpsWorks

AWS OpsWorks is a DevOps platform for managing applic­ations of any scale or complexity on the AWS cloud.
AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers.


## CloudFront (Deploy)
> https://aws.amazon.com/cloudfront/

Amazon CloudFront provides a way to distribute content to end-users with low latency and high data transfer speeds.

Content delivery network (CDN). Securely delivery data. Integrated with AWS – both physical locations that are directly connected to the AWS global infrastructure, as well as other AWS services. 

select delivery method
create a distribution 
* Fast & globa
* Security at the Edge caches
* Highly programmable
* Deep integration with AWS

### Payment
If you use AWS origins such as Amazon S3, Amazon EC2 or Elastic Load Balancing, you don’t pay for any data transferred between these services and CloudFron

## Route 53 (Networking)
> https://aws.amazon.com/route53/

Amazon Route 53 is a scalable and highly available Domain Name System (DNS) and Domain Name Regist­ration service.

DNS, DNS health checks (route traffic to healthy endpoints or to independently monitor the health of your application and its endpoints), buy domain, routing traffic
Amazon Route 53 effectively connects user requests to infrastructure running in AWS – such as Amazon EC2 instances, Elastic Load Balancing load balancers, or Amazon S3 buckets – and can also be used to route users to infrastructure outside of AWS. You can use Amazon Route 53 to configure DNS health checks to route traffic to healthy endpoints or to independently monitor the health of your application and its endpoints. Amazon Route 53 Traffic Flow makes it easy for you to manage traffic globally through a variety of routing types, including Latency Based Routing, Geo DNS, Geoproximity, and Weighted Round Robin—all of which can be combined with DNS Failover in order to enable a variety of low-latency, fault-tolerant architectures. Using Amazon Route 53 Traffic Flow’s simple visual editor, you can easily manage how your end-users are routed to your application’s endpoints—whether in a single AWS region or distributed around the globe. Amazon Route 53 also offers Domain Name Registration – you can purchase and manage domain names such as example.com and Amazon Route 53 will automatically configure DNS settings for your domains.


## Inspector (Security)

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. Amazon Inspector automatically assesses applications for vulnerabilities or deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by level of severity. These findings can be reviewed directly or as part of a detailed assessment report which is available via the Amazon Inspector console or API. To help get started quickly, Amazon Inspector includes a knowledge base of hundreds of rules mapped to common security best practices and vulnerability definitions. Examples of built-in rules include checking for remote root login being enabled, or vulnerable software versions installed. These rules are regularly updated by AWS security researchers.

Network and Host Assessments
one popular CIS 699 checks

## WAF (Security)
> https://aws.amazon.com/waf/

Web app firewall.
Wright you oun rules to HTTP 
Use a ruleset from AWS 
can be attached to either CloudFront or an Application load balancer
Protect from OWASP Top 10   

If Sheld does not work well from the box.
Web application firewall that helps protect your web applications or APIs against common web exploits that may affect availability, compromise security, or consume excessive resources.

WAF gives you control over how traffic reaches your applications by enabling you to create security rules that block common attack patterns, such as SQL injection or cross-site scripting, and rules that filter out specific traffic patterns you define. You can get started quickly using Managed Rules for AWS WAF, a pre-configured set of rules managed by AWS or AWS Marketplace Sellers. The Managed Rules for WAF address issues like the OWASP Top 10 security risks. These rules are regularly updated as new issues emerge. AWS WAF includes a full-featured API that you can use to automate the creation, deployment, and maintenance of security rules.

You can deploy AWS WAF on Amazon CloudFront as part of your CDN solution, the Application Load Balancer that fronts your web servers or origin servers running on EC2, or Amazon API Gateway for your APIs.

* Agile protection against web attacks
* Save time with managed rules
* Improved web traffic visibility
* Ease of deployment & maintenance
* Cost effective web application protection
* Security integrated with how you develop applications

### Payment
With AWS WAF, you pay only for what you use. The pricing is based on how many rules you deploy and how many web requests your application receives. There are no upfront commitments.

## Shield (Security, Load balancing/scaling)
> https://aws.amazon.com/shield/

Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection. 

There are two tiers of AWS Shield - Standard and Advanced.

Standart:
    * All AWS customers benefit from the automatic protections of AWS Shield Standard, at no additional charge. 
    * AWS Shield Standard defends against most common, frequently occurring network and transport layer DDoS attacks that target your web site or applications. 
    * When you use AWS Shield Standard with Amazon CloudFront and Amazon Route 53, you receive comprehensive availability protection against all known infrastructure (Layer 3 and 4) attacks.

For higher levels of protection against attacks targeting your applications running on Amazon Elastic Compute Cloud (EC2), Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator and Amazon Route 53 resources, you can subscribe to AWS Shield Advanced.

Advanced:
    * In addition to the network and transport layer protections that come with Standard, AWS Shield Advanced provides additional detection and mitigation against large and sophisticated DDoS attacks, near real-time visibility into attacks, and integration with AWS WAF, a web application firewall.
    * also gives you 24x7 access to the AWS DDoS Response Team (DRT) and protection against DDoS related spikes in your Amazon Elastic Compute Cloud (EC2), Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator and Amazon Route 53 charges.
    * available globally on all Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 edge locations. You can protect your web applications hosted anywhere in the world by deploying Amazon CloudFront in front of your application. Your origin servers can be Amazon S3, Amazon Elastic Compute Cloud (EC2), Elastic Load Balancing (ELB), or a custom server outside of AWS. 
    * You can also enable AWS Shield Advanced directly on an Elastic IP or Elastic Load Balancing (ELB) in the following AWS Regions - Northern Virginia, Ohio, Oregon, Northern California, Montreal, São Paulo, Ireland, Frankfurt, London, Paris, Stockholm, Singapore, Tokyo, Sydney, Seoul, and Mumbai.

* Seamless integration and deployment
* Customizable protection
* Managed Protection and Attack Visibility
* Cost Efficient

## Guard Duty (Security)

IDS/IPC - Intrusion Detection System an Intrusion Protection System

AWS Guard Duty is a trreat detection service that cotinuously monitors for mailicious, suspicious activity an unauthorised behavior. It uses ML to analyze:
    * CloudTrail logs
    * VPC Flow logs
    * DNS logs
will alert uou of Findings which you can automate via CloudWatch or 3-rd part services 

## Pentesting (Security)

 AWS customers are welcome to carry out security assessments and penetration tests against their AWS infrastructure without prior approval for 8 services:

1- Amazon EC2 instances, NAT Gateways, and Elastic Load Balancers.
2- Amazon RDS.
3- Amazon CloudFront.
4- Amazon Aurora.
5- Amazon API Gateways.
6- AWS Lambda and Lambda Edge functions.
7- Amazon Lightsail resources.
8- Amazon Elastic Beanstalk environments.
For other simulated events you will need to submit a request to AWS. A reply could take up to 7 days

## S3 (Storage)
> https://aws.amazon.com/s3/

Amazon Simple Storage Service (S3)  
Amazon S3 is an object level storage built to store and retrieve any amount of data from anywhere – web sites and mobile apps, corporate applications, and data from IoT sensors or devices. It is designed to deliver 99.999999999% durability, and stores data for millions of applications used by market leaders in every industry.

This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for 99.999999999% (11 9's) of durability, and stores data for millions of applications for companies all around the world.

* Industry-leading performance, scalability, availability, and durability
* Wide range of cost-effective storage classes
* Unmatched security, compliance, and audit capabilities
* Easily manage data and access controls
* Query-in-place services for analytics
* Most supported cloud storage service

### S3 Storage classes
> https://aws.amazon.com/s3/storage-classes/

* The S3 Intelligent-Tiering 
    Storage class is designed to optimize costs by automatically moving data to the most cost-effective access tier, without performance impact or operational overhead. It works by storing objects in two access tiers: one tier that is optimized for frequent access and another lower-cost tier that is optimized for infrequent access. For a small monthly monitoring and automation fee per object, Amazon S3 monitors access patterns of the objects in S3 Intelligent-Tiering, and moves the ones that have not been accessed for 30 consecutive days to the infrequent access tier. If an object in the infrequent access tier is accessed, it is automatically moved back to the frequent access tier. There are no retrieval fees when using the S3 Intelligent-Tiering storage class, and no additional tiering fees when objects are moved between access tiers. It is the ideal storage class for long-lived data with access patterns that are unknown or unpredictable.
* S3 Standard offers high durability, availability, and performance object storage for frequently accessed data.
* Amazon S3 Standard-Infrequent Access (S3 Standard-IA) is for data that is accessed less frequently, but requires rapid access when needed.
* S3 Glacier is a low-cost storage class for data archiving.

## Snowball
> https://aws.amazon.com/snowball/

Petabyte-scale data transport solution that uses devices designed to be secure to transfer large amounts of data into and out of the AWS Cloud. 

Using Snowball addresses common challenges with large-scale data transfers including high network costs, long transfer times, and security concerns. Customers today use Snowball to migrate analytics data, genomics data, video libraries, image repositories, backups, and to archive part of data center shutdowns, tape replacement or application migration projects. Transferring data with Snowball is simple, fast, more secure, and can be as little as one-fifth the cost of transferring data via high-speed Internet.

With Snowball, you don’t need to write any code or purchase any hardware to transfer your data. Simply create a job in the AWS Management Console ("Console") and a Snowball device will be automatically shipped to you. Once it arrives, attach the device to your local network, download and run the Snowball Client ("Client") to establish a connection, and then use the Client to select the file directories that you want to transfer to the device. The Client will then encrypt and transfer the files to the device at high speed. Once the transfer is complete and the device is ready to be returned, the E Ink shipping label will automatically update and you can track the job status via Amazon Simple Notification Service (SNS), text messages, or directly in the Console.

* High speed
* Extremely scalable
* Tamper resistant and secure
* Simple and compatible
* Low cost
* Easy data retrieval

## Glacier (Storage)
> https://aws.amazon.com/glacier/

Amazon Glacier is a low-cost storage service that provides secure and durable storage for data archiving and backup.
Chiper but longer than S3

Amazon S3 Glacier and S3 Glacier Deep Archive are a secure, durable, and extremely low-cost Amazon S3 cloud storage classes for data archiving and long-term backup. They are designed to deliver 99.999999999% durability, and provide comprehensive security and compliance capabilities that can help meet even the most stringent regulatory requirements. Customers can store data for as little as $1 per terabyte per month, a significant savings compared to on-premises solutions. To keep costs low yet suitable for varying retrieval needs, Amazon S3 Glacier provides three options for access to archives, from a few minutes to several hours, and S3 Glacier Deep Archive provides two access options ranging from 12 to 48 hours.

Ways to get data from Glacier:
 * SDK
 * API
 * lifetime policy

* RETRIEVALS AS QUICK AS 1-5 MINUTES
* UNMATCHED DURABILITY & SCALABILITY
* MOST COMPREHENSIVE SECURITY & COMPLIANCE CAPABILITIES
* Low cost
* MOST SUPPORTED BY PARTNERS, VENDORS, & AWS SERVICES

## RDS (Database)
> https://aws.amazon.com/rds/

Amazon Relational Database Service (RDS) makes it easy to set up, operate, and scale familiar relational databases in the cloud.

Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks such as hardware provisioning, database setup, patching and backups. It frees you to focus on your applications so you can give them the fast performance, high availability, security and compatibility they need.

Amazon RDS is available on several database instance types - optimized for memory, performance or I/O - and provides you with six familiar database engines to choose from, including Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle Database, and SQL Server. You can use the AWS Database Migration Service to easily migrate or replicate your existing databases to Amazon RDS.

* Easy to administer
* Highly scalable
* Available and durable
* Fast
* Secure
* Inexpensive (on demand)

## Aurora (Database)
> https://aws.amazon.com/rds/aurora/

MySQL and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.

Amazon Aurora is up to **five times faster than standard MySQL databases** and **three times faster than standard PostgreSQL databases**. It provides the security, availability, and reliability of commercial databases at 1/10th the cost. Amazon Aurora is fully managed by Amazon Relational Database Service (RDS), which automates time-consuming administration tasks like hardware provisioning, database setup, patching, and backups.

Amazon Aurora features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 64TB per database instance. It delivers high performance and availability with up to 15 low-latency read replicas, point-in-time recovery, continuous backup to Amazon S3, and replication across three Availability Zones (AZs).

* High Performance and Scalability
* High Availability and Durability
* Highly Secure
* MySQL and PostgreSQL Compatible
* Fully Managed
* Migration Support

## DynamoDB (Database)
> https://aws.amazon.com/dynamodb/

Amazon DynamoDB is a scalable NoSQL (key-value) data store that manages distri­buted replicas of your data for high availa­bility.

Amazon DynamoDB is a key-value and document database that delivers single-digit millisecond performance at any scale. It's a fully managed, multiregion, multimaster, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications. DynamoDB can handle more than 10 trillion requests per day and can support peaks of more than 20 million requests per second.

1- Performance at scale:
    DynamoDB supports some of the world’s largest scale applications by providing consistent, single-digit millisecond response times at any scale. You can build applications with virtually unlimited throughput and storage.
2- Serverless:
    With DynamoDB, there are no servers to provision, patch, or manage and no software to install, maintain, or operate. DynamoDB automatically scales tables up and down to adjust for capacity and maintain performance.
3- Highly available:
    Availability and fault tolerance are built in, eliminating the need to architect your applications for these capabilities.

* Performance at scale
* No servers to manage
* Enterprise ready (ACID)

## DocumentDB (Database)

Does not support MySQL

## Athena

Amazon Athena is an interactive query service that is mainly used to analyze data in Amazon S3 using standard SQL.

## Redshift (Database)
> https://aws.amazon.com/redshift/

Amazon Redshift is a fast, fully managed, petaby­te-­scale data warehouse that makes it cost-e­ffe­ctive to analyze all your data using your existing business intell­igence tools.

No other data warehouse makes it as easy to gain new insights from all your data. With Redshift you can query petabytes of structured and semi-structured data across your data warehouse and your data lake using standard SQL. Redshift lets you easily save the results of your queries back to your S3 data lake using open formats like Apache Parquet to further analyze from other analytics services like Amazon EMR, Amazon Athena, and Amazon SageMaker.

Redshift is the world’s fastest cloud data warehouse and gets faster every year. For performance intensive workloads you can use the new RA3 instances to get up to 3x the performance of any cloud data warehouse.
Preview the next generation of Redshift with AQUA (Advanced Query Accelerator)
AQUA is a new distributed and hardware accelerated cache that allows Redshift to run up to 10x faster than any other cloud data warehouse.

### Pricing
Amazon Redshift costs less to operate than any other cloud data warehouse
Start small at $0.25 per hour and scale up to petabytes for under $1000 per terabyte per year. Pay only for what you use and know how much you'll spend with predictable monthly costs. Amazon Redshift is at least 50% less expensive than all other cloud data warehouses.

Scale and pay for storage and compute separately and get the optimal amount of storage and compute for diverse workloads. Choose the size of your Redshift cluster based on your performance requirements, and only pay for the storage that you use. The new managed storage automatically scales your data warehouse storage capacity without you having to add and pay for additional compute instances.

## DMS
> https://aws.amazon.com/dms/

AWS Database Migration Service (DMS) helps you migrate databases to the cloud easily and securely while minimizing downtime.

AWS Database Migration Service helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. The AWS Database Migration Service can migrate your data to and from most widely used commercial and open-source databases.

AWS Database Migration Service supports homogeneous migrations such as Oracle to Oracle, as well as heterogeneous migrations between different database platforms, such as Oracle or Microsoft SQL Server to Amazon Aurora. With AWS Database Migration Service, you can continuously replicate your data with high availability and consolidate databases into a petabyte-scale data warehouse by streaming data to Amazon Redshift and Amazon S3.

* Simple to use
* Minimal downtime
* Supports widely used databases
* Low cost
* Fast and easy to set-up
* Relable

## EMR
> https://aws.amazon.com/emr/

Amazon Elastic MapReduce lets you perform big data tasks such as web indexing, data mining, and log file analysis.

EMR is used to process vast amounts of data easily and securely. Use cases include: big data,log analysis, web indexing, data transformations (ETL), machine learning, financial analysis, scientific simulation, and bioinformatics.

Amazon EMR is the industry leading cloud-native big data platform for processing vast amounts of data quickly and cost-effectively at scale. 
Using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi (Incubating), and Presto, coupled with the dynamic scalability of Amazon EC2 and scalable storage of Amazon S3, **EMR gives analytical teams the engines and elasticity to run Petabyte-scale analysis for a fraction of the cost of traditional on-premises clusters**. EMR gives teams the flexibility to run use cases on single-purpose, short lived clusters that automatically scale to meet demand, or on long running highly available clusters using the new multi-master deployment mode. 
If you have existing on-premises deployments of open source tools such as Apache Spark and Apache Hive, you can also run EMR clusters on AWS Outposts, giving you both the ability to scale out on-premises via Outposts or in the cloud.

* EASY TO USE
* Low cost
* Elastic
* RELIABLE* Seure
* Flexible

## QuickStart

**Prebuilt templates** to **help you deploy popular stacks**

Composet of 3 part:
1. Reference architecture for deployment
2. AWS CloudFormation templates tha automate and confugure the deployment
3. A deployment guide explaining the architecture and implementation in detail

AWS Quick Start Reference Deployments outline the architectures for popular enterprise solutions on AWS and provide AWS CloudFormation templates to automate their deployment. Each Quick Start launches, configures, and runs the AWS compute, network, storage, and other services required to deploy a specific workload on AWS, using AWS best practices for security and availability.

Quick Starts are built by AWS solutions architects and partners to help you deploy popular technologies on AWS, based on AWS best practices. These accelerators reduce hundreds of manual installation and configuration procedures into just a few steps, so you can build your production environment quickly and start using it immediately.

## X-Ray

AWS X-Ray helps developers analyze and debug production, distributed applications, such as those built using a microservices architecture. With X-Ray, you can understand how your application and its underlying services are performing to identify and troubleshoot the root cause of performance issues and errors.

## Cloud9 
> https://aws.amazon.com/cloud9/

A cloud IDE for writing, running, and debugging code

## CloudTrail (Logging and Monitoring)
> https://aws.amazon.com/cloudtrail/

AWS CloudTrail provides increased visibility into user activity by recording API calls made on your account.

AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of your AWS account. With CloudTrail, you can log, continuously monitor, and retain account activity related to actions across your AWS infrastructure. CloudTrail provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. This event history simplifies security analysis, resource change tracking, and troubleshooting. In addition, you can use CloudTrail to detect unusual activity in your AWS accounts. These capabilities help simplify operational analysis and troubleshooting.

* Simplified compliance
* Visibility into user and resource activity
* Security analysis and troubleshooting
* Security automation

## Elasticsearch Service (Logging)
> https://aws.amazon.com/elasticsearch-service/

Amazon Elasticsearch Service is a fully managed service that makes it easy for you to deploy, secure, and run Elasticsearch cost effectively at scale. You can build, monitor, and troubleshoot your applications using the tools you love, at the scale you need. The service provides support for open source Elasticsearch APIs, managed Kibana, integration with Logstash and other AWS services, and built-in alerting and SQL querying. Amazon Elasticsearch Service lets you pay only for what you use – there are no upfront costs or usage requirements. With Amazon Elasticsearch Service, you get the ELK stack you need, without the operational overhead.

## CloudWatch (Monitoring)
> https://aws.amazon.com/cloudwatch/
Alarms

Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing you with a unified view of AWS resources, applications, and services that run on AWS and on-premises servers. You can use CloudWatch to detect anomalous behavior in your environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep your applications

* Observability on a single platform across applications and infrastructure
* Easiest way to collect metrics in AWS and on-premises
* Improve operational performance and resource optimization
* Get operational visibility and insight
* Derive actionable insights from logs

## AWS Service Catalog
AWS Service Catalog allows organizations to create and manage catalogs of IT services that are approved for use on AWS. These IT services can include everything from virtual machine images, servers, software, and databases to complete multi-tier application architectures. AWS Service Catalog allows you to centrally manage commonly deployed IT services, and helps you achieve consistent governance and meet your compliance requirements, while enabling users to quickly deploy only the approved IT services they need.


## Kinesis Data Firehose
> https://aws.amazon.com/kinesis/data-firehose/

Amazon Kinesis services make it easy to work with real-time streaming data in the AWS cloud.
Connect data streams from different applications and then provides it as highly avalable real-time data stream to another application.

Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data lakes, data stores and analytics tools. It can capture, transform, and load streaming data into Amazon S3, Amazon Redshift, Amazon Elasticsearch Service, and Splunk, enabling near real-time analytics with existing business intelligence tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match the throughput of your data and requires no ongoing administration. It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage used at the destination and increasing security.

You can easily create a Firehose delivery stream from the AWS Management Console, configure it with a few clicks, and start sending data to the stream from hundreds of thousands of data sources to be loaded continuously to AWS – all in just a few minutes. You can also configure your delivery stream to automatically convert the incoming data to columnar formats like Apache Parquet and Apache ORC, before the data is delivered to Amazon S3, for cost-effective storage and analytics.

* Easy to use
* Integrated with AWS data lakes and data stores
* Serverless data transformation
* Near real-time
* No ongoing administration
* Pay only for what you use

## Lambda (Compute)
> https://aws.amazon.com/lambda/

AWS Lambda is a compute service that runs your code in response to events and automa­tically manages the compute resources for you.

With Lambda, you can run code for virtually any type of application or backend service - all with zero administration. Just upload your code and Lambda takes care of everything required to run and scale your code with high availability. You can set up your code to automatically trigger from other AWS services or call it directly from any web or mobile app.

select language
create permission 
add cloudwatch metrics

just for 15 min or less

* NO SERVERS TO MANAGE
* CONTINUOUS SCALING
* SUBSECOND METERING
* CONSISTENT PERFORMANCE

## CloudFormation (Deploying)
> https://aws.amazon.com/cloudformation/

AWS CloudF­orm­ation lets you create and update a collection of related AWS resources in a predic­table fashion.

AWS CloudFormation provides a common language for you to model and provision AWS and third party application resources in your cloud environment. AWS CloudFormation allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This gives you a single source of truth for your AWS and third party resources.

* Model it all
* Automate & deploy
* It's just code

## Amplify (Develop)
> https://aws.amazon.com/amplify/

AWS Amplify is a development platform for building secure, scalable mobile and web applications. It makes it easy for you to authenticate users, securely store data and user metadata, authorize selective access to data, integrate machine learning, analyze application metrics, and execute server-side code. Amplify covers the complete mobile application development workflow from version control, code testing, to production deployment, and it easily scales with your business from thousands of users to tens of millions. The Amplify libraries and CLI, part of the Amplify Framework, are open source and offer a pluggable interface that enables you to customize and create your own plugins.

## AppSync (Develop)
> https://aws.amazon.com/appsync/

Power your applications with the right data, from one or more data sources, at global scale

AWS AppSync simplifies application development by letting you create a flexible API to securely access, manipulate, and combine data from one or more data sources. AppSync is a managed service that uses GraphQL to make it easy for applications to get exactly the data they need.

With AppSync, you can build scalable applications, including those requiring real-time updates, on a range of data sources such as NoSQL data stores, relational databases, HTTP APIs, and your custom data sources with AWS Lambda. For mobile and web apps, AppSync additionally provides local data access when devices go offline, and data synchronization with customizable conflict resolution, when they are back online.

## CodeStar (Deploy)
> https://aws.amazon.com/codestar/

AWS CodeStar enables you to quickly develop, build, and deploy applications on AWS. AWS CodeStar provides a unified user interface, enabling you to easily manage your software development activities in one place. With AWS CodeStar, you can set up your entire continuous delivery toolchain in minutes, allowing you to start releasing code faster. AWS CodeStar makes it easy for your whole team to work together securely, allowing you to easily manage access and add owners, contributors, and viewers to your projects. Each AWS CodeStar project comes with a project management dashboard, including an integrated issue tracking capability powered by Atlassian JIRA Software. With the AWS CodeStar project dashboard, you can easily track progress across your entire software development process, from your backlog of work items to teams’ recent code deployments. Visit here to learn more.

There is no additional charge for using AWS CodeStar. You only pay for the AWS resources that you provision for developing and running your application (for example, Amazon EC2 instances).

## lightSail

## TCO Calculators (Billing)
> https://aws.amazon.com/tco-calculator/

AWS helps you reduce Total Cost of Ownership (TCO) by reducing the need to invest in large capital expenditures and providing a pay-as-you-go model that empowers you to invest in the capacity you need and use it only when the business requires it.

Our TCO calculators allow you to estimate the cost savings when using AWS.
Provide you a detailed set of reports that can be used in executive presentations.
The calculators also give you the option to modify assumptions that best meet your business needs.
Tool for approximation porposes only

## Landing Zone (Billing)

Help **Enterprises** quickly set-up a secure AWS multy account
Provides you with **baseline env** to get started with multy-account architecture

### AWM
AWS Account Vending Mashine
Automatically provisions and configure new account via Service Catalog Template
Uses Singl Sing-on (SSO) foe managing and accessing ccounts

Env is customizable to allow customers to implement their own acc baselines throug a Landing Zone  configuration and updte pipeline

## Resources Groups and Tagging (Billing)

**Tags** - words or phrases that act as metadata for organisation you AWS resources
**Resources groups** - collection of resources that share one or more **tags**

Helps you organize and consolidate information based on yu project and the resources that you use

Resources Groups can display details about group of resources based on:
 * Metrics
 * Alarms
 * Configuration settings

At any time you can modify settings of you resources groups to change what resources appear

## Cost and Usage Report (Billing)

Generate a detailed spreadsheet enabling you to better analyse and understanfing you AWS account
Places into S3
Use Athena to turn the report into a queryable database
Use QuickSight to visualise you billing datagraphs


## QuickSight
> https://aws.amazon.com/quicksight/

First BI Service with Pay-per-Session Pricing and ML Insights for everyone.

Amazon QuickSight is a fast, cloud-powered business intelligence service that makes it easy to deliver insights to everyone in your organization.

As a fully managed service, QuickSight lets you easily create and publish interactive dashboards that include ML Insights. Dashboards can then be accessed from any device, and embedded into your applications, portals, and websites.

With our Pay-per-Session pricing, QuickSight allows you to give everyone access to the data they need, while only paying for what you use.

## Cost Explorer (Billing)
> https://aws.amazon.com/aws-cost-management/aws-cost-explorer/

AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.

Get started quickly by creating custom reports that analyze cost and usage data. Analyze your data at a high level (for example, total costs and usage across all accounts) or dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies.

## AWS Compliance Programs
> https://aws.amazon.com/compliance/programs/

Compliance Programs - set of internal polices and procedures  of a company to comly with laws, rules and regulations or to uphold business reputation

## AWS Artifact

checklist

AWS Artifact is a self-service audit artifact retrieval portal that provides customers with on-demand access to AWS’ compliance documentation and AWS agreements. You can use AWS Artifact Agreements to review, accept, and track the status of AWS agreements such as the Business Associate Addendum (BAA).

> Additional information:
> You can also use AWS Artifact Reports to download AWS security and compliance documents, such as AWS ISO certifications, Payment Card Industry (PCI), and System and Organization Control (SOC) reports.

## Organizations 

AWS Organizations provides central governance and management across multiple AWS accounts.
root account
organisation units -> users

## AWS Systems Manager

AWS Systems Manager gives you visibility and control of your infrastructure on AWS. Systems Manager provides a unified user interface so you can view operational data from multiple AWS services and allows you to automate operational tasks across your AWS resources.

## AWS Config

AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

## Certificate Manager

AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources

## AWS MFA

AWS Multi-Factor Authentication (MFA) is a simple best practice that adds an extra layer of protection on top of using just your user name and password to authenticate.

## Shared Responsibility Model (Security)
> https://aws.amazon.com/compliance/shared-responsibility-model/
![](https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg)

You - 
    Data
    Configuration
    Customer data
    Platform, app, Indentity, IAM
    OPerating system, Net firewall
    Client side data encrypt and data integrity Auth
    Server side encryption
    New traffic protection

aws - 
    hardware
        region, az, edge
    soft
        Compute, storage, DB, Networking
    operation of managed services
    Global infrastructure
    

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment. As shown in the chart below, this differentiation of responsibility is commonly referred to as Security “of” the Cloud versus Security “in” the Cloud.

**AWS responsibility “Security of the Cloud”** - AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.

**Customer responsibility “Security in the Cloud”** – Customer responsibility will be determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and, as such, requires the customer to perform all of the necessary security configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by the customer on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. For abstracted services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.

This customer/AWS shared responsibility model also extends to IT controls. Just as the responsibility to operate the IT environment is shared between AWS and its customers, so is the management, operation and verification of IT controls shared. AWS can help relieve customer burden of operating controls by managing those controls associated with the physical infrastructure deployed in the AWS environment that may previously have been managed by the customer. As every customer is deployed differently in AWS, customers can take advantage of shifting management of certain IT controls to AWS which results in a (new) distributed control environment. Customers can then use the AWS control and compliance documentation available to them to perform their control evaluation and verification procedures as required. Below are examples of controls that are managed by AWS, AWS Customers and/or both.

**Inherited Controls** – Controls which a customer fully inherits from AWS.
* Physical and Environmental controls

**Shared Controls** – Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:
* Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
* Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
* Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.

**Customer Specific** – Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include:
* Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.

## IAM (Security)
> https://aws.amazon.com/iam/

AWS Identity and Access Management (IAM) lets you securely control access to AWS services and resources.

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

IAM is a feature of your AWS account offered at no additional charge. You will be charged only for use of other AWS services by your users.

May add MFA multi-factor authentication on Root Account.

Create individual IAM user

IAM password policy

## KMS (Security)
> https://aws.amazon.com/kms/

AWS Key Management Service (AWS KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.

AWS Key Management Service (KMS) makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. AWS KMS is a secure and resilient service that uses hardware security modules that have been validated under FIPS 140-2, or are in the process of being validated, to protect your keys. AWS KMS is integrated with AWS CloudTrail to provide you with logs of all key usage to help meet your regulatory and compliance needs.

* Fully managed
* Centralized key management
* Manage encryption for AWS services
* Encrypt data in your applications
* Digitally sign data
* Low cost
* Secure
* Compliance
* Built-in auditing

## Macie (Security)
> https://aws.amazon.com/macie/

A machine learning-powered security service to discover, classify, and protect sensitive data.

monitors S3 data access activity. Works by ML  to Analyze you CloudTrail logs
variety of alerts

## Security Groups vs NACLs (Security)

**Security Groups**
Act as firewall at the **instance** level
Implicity denies all traffic/ You create Allow rules
Eg Allow on EC@ instance on port 22 for ssh

**NACLs**
Security Groups
Act as firewall at the **subnet** level
 You create Allow and Deny rules
Eg Block a specific IP address

## Cognito (Security)
> https://aws.amazon.com/cognito/

Service that provides th login and sign in and access control functionality to your app that you use/
Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0.

## Suport plan
> https://aws.amazon.com/premiumsupport/plans/

At AWS, we want you to be successful. Our Support plans are designed to give you the right mix of tools and access to expertise so that you can be successful with AWS while optimizing performance, managing risk, and keeping costs under control.

Basic Support is included for all AWS customers and includes:

Customer Service & Communities - 24x7 access to customer service, documentation, whitepapers, and support forums.

AWS Trusted Advisor - Access to the 7 core Trusted Advisor checks and guidance to provision your resources following best practices to increase performance and improve security.

AWS Personal Health Dashboard - A personalized view of the health of AWS services, and alerts when your resources are impacted.

Plans: Developer - Unlimited cases / 1 primary contact, Business, Enterprise.

Support
Basic:
 • 7 trusted advisor checks, personal health dashboard, docs/support forms
Developer:
 • Basic + email support
 • 1 contact
 • Response time 24 hours for general, 12 hours for impaired system
Business:
 • Developer + full trusted advisor checks, phone support
• Unlimited contacts
• Response time 1 hour for prod down
Enterprise:
 • Business + senior cloud support engineers
 • Response time 15 minutes for business critical systems
 • Includes Well Architected Review by AWS Solution Architects, self packed labs, concierge support team, dedicated technical account manager 
Support forms for:
• Encountering Abuse (sent to Abuse team)
• Increasing limits beyond a point
• Penetration testing
Acceptable Use Policy:
 • What	you’d expect; don’t do bad things

## Support Concierge

Included as part of the Enterprise Support plan, the Support Concierge Team are AWS billing and account experts that specialize in working with enterprise accounts. The Concierge team will quickly and efficiently assist you with your billing and account inquiries, and work with you to help implement billing and account best practices so that you can focus on running your business.

Support Concierge service includes:

** 24 x7 access to AWS billing and account inquires.

** Guidance and best practices for billing allocation, reporting, consolidation of accounts, and root-level account security.

** Access to Enterprise account specialists for payment inquiries, training on specific cost reporting, assistance with service limits, and facilitating bulk purchases.

## Support API
The AWS Support API provides programmatic access to AWS Support Center features to create, manage, and close your support cases, and operationally manage your Trusted Advisor check requests and status.

## Operations Support 

AWS Operations Support is an Enterprise support program that provides operations assessments and analysis to identify gaps across the operations lifecycle, as well as recommendations based on best practices.

## Abuse Team
> https://aws.amazon.com/premiumsupport/knowledge-center/report-aws-abuse/

The AWS Abuse team can assist you when AWS resources are being used to engage in the following types of abusive behavior:     

I. Spam: You are receiving unwanted emails from an AWS-owned IP address, or AWS resources are being used to spam websites or forums.

II. Port scanning: Your logs show that one or more AWS-owned IP addresses are sending packets to multiple ports on your server, and you believe this is an attempt to discover unsecured ports.

III. Denial of service attacks (DOS): Your logs show that one or more AWS-owned IP addresses are being used to flood ports on your resources with packets, and you believe this is an attempt to overwhelm or crash your server or software running on your server.    

IV. Intrusion attempts: Your logs show that one or more AWS-owned IP addresses are being used to attempt to log in to your resources.

V. Hosting objectionable or copyrighted content: You have evidence that AWS resources are being used to host or distribute illegal content or distribute copyrighted content without the consent of the copyright holder.

VI. Distributing malware: You have evidence that AWS resources are being used to distribute software that was knowingly created to compromise or cause harm to computers or machines on which it is installed.



## AWS Trusted Advisor

7 for free

AWS Trusted Advisor offers a rich set of best practice checks and recommendations across five categories: cost optimization; security; fault tolerance; performance; and service limits. Like your customized cloud security expert, AWS Trusted Advisor analyzes your AWS environment and provides security recommendations to protect your AWS environment. The service improves the security of your applications by closing gaps, examining permissions, and enabling various AWS security features.

AWS Trusted Advisor is an online tool that provides you real time guidance to help you provision your resources following AWS best practices. AWS Trusted Advisor offers a rich set of best practice checks and recommendations across five categories: cost optimization; security; fault tolerance; performance; and service limits.

AWS Trusted Advisor improves the security of your application by closing gaps, enabling various AWS security features, and examining your permissions.

The core security checks include: (Important)
1- Security Groups - Specific Ports Unrestricted.
Checks security groups for rules that allow unrestricted access to specific ports. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data).

2- Amazon S3 Bucket Permissions.
Checks buckets in Amazon Simple Storage Service (Amazon S3) that have open access permissions. Bucket permissions that grant List access to everyone can result in higher than expected charges if objects in the bucket are listed by unintended users at a high frequency. Bucket permissions that grant Upload/Delete access to everyone create potential security vulnerabilities by allowing anyone to add, modify, or remove items in a bucket. This check examines explicit bucket permissions and associated bucket policies that might override the bucket permissions.

3- MFA on Root Account.
Checks the root account and warns if multi-factor authentication (MFA) is not enabled. For increased security, AWS recommends that you protect your account by using MFA, which requires a user to enter a unique authentication code from their MFA hardware or virtual device when interacting with the AWS console and associated websites.

## Consolidated Billing

One bill for all you accounts
You can  designate one master account that pays the charges of all the othe member accounts

Consolidated Billing is offered at no additional cost

Use Cost Explorer to visualize usage for Consolidated Billing

### Volume discounts
Consolidated Billing lets you take advantage of Volume Discounts

## Management Console

The AWS Management Console is used to access and manage Amazon Web Services through a simple and intuitive web-based user interface. The console itself doesn’t provide any recommendations.
The AWS Management Console allows you to access and manage Amazon Web Services through a simple and intuitive web-based user interface. You can also use the AWS Console mobile app to quickly view resources on the go.

Preferences receive builling and other information

### Budgets (Billing)
> https://aws.amazon.com/aws-cost-management/aws-budgets/

AWS Budgets gives you the ability to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

You can also use AWS Budgets to set reservation utilization or coverage targets and receive alerts when your utilization drops below the threshold you define. Reservation alerts are supported for Amazon EC2, Amazon RDS, Amazon Redshift, Amazon ElastiCache, and Amazon Elasticsearch reservations.

## Connect

Amazon Connect is a cloud-based contact center service that makes it easy for businesses to deliver customer service at low cost.

## Concierge Support Team

AWS Concierge Support Team is a specialized offering available only to customers having an Enterprise Support subscription. The Concierge Team assists customers with their billing and account inquiries.


## Infrastructure Event Management
AWS Infrastructure Event Management is a short-term engagement with AWS Support, included in the Enterprise-level Support product offering, and available for additional purchase for Business-level Support subscribers. AWS Infrastructure Event Management partners with your technical and project resources to gain a deep understanding of your use case and provide architectural and scaling guidance for an event. Common use-case examples for AWS Event Management include advertising launches, new product launches, and infrastructure migrations to AWS.


## Personal Health Dashboard
> https://aws.amazon.com/premiumsupport/phd/

AWS Personal Health Dashboard provides alerts and remediation guidance when AWS is experiencing events that may impact you. While the Service Health Dashboard displays the general status of AWS services, Personal Health Dashboard gives you a personalized view into the performance and availability of the AWS services underlying your AWS resources.

The benefits of the AWS personal health dashboard include:
**A personalized View of Service Health: Personal Health Dashboard gives you a personalized view of the status of the AWS services that power your applications, enabling you to quickly see when AWS is experiencing issues that may impact you. For example, in the event of a lost EBS volume associated with one of your EC2 instances, you would gain quick visibility into the status of the specific service you are using, helping save precious time troubleshooting to determine root cause.

**Proactive Notifications: The dashboard also provides forward looking notifications, and you can set up alerts across multiple channels, including email and mobile notifications, so you receive timely and relevant information to help plan for scheduled changes that may affect you. In the event of AWS hardware maintenance activities that may impact one of your EC2 instances, for example, you would receive an alert with information to help you plan for, and proactively address any issues associated with the upcoming change.

**Detailed Troubleshooting Guidance: When you get an alert, it includes remediation details and specific guidance to enable you to take immediate action to address AWS events impacting your resources. For example, in the event of an AWS hardware failure impacting one of your EBS volumes, your alert would include a list of your affected resources, a recommendation to restore your volume, and links to the steps to help you restore it from a snapshot. This targeted and actionable information reduces the time needed to resolve issues.

# Pricing 

AWS consolidated billing enables an organization to consolidate payments for multiple Amazon Web Services (AWS) accounts within a single organization by making a single paying account. For billing purposes, AWS treats all the accounts on the consolidated bill as one account. Some services, such as Amazon EC2 and Amazon S3 have volume pricing tiers across certain usage dimensions that give the user lower prices when they use the service more. For example if you use 50 TB in each account you would normally be charged $23 *50*3 (because they are 3 different accounts), But with consolidated billing you would be charged $23*50+$22*50*2 (because they are treated as one account) which means that you would save $100.

### Free services (Pricing)

IAM
VPC
Organisation & Consolidated Billing
AWS cost Explorer

*Free but can provision AWS Services which cost money*
Auto Scailing
CloudFormation
Elastic Beanstalk
OpsWorks
Amplify
AppSync
CodeStar

## Marketplace
> https://aws.amazon.com/marketplace

digital catalogue with **thousands** of software listings from independent software vendors
May fe free
allows to **sell you soliution** to other AWS customers
