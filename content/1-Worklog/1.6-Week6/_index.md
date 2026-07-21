---
title: "Week 6 - Research and Deployment of Amazon RDS and Amazon DynamoDB Database Systems"
date: 2026-05-26
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---### Week 6 Objectives:

* Set up a centralized logging tool to monitor system health and build a real-time order notification channel.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Study the Amazon CloudWatch monitoring solution, learn about CloudWatch Logs, Metrics, and the mechanism for setting up Alarms. | May 26, 2026 | May 26, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Learn the theory of the Amazon SNS (Simple Notification Service) message transmission service based on the Publish/Subscribe (Pub/Sub) model. | May 27, 2026 | May 27, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Practice configuring CloudWatch Log Groups to collect all operational history and error messages arising from Lambda functions. | May 28, 2026 | May 28, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Create an SNS Topic, and perform Subscribe for the email addresses of administrators and the baking department into the system to receive automated messages. | May 29, 2026 | May 29, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 6 Achievements:

* system operations thinking (Ops) and master the Amazon CloudWatch service: Automatically collect log streams from Backend source code for debugging, Monitor performance measurement indicators (Metrics) such as API error rates and system response times, Set up log filters to detect abnormal behaviors.

* Successfully created a push notification system via Amazon SNS: Initialized a central Topic to distribute event-driven messages, Successfully configured and authenticated Email Subscribe filters to receive messages.

* Familiarized with the ability to automate information sending: Connected the source code so that when there is a new cake order, the system automatically triggers SNS to shoot an email notification immediately to the store owner's phone without manual intervention.