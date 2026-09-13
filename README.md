Nama : Salsabilla Hasan

NPM : 2506548660

Kelas : PBP A

alsa lagi belajar tutorial github, bismillah pbpnya A dan dilancarkan segalanya.. iloveu bu jess, iloveu asdos pbp <3

### Tugas 1

1. Saya menggunakan <section> dan <article> untuk membuat section baru, yaitu Experience. Menurut saya, penggunaan kedua elemen tersebut sangat membantu dalam membuat struktur halaman menjadi lebih terorganisir. Setelah belajar dan mengeksplorasi selama pengerjaan tugas, saya memahami bahwa <section> dapat digunakan sebagai wadah untuk mengelompokkan suatu bagian atau topik pada halaman, sedangkan <article> digunakan untuk membungkus setiap konten pengalaman yang berdiri sendiri. Selain membantu struktur HTML menjadi lebih jelas, pembagian ini juga memudahkan saya ketika ingin memberikan styling pada bagian tersebut menggunakan CSS.

2. Pada awalnya saya cukup struggling ketika membuat tampilan yang responsive. Saya belum terlalu memahami adanya hirarki dan urutan dalam CSS, sehingga saya sempat meletakkan @media untuk responsive di bagian atas dari kode CSS yang baru saya buat. Akibatnya, saya kebingungan ketika tampilan card yang seharusnya berubah dari dua kolom menjadi satu kolom pada tampilan mobile tidak bekerja seperti yang saya harapkan. Setelah melakukan searching dan mencoba memahami kembali cara kerja CSS, saya menyadari bahwa penempatan @media juga berpengaruh terhadap aturan CSS yang diterapkan. Dari proses tersebut, saya belajar untuk lebih memperhatikan urutan dan struktur penulisan CSS, terutama ketika terdapat aturan yang saling berkaitan.

3. Saya menyadari bahwa pengalaman yang saya miliki kemungkinan akan terus bertambah seiring berjalannya waktu. Karena itu, saya ingin nantinya dapat menambahkan pengalaman baru ke dalam website tanpa harus membuka dan mengubah kode HTML setiap kali ingin menambahkan data. Hal tersebut membuat saya tertarik untuk mempelajari bagaimana data dapat dikelola secara lebih dinamis, sehingga website dapat dikembangkan dan diperbarui dengan lebih mudah di kemudian hari.

---------------------------------------------------------------------------------
Penggunaan AI - Tugas 1

Saya menggunakan AI sebagai alat bantu belajar selama proses pengerjaan tugas ini. AI saya gunakan terutama untuk membantu memahami konsep HTML dan CSS yang belum saya pahami, seperti penggunaan elemen semantic <section> dan <article>, CSS Grid dan Flexbox, responsive design, selector CSS, serta debugging ketika terdapat styling yang tidak bekerja sesuai harapan.

Selain itu, saya juga menggunakan AI untuk berdiskusi mengenai ide desain pada section Experience, merapikan wording pada deskripsi pengalaman, dan melakukan review terhadap kode yang saya tulis. Salah satu kendala yang saya diskusikan dengan AI adalah ketika aturan @media untuk responsive tidak bekerja karena berkaitan dengan urutan dan struktur aturan CSS.

Strategi prompting yang saya gunakan adalah menjelaskan bagian yang belum saya pahami, kemudian memberikan potongan kode atau menjelaskan hasil yang saya lihat di browser. Setelah itu, saya meminta AI menjelaskan penyebab masalah atau konsepnya secara bertahap, bukan hanya memberikan hasil akhir. Saya juga mencoba mengimplementasikan dan mengubah kode tersebut sendiri, kemudian melakukan testing dan penyesuaian tampilan di browser.

Bagian yang dibantu AI: pemahaman konsep HTML/CSS, debugging, pemberian contoh syntax, brainstorming desain, serta review dan perapihan kode dan penulisan.

Dokumentasi percakapan AI: ristek.link/AiChatAlsa



### Tugas 2

1. Ketika pengguna membuka halaman portofolio baru, prosesnya dimulai dari request yang dikirim melalui browser. Request tersebut akan diterima oleh urls.py pada project, kemudian diarahkan ke urls.py milik aplikasi main. Setelah URL ditemukan, django akan menjalankan fungsi view yang sesuai. Pada bagian view, data yang dibutuhkan akan diambil dari model. Model berfungsi untuk mengatur struktur data yang tersimpan di database. Setelah data berhasil diambil, view akan mengirimkan data tersebut ke template melalui context. Template kemudian menampilkan data tersebut dalam bentuk halaman HTML yang dapat dilihat oleh pengguna di browser.

Saat mengerjakan bagian ini, saya sempat mengalami beberapa kendala terutama ketika memindahkan bagian experience yang awalnya masih ditulis langsung di HTML menjadi data yang berasal dari database. Saya beberapa kali mengalami error karena perubahan model belum sesuai dengan migration yang ada. Selain itu, ketika melakukan deployment ke PWS, tampilan yang muncul sempat berbeda dengan yang ada di lokal karena database server belum mengikuti perubahan terbaru. Dari proses tersebut saya jadi lebih memahami bahwa perubahan pada model, migration, dan database harus dilakukan secara berurutan.

2. Data untuk bagian portofolio baru lebih baik disimpan di dalam model dibandingkan langsung ditulis di template karena data menjadi lebih mudah dikelola dan dikembangkan. Jika data langsung ditulis di template, setiap kali ingin menambah atau mengubah informasi, saya harus mengubah kode HTML secara manual. Dengan adanya model, data dapat disimpan di database dan dipanggil secara dinamis melalui view. Hal ini membuat aplikasi menjadi lebih fleksibel karena penambahan data baru tidak perlu mengubah struktur halaman secara langsung.

Pada tugas ini, saya menerapkan konsep tersebut dengan memindahkan bagian experience yang sebelumnya masih menggunakan data statis di HTML menjadi data yang berasal dari model Django. Selain itu, saya juga menyesuaikan kembali template dari tutorial agar lebih sesuai dengan desain portfolio yang sudah saya buat sebelumnya, terutama pada bagian card, struktur informasi pengalaman, dan tampilan agar tetap konsisten dengan halaman profile.

Saat melakukan penyesuaian tersebut, saya sempat struggling juga karena template dari tutorial memiliki struktur yang berbeda dengan desain awal saya. Saya perlu mengubah beberapa bagian HTML dan CSS agar data dari model tetap dapat tampil dengan tampilan card yang sesuai dengan konsep portfolio saya..

3. makemigrations dan migrate memiliki fungsi yang berbeda. makemigrations digunakan untuk membuat file migration berdasarkan perubahan yang dilakukan pada model, sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database.

Contoh perubahan model yang saya lakukan adalah saat menambahkan bagian education pada portofolio. Setelah membuat model education, saya menjalankan python manage.py makemigrations untuk membuat migration baru, lalu menjalankan python manage.py migrate agar perubahan tersebut diterapkan ke database. Saya juga mengalami kendala ketika mengubah format tanggal pada education. Awalnya saya menggunakan field tahun biasa, tetapi kemudian mengubahnya menjadi started_at dan ended_at agar formatnya sama seperti experience. Perubahan tersebut membuat Django meminta penyesuaian terhadap database lama. Dari masalah tersebut saya belajar bahwa perubahan model harus dilakukan dengan hati-hati karena setiap perubahan struktur model akan berpengaruh terhadap database.

---------------------------------------------------------------------------------
Penggunaan AI - Tugas 2

Pada tugas ini, saya menggunakan AI sebagai pendamping belajar selama proses pengembangan fitur baru pada project Django, terutama untuk memahami bagaimana sebuah website dapat menampilkan data secara dinamis menggunakan konsep MVT

Berbeda dengan tugas sebelumnya yang lebih banyak berfokus pada HTML dan CSS, pada tugas ini saya menggunakan AI untuk membantu memahami proses pengelolaan data dalam Django. Saya menggunakan AI untuk berdiskusi mengenai cara kerja model sebagai tempat penyimpanan data, bagaimana view mengambil data dari database, bagaimana template menampilkan data tersebut, serta bagaimana hubungan antara perubahan kode dengan struktur database melalui migration.

Salah satu hal yang saya pelajari dengan bantuan AI adalah proses mengubah halaman experience yang sebelumnya masih menggunakan data yang ditulis langsung di HTML menjadi data yang tersimpan pada model Django. Selain itu, saya juga menggunakan AI ketika membuat fitur education, mulai dari menentukan struktur model, membuat migration, hingga menghubungkan data tersebut agar dapat tampil pada halaman website.

Selama pengerjaan tugas ini, saya mengalami beberapa kendala yang saya diskusikan dengan AI. Salah satunya adalah ketika terjadi error pada database setelah melakukan perubahan pada model, seperti ketika field baru pada model belum sesuai dengan migration yang tersedia. Saya juga mengalami kendala ketika melakukan deployment karena data yang tampil pada server PWS berbeda dengan data yang ada pada lokal. Dari proses debugging tersebut, AI membantu saya memahami bahwa perubahan pada kode, migration, dan database merupakan bagian yang saling berkaitan dan harus dilakukan secara berurutan.

Selain membantu dalam penyelesaian error, AI juga saya gunakan untuk mengevaluasi keputusan implementasi yang saya buat. Contohnya ketika saya menyesuaikan template dari tutorial agar sesuai dengan desain portfolio saya sendiri. Saya menggunakan AI untuk berdiskusi mengenai cara mempertahankan struktur Django yang benar tanpa harus mengubah desain card dan tampilan yang sudah saya buat sebelumnya.

Strategi prompting yang saya gunakan adalah memberikan konteks mengenai kondisi project, menjelaskan tujuan yang ingin dicapai, lalu mengirimkan potongan kode atau pesan error yang saya temukan. Saya meminta AI untuk membantu menganalisis penyebab masalah dan menjelaskan konsep yang berkaitan sebelum melakukan perubahan kode. Setelah mendapatkan arahan, saya tetap mencoba menerapkan perubahan tersebut sendiri dan melakukan pengujian pada browser maupun server lokal.

Bagian yang dibantu AI: pemahaman konsep Django MVT, pengelolaan model dan database, migration, debugging error, analisis perbedaan hasil lokal dan deployment, penyesuaian template tutorial dengan struktur project, serta review implementasi fitur baru.

Dokumentasi percakapan AI: ristek.link/AiChatAlsa