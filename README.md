# Mp1-pcv
## Pipeline Restorasi
Proses perbaikan citra disusun secara sistematis dengan tahapan sebagai berikut:

### Denoising dengan Median Filter Manual
Langkah pertama difokuskan pada penghilangan salt-and-pepper noise. Algoritma ini bekerja dengan memindai setiap piksel menggunakan jendela kernel 3x3 dan mengganti nilai piksel pusat dengan nilai median dari tetangganya. Teknik ini dipilih karena kemampuannya dalam membersihkan noise impulsif tanpa menghilangkan integritas tepi objek secara drastis dibandingkan dengan filter rata-rata.

### Perbaikan Kontras dengan Histogram Equalization
Citra input memiliki rentang intensitas yang sempit sehingga terlihat kusam. Tahap ini melibatkan penghitungan fungsi distribusi kumulatif (CDF) secara mandiri untuk setiap saluran warna (B, G, dan R). Nilai intensitas piksel kemudian dipetakan ulang berdasarkan CDF yang telah dinormalisasi agar mencakup rentang 0 hingga 255 secara merata, sehingga detail visual menjadi lebih kontras.

### Sharpening menggunakan Operator Laplacian
Untuk mengatasi efek blur dan mempertegas kembali detail yang hilang selama proses denoising, diterapkan kernel Laplacian. Operasi konvolusi manual ini dilakukan untuk menonjolkan perbedaan gradien pada tepi objek. Hasil akhir dari tahap ini memberikan ketajaman yang lebih baik pada fitur-fitur halus dalam citra.

### Hasil dan Analisis
Berdasarkan hasil eksekusi program, kombinasi ketiga teknik tersebut berhasil meningkatkan kualitas citra secara signifikan. Filter median terbukti efektif menghilangkan bintik hitam dan putih sepenuhnya, sementara ekualisasi histogram berhasil mengembalikan kecerahan warna yang hilang.

Meskipun kualitas visual telah mendekati citra referensi, masih terdapat sedikit butiran halus yang berasal dari Gaussian noise. Hal ini disebabkan oleh sifat filter median yang lebih optimal untuk noise jenis impulsif. Secara keseluruhan, pipeline ini telah memenuhi kriteria restorasi citra dengan menjaga keseimbangan antara pengurangan noise dan pelestarian detail objek.
