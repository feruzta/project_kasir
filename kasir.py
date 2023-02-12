#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
from tabulate import tabulate


# In[11]:


#main
#buat class
class Transaction:
    #metode untuk inisialisasi awal list item transaksi
    def __init__(self):
        """
        fungsi untuk inisialisasi list
        """
        self.data_transaksi = list()

    #metode untuk mengganti nama, kuantitas, atau harga di dalam list item transaksi   
    def add_item(self, nama_item, jumlah_item, harga_item):
        """
        fungsi untuk menambahkan data transaksi
        
        parameters
        nama_item      :str - nama item yang akan ditambahkan
        jumlah_item    :int - jumlah item yang akan dibeli
        harga_item     :int - harga per item yang akan dibeli
        """
        self.data_transaksi.append([nama_item, jumlah_item, harga_item])
        print("Item berhasil ditambahkan!")
    
    #metode untuk mengganti nama, kuantitas, atau harga di dalam list item transaksi
    def update_item_name(self, nama_item, new_nama_item):
        """
        fungsi untuk mengupdate nama item
        """
        self.data_transaksi[self.index_transaksi(nama_item)][0] = new_nama_item
        print("Nama item berhasil diganti!")
        
    def update_item_qty(self, nama_item, new_jumlah_item):
        """
        fungsi untuk mengupdate jumlah item
        """
        self.data_transaksi[self.index_transaksi(nama_item)][1] = new_jumlah_item
        print("Jumlah item berhasil diganti!")
    
    def update_item_price(self, nama_item, new_harga_item):
        """
        fungsi untuk mengupdate harga per item
        """
        self.data_transaksi[self.index_transaksi(nama_item)][2] = new_harga_item
        print("Harga item berhasil diganti!")
    
    #metode untuk memberi index di dalam list item transaksi
    def index_transaksi(self, nama_item):
        """
        fungsi mengembalikan nilai index dari baris yang mengandung value 'nama_item'

        parameters
        nama_item   : str   nama item yang akan ditambahkan

        return
        i       : int   index dari baris yang mengandung judul
        """
        for i in range(len(self.data_transaksi)):
            if nama_item == self.data_transaksi[i][0]:
                return i
    
    #metode untuk menghapus salah satu item yang tidak jadi dibeli di dalam list item transaksi
    def delete_item(self, nama_item):
        """
        fungsi untuk menghapus baris pada suatu item yang tidak jadi dibeli
        """
        
        del_list = [nama_item, self.data_transaksi[self.index_transaksi(nama_item)][1], self.data_transaksi[self.index_transaksi(nama_item)][2]]

        while(del_list in self.data_transaksi):
            self.data_transaksi.remove(del_list)
        
        print("Item berhasil di delete!")
        
    #metode untuk reset semua transaksi
    def reset_transaction(self):
        """
        fungsi untuk reset semua transaksi
        """
        self.data_transaksi = list()
        print("Semua item berhasil di delete!")
        
    #metode untuk mengecek kembali pesanan di dalam list item transaksi
    def check_order(self):
        """
        fungsi untuk menampilkan seluruh order dari transaksi,
        """
        if self.data_transaksi == []:
            """
            Jika list kosong, akan menampilkan strip pada setiap kolom
            """
            data = {'Nama Item': ['-'],
                    'Jumlah Item': [0],
                    'Harga/Item': [0],
                    'Harga Total': [0]}
            df = pd.DataFrame(data)  
            print(df.to_markdown())
        
        else:
            """
            menambahkan list pada tabel
            """
            for i in range(len(self.data_transaksi)):
                if isinstance(self.data_transaksi[i][0], str) and isinstance(self.data_transaksi[i][1], int) and isinstance(self.data_transaksi[i][2], int):              
                    data = pd.DataFrame(self.data_transaksi)
                    data.columns = ['Nama Item', 'Jumlah Item', 'Harga/Item']

                    """
                    memanggil harga total
                    """
                    data['Harga Total'] = data['Jumlah Item'] * data['Harga/Item']

                    print("Pemesanan Berhasil!\n\n")
                    print(data.to_markdown())

                    return

                else:
                    print("Terdapat kesalahan input data")
                    return
    
    #metode untuk mencari total harga yang harus dibayarkan beserta diskon yang didapatkan
    def total_price(self):
        """
        fungsi untuk mencari total harga yang harus dibayarkan
        """
        if self.data_transaksi == []:
            """
            Jika list kosong, akan menampilkan strip pada setiap kolom
            """
            data = {'Nama Item': ['-'],
                    'Jumlah Item': [0],
                    'Harga/Item': [0],
                    'Harga Total': [0]}
            df = pd.DataFrame(data)  
            print(df.to_markdown())
        
        else:
            """
            menambahkan list pada tabel
            """
            for i in range(len(self.data_transaksi)):
                if isinstance(self.data_transaksi[i][0], str) and isinstance(self.data_transaksi[i][1], int) and isinstance(self.data_transaksi[i][2], int):              
                    data = pd.DataFrame(self.data_transaksi)
                    data.columns = ['Nama Item', 'Jumlah Item', 'Harga/Item']

                    """
                    memanggil harga total
                    """
                    data['Harga Total'] = data['Jumlah Item'] * data['Harga/Item']

                    print(data.to_markdown())
                    print(f"\n\nHarga Total = Rp.{data['Harga Total'].sum()}")
        
                    """
                    menggunakan conditioning untuk diskon 5%, 8%, dan 10%
                    """
                    if data['Harga Total'].sum() < 200_000:
                        pass

                    elif (data['Harga Total'].sum() > 200_000) and (data['Harga Total'].sum() <= 300_000):
                        harga_diskon = data['Harga Total'].sum() * 0.95
                        print(f"\n\nAnda mendapatkan diskon 5%! \n\nSetelah diskon, harga total menjadi Rp.{harga_diskon}")

                    elif (data['Harga Total'].sum() > 300_000) and (data['Harga Total'].sum() <= 500_000):
                        harga_diskon = data['Harga Total'].sum() * 0.92
                        print(f"\n\nAnda mendapatkan diskon 8%! \n\nSetelah diskon, harga total menjadi Rp.{harga_diskon}")

                    elif (data['Harga Total'].sum() > 500_000):
                        harga_diskon = data['Harga Total'].sum() * 0.90
                        print(f"\n\nAnda mendapatkan diskon 10%! \n\nSetelah diskon, harga total menjadi Rp.{harga_diskon}")

                    else:
                        pass

                    return

    #metode untuk check data di dalam list item transaksi
    def check_data_transaksi(self):
        print(f"Item yang dibeli adalah: {self.data_transaksi}")
    
    
        
        


# In[12]:


#running metode untuk pertama kali
trnsct_123 = Transaction()

