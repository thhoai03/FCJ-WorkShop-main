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

* **Stack name**: `cakeshop`
* **AWS Region**: `ap-southeast-2` 
* **Parameter AdminEmail**: nhanmai.22072019@gmail.com
* **Parameter SesSender**: nhanmai.22072019@gmail.com
* **Parameter AllowedOrigin**: `*`
* **Confirm changes before deployment**: `y` (to review the list of resources before creation).
* **Allow SAM CLI IAM role creation**: **Y** (allow SAM to automatically create required security roles).
* **Save arguments to configuration file**: `Y` (save the configuration to the `samconfig.toml` file for future deployments).

### Step 3: Retrieve resource information (Outputs)

The deployment process may take 3-5 minutes. Once successfully completed, the terminal screen will print an **Outputs** table. 

Carefully copy and save the following values, as we will use them in the next steps to configure the Frontend and load data:

1. `ApiUrl`: https://ux5v5f7ec5.execute-api.ap-southeast-2.amazonaws.com/dev
2. `UserPoolId`: ap-southeast-2_dpwns0mJd
3. `UserPoolClientId`: 343p8l05p2u2bnodb206m7pa7h
4. `ImagesBucketName`: hmn-bakery-images-131292876211-dev