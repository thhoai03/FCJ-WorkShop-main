---
title: "Blog 3 - Upgrading Amazon EKS Clusters: When the One-Way Street Now Has an \"Undo Button\""
date: 2026-07-17
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---**UPGRADING AMAZON EKS CLUSTERS: WHEN THE ONE-WAY STREET NOW HAS AN "UNDO BUTTON"**

> 🔗 View the original post at: [AWS Study Group FCJ](https://www.facebook.com/share/p/1KMbDkYEfM/)

![Amazon EKS Kubernetes Rollback](/images/blog3.png)

While tracking new updates from AWS, I recently found an extremely notable feature for Amazon EKS: **"Kubernetes version rollback"**. This is a feature that allows undoing a Kubernetes version upgrade within **7 days** if an issue occurs, returning the cluster to its previously safe operating state.

---

### The Problem — The Challenge to Solve

In the open-source world, Kubernetes **does not support** a control plane rollback mechanism. This forces businesses to:

* Build extremely cumbersome testing processes
* Set up complex staging environments
* Extend the upgrade cycle to **months** just to ensure nothing breaks

The reality is that Kubernetes releases up to **3 minor versions** per year. With teams managing tens or hundreds of clusters — especially in highly regulated financial or healthcare environments — the fear of *"upgrading and getting stuck due to errors"* makes them delay updates. Consequently, systems get stuck on old versions, lack critical security patches, and fall into an **out of support** state.

> **The question is:** "Is there a way for Kubernetes upgrades to happen safely, with a 'safety net' to fall back on if compatibility issues arise?"

---

### The Solution: Kubernetes version rollback on Amazon EKS

Instead of accepting the risk or spending effort rebuilding the entire cluster from scratch when encountering a compatibility error (e.g., from version 1.34 to 1.35), you can now simply press **"undo"** within 7 days.

The preparation and execution process is very rigorous:

* **Automated safety assessment:** Before rolling back, EKS automatically scans the cluster (Cluster Insights) to warn about the compatibility of current nodes or bundled add-ons. If you want to proceed quickly, you can use the `--force` flag to skip this step.

* **Full support for EKS Auto Mode:** For those using the fully automated mode (Auto Mode), EKS rolls back both the control plane and the physical nodes synchronously. This process strictly respects the **Pod Disruption Budget (PDB)** configuration to ensure applications are not suddenly amplified.

* **Flexible Cancel API:** If node downgrading takes too long or you want to change the plan, you can use the **Cancel API** command to stop immediately and readjust the PDB configuration.

---

### Actual Operational Architecture

```
Select cluster to rollback
    → View detailed report (Cluster Insights)
    → Trigger Rollback
    → Control plane downgrades (~20 minutes)
    → Nodes gracefully downgrade ✅
```

Throughout this process, the applications on the cluster continue to **operate normally**, without any service disruption.

---

### Conclusion & Recommendation

This rollback feature is not just a minor technical utility, but a **turning point that completely changes the EKS operational mindset**. It removes the biggest barrier preventing businesses from keeping their systems fresh and secure.

Notably, AWS provides this feature **"completely free"** across all commercial regions (you only pay standard EKS and EC2 resource costs as usual).

For teams operating EKS, this is definitely a feature that must be included in the **Standard Operating Procedure (SOP)**. From now on, each Kubernetes upgrade cycle will no longer be stressful night shifts, but simply an operational process that can be controlled and reversed at any time.

---

> 📖 **Reference:** https://aws.amazon.com/blogs/containers/upgrade-amazon-eks/