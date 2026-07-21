---
title: "Week 12 - Reviewing, Comprehensively Evaluating the Project Architecture, and Finalizing the Graduation Internship Report"
date: 2026-07-12
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---### Week 12 Objectives:

* Comprehensively connect API Gateway (with Cognito JWT Authorizer) with the 16 Lambda functions and the Frontend, complete the notification layer (SNS/SES) and monitoring (CloudWatch/CloudTrail), perform End-to-End testing, and package the project for acceptance.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Declare Amazon API Gateway (REST) ​​in the SAM template: enable full CORS, attach Cognito JWT Authorizer for admin endpoints, open public endpoints for viewing products, registering, logging in, ordering; run `sam deploy` to release the API to the prod stage. | July 12, 2026 | July 12, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Declare the SNS topic `hmn-order-notify` and subscribe to the admin email; verify the email on Amazon SES (sandbox environment); enable CloudWatch Logs/Metrics + Alarms for 16 Lambda functions; create a CloudTrail trail `hmn-bakery-audit`. | July 13, 2026 | July 13, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Update the API endpoint environment variable in the Vite configuration file (.env) of the Frontend; run `npm run build`, sync `aws s3 sync dist/` to the bucket and create a CloudFront Invalidation. | July 14, 2026 | July 14, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Conduct End-to-End testing on the real interface: register → confirm OTP → login → browse products → add to cart → order cake → check records in `hmn-orders`, SNS email and confirm SES email; compile documents to package the 12-week report. | July 15, 2026 | July 17, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 12 Achievements:

* Successfully connected the entire chain of the serverless cake ordering system comprehensively: React SPA → CloudFront/WAF → API Gateway → Lambda → DynamoDB, where the Cognito JWT Authorizer validates tokens right at the API gateway, prematurely blocking any invalid requests before reaching Lambda.

* Successfully integrated the real-time dual notification flow: the order creation function simultaneously saves the order to DynamoDB and publishes to SNS to shoot a detailed order email to the admin's inbox, while sending a confirmation SES email to the customer.

* End-to-End testing passed successfully across two scenarios:
  * **Happy Path**: ordering a "Strawberry Cream Cake" on the web interface, the system responds with an instant successful order; the order appears accurately in the `hmn-orders` table (data encrypted at-rest), with notification and confirmation emails arriving in inboxes immediately.
  * **Negative Path**: sending hundreds of simulated spam requests as an attack — WAF activates a rate-based rule to block the spam source; calling an admin endpoint with an expired token — API Gateway returns a 401/403; simulating a notification send error — the message falls into the DLQ `hmn-lambda-dlq` awaiting reprocessing, avoiding data loss.

* Completed the monitoring and auditing layer with clear roles: CloudWatch tracks "what happens inside the application" (logs, metrics, alarms for 5xx errors, high latency, DLQ accumulation). CloudTrail records "who impacted the infrastructure", audit logs are stored separately in an isolated bucket — traces cannot be deleted/modified even if the application part is compromised.

* Successfully packaged the entire source code (AWS SAM repo + React), architecture diagram, and operational logs into a complete AWS cloud project internship report portfolio.