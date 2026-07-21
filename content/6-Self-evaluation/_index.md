---
title: "Self-evaluation"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 6. </b> "
---# Internship Self-Evaluation

After 12 weeks of commitment to the internship program and directly developing the HMN Bakery project, I would like to self-evaluate what I have achieved, as well as the anticipation that need to be continuously improved.

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