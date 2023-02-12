
from kasir import trnsct_123


"""
Test 1:
Menambahkan item berikut:
Nama Item: Ayam Goreng, Qty: 2, Harga: 20_000
Nama Item: Pasta Gigi, Qty: 3, Harga: 15_000
"""
trnsct_123.add_item("Ayam Goreng", 2, 20_000)
trnsct_123.add_item("Pasta Gigi", 3, 15_000)
#check kembali list
trnsct_123.check_data_transaksi()


"""
Test 2:
Menghapus item Pasta Gigi dari list
"""
trnsct_123.delete_item("Pasta Gigi")
#check kembali list
trnsct_123.check_data_transaksi()


"""
Test 3:
Reset semua item dari list
"""
trnsct_123.reset_transaction()


"""
Test 4:
Mengeluarkan output total belanja
"""
trnsct_123.total_price()


