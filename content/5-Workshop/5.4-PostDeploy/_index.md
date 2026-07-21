---
title: "Post-Deploy Configuration"
date: 2026-07-21
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---#4. Post-Deployment Configuration

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
   aws cognito-idp admin-add-user-to-group --user-pool-id <UserPoolId> --username <your-admin-email> --group-name admin
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