### Google Cloud FAQ

---
## Compute Engine

### 1. How many CPU cores are in one vCPU on Compute Engine?
One vCPU is equivalent to a single **hyperthread** on a CPU. A standard CPU core typically has two hyperthreads. For example, you can see this in the specifications for an [Intel® Xeon® Processor E7](https://ark.intel.com/content/www/us/en/ark/products/93806/intel-xeon-processor-e74850-v4-40m-cache-2-10-ghz.html) or in the [Intel Xeon - Skylake specifications](https://en.wikipedia.org/wiki/List_of_Intel_Skylake-based_Xeon_microprocessors).

Essentially, you can consider one vCPU to be half of a physical CPU core.

### 2. Is there a price difference between a static IP and an ephemeral IP?
Both **static** and **ephemeral** external IP addresses have the same price per hour when they are attached to a running VM. However, a static IP address becomes more expensive if you reserve it but don't assign it to a VM.

---
## Persistent Disk

### 1. Is there a best practice for taking snapshots to avoid performance impact?
The concept of snapshots on Google Cloud is different from on-premises virtualization products. With Google Cloud Persistent Disks, each snapshot after the initial full backup only stores new or changed data and is saved to Cloud Storage. Your VM continues to use its original Persistent Disk for all read and write operations.

Because the snapshot process does not affect your VM's ongoing performance, you can take many snapshots without worrying about a performance hit. A snapshot is only used when you need to restore it to a new Persistent Disk.

---
## Cloud Storage

### 1. Can a Transfer Appliance be shipped to my data center in Indonesia?
Google Cloud's Transfer Appliance is not currently available for shipment to Indonesia. As an alternative, you can consider using a third-party service like [Iron Mountain's Offline Data Import](https://cloud.google.com/blog/products/gcp/iron-mountain-increases-bandwidth-to-google-cloud-by-10x-for-faster-data-ingestion-).

---
## Cloud Identity

### 1. Can we switch from Cloud Identity to Workspace?
You don't switch from Cloud Identity to Google Workspace; you **upgrade** to it. You can purchase a Google Workspace license for your Cloud Identity account, allowing users to have both a Cloud Identity license and a Google Workspace license simultaneously.
