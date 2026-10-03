Nama : Salsabilla Hasan

NPM : 2506548660

Kelas : PBP A

alsa lagi belajar tutorial github, bismillah pbpnya A dan dilancarkan segalanya.. iloveu bu jess, iloveu asdos pbp <3

## Progres Mingguan

| Tugas | Topik | Yang Saya Bangun |
|---|---|---|
| Tugas 1 | HTML & CSS | Halaman profil dan section Experience yang responsif |
| Tugas 2 | Django MVT | Memindahkan Experience ke model Django dan menambahkan Education |
| Tugas 3 | Form & Data Delivery | ModelForm, CRUD Education, serta endpoint JSON |
| Tugas 4 | Autentikasi & Otorisasi | Login/logout, cookie, peran Editor, dan fitur star |
| Tugas 5 | JavaScript & AJAX | Halaman Experience berbasis AJAX: pencarian dengan debouncing, modal tambah data, toast, dan perlindungan XSS |

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

### Tugas 3
1. Menurut saya kita menggunakan ModelForm itu supaya mempermudah pembuatan form pada Django, nah ini juga sudah dijelaskan di tutorial kalau ModelForm ini digunakan supaya struktur form bisa dibuat berdasarkan model Django yang sudah ada, sehingga kita tidak perlu membuat seluruh field form secara manual. Lalu kita diwajibkan untuk menambah CSRF token dikarenakan Django perlu memastikan kalau request pada form tersebut sudah terautorisasi, jadi CSRF token membantu melindungi request tersebut.

2. Setelah mempelajari JSON dan XML saya mengetahui bahwa format JSON ini lebih ringkas dan banyak digunakan dibandingkan dengan XML yang menurut saya syntax-nya lumayan complex menggunakan banyak tag.

3. Awalnya data kita itu masih berupa data yang dikenali Django. Lalu data tersebut kemudian diambil dari database dan akan diubah dulu ke format JSON dengan serialization. Setelah menjadi JSON, data bisa dikirim melalui HTTP response ke client. Kalau data tersebut ingin dipakai lagi di Django sebagai object, JSON tadi bisa dideserialize supaya kembali menjadi object yang bisa diproses oleh Python. Kita harus melakukan serialization dikarenakan model Django tidak otomatis berbentuk JSON, jadi serialization berdasarkan yang saya pahami adalah proses mengubah data ke format yang bisa dikirim sebagai JSON.

---------------------------------------------------------------------------------
Penggunaan AI - Tugas 3

Dalam mengerjakan Tugas 3 ini, saya menggunakan AI sebagai alat bantu untuk memahami materi dan proses implementasi pada Tutorial 3. Sebelum mengerjakan tugas, saya melihat kembali tutorial, terutama pada contoh pembuatan form untuk bagian Project, sebagai acuan untuk memahami bagaimana implementasi form dilakukan pada Django.

Saya menggunakan AI untuk membantu memahami dan mengimplementasikan ModelForm, CSRF token, Create, Update, Delete, JSON, serialization, dan deserialization. Saya juga menggunakan AI untuk membantu membaca error yang muncul saat menjalankan program, seperti error NoReverseMatch pada URL Update Education, serta untuk membantu memahami perbedaan tipe ID antara model Project dan Education. Selain itu, AI membantu saya dalam menyesuaikan tampilan button pada halaman Education dan mencari penyebab gambar thumbnail yang tidak muncul.

Selama pengerjaan, saya menemukan bahwa saran dari AI tidak selalu dapat langsung diterapkan pada project saya karena AI tidak menjalankan dan melihat kondisi project secara langsung. Beberapa solusi perlu disesuaikan kembali dengan kode yang sudah saya buat.
Contohnya, ketika terjadi error pada URL Update Education, saya perlu mencocokkan kembali tipe ID pada model Education dengan URL yang digunakan. Saya juga melakukan pengecekan dan testing langsung pada browser untuk memastikan fitur Create, Update, Delete, dan endpoint JSON benar-benar berjalan.

Pada bagian tampilan, saya juga menyesuaikan kembali hasil yang diberikan AI dengan desain portfolio yang saya inginkan, terutama pada posisi dan ukuran button. Untuk bagian thumbnail, saya melakukan percobaan menggunakan link gambar yang dapat diakses langsung oleh browser sampai gambar berhasil ditampilkan.

Strategi prompting yang saya gunakan adalah memberikan konteks project saya terlebih dahulu, kemudian memberikan kode atau error yang sedang saya temui. Setelah itu saya meminta penjelasan secara bertahap dan menyesuaikan solusi berdasarkan struktur project yang sudah saya miliki. Saya tidak hanya meminta kode secara langsung, tetapi juga meminta penjelasan mengenai fungsi dari setiap bagian kode agar saya dapat memahami alasan penggunaannya.

Dokumentasi percakapan AI: ristek.link/AiChatAlsa


### Tugas 4
Dalam Individual Assignment 4, saya mempelajari cara menerapkan role editor pada website Django. Saya belajar menggunakan Django Group untuk menentukan pengguna yang memiliki akses sebagai editor.

Saya juga memahami cara membedakan hak akses Eeitor dengan pengguna biasa dan superuser, terutama bahwa editor hanya dapat mengubah data tanpa dapat membuat atau menghapus data. Selain itu, saya belajar bahwa pembatasan tersebut harus diperiksa di sisi server agar akses tetap aman meskipun pengguna mencoba menjalankan aksi secara langsung.

Dengan bantuan AI sebagai teman belajar, saya dapat memahami konsep, mencari kesalahan pada implementasi, dan menyesuaikan kode dengan project yang saya kerjakan sendiri.

## Redesign Portofolio

Portofolio ini saya redesign dengan konsep galeri museum vintage. Saya ingin setiap pengunjung merasa seperti masuk ke sebuah museum.

Konsep ini sudah lama saya rancang di Figma, mulai dari moodboard, referensi visual, sampai pemilihan elemen seperti bingkai oval, bintang emas, klip, segel lilin, dan roll film. Namun, untuk menuangkan desain tersebut ke dalam kode, saya membutuhkan bantuan. Karena itu, dalam proses redesign ini saya menggunakan AI (Claude dari Anthropic) sebagai partner kerja.

Dengan AI, saya mengeksplorasi tata letak setiap section berdasarkan referensi dan arahan saya, lalu menerjemahkannya menjadi kode: menulis ulang style.css, menyesuaikan template HTML, hingga membantu menelusuri error saat deploy ke PWS. Sepanjang proses itu, saya tetap yang menentukan arah desain, memilih elemen, merevisi hasil yang belum sesuai, lalu mengintegrasikan, menguji di desktop maupun mobile, dan melakukan deploy.

Saya menuliskan bagian ini karena ingin transparan tentang proses di balik website ini. Seluruh kode hasil bantuan AI sudah saya baca, sesuaikan dengan struktur project saya, dan uji sebelum di-commit. Bagi saya, proyek ini juga menjadi proses belajar: bagaimana sebuah desain di Figma bisa dihidupkan menjadi website yang benar-benar berjalan.

### Tugas 5

1. Debouncing menurut saya adalah teknik untuk menunda suatu fungsi sampai pengguna berhenti melakukan sesuatu selama beberapa saat. Awalnya saya bingung kenapa pencarian tidak langsung dijalankan setiap kali saya mengetik, lalu saya bertanya ke AI dan dijelaskan dengan analogi pelayan restoran. Kalau pelayan langsung pergi ke dapur setiap kali kita menyebut satu kata pesanan, pelayannya akan capek dan dapurnya bingung, padahal pesanan yang benar hanya yang terakhir. Pelayan yang baik akan menunggu sampai kita selesai bicara, baru pergi ke dapur sekali saja. Dari situ saya jadi paham kalau debouncing membuat pencarian menunggu sekitar 300 milidetik setelah saya berhenti mengetik, dan kalau saya mengetik lagi sebelum waktunya habis, waktunya diulang dari awal.

Teknik ini penting untuk fitur pencarian karena tanpa debouncing, setiap huruf yang diketik akan langsung mengirim permintaan ke server. Contohnya ketika saya mengetik "RISTEK", berarti ada enam permintaan yang dikirim, padahal yang saya butuhkan hanya hasil yang terakhir. Saya juga mencoba membuktikannya sendiri dengan melihat tab Network di DevTools, dan ternyata setelah memakai debouncing, permintaan yang muncul hanya satu ketika saya mengetik dengan lancar. Jadi menurut saya debouncing membantu supaya server tidak terlalu terbebani dan hasil pencarian tetap terasa cepat.

2. Setelah mempelajari tutorial, saya mengetahui bahwa fetch() tidak langsung memberikan data, tetapi memberikan Promise atau semacam "janji" bahwa data akan datang nanti. Karena itu kita perlu menggunakan await supaya kode menunggu dulu sampai jawaban dari server benar-benar datang, baru setelah itu lanjut ke baris berikutnya. await ini juga hanya bisa dipakai di dalam fungsi yang diberi async.

Saya sempat bingung dengan await, jadi saya bertanya ke AI apa sebenarnya maksud await dan apa yang terjadi kalau tidak dipakai. AI menjelaskannya dengan analogi memesan makanan di food court yang memakai nomor antrean. Saat kita memesan, kasir tidak langsung memberikan makanannya, tetapi hanya memberikan struk nomor antrean. Struk itu sama seperti Promise, yaitu janji bahwa makanannya akan datang nanti. await sama seperti menunggu sampai nomor kita dipanggil, baru setelah itu kita ambil makanannya.

Kalau await tidak digunakan, kode akan langsung lanjut berjalan sebelum datanya datang, jadi yang kita pegang masih Promise, bukan datanya. Akibatnya, response.ok menjadi undefined dan response.json() bisa error, sehingga halaman tidak bisa menampilkan data dengan benar. Selain itu, error dari server juga tidak akan tertangkap oleh try...catch. AI juga menjelaskan bahwa await hanya bisa dipakai di dalam fungsi yang diberi async. Analogi antrean ini membuat saya lebih mudah memahami kenapa await diperlukan.

3. XSS (Cross-Site Scripting) adalah serangan ketika seseorang menyisipkan kode JavaScript ke dalam website, lalu kode tersebut ikut dijalankan di browser orang lain yang membuka website itu. Saat mengikuti tutorial, saya mencoba sendiri menambahkan data dengan judul <img src="x" onerror="alert('XSS!')">, dan ternyata benar muncul alert di halaman. Dari situ saya jadi sadar kalau data yang dimasukkan pengguna bisa berbahaya kalau tidak ditangani dengan benar.

Menurut saya data yang ditampilkan lewat AJAX lebih rentan karena template Django sebenarnya sudah otomatis melakukan escaping, jadi karakter seperti < dan > diubah menjadi teks biasa. Sedangkan ketika data ditampilkan lewat JavaScript menggunakan innerHTML, Django sudah tidak ikut campur lagi, sehingga browser bisa menganggap data tersebut sebagai kode HTML sungguhan. Ketika saya bertanya ke AI dan meminta pengecekan kode, saya juga baru tahu bahwa template Experience saya sebelumnya memakai |safe, yang ternyata mematikan perlindungan otomatis dari Django. Karena itu, pada tugas ini saya menambahkan escapeHtml di JavaScript dan strip_tags di form Django supaya data yang masuk dan yang ditampilkan sama-sama aman.

---------------------------------------------------------------------------------
Penggunaan AI - Tugas 5

Pada tugas ini saya menggunakan AI (Claude dari Anthropic) sebagai teman belajar. Karena JavaScript dan AJAX masih cukup baru buat saya, saya lebih banyak bertanya dulu tentang konsepnya sebelum mengerjakan, misalnya apa itu AJAX, kenapa fetch perlu await, bagaimana debouncing bekerja, dan kenapa data dari JavaScript bisa terkena XSS. Saya juga meminta AI menjelaskan dengan analogi sederhana supaya saya lebih mudah membayangkannya.

Saat mengerjakan, saya memberikan konteks berupa instruksi tugas dan kode project saya, lalu AI membantu memberikan arahan dan contoh kode secara bertahap. Setiap selesai satu langkah, saya mencoba menjalankannya sendiri di browser, lalu bertanya lagi kalau ada bagian yang belum saya pahami. Contohnya saya sempat bertanya kenapa pencarian Experience memakai Q sedangkan pencarian Projects di tutorial tidak, dan dari situ saya jadi paham kalau Q dipakai untuk mencari dengan kondisi "atau" di lebih dari satu field.

Bagian yang dibantu AI adalah pemahaman konsep AJAX, fetch, async/await, debouncing, CSRF, dan XSS, serta arahan dan contoh kode untuk membuat halaman Experience berbasis AJAX, fitur star, pencarian dengan debouncing, modal tambah data, toast, dan perlindungan XSS.

Selama prosesnya, saya juga sadar bahwa AI tidak bisa melihat tampilan website saya secara langsung. Waktu tutorial, kartu proyek saya sempat tidak muncul, dan saya harus mengecek Console, mengirim screenshot, dan mengecek ulang HTML saya sampai ketemu bahwa form pencarian tidak sengaja terhapus dan carousel saya jadi double. Saya juga tidak selalu mengikuti saran AI, misalnya saya memilih Experience dibanding Education yang disarankan, dan saya meminta modal hapus yang sesuai dengan desain portfolio saya dibanding memakai confirm() bawaan browser.

Semua kode yang dibantu AI sudah saya baca, sesuaikan dengan project saya, dan saya uji untuk setiap peran sebelum di-commit.

Dokumentasi percakapan AI: ristek.link/AiChatAlsa