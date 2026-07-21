---
title: "Architecture & APIs"
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
| **Auth** | POST | `/auth/resend-otp` | Public | Resend OTP code |
| **Auth** | POST | `/auth/login` | Public | Login and receive JWT token |
| **Auth** | POST | `/auth/forgot-password` | Public | Send password recovery code |
| **Auth** | POST | `/auth/reset-password` | Public | Set a new password |
| **Product** | GET | `/products` | Public | Get product list |
| **Product** | GET | `/products/{id}` | Public | View details of a product |
| **Product** | POST | `/products` | **Admin** | Add a new product |
| **Product** | PUT | `/products/{id}` | **Admin** | Edit product information |
| **Product** | DELETE | `/products/{id}` | **Admin** | Delete a product |
| **Order** | POST | `/orders` | Public | Place an order (triggers SNS + SES) |
| **Order** | GET | `/orders/my` | **User** | View own order history |
| **Order** | GET | `/orders` | **Admin** | View all orders list |
| **Order** | PUT | `/orders/{id}/status` | **Admin** | Update order status |
| **User** | GET | `/users` | **Admin** | Get user list from Cognito |
| **User** | PATCH | `/users/{username}/status` | **Admin** | Lock or unlock account |
| **Admin** | GET | `/admin/statistics` | **Admin** | Get data for Dashboard |
| **Upload** | POST | `/uploads/presign` | **Admin** | Request Presigned URL to upload images to S3 |

> ⚠️ **Security Note:**
> Routes with **Admin** access require the user to provide a valid JWT (idToken), and that account must belong to the `admin` group in Cognito. The token is sent in the header of the HTTP Request: `Authorization: <idToken>`.