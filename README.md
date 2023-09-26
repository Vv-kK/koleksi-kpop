# [Melody Mementos](https://melody-mementos.adaptable.app/)

<details>
<summary> Tugas 2 </summary>

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
</details>

<details> 
<summary>Tugas 3</summary>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?
Form POST dan GET digunakan untuk mengirim data dari form ke server. 
Saat mengirimkan data dengan POST, nilai variabel tidak ditampilkan di URL karena request dikirimkan sebagai bagian dari HTTP Request Body. Sedangkan, GET menampilkan nilai variabel di URL. Maka dari itu, POST dianggap lebih aman dibandingkan GET terutama jika data yang ditransmisi adalah data sensitif.
Karena nilai variabel dimasukkan pada method GET, maka data yang dapat ditransmisi juga terbatas, sehingga POST lebih cocok digunakan jika mengirim data yang berukuran besar.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML dan JSON banyak digunakan untuk mengirimkan data yang terstruktur, sedangkan HTML lebih digunakan untuk membuat tampilan pada web aplikasi. 
Pengiriman data menggunakan XML dan JSON memiliki struktur yang berbeda. XML mengirim data dengan struktur tree dimana tiap data akan memiliki tag dan closing tag. Dokumen XML juga harus memiliki root element yang merupakan parent dari tag lainnya. Di sisi lain, dokumen JSON mengirim data dalam bentuk yang mirip dengan object pada JavaScript, yaitu berbentuk seperti dictionary pada python. Dokumen JSON terdiri dari key-value pair yang sepenuhnya text, sehingga mudah untuk dibaca manusia.
Lalu, HTML digunakan untuk menampilkan data yang diterima itu agar lebih nyaman dilihat di web aplikasi yang dibuat, misalnya dengan bentuk tabel. Namun, HTML juga bisa digunakan untuk mengirim data berbentuk formulir atau dari parameter URL.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Hal ini karena penyajian data dengan JSON lebih mudah dibaca untuk manusia dan bentuknya lebih sederhana daripada XML, tetapi tetap mampu untuk merepresentasikan struktur data yang kompleks. Selain itu, JSON memiliki sintaks yang lebih ringan yang berarti data yang sama memiliki ukuran file lebih kecil, sehingga pertukaran data akan lebih efisien. JSON juga dapat digunakan dengan berbagai bahasa pemrograman dan syntax-nya mirip dengan JavaScript. 

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
Pertama, Saya membuat forms.py yang berguna sebagai struktur input form yang ingin dibuat. File tersebut kemudian diisi dengan sebuah class yang bernama ProductForm yang mengambil bentuk dasar dari ModelForm. Kemudian, saya menyatakan objek yang ingin dibuat adalah 'Item' dan atribut apa saja yang perlu diinput pengguna. 
Setelahnya, saya menambahkan fungsi baru pada views.py yang membuat instansiasi dari class ProductForm. Fungsi juga mengecek apakah input yang dimasukkan valid dan menyimpannya jika valid. Melalui fungsi ini juga, tampilan untuk input form di render dengan memanggil fungsi yang merender html create_product.
Selanjutnya, saya membuat file html dengan nama create_product.html dalam folder templates di aplikasi main. Lalu, saya menulis terlebih dahulu keterangan bahwa file ini extends dari base.html dan menyatakan bagian block content. Kemudian, saya membuat form dengan method POST karena form ini bertujuan menambahkan item baru ke database. Lalu, struktur form yang ada di forms.py diambil dengan perantara views.py untuk ditampilkan sebagai tabel. Juga ada tombol untuk mengirimkan data yang telah dimasukkan.
Saya juga menambahkan button yang mengarah ke halaman input form ketika ditekan. Penambahan button dilakukan melalui main.html dan button disisipkan hyperlink ke halaman create_product.
Terakhir untuk checklist pertama adalah membuat routing di urls.py pada aplikasi main agar create_product dapat diakses. Routing dilakukan dengan import fungsi baru (create_product) tadi dan menambahkannya juga dalam urlpatterns.
<br>
Pada checklist selanjutnya, saya pertama menambahkan code pada fungsi show_main untuk menampilkan data dalam format HTML. Saya menambahkan variabel items yang berisi semua datanya, dimana akan digunakan untuk menampilkan data di HTML. Kemudian di main.html saya menambahkan kode untuk menampilkan data dalam bentuk tabel seperti berikut.

```
<table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Artist</th>
            <th>Description</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.artist}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
```

Untuk data dengan format XML dan JSON, masing-masing dibuat fungsi dan menyimpan semua objek dari Item dalam sebuah variabel. Lalu, data itu di serialize masing-masing sebagai XML dan JSON sesuai fungsinya. Hasil serialisasi itu di-return sebagai HTTP Response.
Untuk menampilkan data dengan format XML dan JSON berdasarkan ID hanya berbeda saat mengambil objek dari Item. Disini diambil objek dari id yang diinginkan saja dan tidak semua objek. Data diserialisasi dan hasilnya di-return sebagai HTTP Response.
<br>
Saya melakukan routing dengan mengimport semua nama fungsi baru di views.py pada urls.py di aplikasi main. Selanjutnya, tambahkan path untuk setiap fungsi di urlpatterns. 
<br>
Terakhir, untuk menjawab pertanyaan di README saya membuka referensi materi dari tutorial 2, slides kuliah, dan membaca artikel di internet.

### 5. Screenshot dari hasil akses URL pada Postman
1. HTML
![](/image/show_main_html.jpg)
![](/image/show_main_html_2.jpg)
![](/image/show_main_html_3.jpg)
![](/image/show_main_html_4.jpg)

2. XML
![](/image/show_xml.jpg)

3. JSON
![](/image/show_json.jpg)

4. XML by ID
![](/image/show_xml_by_id.jpg)

5. JSON by ID
![](/image/show_json_by_id.jpg)
</details>

<details>
<summary>Tugas 4</summary>

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm merupakan library bawaan dari Django yang berfungsi untuk membuat formulir registrasi pengguna baru, sehingga programmer tidak perlu membuat kode dari awal. Kelebihannya adalah kemudahan yang diberikan pada programmer karena dapat memvalidasi input username dan password sesuai aturan dasar, misalnya panjang password harus lebih dari 8 karakter. Di sisi lain, kekurangannya adalah kurangnya kustomisasi yang dapat dilakukan, misalnya tidak bisa menambahkan field jenis kelamin dan tidak bisa menambahkan captcha. UserCreationForm juga perlu kustomisasi lebih untuk menambahkan aturan pembuatan password yang lebih kuat, seperti wajib mengandung huruf kapital.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses memverifikasi pengguna yang sedang memanfaatkan apliaksi kita. Contohnya adalah proses login. Sedangkan otorisasi adalah proses pengecekan apakah pengguna boleh mengakses suatu hal. Keduanya penting karena autentikasi dan otorisasi memiliki peran yang berbeda dimana keduanya saling melengkapi. Autentikasi menghambat hacker untuk berpura-pura menjadi seorang pengguna dan otorisasi menghambat orang-orang tidak berkepentingan untuk melakukan suatu aksi tertentu. 

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah penyimpanan data dengan ukuran maksimal 4 KB yang akan dihapus/kadaluarsa sesuai waktu yang ditentukan programmer. Sesi pengguna itu sendiri hanya bertahan dalam 1 tab dan sesi berakhir saat sesi ditutup, berarti pengguna harus login kembali. Sesi antara satu pengguna dengan yang lainnya dibedakan dengan session ID. Nilai session ID ini disimpan sebagai cookie, sehingga dapat diakses oleh semua window. Hal ini menghasilkan holding state, sehingga pengguna tidak perlu berulang kali melakukan login.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Cookies itu sendiri tidak dapat digunakan untuk mentransfer virus. Namun, perlu diwaspadai jika cookies berisi informasi sensitif yang tidak di enkripsi karena dapat dicuri/dimodifikasi informasinya. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya mengimport semua fungsi yang dibutuhkan untuk membuat register, login, dan logout. Lalu, saya membuat fungsi baru di views.py bernama register yang membuat suatu form default dengan USerCreationForm bawaan Django. Di dalam fungsi itu dibuat kondisi ketika pengguna request methodnya adalah POST, maka akan dibuat UserCreationForm sesuai input yang dimasukan pengguna pada request.POST. Jika formnya berisi data yang valid, maka form akan disimpan dengan form.save(), menampilkan pesan sukses dengan message.success(), dan pengguna diteruskan ke halaman login dengan return. Jika tidak valid, pengguna akan tetap di halaman register.html. 
Selanjutnya, saya membuat file register.html di dalam folder templates dan mengisinya dengan code sebagai berikut.
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Selanjutnya, saya membuat fungsi login_user di views.py. Saya membuat kasus ketika request methodnya adalah post dimana program akan mengambil input username dan password yang dimasukkan lalu dilakukan autentikasi. Jika autentikasi berhasil, maka dilakukan login dengan function built-in dan mengarahkan pengguna ke halaman main. Ketika request methodnya bukan POST, maka pengguna tetap di halaman login. Untuk tampilan login, saya membuat login.html dengan isi code sebagai berikut.
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Selanjutnya, untuk logout saya membuat fungsi yang memanfaatkan function built-in logout dan mengembalikan pengguna ke halaman login. Lalu, pengguna dapat melakukan logout dengan button logout yang saya tambahkan pada halaman utama dengan kode tambahan di main.html (setelah button add new product) sebagai berikut.
```html
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```
Setelah itu saya melakukan routing di urls.py dengan mengimport semua fungsi yang baru dibuat dan menambahkan path nya ke urlpatterns. Saya juga menambahkan restriksi untuk halaman main yang hanya dapat diakses ketika sudah login agar pengalaman pengguna semakin lancar. Saya membuat ini dengan decorator login_required yang ada dari Django.

Checklist kedua saya lakukan dengan menjalankan server dan mengakses localhost. Saya memanfaatkan halaman register yang telah saya buat untuk membuat 2 akun dan mengisi dengan dummy data. Kemudian, saya melakukan checklist ketiga, yaitu integrasi Item dengan User. Langkah pertama yang saya lakukan adalah mengimport User dan menambahkan atribut user di model Item. Lalu, saya melakukan migrations. Langkah selanjutnya, saya mengubah function create_product di views.py. Function perlu diganti supaya form tidak langsung disimpan ke database. Saya menambahkan informasi user di formnya sesuai dengan user yang sekarang login dan setelahnya baru disimpan ke database. Lalu, item yang ditampilkan juga di-filter agar yang ditampilkan hanya item dari user yang sedang login di sesi itu. 

Checklist keempat saya lakukan dengan menyimpan jam login dengan cookie pada function login menambahkan code `response.set_cookie('last_login', str(datetime.datetime.now()))` Saya menambahkan informasi ini dalam dictionary context function show_main yang di pass ke main.html agar bisa di render informasinya. Kemudian, saya juga merubah value dari nama dalam dictionary context function show_main agar mengirimkan username dari user yang sekarang sedang login.

Terakhir, saya menjawab pertanyaan dengan membaca kembali tutorial, slides, dan mencari informasi di internet.
</details>