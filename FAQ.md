# Google Cloud FAQ
## Compute Engine
### 1. Berapa banyak CPU core untuk satu vCPU di Compute Engine?
  > 1 vCPU sama dengan 1 _[hyperthread](https://www.youtube.com/watch?v=lrT9Bl0MCXQ)_ di CPU. Dimana umumnya setiap 1 core didalam CPU memiliki 2 _hyperthread_. Contohnya dari spesifikasi [Intel® Xeon® Processor E7](https://ark.intel.com/content/www/us/en/ark/products/93806/intel-xeon-processor-e74850-v4-40m-cache-2-10-ghz.html), penjelasan pengaturan [berapa vCPU untuk VM](https://help.tableau.com/current/server/en-us/ts_gcp_virtual_machine_selection.htm) yang akan dipasang Tableau, atau [daftar spesifikasi Intel Xeon - Skylake](https://en.wikipedia.org/wiki/List_of_Intel_Skylake-based_Xeon_microprocessors).
  > 
  > Jadi 1 vCPU bisa dikatakan 1/2 core di CPU.

### 2. Apakah harga dari *[static IP](https://cloud.google.com/compute/docs/ip-addresses#reservedaddress)* dan *[ephemeral IP](https://cloud.google.com/compute/docs/ip-addresses#ephemeraladdress)* berbeda?
  > [Harga](https://cloud.google.com/vpc/network-pricing) keduanya sama, tapi akan mahal _static IP_ kalau kita tidak menggunakan _static IP_ tersebut.

## Persistent Disk
### 1. Apakah ada [best practice untuk snapshot](https://cloud.google.com/compute/docs/disks/snapshot-best-practices) untuk mencegah [dampak ke performance saat snapshot](https://4sysops.com/archives/performance-impact-of-snapshots-in-vmware-vsphere-7/)?
  > Konsep dari snapshot di Google Cloud berbeda dibandingkan produk virtualisasi di on-premise. Dimana setiap snapshot Persistent Disk menyimpan data yang bertambah atau berubah ke Cloud Storage setelah full backup di snapshot pertama, dan VM akan tetap menggunakan Persistent Disk-nya untuk mengakses dan menyimpan data. VM akan menggunakan snapshot, ketika snapshot tadi kita restore menjadi persistent disk. Jadi tidak ada masalah performance yang berdampak ke VM jika kita melakukan banyak snapshot.

## Cloud Storage
### 1. Apakah [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview) bisa dikirimkan ke data center saya di Indonesia?
  > Transfer Appliance belum support untuk pengiriman ke Indonesia. Mungkin kita bisa mencoba layanan [Offline Data Import](https://cloud.google.com/blog/products/gcp/iron-mountain-increases-bandwidth-to-google-cloud-by-10x-for-faster-data-ingestion-) dari 3rd party. 

## Cloud Identity
### 1. Apakah kita bisa ganti dari Cloud Identity ke Workspace?
  > Hal tersebut bisa kita lakukan, tapi bukan diganti melainkan [diupgrade](https://support.google.com/cloudidentity/answer/7668760#zippy=%2Ccloud-identity-and-google-workspace). Caranya kita beli license/subscribe Google Workspace untuk Cloud Identity kita. User bisa memiliki Cloud Identity license dan Google Workspace license secara bersamaan.
