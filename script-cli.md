### Project
- [gcloud projects create](https://cloud.google.com/sdk/gcloud/reference/projects/create).
    > **Penjelasan:** Memahami cara membuat proyek baru di Google Cloud adalah keterampilan dasar yang sangat penting karena semua sumber daya dikelola dalam konteks proyek. Pastikan untuk menguasai cara membuat proyek baru menggunakan `gcloud` dan pahami konsep seperti Project ID, Name, dan Number.

- [gcloud projects list](https://cloud.google.com/sdk/gcloud/reference/projects/list).
    > **Penjelasan:** Saat bekerja dengan beberapa proyek, penting untuk dapat melihat daftar proyek yang tersedia dalam satu akun. Ini membantu dalam navigasi dan manajemen proyek secara efisien.

- [gcloud projects update](https://cloud.google.com/sdk/gcloud/reference/projects/update).
    > **Penjelasan:** Mempelajari cara memperbarui proyek yang ada, seperti mengubah metadata proyek. Dalam beberapa kasus, metadata yang tepat dapat memengaruhi kebijakan akses dan penggunaan sumber daya.

### Config
- [gcloud config configurations](https://cloud.google.com/sdk/gcloud/reference/config/configurations).
    > **Penjelasan:** Dalam ujian, seringkali perlu bekerja di berbagai konfigurasi dan lingkungan. Memahami cara membuat, mengelola, dan mengganti konfigurasi `gcloud` akan sangat membantu ketika berpindah antar proyek atau akun.

- [gcloud config configurations create](https://cloud.google.com/sdk/gcloud/reference/config/configurations/create).
    > **Penjelasan:** Membuat konfigurasi baru memungkinkan pengguna mengisolasi pengaturan untuk proyek atau akun yang berbeda, yang sangat penting dalam pengelolaan multi-lingkungan atau multi-tim.

- [gcloud config configurations list](https://cloud.google.com/sdk/gcloud/reference/config/configurations/list).
    > **Penjelasan:** Mengetahui cara melihat daftar konfigurasi membantu dalam pengelolaan konfigurasi yang telah dibuat dan dalam menentukan konfigurasi mana yang aktif.

- [gcloud config configurations activate](https://cloud.google.com/sdk/gcloud/reference/config/configurations/activate).
    > **Penjelasan:** Mengaktifkan konfigurasi tertentu memungkinkan pengguna untuk dengan cepat berpindah antara konfigurasi saat bekerja di berbagai proyek atau akun.

- [gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set).
    > **Penjelasan:** Perintah ini memungkinkan pengguna untuk mengatur nilai tertentu dalam konfigurasi saat ini, seperti proyek aktif atau region default.

### Kubernetes
- [gcloud container clusters create](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create).
    > **Penjelasan:** Penting untuk memahami cara membuat kluster Kubernetes di Google Kubernetes Engine (GKE). Ini termasuk pengaturan seperti jumlah node, lokasi, dan konfigurasi jaringan.

- [gcloud container clusters update](https://cloud.google.com/sdk/gcloud/reference/container/clusters/update).
    > **Penjelasan:** Setelah kluster dibuat, kemampuan untuk memperbaruinya (misalnya mengubah ukuran atau pengaturan lainnya) akan sering diuji dalam skenario ujian.

- [gcloud container clusters upgrade](https://cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade).
    > **Penjelasan:** Meng-upgrade kluster Kubernetes adalah proses penting dalam menjaga keamanan dan stabilitas kluster. Pahami cara melakukan upgrade versi Kubernetes dan manajemen upgrade node.

- [gcloud container node-pools create](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create).
    > **Penjelasan:** Node pool memungkinkan manajemen set node dalam kluster GKE. Memahami cara membuat node pool adalah keterampilan penting dalam pengelolaan kluster yang efisien.

- [gcloud container node-pools update](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/update).
    > **Penjelasan:** Memperbarui node pool sangat penting untuk mengubah konfigurasi seperti jenis mesin atau ukuran node.

- [gcloud container node-pools rollback](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/rollback).
    > **Penjelasan:** Rollback node pool memungkinkan pengembalian ke konfigurasi sebelumnya jika terjadi kesalahan saat pembaruan, sebuah langkah penting dalam strategi DevOps dan CI/CD.

- Kubectl --> deploy pod/deployment, auto scaling, expose deployment
    > **Penjelasan:** Ketahui dasar-dasar `kubectl` untuk pengelolaan kluster Kubernetes, termasuk cara men-deploy aplikasi, menskalakan otomatis, dan mengekspose deployment ke internet. Ini adalah keterampilan fundamental yang sering diuji dalam konteks manajemen beban kerja di Kubernetes.

### App Engine
- [gcloud app create](https://cloud.google.com/sdk/gcloud/reference/app/create).
    > **Penjelasan:** App Engine memungkinkan deployment aplikasi secara otomatis. Pahami cara membuat aplikasi baru di App Engine, terutama perbedaan antara App Engine Standard dan Flexible Environment.

- [gcloud app deploy](https://cloud.google.com/sdk/gcloud/reference/app/deploy).
    > **Penjelasan:** Kemampuan untuk men-deploy aplikasi ke App Engine secara efisien adalah keterampilan penting yang diuji dalam ujian. Pastikan memahami proses deployment, serta bagaimana file `app.yaml` berfungsi.

- [gcloud app browse](https://cloud.google.com/sdk/gcloud/reference/app/browse).
    > **Penjelasan:** Mengetahui cara membuka aplikasi yang telah di-deploy dalam browser memungkinkan pengguna untuk segera memeriksa status deployment.

- [gcloud app services set-traffic](https://cloud.google.com/sdk/gcloud/reference/app/services/set-traffic).
    > **Penjelasan:** Manajemen lalu lintas di antara beberapa versi aplikasi sangat penting. Pahami cara mengarahkan lalu lintas ke versi aplikasi tertentu.

- [gcloud app versions migrate](https://cloud.google.com/sdk/gcloud/reference/app/versions/migrate).
    > **Penjelasan:** Mempersiapkan migrasi antar versi aplikasi memungkinkan pengguna memastikan aplikasi berjalan dengan lancar selama proses upgrade.

- [gcloud app update](https://cloud.google.com/sdk/gcloud/reference/app/update).
    > **Penjelasan:** Memperbarui aplikasi di App Engine adalah proses penting yang memerlukan pemahaman mendalam tentang konfigurasi aplikasi dan layanan yang dijalankan.

### VPC & Firewall
- [gcloud compute networks create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create).
    > **Penjelasan:** Virtual Private Cloud (VPC) adalah tulang punggung jaringan di Google Cloud. Ketahui cara membuat VPC dan pahami konsep seperti mode auto dan custom.

- [gcloud compute networks subnets create](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    > **Penjelasan:** Pahami cara membuat subnet dalam jaringan VPC, termasuk konfigurasi seperti region dan rentang IP.

- [gcloud compute networks subnets update](https://cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    > **Penjelasan:** Memperbarui subnet sangat penting, terutama saat menambahkan rentang IP baru atau mengubah konfigurasi subnet.

- [gcloud compute firewall-rules create](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
    > **Penjelasan:** Mengelola aturan firewall sangat penting untuk menjaga keamanan jaringan. Pahami cara membuat aturan firewall untuk mengizinkan atau menolak lalu lintas masuk dan keluar.

- [gcloud compute firewall-rules update](https://cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update).
    > **Penjelasan:** Memperbarui aturan firewall penting untuk menyesuaikan aturan jaringan seiring perubahan kebutuhan keamanan atau aplikasi.
