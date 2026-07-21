---
title: "Week 10 - Frontend Development: React 19, S3, CloudFront, WAF & Route 53"
date: 2026-06-29
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---
### Week 10 Objectives:

* Begin the realization phase of the project on a real Cloud environment, successfully configure and run a secure web interface via CDN.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Initialize the Frontend project using ReactJS 19 + Vite on VS Code following the SPA model: configure React Router v7, the Context API system (AuthContext, CartContext, WishlistContext, ToastContext), and two layouts (PublicLayout / AdminLayout); run `npm run build` to package the interface into the dist folder. | June 29, 2026 | June 30, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Declare the Frontend infrastructure in the AWS SAM template.yaml: S3 Bucket in private mode (Block Public Access), CloudFront Distribution with Origin Access Control (OAC) and Bucket Policy; run `sam build` and `sam deploy` to create resources. | July 1, 2026 | July 1, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Add to the SAM template: AWS WAF Web ACL with a Rate-based rule to limit request frequency against spam, attached to CloudFront; declare Amazon Cognito User Pool + App Client (register, confirm OTP via email, forgot/reset password). | July 2, 2026 | July 2, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Sync the build to S3 using the `aws s3 sync dist/` command and create a CloudFront Invalidation to refresh the cache; configure Route 53 DNS and a TLS certificate from ACM for the website to run on HTTPS. | July 3, 2026 | July 5, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 10 Achievements:

* Completed the React 19 SPA Frontend for HMN Bakery: Full navigation for two modules, PublicLayout for customers (home, product details, cart, checkout, wishlist, order history) and AdminLayout for management (dashboard, products, orders, users, statistics). Global state is neatly managed using Context API.

* The entire edge infrastructure is defined using AWS SAM (Infrastructure as Code), no manual operations on the Console: With just one `sam deploy` command, the entire S3 + CloudFront + WAF + Cognito stack can be intactly recreated, easily version-controlled via Git and rollbacked when necessary.

* The S3 Bucket is completely closed to the Internet (Public Access: Blocked); the OAC mechanism works accurately — only CloudFront is allowed to read the bucket's content.

* The website runs stably over CDN with HTTPS (Route 53 + ACM), the interface responds quickly from edge locations near users.

* The AWS WAF shield is successfully activated in front of CloudFront with rate limiting; Amazon Cognito issues JWT (idToken) with a 1-hour expiration and authorization by admin group, ready for the dynamic data API call flow.