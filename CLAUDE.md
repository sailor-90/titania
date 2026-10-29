# TITANIA

PWA induk MT TITANIA: satu ikon di layar utama HP, isinya hanya menu 5 pintasan (Loadicator, Passage Plan, Compass Error, Weekly Report, PMN). Tiap kartu membuka aplikasi aslinya dari alamat `sailor-90.github.io/...` di dalam iframe layar penuh. **TITANIA tidak menyimpan kode aplikasi lain.** Mengubah atau merilis aplikasi dilakukan di proyek masing-masing (`kapal/...`) seperti biasa; TITANIA otomatis menampilkan versi terbarunya.

## Sebelum mengubah kode
- Baca graphify-out/GRAPH_REPORT.md dulu untuk memahami struktur proyek. Folder itu hanya ada di komputer ini dan tidak ikut git; kalau tidak ada atau usang, jalankan /graphify dulu.
- Setelah perubahan yang menambah atau mengubah fungsi, fitur, atau file, dan hasilnya sudah dicek serta di-commit, jalankan /graphify . --update atau ingatkan user.

## Susunan file
- `index.html` menu + penampil iframe (CSS dan JS inline). `apps.js` daftar pintasan (tambah aplikasi = tambah satu baris). `sw.js` hanya cache kerangka menu. `manifest.webmanifest`, ikon PNG dari `make_icons.py`.

## Cara menjalankan dan menguji
- Lokal: `python3 -m http.server <port>` di folder ini (cek port bebas dulu). Uji daftar: `node test_apps.js`.
- Iframe lintas-origin (localhost memuat github.io) tampil kosong di browser pane; hanya uji benar saat satu origin, yaitu setelah dirilis ke `sailor-90.github.io/titania/`. Menu dan tombol tetap bisa dicek lokal.

## Aturan dan jebakan
- Rilis: repo publik GitHub Pages bernama `titania`; belum dibuat.
- Ikon TITANIA di HP adalah instalasi baru: penyimpanan lokalnya kosong, data lokal ikon lama tidak ikut pindah (ekspor/impor per aplikasi, lihat CLAUDE.md tiap proyek). Jangan hapus ikon lama sebelum TITANIA terbukti jalan.
- Offline tiap aplikasi dipegang service worker aplikasi itu sendiri; buka tiap aplikasi sekali saat online. Setelah rilis aplikasi, tutup dan buka lagi di HP agar versi baru terpakai.
