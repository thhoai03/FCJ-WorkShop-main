---
title: "Resource Cleanup"
date: 2026-07-21
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---
# 6. Resource Cleanup

Although Serverless architecture (Lambda, API Gateway, DynamoDB On-demand) has a major advantage that **if not used, it costs nothing** (Pay-as-you-go), the system still uses Amazon S3, KMS, and some other resources that may incur small storage costs if left over time.

Therefore, after finishing the practice or no longer needing to maintain the HMN Bakery project on the AWS environment, you should delete all resources to avoid unexpected charges.

---

### Steps to delete the system

#### Step 1: Delete all files in S3 Buckets

AWS CloudFormation (the SAM tool uses under the hood) will **not allow deleting** an S3 bucket if it still contains files inside.

1. Log into the [AWS Console - S3](https://s3.console.aws.amazon.com/s3/home).
2. Find the bucket containing product images (named starting with hmn-bakery-images-...) and the CloudTrail log bucket (hmn-audit-logs-...).
3. Click the **Empty** button to clear all files in both buckets.

#### Step 2: Delete CloudFront and WAF (Frontend)

If you deployed the Frontend to CloudFront:
1. Go to **CloudFront**, disable the distribution, then delete it.
2. Go to **WAF & Shield**, delete the WebACL associated with CloudFront.
3. Empty and delete the Frontend S3 Bucket.

#### Step 3: Delete Stack with SAM CLI

Open a terminal, ensure you are in the cake-shop-backend directory, and run the following command:

`ash
sam delete
`

AWS SAM will prompt for confirmation:
* Are you sure you want to delete the stack hmn-bakery in the region ap-southeast-1 ? [y/N]: Enter y.
* Are you sure you want to delete the folder hmn-bakery in S3 which contains the artifacts? [y/N]: Enter y (to also delete the bucket containing SAM's temporary build files).

> **Note on KMS Keys and SQS DLQ:**
> sam delete will automatically delete the SQS DLQ. However, AWS KMS Customer Managed Keys will be scheduled for deletion (pending deletion for 7-30 days) to prevent accidental data loss. During this pending state, they do not incur charges.

#### Step 4: Double-check (Optional)

To be 100% sure everything has been cleared, you can go to the [AWS Console - CloudFormation](https://console.aws.amazon.com/cloudformation/), and check if the hmn-bakery stack has transitioned to the **DELETE_COMPLETE** state. If successfully deleted, your AWS system has returned to its initial state.
