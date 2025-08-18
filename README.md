### Google Cloud Associate Cloud Engineer (ACE) Certification Preparation

_[DISCLAIMER] The links and materials provided here are intended as supplementary resources for learning. This personally documented material does not represent official information from Google Cloud, although some of it is sourced from official Google Cloud resources. Unofficial materials indicate that the content is not direct information from Google._

---
## Exam Preparation Materials
### 1. Google Cloud Courses
- [Google Cloud Fundamentals: Core Infrastructure](https://www.cloudskillsboost.google/paths/11/course_templates/60)
  > This course is fantastic for building a strong foundation. It covers fundamental concepts and introduces the core services you'll be tested on.

- [Google Cloud Associate Cloud Engineer Course [2025] - Pass the Exam!](https://www.youtube.com/watch?v=OlAmyf8_4O4&ab_channel=freeCodeCamp.org)
  > This is a key resource. It provides a complete overview of the exam topics, often with practical demonstrations of the services.

### 2. Kubernetes Course
- [Docker Containers and Kubernetes Fundamentals – Full Hands-On Course](https://www.youtube.com/watch?v=kTp5xUtcalw&ab_channel=freeCodeCamp.org)
- [Getting Started with Google Kubernetes Engine](https://www.cloudskillsboost.google/paths/11/course_templates/2)
  > Containers and Kubernetes are crucial topics for the ACE exam. This video helps solidify your understanding of these concepts within the Google Cloud ecosystem.

### 3. Exam Guide
- [Associate Cloud Engineer: Certification Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer)
  > This is the official blueprint for the exam. Reviewing the five domains listed here is the best way to identify areas you need to focus on.

### 4. Exam Readiness
- [Preparing for Your Associate Cloud Engineer Journey](https://www.cloudskillsboost.google/journeys/11/course_templates/77)
  > This e-learning course is a must-do. It offers practice questions and a guided review of key topics, helping you gauge your readiness.

- [Associate Cloud Engineer Sample Questions](https://docs.google.com/forms/d/e/1FAIpQLSfexWKtXT2OSFJ-obA4iT3GmzgiOCGvjrT9OfxilWC1yPtmfQ/viewform)
  > Use this form to simulate the exam environment and get a feel for the types of questions you'll encounter.

- [Google Cloud Associate Cloud Engineer - The Certified Q&A for GCP](https://www.youtube.com/playlist?list=PLQMsfKRZZviRwqJwNmh1eAWnRMvlrk40x)
  > Practice with these sample questions and their explanations to understand the reasoning behind the correct answers.

## Official Documentation
> **Explanation:** This section contains relevant Google documentation for the exam topics. Since documentation is usually very long, I have added key points to study to make exam preparation easier. Be sure to focus on these points when reading the documentation, though it is excellent if you understand all the information in the documentation.

### 1. Compute Engine
- [Automatically apply VM configuration updates in a MIG](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)
  > Key points to study:
  - How VM updates work in **Managed Instance Groups (MIGs)**.
  - Using **maximum surge** and **maximum unavailable** to:
    - Ensure VM capacity doesn't decrease to handle user requests.
    - Prevent updates from causing additional costs.
  - **Rolling back** after an update if bugs are found in the new application version.
  - The difference between **proactive** and **opportunistic** updates.
  - The difference between **canary** and **rolling** updates.

- [About OS Login](https://cloud.google.com/compute/docs/oslogin/)
  > Key points to study:
  - What **OS Login** is and how it works.

- [Set up OS Login](https://cloud.google.com/compute/docs/oslogin/set-up-oslogin)
  > Key points to study:
  - The difference between `roles/compute.osLogin` and `roles/compute.osAdminLogin`.

- [Access control overview](https://cloud.google.com/compute/docs/access)
  > Key points to study:
  - The difference between several **IAM Roles**, such as `Compute Engine Network Admin` and `Compute Engine Security Admin`.

### 2. App Engine
- [Choose an App Engine environment](https://cloud.google.com/appengine/docs/the-appengine-environments)
  > Key points to study:
  - The difference between **App Engine Standard** and **App Engine Flex**.

- [How instances are managed](https://cloud.google.com/appengine/docs/standard/how-instances-are-managed)
  > Key points to study:
  - The difference between **automatic**, **basic**, and **manual scaling**.
  - App Engine can **auto-scale** based on parameters like **CPU utilization**, **concurrent requests**, and **throughput**.
  - What happens during **App Engine startup and shutdown**.

- [Roles that grant access](https://cloud.google.com/appengine/docs/standard/roles)
  > Key points to study:
  - The difference between several **IAM Roles**, such as `App Engine Service Admin` and `App Engine Deployer`.
  - Whether `App Engine Viewer` can see source code, or if only `App Engine Code Viewer` can.

### 3. Kubernetes
- [Node pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools)
  > Key points to study:
  - What **node pools** are and how to use them.

- [Resize a Standard cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster)
  > Key points to study:
  - How to **resize a cluster** and **node pools**.

- [Standard cluster upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades)
  > Key points to study:
  - How **cluster upgrades** in Google Kubernetes Engine work.
  - **Node pool upgrade strategies**, such as **surge upgrades** vs. **blue-green upgrades**.
  - The difference between **manual** and **automatic upgrades**.

- [Release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
  > Key points to study:
  - What **release channels** are and how to determine the right one.

- [Maintenance windows and exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)
  > Key points to study:
  - How to configure **GKE** to not perform cluster upgrades on specific dates using **exclusions**.

- [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)
  > Key points to study:
  - What **GKE Sandbox** is.

- [Google Kubernetes Engine access control](https://cloud.google.com/kubernetes-engine/docs/concepts/access-control)
  > Key points to study:
  - The difference between protection via **IAM** and **RBAC**.

### 4. Cloud Storage
- [Storage classes](https://cloud.google.com/storage/docs/storage-classes)
  > Key points to study:
  - The differences between **storage classes**.

- [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle)
  > Key points to study:
  - What **Object Lifecycle Management** is.
  - How to configure **lifecycle actions** and **lifecycle conditions**.

- [Object Retention Lock](https://cloud.google.com/storage/docs/object-lock)
  > Key points to study:
  - The use of **object lock** and its use cases.

- [IAM roles for Cloud Storage](https://cloud.google.com/storage/docs/access-control/iam-roles)
  > Key points to study:
  - The difference between several **IAM Roles**, such as `Storage Object Creator`, `Storage Object Viewer`, `Storage Object User`, `Storage Object Admin`, and `Storage Admin`.

### 5. BigQuery
- [Introduction to BigQuery jobs](https://cloud.google.com/bigquery/docs/jobs-overview)
  > Key points to study:
  - What a **job** is in BigQuery.

- [Access control with IAM](https://cloud.google.com/bigquery/docs/access-control)
  > Key points to study:
  - The level of **IAM Role** application on a project, dataset, or table/view.
  - The difference between several **IAM Roles**, such as `BigQuery Data Viewer`, `BigQuery User`, and `BigQuery Job User`.

### 6. Miscellaneous
- [Cloud Billing: Access control & permissions](https://cloud.google.com/billing/docs/how-to/billing-access)
  > Key points to study:
  - How a **billing account** works and its relationship to projects because you can link one billing account to multiple projects. 
  - The difference between several **IAM Roles** for billing accounts, such as `Billing Account User`, `Project Billing Manager`, and `Billing Account Administrator`.

- [Cloud Logging: Routing and storage overview](https://cloud.google.com/logging/docs/routing/overview)
  > Key points to study:
  - How to configure logs to be stored in **BigQuery** for analysis or **Cloud Storage** for archiving.

- [Moving a project](https://cloud.google.com/resource-manager/docs/moving-projects-folders)
  > Key points to study:
  - How to **move a project** in Google Cloud. A key point to remember is that when you move a project, all resources within it (like VMs, buckets, etc.) move with it.

## Additional Materials (Optional)
### 1. Infrastructure as Code (IAC)
- [HashiCorp Terraform Associate Certification Course - Pass the Exam!](https://www.youtube.com/watch?v=V4waklkBC38&ab_channel=freeCodeCamp.org)
  > A video to learn about Terraform. This material will not be on the Google exam, but it is useful for preparing for the HashiCorp Certified: Terraform Associate exam.
