# Preparation for Google Associate Cloud Engineer (ACE) Certification
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
- [Preparing for Your Associate Cloud Engineer Journey](https://www.cloudskillsboost.google/journeys/11/course_templates/77)
    > E-learning untuk latihan persiapan ujian Google Cloud Associate Cloud Engineer dari Google Cloud. Materi berisikan eksplorasi topik yang keluar di ujian dan beberapa contoh soal ujian.

- [Associate Cloud Engineer Sample Questions](https://docs.google.com/forms/d/e/1FAIpQLSfexWKtXT2OSFJ-obA4iT3GmzgiOCGvjrT9OfxilWC1yPtmfQ/viewform)
    > Simulasi ujian via Google Forms untuk mengenali format pertanyaan ujian Google Cloud Associate Cloud Engineer nanti.

## Official Documentation
### 1. Compute Engine
- [Automatically apply VM configuration updates in a MIG](https://cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups) untuk mempelajari:
  - Bagaimana update VM di Managed Instance Groups bekerja.
  - Bagaimana memanfaatkan maximum surge dan maximum unavailable agar:
    - Kapasitas VM tidak berkurang untuk menghandle request dari user.
    - Update yang dilakukan tidak mengeluarkan biaya tambahan.
  - Bagaimana rolling-back setelah update karena ditemukan bug pada aplikasi versi terbaru.
  - Perbedaan proactive dan opportunistic update.
  - Perbedaan canary dan rolling-update.

- [About OS Login](https://cloud.google.com/compute/docs/oslogin/) untuk mempelajari:
  - Apa itu OS Login.

- [Set up OS Login](https://cloud.google.com/compute/docs/oslogin/set-up-oslogin) untuk mempelajari:
  - Perbedaan roles/compute.osLogin dan roles/compute.osAdminLogin.

- [Access control overview](https://cloud.google.com/compute/docs/access) untuk mempelajari:
  - Perbedaan beberapa IAM Role, contohnya Compute Engine Network Admin dan Compute Engine Security Admin.

### 2. App Engine
- [Choose an App Engine environment](https://cloud.google.com/appengine/docs/the-appengine-environments) untuk mempelajari:
  - Perbedaan App Engine Standard dan App Engine Flex.

- [How instances are managed](https://cloud.google.com/appengine/docs/standard/how-instances-are-managed) untuk mempelajari:
  - Perbedaan automatic, basic dan manual scaling.
  - App Engine bisa auto scaling berdasarkan apa, contohnya CPU utilization, concurrent request, dan throughput.
  - Apa yang terjadi dengan App Engine ketika startup dan shutdown.

- [Roles that grant access](https://cloud.google.com/appengine/docs/standard/roles) untuk mempelajari:
  - Perbedaan beberapa IAM Role, contohnya App Engine Service Admin dan App Engine Deployer.
  - Apakah App Engine Viewer bisa melihat source code, atau App Engine Code Viewer yang bisa.

### 3. Kubernetes
- [Node pools](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) untuk mempelajari:
  - Apa itu node pools.

- [Resize a Standard cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster) untuk mempelajari:
  - Cara resize cluster dan node pools.

- [Standard cluster upgrades](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades) untuk mempelajari:
  - Bagaimana upgrade cluster di Google Kubernetes Engine bekerja.
  - Apa saja strategi dalam upgrade node pool, contohnya surge upgrades vs. blue-green upgrades.
  - Perbedaan upgrade manual dan otomatis.

- [Release channels](https://cloud.google.com/kubernetes-engine/docs/concepts/release-channels) untuk mempelajari:
  - Apa perbedaan release channel.
  - Menentukan release channel yang akan digunakan.

- [Maintenance windows and exclusions](https://cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) untuk mempelajari:
  - Mengatur agar GKE tidak mengupgrade cluster ditanggal tertentu menggunakan exclusions.

- [GKE Sandbox](https://cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) untuk mempelajari:
  - Apa itu GKE Sandbox.

- [Google Kubernetes Engine access control](https://cloud.google.com/kubernetes-engine/docs/concepts/access-control) untuk mempelajari:
  - Perbedaan antara proteksi via IAM dan RBAC.

### 4. BigQuery
- [Introduction to BigQuery jobs](https://cloud.google.com/bigquery/docs/jobs-overview) untuk mempelajari:
  - Apa itu job.

- [Access control with IAM](https://cloud.google.com/bigquery/docs/access-control) untuk mempelajari:
  - Perbedaan level penerapan IAM Role, bisa di project, dataset, atau table/view.
  - Perbedaan beberapa IAM Role, contohnya BigQuery Data Viewer, BigQuery User, BigQuery Job User.

### 5. Others
- [Cloud Billing: Access control & permissions](https://cloud.google.com/billing/docs/how-to/billing-access) untuk mempelajari:
  - Bagaimana billing account bekerja, berikut hubungannya dengan project.
  - Perbedaan beberapa IAM Role untuk billing account, contohnya Billing Account User, Project Billing Manager dan Billing Account Administrator.

- [Cloud Logging: Routing and storage overview](https://cloud.google.com/logging/docs/routing/overview) untuk mempelajari:
  - Bagaimana mengatur agar log bisa disimpan kedalam BigQuery untuk diolah disana atau Cloud Storage untuk archival.

- [Moving a project](https://cloud.google.com/resource-manager/docs/moving-projects-folders) untuk mempelajari:
  - Bagaimana memindahkan project.

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
