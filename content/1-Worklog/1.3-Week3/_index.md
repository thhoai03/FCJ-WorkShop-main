---
title: "Week 3 - Theoretical Research and Practical Deployment of Amazon EC2 Virtual Server Service"
date: 2026-05-05
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---### Week 3 Objectives:

* Increase website interface loading speed and set up a firewall to prevent cyber attacks at the application layer.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Learn the principles of the Amazon CloudFront Content Delivery Network (CDN), the concept of Edge Location and TTL (Time-To-Live). | May 5, 2026 | May 5, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Learn the Origin Access Control (OAC) security mechanism to isolate the S3 Bucket from the public Internet environment. | May 6, 2026 | May 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Study theory on AWS WAF (Web Application Firewall), Web ACLs operating mechanism, and rule sets (Rules). Configure AWS Route 53 to manage the domain name. | May 7, 2026 | May 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5-6 | Initialize a CloudFront Distribution connected to S3, then configure AWS WAF directly attached to CloudFront to set up malware filtering and block bad IPs. | May 8, 2026 | May 9, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 3 Achievements:

* Understand the nature of CDN networks and master the Amazon CloudFront service: Caching mechanisms at Edge Locations, Data compression optimization methods to increase cake product image loading speed, Manual Cache Invalidation mechanism when updating new source code.

* Successfully configured the OAC (Origin Access Control) security protocol: Completely locked direct access from the Internet to the S3 Bucket, Forced all access traffic to go through the intermediate CloudFront gateway to maximize source code protection.

* Familiarized with and manually configured AWS WAF Web Application Firewall: Initialized the Web ACLs access control list, Installed common anti-attack rule sets (AWS Managed Ruleset), Self-established Rate-based rules to automatically block IPs deliberately spamming continuous requests beyond the allowed threshold (e.g., >100 requests/5 minutes).