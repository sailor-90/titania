# TITANIA

PWA induk MT TITANIA: satu ikon di layar utama HP, isinya hanya menu 5 pintasan (Loadicator, Passage Plan, Compass Error, Weekly Report, PMN). Tiap kartu membuka aplikasi aslinya dari alamat `sailor-90.github.io/...` di dalam iframe layar penuh. **TITANIA tidak menyimpan kode aplikasi lain.** Mengubah atau merilis aplikasi dilakukan di proyek masing-masing (`kapal/...`) seperti biasa; TITANIA otomatis menampilkan versi terbarunya.

## Sebelum mengubah kode
- Baca graphify-out/GRAPH_REPORT.md dulu untuk memahami struktur proyek. Folder itu hanya ada di komputer ini dan tidak ikut git; kalau tidak ada atau usang, jalankan /graphify dulu.
- Setelah perubahan yang menambah atau mengubah fungsi, fitur, atau file, dan hasilnya sudah dicek serta di-commit, jalankan /graphify . --update atau ingatkan user.

## Susunan file
- `index.html` menu + penampil iframe (CSS dan JS inline). `apps.js` daftar pintasan (tambah aplikasi = tambah satu baris). `sw.js` hanya cache kerangka menu. `manifest.webmanifest`, ikon PNG dari `make_icons.py`.

## Cara menjalankan dan menguji
- Setelah rilis, iPhone yang sudah memasang TITANIA perlu menutup dan membuka aplikasi sekali (service worker baru ambil alih); sw.js memakai fetch `no-cache` agar versi baru cepat terpakai.
- Lokal: `python3 -m http.server <port>` di folder ini (cek port bebas dulu). Uji daftar: `node test_apps.js`.
- Iframe lintas-origin (localhost memuat github.io) tampil kosong di browser pane; uji isi aplikasi di https://sailor-90.github.io/titania/ (satu origin). Menu dan tombol bisa dicek lokal.

## Aturan dan jebakan
- Rilis: sudah live di https://sailor-90.github.io/titania/ (repo publik `sailor-90/titania`, Pages dari branch main). Diunggah lewat web GitHub (file upload), jadi repo lokal ini belum punya remote dan riwayat commit lokal tidak sama dengan repo GitHub. Tidak ada `gh` di komputer ini. Perubahan berikutnya: unggah file yang berubah lewat https://github.com/sailor-90/titania/upload atau GitHub Desktop. Jangan menambah remote tanpa izin.
- iOS aplikasi layar utama: `innerHeight`/`100vh` bisa lebih pendek dari layar fisik (iPhone Pro Max: 873 vs 932), dan elemen `position:fixed` tidak dicat di area sisanya, jadi muncul pita di bawah. Solusinya: `fit()` mengisi `--vh` dari `screen.height`, layout memakai `position:absolute` setinggi `--vh`, dan warna latar `<html>` disamakan dengan aplikasi yang terbuka (`syncBg`). Jangan kembali ke `position:fixed; inset:0` untuk menu/penampil. Ditemukan lewat iPhone Mirroring.
- Kembali ke menu hanya lewat tombol melayang, dengan dialog konfirmasi Ya/Tidak. Gestur geser dari tepi/back diserap oleh satu entri riwayat penjaga (`guardOn`) supaya tidak keluar aplikasi saat mengedit; jangan menambah `pushState` per aplikasi.
- Ikon TITANIA di HP adalah instalasi baru: penyimpanan lokalnya kosong, data lokal ikon lama tidak ikut pindah (ekspor/impor per aplikasi, lihat CLAUDE.md tiap proyek). Jangan hapus ikon lama sebelum TITANIA terbukti jalan.
- Offline tiap aplikasi dipegang service worker aplikasi itu sendiri; buka tiap aplikasi sekali saat online. Setelah rilis aplikasi, tutup dan buka lagi di HP agar versi baru terpakai.
