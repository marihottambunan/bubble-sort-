# Bubble Sort Implementation

## Mengapa Bubble Sort Memiliki Kompleksitas O(n²)?

Bubble Sort merupakan algoritma pengurutan yang menggunakan pendekatan perbandingan berulang antara elemen-elemen yang berdekatan. Algoritma ini mendapat nama "bubble" karena elemen-elemen kecil secara bertahap "mengapung" ke atas seperti gelembung udara, sementara elemen besar "tenggelam" ke bawah.

Karakteristik utama Bubble Sort adalah penggunaan **nested loop** (perulangan bersarang):

1. **Perulangan luar** mengontrol jumlah pass yang dilakukan sebanyak `n-1` kali
2. **Perulangan dalam** melakukan perbandingan dan pertukaran elemen sebanyak `n-i-1` kali pada setiap pass

Dengan struktur ini, total jumlah perbandingan yang dilakukan adalah:
(n-1) + (n-2) + (n-3) + ... + 2 + 1 = n(n-1)/2

Formula ini menghasilkan pertumbuhan kuadratik, sehingga kompleksitas waktu algoritma adalah **O(n²)**.

## Ilustrasi Proses Sorting

Misalkan kita memiliki array dengan 4 elemen:

Proses Bubble Sort akan berjalan sebagai berikut:

- **Pass 1**: Melakukan 3 perbandingan → elemen terbesar (8) pindah ke posisi terakhir
- **Pass 2**: Melakukan 2 perbandingan → elemen terbesar kedua (5) pindah ke posisi yang tepat  
- **Pass 3**: Melakukan 1 perbandingan → array sudah terurut sempurna

**Total perbandingan = 3 + 2 + 1 = 6 operasi**

Pola ini berlaku untuk ukuran array apapun:

| Ukuran Array | Jumlah Perbandingan |
|--------------|---------------------|
| 10 elemen    | 45 perbandingan     |
| 50 elemen    | 1.225 perbandingan  |
| 1000 elemen  | 499.500 perbandingan|

## Analisis Kompleksitas

Pertumbuhan jumlah operasi mengikuti pola kuadratik karena:

1. **Struktur nested loop** memaksa setiap elemen dibandingkan dengan hampir semua elemen lainnya
2. **Keterbatasan algoritma** yang hanya bisa menukar elemen bersebelahan
3. **Tidak ada mekanisme skip** untuk menghindari perbandingan yang tidak perlu (tanpa optimasi)

Meskipun optimasi seperti **early termination** dapat memperbaiki best case menjadi O(n), worst case dan average case tetap mempertahankan kompleksitas **O(n²)**.

## Kesimpulan

Bubble Sort memiliki kompleksitas **O(n²)** karena jumlah operasi perbandingan meningkat secara kuadratik seiring bertambahnya ukuran data. Hal ini menjadikan algoritma ini kurang efisien untuk dataset besar, namun tetap berguna untuk pembelajaran konsep dasar sorting dan implementasi pada data berukuran kecil.

