# Preparation for GCP Associate Cloud Engineer (ACE) Certification
_[DISCLAIMER] Links dan materials yang ada disini dipergunakan untuk tambahan materi belajar. Sumber belajar yang saya dokumentasikan sendiri ini tidak merepresentasikan informasi resmi dari pihak Google Cloud, meskipun beberapa link dan material bersumber resmi dari Google Cloud._

---
## Exam Preparation Materials
### 1. Google Cloud Course
- [Google Cloud Associate Cloud Engineer Course - Pass the Exam!](https://www.youtube.com/watch?v=jpno8FSqpc8) **(Unofficial)**

    > Video material dari Antoni Tzavelas di freecodecamp. Silahkan dipelajari untuk memperkuat konsep dasar Google Cloud, dimana materi ini cocok untuk pemula dan terdapat beberapa demo yang ditampilkan.

- [Google Cloud Associate Cloud Engineer - The Certified Q&A for GCP](https://www.youtube.com/playlist?list=PLQMsfKRZZviRwqJwNmh1eAWnRMvlrk40x) **(Unofficial)**

    > Video material dari AwesomeGCP. Silahkan dipelajari untuk pembahasan contoh soal yang mungkin diujikan nanti.

### 2. Kubernetes Course
- [Belajar Kubernetes untuk Pemula](https://www.youtube.com/playlist?list=PL-CtdCApEFH8XrWyQAyRd6d_CKwxD8Ime)

    > Video material dari Programmer Zaman Now. Silahkan dipelajari untuk memperkuat konsep dasar tentang Kubernetes.

### 3. Exam Guide
- [Associate Cloud Engineer: Certification Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer?skip_cache=true)

    > Membahas 5 domain/section yang akan ditanyakan diujian. Bisa dicek beberapa poin mana yang tidak dimengerti untuk dipelajari lebih lanjut.

### 4. Exam Readiness
- [Associate Cloud Engineer Sample Questions](https://docs.google.com/forms/d/e/1FAIpQLSfexWKtXT2OSFJ-obA4iT3GmzgiOCGvjrT9OfxilWC1yPtmfQ/viewform)

    > Simulasi ujian via Google Forms untuk mengenali format pertanyaan ujian GCP ACE nanti.

## Official Documentation
### 1. Permission
- [Cloud Billing: Access control & permissions](https://cloud.google.com/billing/docs/how-to/billing-access) untuk mempelajari:
  - Bagaimana billing di Google Cloud bekerja.
  - Mengenal perbedaan beberapa IAM Role terkait Cloud Billing, contohnya Billing Account User dengan Billing Account Administrator.

- [Big Query: Access control with IAM](https://cloud.google.com/bigquery/docs/access-control) untuk mempelajari:
  - Scope penerapan Role, bisa di project, dataset, atau table/view.
  - Mengenal perbedaan beberapa IAM Role terkait Big Query, contohnya BigQuery Data Editor dengan BigQuery Job User.

- [Compute Engine: Access control overview](https://cloud.google.com/compute/docs/access) untuk mempelajari:
  - Mengenal perbedaan beberapa IAM Role terkait Compute Engine, contohnya Compute Engine Network Admin dengan Compute Engine Security Admin.

- [App Engine: Roles that grant access](https://cloud.google.com/appengine/docs/standard/python/roles) untuk mempelajari:
  - Mengenal perbedaan beberapa IAM Role terkait App Engine, contohnya App Engine Code Viewer dengan App Engine Deployer.

### 2. Maintenance


### 3. Kubernetes
- [Node pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) dan resizing a cluster https://cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster) untuk mempelajari:
  - Apa itu node pools.
  - Resize cluster dan node pools.

https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot
https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades
https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions


https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods

--> Security & Update
https://cloud.google.com/kubernetes-engine/docs/concepts/access-control

App Engine Standard & Flex
https://cloud.google.com/appengine/docs/the-appengine-environments
https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed

Etc.
https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups
https://cloud.google.com/resource-manager/docs/moving-projects-folders
https://cloud.google.com/logging/docs/routing/overview
https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images

## Hands-on Labs (Optional)
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/catalog?price%5B%5D=free)

    > Kumpulan lab Google Cloud yang disediakan gratis. Untuk mencoba bisa mendaftar menggunakan akun Google kita.

- [Play with Docker](https://labs.play-with-docker.com/)
- [Kubernetes: Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)

    > Hands-on Labs gratis untuk belajar Docker dan Kubernetes. Lab berjalan di browser tanpa memerlukan instalasi.

## Additional Material (Optional)
### 1. Infrastructure as Code (IAC)
- [HashiCorp Terraform Associate Certification Course - Pass the Exam!](https://www.youtube.com/watch?v=V4waklkBC38&ab_channel=freeCodeCamp.org) **(Unofficial)**

    > Video material dari Andrew Brown (ExamPro) di freecodecamp. Silahkan dipelajari untuk mempelajari Terraform dan mempersiapkan ujian HashiCorp Certified: Terraform Associate.
