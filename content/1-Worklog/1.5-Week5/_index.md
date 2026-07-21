---
title: "Week 5 - Establishing a Secure Custom Virtual Network Architecture with Amazon VPC"
date: 2026-05-18
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---
### Week 5 Objectives:

* Design a high-speed access storage repository for order information and deploy an encryption solution for sensitive customer data.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Learn the theory of the Amazon DynamoDB NoSQL database, table structures (Tables), attributes (Attributes), and data distribution mechanisms. | May 18, 2026 | May 18, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Analyze key design techniques in DynamoDB including Partition Key and Sort Key. | May 19, 2026 | May 19, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Study the AWS KMS (Key Management Service) encryption key management service and secure data encryption standards. | May 20, 2026 | May 20, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Proceed to create tables on DynamoDB, initialize a Customer Managed Key in KMS, and configure data encryption at rest. | May 21, 2026 | May 21, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 5 Achievements:

* NoSQL principles and master data design skills on Amazon DynamoDB: Determine the Partition Key (e.g., `OrderId`) to optimize order search performance, Set up an automatic scaling mechanism for capacity and read/write bandwidth according to actual needs (On-Demand Capacity), Understand the distributed storage feature and automatic data replication across multiple availability zones (Multi-AZ) to prevent data loss.

* Successfully created a high-level data security solution using AWS KMS: Initialized and managed the lifecycle of Symmetric CMK, Defined Key Policies to strictly control who/which services are allowed to decrypt data.

* Familiarized with the automatic encryption at rest process: Integrated KMS directly into DynamoDB, ensuring all order information, phone numbers, and delivery addresses of customers are automatically encrypted before being written to AWS hard drives.