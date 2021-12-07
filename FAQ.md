# Google Cloud FAQ
## Compute Engine
### 1. Berapa banyak CPU core untuk satu vCPU di Compute Engine?
  > 1 vCPU sama dengan 1 [_hyperthread_](https://www.youtube.com/watch?v=lrT9Bl0MCXQ) di CPU. Dimana umumnya setiap 1 core didalam CPU memiliki 2 _hyperthread_. Contohnya dari spesifikasi [Intel® Xeon® Processor E7](https://ark.intel.com/content/www/us/en/ark/products/93806/intel-xeon-processor-e74850-v4-40m-cache-2-10-ghz.html), penjelasan pengaturan [berapa vCPU untuk VM](https://help.tableau.com/current/server/en-us/ts_gcp_virtual_machine_selection.htm) yang akan dipasang Tableau, atau yang ada [didaftar ini](https://en.wikipedia.org/wiki/List_of_Intel_Skylake-based_Xeon_microprocessors)).
  > 
  > Jadi 1 vCPU bisa dikatakan 1/2 core di CPU.

### 2. Apakah harga dari static IP dan ephemeral IP berbeda?
  > [Harga](https://cloud.google.com/vpc/network-pricing) keduanya sama, tapi akan mahal static IP kalau kita tidak menggunakan static IP tersebut.

## Cloud Identity
### 1. Apakah kita bisa ganti dari Cloud Identity ke Workspace?
  > Hal tersebut bisa kita lakukan, tapi bukan diganti melainkan [diupgrade](https://support.google.com/cloudidentity/answer/7668760#zippy=%2Ccloud-identity-and-google-workspace). Caranya kita beli license/subscribe Google Workspace untuk Cloud Identity kita. User bisa memiliki Cloud Identity license dan Google Workspace license secara bersamaan.
