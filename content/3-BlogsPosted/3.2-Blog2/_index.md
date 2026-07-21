---
title: "Blog 2 - Serverless Backend – Handling Variable Traffic Without Server Management"
date: 2026-07-10
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---**[AWS Architecture] Serverless Backend – Handling Variable Traffic Without Server Management**

> 🔗 View the original post at: [AWS Study Group FCJ](https://www.facebook.com/groups/awsstudygroupfcj/posts/2208749799889980)

![Serverless Backend Architecture](/images/blog2.png)

This article covers optimizing the Frontend, handling order placement logic (Backend), and data storage. A specific characteristic of the F&B industry is that order volumes often **"spike" extremely high** during certain hours.

---

### Why Choose Serverless Instead of EKS?

Initially, the team considered setting up containers running on EKS, but after considering the cost of maintaining the cluster and administration effort, the team decided to pivot to a **100% Serverless** architecture.

Instead of maintaining a continuously running monolith backend, the team divided the business logic into **independent functions**.

---

### Serverless Processing Flow

As shown in the architecture diagram, the dynamic processing flow goes through **Amazon API Gateway**. It acts as a smart door, receiving purchase requests from users and routing them to the correct processing destination.

Behind API Gateway is **AWS Lambda** — the "heart" of the system. Lambda receives the order payload, checks its validity, and funds to finalize the order.

> **The killer feature of Lambda** is its ultra-fast Auto-scaling capability:
> * 100 people place orders simultaneously → AWS automatically provisions **100 Lambda environments** running in parallel
> * When no one buys → automatically **scales down to 0**
> * No more concept of an "idle running server"

---

### Why Choose DynamoDB Instead of RDS/MySQL?

After Lambda finishes processing, the data is written to **Amazon DynamoDB**.

| Criteria | DynamoDB | RDS/MySQL |
|---|---|---|
| Read/write speed | **Milliseconds** | Slower under heavy load |
| Auto-scaling | ✅ On-demand | ❌ Requires configuration |
| Suitable for bulk ordering | ✅ Highly suitable | ❌ Not optimal |
| Data encryption | ✅ AWS KMS | ✅ Supported |

To ensure security, the team enables data encryption with **AWS KMS**, ensuring customer information is encrypted directly at the storage layer.

---

### Benefits and Limitations

**✅ Benefits:** Developers only focus on writing Python/NodeJS code for purchasing logic, while upgrading RAM, patching OS vulnerabilities, or load balancing is fully handled by AWS.

**⚠️ Limitations:** Serverless Backend experiences **"Cold Starts"** (slowness on the first call after a long period of inactivity). To mitigate this, the team is applying the **Provisioned Concurrency** feature for several critical Lambdas.