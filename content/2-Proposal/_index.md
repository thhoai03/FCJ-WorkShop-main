---
title: "Proposal"
date: 2026-05-04
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
# HMN Bakery — Online Cake Ordering Website

## Comprehensive AWS Serverless Solution for Smart Cake Ordering System

---

### 1. General Introduction

**HMN Bakery** is an online cake ordering website built entirely on a **serverless** model on the AWS platform. Customers can visit the website, register an account, log in, browse product categories, view cake details, add to cart, save favorite products, and place orders. The system automatically saves orders, notifies administrators via email, and sends order confirmation emails to customers. Administrators can manage products, orders, users, and view revenue statistics.

The entire system is designed with a **no server management** approach, helping to optimize costs, automatically scale according to traffic, and ensure security, reliability, and monitoring criteria ready for a production environment.

The main components are organized into **4 layers**: Frontend (Edge & Security), Backend (API & Routing + Serverless Compute), Database & Security, and Notification & Monitoring.

---

### 2. System Architecture Diagram

![HMN Bakery Architecture Diagram](/images/2-Proposal/sodokientruc.png)

---

### 3. Frontend — Edge & Security

The user interface is developed using **ReactJS 19** with Vite as the build tool, as a Single Page Application (SPA). The interface is divided into two main layouts:

- **PublicLayout** — for customers: home page, product details, cart, checkout, wish list, order history
- **AdminLayout** — for administrators: dashboard, product management, orders, users, statistics

| AWS Service | Role |
|---|---|
| **Amazon S3** | Host the React build (HTML/CSS/JS) privately |
| **Amazon CloudFront** | Global CDN for interface delivery via Origin Access Control (OAC) |
| **Route 53 + ACM** | Domain and TLS/HTTPS certificate management |
| **AWS WAF** | Firewall to filter malicious traffic, rate limiting |
| **Amazon Cognito** | User authentication, issuing JWTs (1-hour expiration) |

**User flow:**
> Visitors access via CloudFront → load React UI from S3 → register/log in via Cognito (email OTP confirmation) to receive JWT → interact with the system

---

### 4. Backend — API & Routing + Serverless Compute

The business logic is built on a serverless architecture using **AWS SAM** with Node.js 20 running on ARM64 architecture, without persistent servers.

#### Amazon API Gateway (REST)
Receives all requests from the frontend, fully supporting CORS. Uses **Cognito JWT Authorizer** to authenticate tokens. Public endpoints (view products, register, place order) do not require authentication; admin endpoints require a valid admin group JWT.

#### AWS Lambda — 19 Business Functions

| Group | Functions | Purpose |
|---|---|---|
| **Auth** | 6 functions | Register, confirm OTP, login, forgot password, reset password, resend OTP |
| **Product** | 5 functions | Get list, details, add, edit, delete product |
| **Order** | 4 functions | Create order (with SNS + SES), get all orders, get my orders, update status |
| **User** | 2 functions | User list from Cognito, lock/unlock account |
| **Admin** | 1 func | Overall statistics (total orders, revenue, products) |
| **Upload** | 1 func | Generate presigned URL for image upload |

> Each Lambda: 15-second timeout, 256 MB memory, auto-scaling on demand.

**Image Upload with Presigned URL:** Client calls the `/uploads/presign` endpoint to request a signed URL (step 8a), then directly uploads the image to S3 via HTTP PUT (step 8b). This avoids Lambda's 6 MB payload limit and increases upload speed.

**Amazon SQS (Dead Letter Queue):** The `hmn-lambda-dlq` queue retains messages for 14 days. Failed asynchronous tasks are pushed to the DLQ for reprocessing, avoiding loss of orders or notifications.

---

### 5. Database & Security

| AWS Service | Role |
|---|---|
| **Amazon DynamoDB** | NoSQL database — `hmn-products` and `hmn-orders` tables (PAY_PER_REQUEST) |
| **Amazon S3 (Cake Images)** | `hmn-bakery-images` bucket to store product images, uploaded via presigned URL |
| **AWS KMS** | At-rest data encryption for DynamoDB and S3 |

**DynamoDB Design:**
- `hmn-products`: partition key `id` — stores product info
- `hmn-orders`: partition key `id` + GSI `status-index` (status + createdAt) — efficiently query orders by status

---

### 6. Notification & Monitoring

| AWS Service | Role |
|---|---|
| **Amazon SNS** | `hmn-order-notify` topic sends alert emails to admin on new orders |
| **Amazon SES** | Sends order confirmation emails to customers|
| **Amazon CloudWatch** | Collects logs, metrics, Alarms for anomalies |
| **AWS CloudTrail** | `hmn-bakery-audit` trail records all API calls at the account level |
| **Amazon S3 (Audit Logs)** | `hmn-audit-logs` bucket — blocks public access, lifecycle auto-deletes after 90 days |

> **Clear Separation of Roles:** CloudWatch handles *"what happens inside the application"*, CloudTrail handles *"who interacts with infrastructure"*, SNS/SES handles *"business notifications"*.

---

### 7. Main 10-Step Processing Flow

| Step | Description |
|---|---|
| ① | Customers access the website via **CloudFront** |
| ② | Load React UI from **S3** |
| ③ | Log in and authenticate via **Cognito** → receive JWT |
| ④ | Send order request via **API Gateway** |
| ⑤ | **Cognito JWT Authorizer** validates the token |
| ⑥ | **Lambda** processes business logic |
| ⑦ | Read/write orders to **DynamoDB** |
| ⑧a | Lambda generates presigned URL → client uploads image |
| ⑧b | Direct image upload to **S3** via HTTP PUT |
| ⑨ | Publish event to **SNS** → notify admin via email |
| ⑩ | **SES** sends confirmation email to customer |

---

### 8. Architectural Advantages

* **No Server Management** — AWS handles the entire infrastructure
* **Auto-scaling** — scales automatically from 0 to hundreds of concurrent requests
* **Multi-layered Security** — WAF + Cognito + KMS + CloudTrail
* **Cost Optimization** — pay only for actual requests
* **Infrastructure as Code** — entire infrastructure defined using AWS SAM, easy rollback and redeployment