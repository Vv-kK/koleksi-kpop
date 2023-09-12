# [Melody Mementos](https://melody-mementos.adaptable.app/)


### 1. Cara meimplementasi checklist pada tugas
Saya membuat proyek Django baru dengan pertama membuat folder baru di lokal dan github dengan nama yang sama. Saya menghubungkan keduanya dengan perintah git add remote origin. Lalu, saya membuat virtual environment untuk projek baru ini dan mendownload django serta requirements lainnya. Lalu, saya membuat proyek django baru dengan perintah "django-admin startproject shopping_list ." 
Saya mengganti allowed hosts di settings.py agar dapat diakses oleh semua host dan menambahkan dokumen .gitignore dengan isi seperti di tutorial 0. 
Kemudian saya membuat aplikasi main dengan perintah "python manage.py startapp main" dan menambahkan 'main' di installed apps pada settings.py agar aplikasi tersebut dapat dijalankan dalam proyek
Untuk routing proyek perlu ditambahkan path baru dalam urlpatterns yang mengarah ke main dan ketika URL terkait diakses, akan mengacu ke urls.py yang ada di aplikasi main
Lalu, checklist selanjutnya dilakukan dengan membuat function di models.py yang berisi atribut yang diinginkan. Diluar atribut wajib, saya menambahkan 2 atribut lagi, yaitu artist sebagai artist yang merilis produk tersebut dengan tipe CharField dan date_release sebagai tanggal rilis produk dengan tipe DateField
Checklist selanjutnya adalah membuat fungsi di views.py. Saya membuat fungsi bernama show_main untuk menampilkan data pada tampilannya. Untuk itu, terdapat dictionary yang nanti value-nya dapat diakses dengan memanggil key-nya di main.html. Setelah itu function return function render dimana akan me-render tampilan HTML.
Untuk routing perlu ditambahkan urls.py di dalam aplikasi main. Lalu, menambahkan url_pattern yang didalamnya ada function path dimana ketika berada di main akan memanggil fungsi show_main pada views.py.
Terakhir saya melakukan deployment di adaptable dengan menghubungkannya pada repo yang ada di github. Saya memilih repo proyek yang baru saja di buat dan menggunakan branch main. Lalu, saya memilih python app template sebagai template deployment dan PostgreSQL sebagai tipe basis data. python version saya memasukkan versi 3.8 sesuai venv saya dan atart commmandnya "python manage.py migrate && gunicorn koleksi_kpop.wsgi". Terakhir saya memasukkan nama aplikasi, mencentang "HTTP Listener On Port", dan melakukan deployment.

### 2. Bagan berisi request client ke web aplikasi berbasis Django beserta responnya
![](/image/bagan%20http%20req.jpg)
Pada saat pertama urls.py menerima HTTP request, urls.py akan mencari path yang sesuai dengan requestnya. Lalu, akan diarahkan ke views.py sesuai dengan URL yang korespondensi dan menjalankan fungsi yang dipanggil. Pada fungsi tersebut, kita dapat menulis, membaca, dan menghapus dari database. Kemudian, tampilan di render main.html dengan memanfaatkan data yang dibaca oleh views.py.

### 3. Mengapa menggunakan virtual environment? 
venv digunakan untuk memisahkan dependencies antara proyek karena tiap proyek memiliki kebutuhan yang berbeda sehingga bisa saja bentrok antarproyek. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment jika proyek tersebut tidak bentrok dengan proyek lain yang juga dibuat tanpa virtual environment. Misal kedua proyek tersebut menggunakan django dengan versi yang berbeda, maka tidak mungkin akan berhasil.

### 4. Perbedaan MVC, MVT, MVVM
1. MVC adalah Model, View, Controller. Model bertugas mengatur data dan logika (backend). View bertugas untuk mengatur bagaimana informasi atau data akan ditampilkan ke pengguna. Controller bertugas untuk menerima input dari pengguna, lalu memprosesnya dengan memberikan perintah ke model untuk mengolah data dan view untuk mengolah tampilan.

2. MVT adalah Model, View, Template. Model bertugas mengatur data dan logika, juga memberikan data yang dibutuhkan ke view. View bertugas untuk menyediakan/menyiapkan data yang dibutuhkan oleh template agar siap dipakai. Template berfungsi untuk mengatur tampilan dari data-data tersebut.

3. MVVM adalah Model, View, ViewModel. Model bertugas untuk mengatur data dan logika. View bertugas untuk mengatur tampilan pengguna dan hanya menampilkan data pada tempat yang sesuai, tanpa adanya proses logika. ViewModel bertugas sebagai perantara Model dan View, dimana data dari Model akan di-format disini dan dikirim ke view untuk ditampilkan. 

Perbedaan: 
- Ketika mau melakukan modifikasi pada data, di MVC yang melakukannya adalah controller, di MVT dilakukan dengan cara view mengirimkan perintah ke model dan dilaksanakan oleh model, di MVVM dilakukan dengan cara viewmodel mengirimkan perintah ke model dan modifikasi akan dilakukan oleh model. 
- Ketika ingin mengubah tampilan, di MVC dilakukan dengan cara controller mengirimkan perintah ke view dan view yang melakukan perubahan, di MVT hal ini dilakukan oleh template, dan di MVVM hal ini dilakukan oleh view setelah mendapat perintah dari viewmodel.