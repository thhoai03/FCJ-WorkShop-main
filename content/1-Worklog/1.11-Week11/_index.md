---
title: "Week 11 - Backend Implementation: Serverless Architecture with AWS SAM"
date: 2026-07-06
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---
### Week 11 Objectives:

* **Important Note:** From Week 1 to Week 10, the team *practiced* and explored individual services on the AWS Console. Starting from Week 11, the team officially **built the actual Backend for the project** and fully automated the deployment using **AWS SAM (Serverless Application Model)**.
* Realize the encrypted NoSQL data layer (DynamoDB + KMS + Image S3) and program, deploy 16 Lambda functions processing business logic to the serverless cloud via AWS SAM.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Declare the data layer in template.yaml: two DynamoDB tables `hmn-products` and `hmn-orders` in PAY_PER_REQUEST mode, enabling SSE encryption with a KMS key; Image S3 bucket encrypted with AES-256. | July 6, 2026 | July 6, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Write Node.js 20 source code (ARM64 architecture) on VS Code for the Auth function group integrating Cognito (register, confirm OTP, login, forgotten password, reset password, resend OTP) and the Product group (get list, details, add, edit, delete products). | July 7, 2026 | July 7, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Write the Order function group (create order: generate id → write to DynamoDB → publish to SNS → send SES email; get all orders for admin; get my orders; update status), User, Admin, and Upload groups (create presigned URL). | July 8, 2026 | July 8, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Attach minimum IAM Policies (Least Privilege) for each function; run `sam build`, test locally using `sam local invoke`, then `sam deploy` all 16 Lambda functions. | July 9, 2026 | July 11, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 11 Achievements:

* Successfully built a production-ready data layer: Two on-demand DynamoDB tables auto-scaling, paying only for actual read/write throughput; GSI `status-index` allows efficient order queries by status; data encrypted at-rest using KMS.

* The cake image bucket allows public read access for display on the interface but only accepts uploads via signed presigned URLs; DynamoDB only stores references (key/URL) to the images.

* Synchronously deployed 16 Lambda functions across 6 business groups (Auth, Product, Order, User, Admin, Upload) using a single `sam deploy` command — all infrastructure and source code are managed centrally in template.yaml, without manual Console operations.

* Applied the Presigned URL design pattern for image uploads: the client uploads images directly to S3 via HTTP PUT, bypassing Lambda's 6 MB payload limit, reducing costs and increasing upload speed.

* Ensured reliability and security at the compute layer: Failed asynchronous tasks (sending emails, notifications) are pushed to the DLQ `hmn-lambda-dlq` for reprocessing, ensuring no lost orders or notifications. Each Lambda function only has exactly the necessary permissions on its own resources.

* Local testing with `sam local invoke` was successful: a simulated cake order was accurately recorded into the `hmn-orders` table before integrating API Gateway.