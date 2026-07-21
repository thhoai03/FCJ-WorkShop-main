---
title: "Deploy Backend"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---
#3. Deploy Backend with AWS SAM

After completing the tool installation in the previous step, we will use AWS SAM to deploy the entire backend infrastructure of HMN Bakery to AWS. This process will automatically create API Gateway, Lambda, DynamoDB, Cognito, S3, and configure IAM Roles.

---

### Step 1: Build the application

Open a terminal (or PowerShell), navigate to the backend directory, and run the build command:

```bash
cd cake-shop-backend
sam build
```
This command will download the necessary Node.js libraries and package the Lambda source code based on the configuration in the `template.yaml` file.

### Step 2: Deploy the application

Continue running the deploy command in guided interactive mode (`--guided`):

```bash
sam deploy --guided
```

During execution, AWS SAM will ask you some questions to configure the system. Enter information similar to the following:

* **Stack name**: `hmn-bakery`
* **AWS Region**: `ap-southeast-1` (or your preferred region)
* **Parameter AdminEmail**: Enter your personal email. This email will be used to receive notifications from Amazon SNS whenever a customer places a new order. *(Note: After deployment, you must open your email and click **Confirm subscription** in the email from AWS)*.
* **Parameter SesSender**: Enter the email address you verified in the Amazon SES service. This email acts as the sender for confirmation emails to customers.
* **Parameter AllowedOrigin**: Enter `*` when developing in a dev environment, or enter the exact frontend domain name (e.g., `https://hmnbakery.com`) when running in production.
* **Confirm changes before deployment**: `y` (to review the list of resources before creation).
* **Allow SAM CLI IAM role creation**: **Y** (allow SAM to automatically create required security roles).
* **Save arguments to configuration file**: `Y` (save the configuration to the `samconfig.toml` file for future deployments).

### Step 3: Retrieve resource information (Outputs)

The deployment process may take 3-5 minutes. Once successfully completed, the terminal screen will print an **Outputs** table. 

Carefully copy and save the following values, as we will use them in the next steps to configure the Frontend and load data:

1. `ApiUrl`: The API Gateway URL (e.g., `https://xxx.execute-api.ap-southeast-1.amazonaws.com/Prod/`)
2. `UserPoolId`: The Cognito User Pool ID.
3. `UserPoolClientId`: The Cognito Client access ID.
4. `ImagesBucketName`: The S3 bucket name storing product images.