### Project
- [gcloud projects create](https://cloud.google.com/sdk/gcloud/reference/projects/create)
  > Understanding how to create a new project in Google Cloud is a critical foundational skill, as all resources are managed within a project's context. Be sure to master how to create a new project using `gcloud` and understand concepts like Project ID, Name, and Number.

- [gcloud projects list](https://cloud.google.com/sdk/gcloud/reference/projects/list)
  > When working with multiple projects, it's essential to be able to see a list of the available projects within a single account. This helps with efficient project navigation and management.

- [gcloud projects update](https://cloud.google.com/sdk/gcloud/reference/projects/update)
  > Learn how to update an existing project, such as changing project metadata. In some cases, proper metadata can affect access policies and resource usage.

---

### Config
- [gcloud config configurations](https://cloud.google.com/sdk/gcloud/reference/config/configurations)
  > In exams, it's often necessary to work in various configurations and environments. Understanding how to create, manage, and switch `gcloud` configurations is extremely helpful when moving between different projects or accounts.

- [gcloud config configurations create](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create)
  > Creating a new configuration allows users to isolate settings for different projects or accounts, which is crucial for managing multi-environment or multi-team setups.

- [gcloud config configurations list](https://cloud.google.com/sdk/gcloud/reference/config/configurations/list)
  > Knowing how to list configurations helps in managing created configurations and in determining which configuration is currently active.

- [gcloud config configurations activate](https://cloud.google.com/sdk/gcloud/reference/config/configurations/activate)
  > Activating a specific configuration allows users to quickly switch between configurations when working on various projects or accounts.

- [gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set)
  > This command allows users to set a specific value in the current configuration, such as the active project or default region.

---

### Kubernetes
- [gcloud container clusters create](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create)
  > It's important to understand how to create a Kubernetes cluster in Google Kubernetes Engine (GKE). This includes settings like the number of nodes, location, and network configuration.

- [gcloud container clusters update](https://cloud.google.com/sdk/gcloud/reference/container/clusters/update)
  > Once a cluster is created, the ability to update it (e.g., changing its size or other settings) is often tested in exam scenarios.

- [gcloud container clusters upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade)
  > Upgrading a Kubernetes cluster is an important process for maintaining cluster security and stability. Understand how to perform a Kubernetes version upgrade and manage node upgrades.

- [gcloud container node-pools create](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create)
  > Node pools allow for the management of sets of nodes within a GKE cluster. Understanding how to create a node pool is a key skill for efficient cluster management.

- [gcloud container node-pools update](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update)
  > Updating a node pool is critical for changing configurations like machine type or node size.

- [gcloud container node-pools rollback](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback)
  > Rolling back a node pool allows for a return to a previous configuration if an error occurs during an update, a crucial step in DevOps and CI/CD strategies.

- Kubectl --> deploy pod/deployment, auto scaling, expose deployment
  > Know the basics of `kubectl` for Kubernetes cluster management, including how to deploy applications, auto-scale, and expose deployments to the internet. These are fundamental skills often tested in the context of workload management in Kubernetes.

---

### App Engine
- [gcloud app create](https://cloud.google.com/sdk/gcloud/reference/app/create)
  > App Engine allows for automated application deployment. Understand how to create a new application in App Engine, especially the difference between the App Engine Standard and Flexible Environments.

- [gcloud app deploy](https://cloud.google.com/sdk/gcloud/reference/app/deploy)
  > The ability to efficiently deploy an application to App Engine is a key skill tested in exams. Be sure to understand the deployment process, as well as how the `app.yaml` file functions.

- [gcloud app browse](https://cloud.google.com/sdk/gcloud/reference/app/browse)
  > Knowing how to open a deployed application in a browser allows users to quickly check the deployment status.

- [gcloud app services set-traffic](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic)
  > Managing traffic between different versions of an application is very important. Understand how to direct traffic to a specific application version.

- [gcloud app versions migrate](https://cloud.google.com/sdk/gcloud/reference/app/versions/migrate)
  > Preparing for migration between application versions allows users to ensure the application runs smoothly during the upgrade process.

- [gcloud app update](https://cloud.google.com/sdk/gcloud/reference/app/update)
  > Updating an application in App Engine is a critical process that requires a deep understanding of the application's configuration and the services it runs.

---

### VPC & Firewall
- [gcloud compute networks create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create)
  > Virtual Private Cloud (VPC) is the backbone of networking in Google Cloud. Know how to create a VPC and understand concepts like auto and custom modes.

- [gcloud compute networks subnets create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create)
  > Understand how to create subnets within a VPC network, including configurations like region and IP range.

- [gcloud compute networks subnets update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update)
  > Updating a subnet is very important, especially when adding a new IP range or changing the subnet's configuration.

- [gcloud compute firewall-rules create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create)
  > Managing firewall rules is crucial for network security. Understand how to create firewall rules to allow or deny inbound and outbound traffic.

- [gcloud compute firewall-rules update](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update)
  > Updating firewall rules is important for adapting network rules as security or application needs change.
