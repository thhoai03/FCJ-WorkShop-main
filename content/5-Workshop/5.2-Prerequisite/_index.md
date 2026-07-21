---
title: "Prerequisites"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---
# 2. Prerequisite Requirements

To automatically build and deploy the HMN Bakery backend system to AWS, you need to pre-install and configure the tools below on your personal computer.

---

### 1. Install AWS CLI

The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services.

* Download and install: [AWS CLI Installation Guide](https://aws.amazon.com/cli/)
* After installation, you need to configure your AWS account (with AdministratorAccess permissions to create resources):
  ```bash
  aws configure
  ```
  Enter `Access Key ID`, `Secret Access Key`, and `Default region name` (e.g., `ap-southeast-1`).

### 2. Install AWS SAM CLI

The AWS Serverless Application Model (SAM) CLI is a specialized tool for building and deploying serverless applications on AWS.

* Download and install: [SAM CLI Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
* Verify successful installation:
  ```bash
  sam --version
  ```

### 3. Install Node.js

Node.js is the required runtime environment for running Lambda code (Node.js 20) as well as data seeding scripts.

* Download and install: Node.js version **20.x** or higher from the [Node.js](https://nodejs.org/) homepage.
* Verify successful installation:
  ```bash
  node -v
  npm -v
  ```

### 4. Source Code Directory Structure

After downloading the project source code, make sure you have the following directory structure:

```text
cake-shop-backend/
├─ template.yaml # Defines entire infrastructure (AWS SAM)
├─ src/
│ ├─ package.json # AWS SDK v3 dependencies
│ ├─ functions/ # Directory containing Lambda functions (auth, product, order,...)
│ ├─ shared/ # Shared code (dynamoClient, cognitoClient, response...)
│ └─ data/ # Scripts and data to seed the database
└─ architecture/ # Contains system diagrams
```

👉 **Next step:** After fully installing the tools above, proceed to the next step to **Deploy** the system.