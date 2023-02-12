# project-kasir-pacmann

Aplikasi kasir sederhana dengan menggunakan bahasa pemrograman Python tanpa terhubung dengan database.

# Tujuan Pengerjaan Project
1. Membuat aplikasi kasir sederhana yang dapat melakukan tugas:  
  a. Menambah item barang yang ingin dibeli.  
  b. Mengupdate item barang yang ingin dibeli.  
  c. Menampilkan daftar item barang.  
  d. Menghapus sebagian atau keseluruhan item barang yang telah diinput sebelumnya.  
  e. Menampilkan total harga barang dari hasil inputan sebelumnya dengan atau tanpa perhitungan diskon.  
2. Membuat program dengan bahasa pemrograman Python yang belum terhubung ke database.  
3. Mengaplikasikan pembuatan program yang berbasis fungsi (function) atau objek (OOP).
4. Mengaplikasikan penulisan kode yang bersih (clean code).

# Alur Program
a.	Membuat class Transaction() yang kemudian dapat diakses dengan memasukkan trnsct_123 = Transaction(). Kemudian, diberikan metode untuk inisialisasi list awal dengan atribut data_transaksi.  

b.	Membuat metode add_item([<nama_item>, <jumlah_item>, <harga_item>]). Fungsi yang digunakan berupa .append ke dalam list data_transaksi.  

![flow normal](https://user-images.githubusercontent.com/45326615/218318706-1a8751f7-bd10-4d59-b6c7-66c719a41c33.jpg)

c.	Membuat metode update dengan rincian sebagai berikut dengan mengganti data di index sekian dengan menggunakan nilai baru.  

    i.	Membuat metode update_item_name(<nama_item>, <new_nama_item>)  
    ii.	Membuat metode update_item_qty(<nama_item>, <new_jumlah_item>)  
    iii.	Membuat metode update_item_price(<nama_item>, <new_harga_item>)

d.	Membuat metode delete_item(<nama item>). Fungsi yang digunakan adalah while yang kemudian menggunakan .remove berdasarkan ketentuan nama_item.  

e.	Membuat metode reset_transaction(). Fungsi yang digunakan adalah membuat atribut data_transaksi menjadi kosong kembali.  

 f.	Membuat metode check_order(). Fungsi yang digunakan adalah fungsi conditional sebagai syarat untuk checking kondisi awal, yang dilanjutkan dengan fungsi looping for, dan juga dibantu dengan pembentukan data frame menggunakan Pandas.  

 g.	Membuat metode total_price(). Fungsi yang digunakan adalah fungsi conditional sebagai syarat untuk checking kondisi awal, dilanjutkan dengan fungsi looping for, dibantu dengan pembentukan data frame menggunakan Pandas, dan juga fungsi .sum untuk menjumlahkan harga akhir, kemudian diteruskan ke dalam fungsi conditional untuk melihat harga diskon.  
 
# Testing
Untuk menjalankan test, jalankan perintah `python3 test.py` . Bila tidak ada exception yang muncul, maka berarti fungsin-fungsi yang ada berjalan normal.  
  
  Test Case 1:
  ![test_1](https://user-images.githubusercontent.com/45326615/218318378-49ae38af-8e68-475d-b4f2-c7bd668e61f9.png)
  
  Test Case 2:
  ![test_2](https://user-images.githubusercontent.com/45326615/218318412-ba8d7c0b-4de6-4460-8e09-e27d2ba85a9d.png)
  
  Test Case 3:
  ![test_3](https://user-images.githubusercontent.com/45326615/218318430-b7dc1bd6-1359-4e01-b403-8a74fdf5afc2.png)
  
  Test Case 4:
  ![test_4](https://user-images.githubusercontent.com/45326615/218318439-b37a54c3-e204-407b-98a8-8e5348d0cef3.png)


  
