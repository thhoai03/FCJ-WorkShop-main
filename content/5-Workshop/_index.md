---
title: "Workshop"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5. </b> "
---# HMN Bakery Deployment Guide

Welcome to the workshop documentation for deploying the **HMN Bakery — Online Cake Ordering Website** project.

> 🚀 **Live Demo:** [https://d1babxppbit8as.cloudfront.net/](https://d1babxppbit8as.cloudfront.net/)
> 
> 🔑 **Admin Test Account:** 
> * **Email:** `hoaik4d5@gmail.com`
> * **Password:** `123abcd`

### Activity Demo Video
<!-- Please upload your DemoNhomHMN.mp4 video to YouTube (Unlisted) and replace the YOUR_YOUTUBE_VIDEO_ID below with the actual Video ID -->
<iframe width="100%" height="500" src="https://www.youtube.com/embed/E0BoPDcxsTQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

In this workshop, we will go step-by-step to deploy the entire Serverless Backend system using AWS SAM (Serverless Application Model), set up initial data, and connect it with the ReactJS Frontend.

The system core uses AWS services including:
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