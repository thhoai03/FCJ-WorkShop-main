---
title: "Week 8 - Exploring the Ecosystem of Managed AI Services on AWS"
date: 2026-06-09
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---### Week 8 Objectives:

* Complete the logical mind map of the Backend background data processing flow and map the processing steps into a closed loop process.

### Tasks completed during the week:

| Day | Tasks | Start Date | End Date | References |
| --- | --- | --- | --- | --- |
| 2 | Analyze the Backend flow upon receiving a request: How API Gateway receives the POST packet of cake order data from the customer, validates the format, and forwards it to Lambda. | June 9, 2026 | June 9, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 3 | Study the interaction flow between Lambda and DynamoDB: Logic to check IAM permissions, call KMS to get a key to encrypt data, and then execute a write command to the database table. | June 10, 2026 | June 10, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | Analyze the Ops flow: Logic to trigger secondary action chains after a successful cake order (Lambda calls SNS to shoot an email and simultaneously CloudWatch captures the log). | June 10, 2026 | June 10, 2026 | https://cloudjourney.awsstudygroup.com/ |
| 5 | Proceed to concatenate all Frontend and Backend flows. | June 11, 2026 | June 11, 2026 | https://cloudjourney.awsstudygroup.com/ |

### Week 8 Achievements:

* Understand the nature of System Integration flows and master Decoupled Architecture thinking: Services operate independently but connect smoothly through encrypted API function call protocols, Understand how to control bottleneck errors when data pours in massively.

* Successfully built a comprehensive data processing scenario.

* Gained solid system logic thinking capabilities before entering the actual assembly phase on the Cloud environment.