---
title: "Blog 1 - Operational Automation with Event-Driven and AWS Security Hub"
date: 2026-07-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---**[AWS Architecture] Operational Automation with Event-Driven and AWS Security Hub**

> 🔗 View the original post at: [AWS Study Group FCJ](https://www.facebook.com/groups/awsstudygroupfcj/posts/2208759786555648)

![Event-Driven Architecture and AWS Security Hub](/images/blog1.png)

As the number of users and services increases, sitting and opening CloudWatch to monitor logs all day becomes practically impossible. Instead of waiting for operators to detect incidents, prioritizing building the system in an **Event-Driven** direction allows the system itself to automatically detect and handle anomalies.

---

### Practical Example: Notification Flow After Ordering

A simple example is the notification flow after a customer places an order. When Lambda successfully writes data to DynamoDB, Lambda **does not** directly call the Gmail API to send an email. Instead, it only **emits an event** to Amazon SNS. Services that need to receive notifications, such as the email sending system or other services, simply need to subscribe to the SNS Topic to receive the event.

This approach helps Lambda complete its task faster, reduce execution time and also save costs because the notification sending part is handled by SNS.

---

### Automatically Detecting and Blocking Attacks with Security Hub

Within the system, **AWS WAF** will record suspicious requests into CloudWatch. **AWS Security Hub** aggregates and analyzes security alerts. If it detects an IP showing signs of system scanning or abnormal attacks, Security Hub will generate a **Finding**.

At that moment, **Amazon EventBridge** will catch this event and automatically trigger an **AWS Lambda** to update the blocklist on WAF. The entire process from detection to blocking the IP happens **automatically**, without requiring operational engineer intervention.

Automated processing flow:
```
Attacking IP → AWS WAF logs → CloudWatch
→ Security Hub creates Finding
→ EventBridge catches the event
→ Lambda updates WAF Blocklist ✅
```

---

### Architecture Evaluation

What is highly appreciated about this architecture is its capability to **react in near real-time**. Behaviors like password guessing or vulnerability scanning can be detected and handled in just **a few seconds**, helping to:

* Significantly reduce Mean Time To Recovery (**MTTR**)
* Limit risks for the entire system
* Completely eliminate dependency on manual intervention by operational engineers