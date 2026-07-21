---
title: "Week 9 - HMN Bakery Project Architecture Design, Configuring Amazon SNS Alerts and CloudWatch"
date: 2026-06-22
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---
### Week 9 Objectives:

* Translate all theoretical analysis results into a comprehensive architecture diagram, and publish the technical explanatory document for the project.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Draw the Edge & Security block including icons: User, Amazon ACM, Route 53, Amazon CloudFront, Amazon S3 (React Static Web), and AWS WAF; draw the Authentication (Auth) block with Amazon Cognito. | June 22, 2026 | June 22, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Draw the API & Routing block with Amazon API Gateway (REST, Cognito JWT Authorizer) and the Serverless Compute block including AWS Lambda (16 business functions) connected to the Amazon SQS-DLQ error queue. | June 23, 2026 | June 23, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Draw the Database & Security block (Amazon DynamoDB, AWS KMS, Amazon S3 Audit Logs), Image Storage block (Amazon S3 Cake Images), and Notification & Monitoring block (Amazon SNS, Amazon SES, Amazon CloudWatch, AWS CloudTrail). | June 24, 2026 | June 24, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Connect the business flow arrows and number them from 1 to 10, adding two sub-steps 8a and 8b; check visual design errors and export high-quality image/PDF files. | June 25, 2026 | June 27, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 9 Achievements:

* Understand the nature of system architecture diagrams and master the skill of visually representing cloud computing resources according to official AWS icon standards.

* Completely designed the General Architecture Diagram for the HMN Bakery Serverless Cake Ordering Website system with 4 clear logical partition layers: Edge & Security (ACM, Route 53, CloudFront, Static Web S3, WAF) along with the Cognito Auth block; API & Routing + Serverless Compute (API Gateway, 16 Lambda functions, SQS-DLQ); Database & Security (DynamoDB, KMS, S3 Audit Logs); Notification & Monitoring (SNS, SES, CloudWatch, CloudTrail).

* Fully represents the 10 main flow steps: (1) access website via CloudFront → (2) load React interface from S3 → (3) login via Cognito → (4) send API → (5) JWT authentication → (6) trigger Lambda → (7) read/save order to DynamoDB → (8a/8b) request presigned URL and upload image directly to S3 → (9) notify admin via SNS → (10) confirm email via SES.

* Accurately uses one-way/two-way and dashed arrows to distinguish business data flows from protection relations (WAF protect), encryption (KMS), and monitoring (logs/metrics, access log, audit log).

* The diagram was exported in a non-pixelated vector image format, ready to be inserted as the central template page in the final report.