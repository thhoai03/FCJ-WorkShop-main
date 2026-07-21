import os
import shutil

content_mapping = {
    r"5-Workshop\_index.md": r"""---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# HMN Bakery Deployment Guide

Welcome to the workshop documentation for deploying the **HMN Bakery — Online Cake Ordering Website** project.

> 🚀 **Live Demo:** [https://d1babxppbit8as.cloudfront.net/](https://d1babxppbit8as.cloudfront.net/)
> 
> 🔑 **Admin Test Account:** 
> * **Email:** `hoaik4d5@gmail.com`
> * **Password:** `123abcd`

### Activity Demo Video
<video width="100%" controls>
  <source src="/videos/DemoNhomHMN.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

In this workshop, we will go step-by-step to deploy the entire Serverless Backend system using AWS SAM (Serverless Application Model), set up initial data, and connect it with the ReactJS Frontend.

The system uses core AWS services including:
* **Amazon API Gateway** (REST API)
* **AWS Lambda** (Node.js Compute)
* **Amazon DynamoDB** (NoSQL Database)
* **Amazon Cognito** (Authentication)
* **Amazon S3** (Storage & Frontend Hosting)
* **Amazon SNS / SES** (Notifications & Email)

---

### Practice Content:

1. **[Architecture & API Overview](5.1-Overview/)**: Understand the system and API endpoints.
2. **[Prerequisite Requirements](5.2-Prerequisite/)**: Prepare the environment (AWS CLI, SAM CLI, Node.js).
3. **[Deploy Backend with SAM](5.3-Deploy/)**: Deploy infrastructure to AWS with a single command.
4. **[Post-Deploy Configuration](5.4-PostDeploy/)**: Load seed data and create an Admin account.
5. **[Connect React Frontend](5.5-Frontend/)**: Configure the Frontend environment to connect to the Backend.
6. **[Resource Cleanup](5.6-Cleanup/)**: Delete the system to avoid incurring costs when not in use.
""",
    r"5-Workshop\5.1-Overview\_index.md": r"""---
title: "Architecture & API"
date: 2026-07-21
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

# 1. Architecture & API Overview

The backend for the HMN bakery website is deployed using **AWS SAM**. The entire architecture operates on a serverless model: `API Gateway → Lambda → DynamoDB`, utilizing authentication via `Cognito` and sending notifications through `SNS/SES`.

---

### API Endpoints List

Below is the routing table for the APIs in the system:

| Group | Method | Path | Access Rights | Lambda Execution |
|---|---|---|---|---|
| **Auth** | POST | `/auth/register` | Public | Account registration + send OTP |
| **Auth** | POST | `/auth/verify-otp` | Public | Verify OTP code |
| **Auth** | POST | `/auth/login` | Public | Login and receive JWT token |
| **Auth** | POST | `/auth/forgot-password` | Public | Send password recovery code |
| **Auth** | POST | `/auth/reset-password` | Public | Set a new password |
| **Product** | GET | `/products` | Public | Get product list |
| **Product** | GET | `/products/{id}` | Public | View details of a product |
| **Product** | POST | `/products` | **Admin** | Add a new product |
| **Product** | PUT | `/products/{id}` | **Admin** | Edit product information |
| **Product** | DELETE | `/products/{id}` | **Admin** | Delete a product |
| **Order** | POST | `/orders` | Public | Place an order (triggers SNS + SES) |
| **Order** | GET | `/orders` | **Admin** | View all orders list |
| **Order** | PUT | `/orders/{id}/status` | **Admin** | Update order status |
| **User** | GET | `/users` | **Admin** | Get user list from Cognito |
| **User** | PATCH | `/users/{username}/status` | **Admin** | Lock or unlock account |
| **Admin** | GET | `/admin/statistics` | **Admin** | Get data for Dashboard |
| **Upload** | POST | `/uploads/presign` | **Admin** | Request Presigned URL to upload images to S3 |

> ⚠️ **Security Note:**
> Routes with **Admin** access require the user to provide a valid JWT (idToken), and that account must belong to the `admin` group in Cognito. The token is sent in the header of the HTTP Request: `Authorization: <idToken>`.
""",
    r"5-Workshop\5.2-Prerequisite\_index.md": r"""---
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
├─ template.yaml            # Defines entire infrastructure (AWS SAM)
├─ src/
│  ├─ package.json          # AWS SDK v3 dependencies
│  ├─ functions/            # Directory containing Lambda functions (auth, product, order,...)
│  ├─ shared/               # Shared code (dynamoClient, cognitoClient, response...)
│  └─ data/                 # Scripts and data to seed the database
└─ architecture/            # Contains system diagrams
```

👉 **Next step:** After fully installing the tools above, proceed to the next step to **Deploy** the system.
""",
    r"5-Workshop\5.3-Deploy\_index.md": r"""---
title: "Deploy Backend"
date: 2026-07-21
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# 3. Deploy Backend with AWS SAM

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
* **Confirm changes before deploy**: `y` (to review the list of resources before creation).
* **Allow SAM CLI IAM role creation**: **Y** (allow SAM to automatically create required security roles).
* **Save arguments to configuration file**: `Y` (save the configuration to the `samconfig.toml` file for future deployments).

### Step 3: Retrieve resource information (Outputs)

The deployment process may take 3-5 minutes. Once successfully completed, the terminal screen will print an **Outputs** table. 

Carefully copy and save the following values, as we will use them in the next steps to configure the Frontend and load data:

1. `ApiUrl`: The API Gateway URL (e.g., `https://xxx.execute-api.ap-southeast-1.amazonaws.com/Prod/`)
2. `UserPoolId`: The Cognito User Pool ID.
3. `UserPoolClientId`: The Cognito Client access ID.
4. `ImagesBucketName`: The S3 bucket name storing product images.
""",
    r"5-Workshop\5.4-PostDeploy\_index.md": r"""---
title: "Post-Deploy Configuration"
date: 2026-07-21
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# 4. Post-Deployment Configuration

After the backend deployment is complete, your DynamoDB database and Cognito authentication systems are completely empty. We need to load some sample product data (seed) and grant permissions for an administrator account (Admin).

---

### a) Load sample product data into DynamoDB

We will run a provided Node.js script in the source code to create a sample list of cakes into the `hmn-products` table.

1. Navigate to the `src` directory and install libraries:
   ```bash
   cd src
   npm install
   ```

2. Run the data seeding script. *(Note: Change the table name or region if you entered differently during deployment)*:
   
   **On PowerShell (Windows):**
   ```powershell
   $env:PRODUCTS_TABLE="hmn-products"; $env:AWS_REGION="ap-southeast-1"; node data/seed.js
   ```

   **On Bash (Mac/Linux):**
   ```bash
   PRODUCTS_TABLE="hmn-products" AWS_REGION="ap-southeast-1" node data/seed.js
   ```

### b) Initialize Admin account

According to the system design, features like adding/editing/deleting products, managing orders, and viewing statistics require users to log in with an account belonging to the **admin** group in Cognito.

1. **Create an account:** Use the public API to register a new account (call `/auth/register` and `/auth/verify-otp` APIs), or you can register yourself via the Frontend interface in the next step.
   
2. **Grant Admin permissions:** Once you have an account (e.g., your email is `admin@domain.com`), assign that account to the `admin` group using the following AWS CLI command:

   ```bash
   aws cognito-idp admin-add-user-to-group \
     --user-pool-id <UserPoolId> \
     --username <your-admin-email> \
     --group-name admin
   ```
   *(Replace `<UserPoolId>` with the value obtained in the Outputs screen after deployment).*

### c) Configure Amazon SES (Email)

By default, a new Amazon SES account is always in the **Sandbox** state. In this mode, SES only allows sending emails to Verified Identities.

If you want to send order confirmation emails to any customer email:
1. Log in to the AWS Console, find the **Amazon SES** service.
2. Request AWS to enable **Production access**.
3. If not granted production access, you can only test the email sending function by manually verifying the recipient's email in the SES console.

---
👉 After loading data and having an Admin account, your Backend is fully ready to operate!
""",
    r"5-Workshop\5.5-Frontend\_index.md": r"""---
title: "Connect Frontend"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# 5. Connect React Frontend with Serverless Backend

Once the Backend is ready, the next step is to configure the Frontend so the React application knows how to call the APIs on AWS.

---

### Step 1: Declare environment variables

Open the `cake-shop-frontend` directory, find (or create a new) file named `.env` in the frontend root directory.

Add the following environment variable to the `.env` file, replacing the value `<ApiUrl from Outputs>` with the actual API Gateway URL you received after deploying the backend:

```env
VITE_API_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/Prod/
```

### Step 2: Integrate API and Auth (Processing flow)

The Frontend needs to be programmed to interact with the Backend safely and correctly. Below is the main operational flow you need to establish in the `src/services/api.js` and `src/services/auth.js` files:

1. **Handle login and save Token:**
   After successfully calling the `/auth/login` API, the backend will return a JWT string (`idToken`). The Frontend needs to save this string into `localStorage` or a secure state management mechanism to use for subsequent requests.

2. **Call authenticated API (Admin Request):**
   Every HTTP request directed at administrator features (such as adding products, viewing orders) must attach the token to the header:
   ```javascript
   // Example of attaching header using axios or fetch
   headers: {
     'Authorization': idToken
   }
   ```
   If the API Gateway does not find this token (or the token doesn't belong to the `admin` group), it will automatically block the request and return a 401/403 error.

3. **Image Upload Mechanism:**
   The system does not send large image files directly through API Gateway and Lambda to avoid exceeding the payload limit (6 MB) and save computing costs.
   The image upload flow goes through 2 steps:
   - **Step 1:** The Frontend calls the `/uploads/presign` API to request a temporary "Pass" (a pre-signed secure URL).
   - **Step 2:** The Frontend uses the received `uploadUrl` to directly send the image file to **Amazon S3** via the HTTP `PUT` protocol.

---

### Step 3: Run the application

After finishing the `.env` configuration, open a terminal in the `cake-shop-frontend` directory and start the development server:

```bash
npm install
npm run dev
```

Now you can access `http://localhost:5173` in your browser. The React Frontend will display real data retrieved from DynamoDB via API Gateway, completing the HMN Bakery Online Cake Ordering system!
""",
    r"5-Workshop\5.6-Cleanup\_index.md": r"""---
title: "Resource Cleanup"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# 6. Resource Cleanup (Cleanup)

Although Serverless architecture (Lambda, API Gateway, DynamoDB On-demand) has a major advantage that **if not used, it costs nothing** (Pay-as-you-go), the system still uses Amazon S3, KMS, and some other resources that may incur small storage costs if left over time.

Therefore, after finishing the practice or no longer needing to maintain the HMN Bakery project on the AWS environment, you should delete all resources to avoid unexpected charges.

---

### Steps to delete the system

#### Step 1: Delete all images in S3 Buckets

AWS CloudFormation (the tool SAM uses under the hood) will **not allow deleting** an S3 bucket if it still contains files inside.

1. Log into the [AWS Console - S3](https://s3.console.aws.amazon.com/s3/home).
2. Find the bucket containing product images (named starting with `hmn-bakery-images-...`).
3. Select all image files inside and click the **Delete** button to clear the bucket.

#### Step 2: Delete Stack with SAM CLI

Open a terminal, ensure you are in the `cake-shop-backend` directory, and run the following command:

```bash
sam delete
```

AWS SAM will prompt for confirmation:
* `Are you sure you want to delete the stack hmn-bakery in the region ap-southeast-1 ? [y/N]:` Enter `y`.
* `Are you sure you want to delete the folder hmn-bakery in S3 which contains the artifacts? [y/N]:` Enter `y` (to also delete the bucket containing SAM's temporary build files).

#### Step 3: Double-check (Optional)

To be 100% sure everything has been cleared, you can go to the [AWS Console - CloudFormation](https://console.aws.amazon.com/cloudformation/), and check if the `hmn-bakery` stack has transitioned to the **DELETE_COMPLETE** state. If successfully deleted, your AWS system has returned to its initial state.
""",
    r"6-Self-evaluation\_index.md": r"""---
title: "Self-evaluation"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

# Internship Self-Evaluation

After 12 weeks of commitment to the internship program and directly developing the HMN Bakery project, I would like to self-evaluate what I have achieved, as well as the shortcomings that need to be continuously improved.

---

### 1. Work completion level

Overall, I evaluate my work completion level as **Good (90%)**.
* Completely finished the backend for HMN Bakery running 100% on the AWS Serverless platform.
* Successfully integrated complex services like Cognito (authentication) and SES (email delivery).
* Completed weekly reports on schedule and fully participated in offline events.

However, there is still 10% unfulfilled as the Frontend was sometimes delayed compared to the Backend, and some advanced features (like caching with Redis) were not implemented due to time constraints.

---

### 2. Skills acquired

**Hard skills:**
* Shifted mindset from traditional web development (running servers 24/7) to Serverless mindset (only runs upon request).
* Learned how to use AWS SAM to write infrastructure as code instead of manual clicking on the console, making deployment much easier.
* Deeper understanding of NoSQL (DynamoDB). Initially, I struggled because I was used to designing MySQL-style tables, but now I grasp how to design according to Access Patterns.
* Learned proper security authorization (IAM Roles) instead of giving arbitrary permissions.

**Soft skills:**
* English document reading skills: AWS documentation is very long, forcing me to read a lot and extract important information myself.
* Time management and debugging skills: When Lambda encountered errors, I knew how to open CloudWatch to inspect logs instead of guessing blindly.

---

### 3. Strengths and Weaknesses

**Strengths:**
* Proactive in researching. Initially, the team planned to use EKS, but seeing the high costs, I proactively proposed and self-learned Serverless to do it.
* Stuck to the goal, didn't give up when facing tough errors (especially API Gateway CORS errors and S3 permission errors).

**Weaknesses to improve:**
* Ability to optimize Node.js code in Lambda is not truly good yet; sometimes "cold starts" are still a bit slow.
* NoSQL database design still occasionally carries an SQL flavor; need to delve deeper into Single-Table Design.
* Text presentation and documentation are sometimes a bit disjointed.

---

### 4. Future orientation

In the coming time, I plan to review and take the **AWS Certified Developer - Associate** exam to consolidate all the knowledge I've learned over the past 3 months. I will also continue upgrading the HMN Bakery project, adding Redis to reduce the load for DynamoDB and optimize page load speed.
""",
    r"7-Feedback\_index.md": r"""---
title: "Feedback & Suggestions"
date: 2026-07-21
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

# Program Feedback and Suggestions

Wrapping up the 3-month internship, I want to send my sincere thanks to the organizing committee, mentors, and companions in the program. Below are some personal thoughts and small contributions from me to help the program become even better.

---

### 1. Pros of the program

* **Extremely realistic environment:** Not tied to mere theories. Being provided with real AWS accounts and deploying systems by hand helped us students figure out a lot of things.
* **Strong support community:** The Q&A group was very active. Every time I got stuck with an error (especially trivial IAM or network errors), I posted on the group and was supported enthusiastically and quickly by the mentors.
* **Quality Offline sessions:** The meetings at the AWS office not only broadened my horizons about professional working environments but also created opportunities to connect with many talented students from other schools. The cloud architecture competition experience was truly exciting.

---

### 2. Some encountered difficulties

* **Overwhelmed by knowledge in the early stages:** In the first 2-3 weeks, the amount of new concepts (VPC, Subnet, IAM, Route53...) hitting me was too much, making me a bit exhausted and taking a lot of time to catch up.
* **Resource limitations:** Because the sandbox account has some barriers (for example, SES requires manual email verification, or limits on some advanced services), it sometimes disrupted testing the actual flow of the project.

---

### 3. Small suggestions for subsequent batches

* **Add more Hands-on workshops:** I think if the program had 1-2 step-by-step direct instruction sessions for a small-scale sample project at the beginning of the course, new interns would be less "overwhelmed" and would have momentum to develop their own projects.
* **Suggest a skill roadmap:** It would be great if the organizers had a specific roadmap list (like what to study in week 1, what to do in week 2) so that students without a solid foundation won't get lost in a "forest" of AWS documentation.

Overall, this was a milestone internship for me personally. It gave me not only professional knowledge but also forged my problem-solving mindset. Once again, I would like to send my thanks to everyone!
"""
}

base_dir = r"C:\Users\Ngocg\.gemini\antigravity\scratch\FCJ-WorkShop-main\content"

for rel_path, en_content in content_mapping.items():
    md_path = os.path.join(base_dir, rel_path)
    vi_path = md_path.replace("_index.md", "_index.vi.md")
    
    # Copy to .vi.md (overwrite if exists)
    if os.path.exists(md_path):
        shutil.copy2(md_path, vi_path)
        print(f"Copied {rel_path} to {vi_path}")
        
    # Write en content
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(en_content)
        print(f"Written english content to {rel_path}")

