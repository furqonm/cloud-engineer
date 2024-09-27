# Persiapan untuk Sertifikasi Google Cloud Associate Cloud Engineer (ACE)
_[DISCLAIMER] Tautan dan materi yang terdapat di sini disediakan sebagai tambahan untuk pembelajaran. Sumber-sumber belajar yang saya dokumentasikan sendiri ini tidak mewakili informasi resmi dari pihak Google Cloud, meskipun beberapa tautan dan materi berasal dari sumber resmi Google Cloud._

---
## Materi Persiapan Ujian
### 1. Kursus Google Cloud
- [Google Cloud Fundamentals: Core Infrastructure](https://www.cloudskillsboost.google/paths/11/course_templates/60)
    > Video ini memperkuat konsep dasar serta membahas beberapa layanan yang sering digunakan di Google Cloud. Materi ini bersifat fundamental dan cocok bagi pemula di dunia cloud.

- [Google Cloud Associate Cloud Engineer Course - Pass the Exam!](https://www.youtube.com/watch?v=jpno8FSqpc8) **(Tidak Resmi)**
    > Video ini memberikan penjelasan cukup lengkap beserta demo layanan yang akan diujikan dalam ujian Google Cloud.

### 2. Kursus Kubernetes
- [Introduction to Container and Kubernetes in Google Cloud Platform](https://www.youtube.com/watch?v=JKBANQEwMgI) **(Tidak Resmi)**
- [Getting Started with Google Kubernetes Engine](https://www.cloudskillsboost.google/paths/11/course_templates/2)
    > Video ini membantu memperkuat pemahaman dasar tentang Kubernetes di Google Cloud.

### 3. Panduan Ujian
- [Associate Cloud Engineer: Certification Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer?skip_cache=true)
    > Membahas 5 domain/section yang akan diujikan. Anda dapat memeriksa poin-poin mana yang belum dipahami untuk dipelajari lebih lanjut.

### 4. Kesiapan Ujian
- [Preparing for Your Associate Cloud Engineer Journey](https://www.cloudskillsboost.google/journeys/11/course_templates/77)
    > E-learning dari Google Cloud untuk latihan persiapan ujian Google Cloud Associate Cloud Engineer. Materi ini mencakup eksplorasi topik yang akan muncul dalam ujian serta beberapa contoh soal.

- [Associate Cloud Engineer Sample Questions](https://docs.google.com/forms/d/e/1FAIpQLSfexWKtXT2OSFJ-obA4iT3GmzgiOCGvjrT9OfxilWC1yPtmfQ/viewform)
    > Simulasi ujian melalui Google Forms untuk mengenali format soal dalam ujian Google Cloud Associate Cloud Engineer.

- [Google Cloud Associate Cloud Engineer - The Certified Q&A for GCP](https://www.youtube.com/playlist?list=PLQMsfKRZZviRwqJwNmh1eAWnRMvlrk40x) **(Tidak Resmi)**
    > Video yang berisi contoh soal dan pembahasan jawabannya.

## Dokumentasi Resmi
> **Penjelasan:** Bagian ini berisi dokumentasi dari Google yang relevan untuk topik ujian. Karena dokumentasi biasanya sangat panjang, saya menambahkan poin-poin penting yang perlu dipelajari agar memudahkan persiapan ujian. Pastikan untuk fokus pada poin-poin tersebut saat membaca dokumentasi, meskipun sangat bagus kalau mengerti semua informasi yang tertera dalam dokumentasi.

### 1. Compute Engine
- [Automatically apply VM configuration updates in a MIG](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)
    > Poin-poin yang harus dipelajari:
    - Cara kerja update VM di Managed Instance Groups.
    - Memanfaatkan maximum surge dan maximum unavailable agar:
        - Kapasitas VM tidak berkurang untuk menangani permintaan pengguna.
        - Update yang dilakukan tidak menyebabkan biaya tambahan.
    - Rolling-back setelah update jika ditemukan bug di aplikasi versi terbaru.
    - Perbedaan antara proactive dan opportunistic update.
    - Perbedaan antara canary dan rolling-update.

- [About OS Login](https://cloud.google.com/compute/docs/oslogin/)
    > Poin-poin yang harus dipelajari:
    - Apa itu OS Login dan bagaimana fungsinya.

- [Set up OS Login](https://cloud.google.com/compute/docs/oslogin/set-up-oslogin)
    > Poin-poin yang harus dipelajari:
    - Perbedaan roles/compute.osLogin dan roles/compute.osAdminLogin.

- [Access control overview](https://cloud.google.com/compute/docs/access)
    > Poin-poin yang harus dipelajari:
    - Perbedaan beberapa IAM Role, seperti Compute Engine Network Admin dan Compute Engine Security Admin.

### 2. App Engine
- [Choose an App Engine environment](https://cloud.google.com/appengine/docs/the-appengine-environments)
    > Poin-poin yang harus dipelajari:
    - Perbedaan antara App Engine Standard dan App Engine Flex.

- [How instances are managed](https://cloud.google.com/appengine/docs/standard/how-instances-are-managed)
    > Poin-poin yang harus dipelajari:
    - Perbedaan antara automatic, basic, dan manual scaling.
    - App Engine dapat auto scaling berdasarkan parameter seperti CPU utilization, concurrent request, dan throughput.
    - Apa yang terjadi saat App Engine startup dan shutdown.

- [Roles that grant access](https://cloud.google.com/appengine/docs/standard/roles)
    > Poin-poin yang harus dipelajari:
    - Perbedaan beberapa IAM Role, seperti App Engine Service Admin dan App Engine Deployer.
    - Apakah App Engine Viewer dapat melihat source code, atau hanya App Engine Code Viewer yang bisa.

### 3. Kubernetes
- [Node pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools)
    > Poin-poin yang harus dipelajari:
    - Apa itu node pools dan bagaimana cara menggunakannya.

- [Resize a Standard cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster)
    > Poin-poin yang harus dipelajari:
    - Cara resize cluster dan node pools.

- [Standard cluster upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades)
    > Poin-poin yang harus dipelajari:
    - Bagaimana upgrade cluster di Google Kubernetes Engine bekerja.
    - Strategi upgrade node pool, seperti surge upgrades vs. blue-green upgrades.
    - Perbedaan upgrade manual dan otomatis.

- [Release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
    > Poin-poin yang harus dipelajari:
    - Apa itu release channel dan bagaimana menentukan release channel yang tepat.

- [Maintenance windows and exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)
    > Poin-poin yang harus dipelajari:
    - Cara mengatur agar GKE tidak melakukan upgrade pada cluster di tanggal tertentu menggunakan exclusions.

- [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)
    > Poin-poin yang harus dipelajari:
    - Apa itu GKE Sandbox.

- [Google Kubernetes Engine access control](https://cloud.google.com/kubernetes-engine/docs/concepts/access-control)
    > Poin-poin yang harus dipelajari:
    - Perbedaan antara proteksi via IAM dan RBAC.

### 4. Cloud Storage
- [Storage classes](https://cloud.google.com/storage/docs/storage-classes)
    > Poin-poin yang harus dipelajari:
    - Perbedaan storage class.

- [Object Lifecycle Management](https://cloud.google.com/storage/docs/lifecycle)
    > Poin-poin yang harus dipelajari:
    - Apa itu object lifecycle management.
    - Cara mengonfigurasi lifecycle actions dan lifecycle conditions.

- [Object Retention Lock](https://cloud.google.com/storage/docs/object-lock)
    > Poin-poin yang harus dipelajari:
    - Kegunaan object lock dan use case-nya.

- [IAM roles for Cloud Storage](https://cloud.google.com/storage/docs/access-control/iam-roles)
    > Poin-poin yang harus dipelajari:
    - Perbedaan beberapa IAM Role, seperti Storage Object Creator, Storage Object Viewer, Storage Object User, Storage Object Admin, dan Storage Admin.

### 5. BigQuery
- [Introduction to BigQuery jobs](https://cloud.google.com/bigquery/docs/jobs-overview)
    > Poin-poin yang harus dipelajari:
    - Apa itu job di BigQuery.

- [Access control with IAM](https://cloud.google.com/bigquery/docs/access-control)
    > Poin-poin yang harus dipelajari:
    - Level penerapan IAM Role di project, dataset, atau table/view.
    - Perbedaan beberapa IAM Role, seperti BigQuery Data Viewer, BigQuery User, dan BigQuery Job User.

### 6. Lain-lain
- [Cloud Billing: Access control & permissions](https://cloud.google.com/billing/docs/how-to/billing-access)
    > Poin-poin yang harus dipelajari:
    - Cara kerja billing account serta hubungannya dengan project.
    - Perbedaan beberapa IAM Role untuk billing account, seperti Billing Account User, Project Billing Manager, dan Billing Account Administrator.

- [Cloud Logging: Routing and storage overview](https://cloud.google.com/logging/docs/routing/overview)
    > Poin-poin yang harus dipelajari:
    - Cara mengatur log agar disimpan ke BigQuery untuk analisis atau Cloud Storage untuk arsip.

- [Moving a project](https://cloud.google.com/resource-manager/docs/moving-projects-folders)
    > Poin-poin yang harus dipelajari:
    - Cara memindahkan project di Google Cloud.

## Hands-on Labs (Opsional)
- [Google Cloud Skills Boost](https://www.cloudskillsboost.google/catalog?price%5B%5D=free)
    > Kumpulan lab Google Cloud yang disediakan secara gratis. Anda bisa mencoba dengan mendaftar menggunakan akun Google.

- [Play with Docker](https://labs.play-with-docker.com/)
- [Kubernetes: Hello Minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)
    > Hands-on Labs gratis untuk belajar Docker dan Kubernetes. Lab berjalan di browser tanpa memerlukan instalasi.

## Materi Tambahan (Opsional)
### 1. Infrastructure as Code (IAC)
- [HashiCorp Terraform Associate Certification Course - Pass the Exam!](https://www.youtube.com/watch?v=V4waklkBC38&ab_channel=freeCodeCamp.org) **(Tidak Resmi)**
    > Video untuk mempelajari Terraform. Materi ini tidak akan diujikan dalam ujian Google, tetapi bermanfaat untuk persiapan ujian HashiCorp Certified: Terraform Associate.
