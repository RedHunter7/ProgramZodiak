confirm = "n"
ThnIni=2020
while(confirm=="n"):
    print("") 
    print("Selamat Datang di OneSpin Star:") #Seputar Bintang
    print("1.Penebak Zodiak")
    print("2.Seputar tanggal lahir")
    print("3.Penghitung Usia")
    print("4.Keluar")
    X=input("Pilih salah satu (1,2,3,4).. ")
    print("")
    if (X=="1"):
        print("Kami dapat menebak zodiak yang anda pikirkan. Bisa milik sendiri, bisa Zodiak lain.")
        print( "Silhkan jawab dengan ya atau tidak dengan (y/n)")    
        confirm = "y"
        while(confirm=="y"):
         r = input("Terdapat huruf R, apakah begitu? ")
         if (r == "n"):
          i = input("Apakah terdapat huruf I? ")
          if (i == "y"):
            c = input("Saya mendapat gambaran tentang huruf yang melengkung, apakah terdapat C? ")
            if (c == "y"):
             print("Anda pasti Pisces")
            else:
             print("Oh, saya keliru C dengan G. Anda pasti Gemini") 
          else:
             print("Anda pasti Leo")
             print()
      
         else: 
           a = input("Terdapat huruf A, apakah begitu? ")
           if (a=="n"):
             s = input("Mungkinkah terdapat huruf S? ")
             if (s=="y"):
               print("Mungkin anda Scorpio")
             else:
               print("Hmm... Bisa jadi anda Virgo")  
               
           else:
            i = input("Apakah terdapat I? ")
            if(i == "n"):
             s = input("Mungkinkah terdapat huruf S? ")
             if(s=="y"):
              print("Anda pasti Taurus")        
             else:
               print("Anda pasti Cancer")
               
            else:
             s = input("Pasti terdapat huruf S? ")
             if(s=="n"):
              n = input("Apakah ada huruf N? ")
              if (n=="y"):
               print("Anda pasti Capricorn")
              else:
               print("Anda pasti Libra")     
               
             else:
              e = input("Apakah terdapat E? ")
              if (e=="y"):
               print("Anda pasti Aries")
              else:
               t = input("Mungkin ada huruf T? ")
               if (t=="y"):
                print("Anda pasti Sagittarius")
               else:
                print("Mungkin anda Aquarius")
         print("")
         confirm = input("Apakah ingin mengulanginya lagi (y)? Atau kembali ke menu awal(n)?")    
         
    elif(X=="2"):
     confirm="y"
     while(confirm=="y"):
         Bln=["Default", "Januari", "Februari", "Maret", "April", "Mei", "Juni","Juli","Agustus","September","Oktober","November","Desember"]
         def Age():
          usia= int(ThnIni)-int(Year)
          print("Usia anda sekarang ",usia,"tahun")
         def Youre(yourzodiac):
            print("Anda adalah seorang ", yourzodiac)   
         def Sign():
            def Jan():
             if(Month>=20):
              yz="Aquarius" 
              Youre(yz)
             else:
              yz="Capricorn"
              Youre(yz)
            def Feb():
              if(Month<=18):
                yz="Aquarius"
                Youre(yz)
              else:
                yz="Pisces"
                Youre(yz)
            def Mar():
              if(Month<=20):
                yz="Pisces"
                Youre(yz)
              else:
                yz="Aries"
                Youre(yz)
            def Apr():
              if(Month<=19):
                yz="Aries"
                Youre(yz)
              else:
                yz="Taurus"
                Youre(yz)  
            def May():
              if(Month<=20):
                yz="Taurus"
                Youre(yz)
              else:
                yz="Gemini"
                Youre(yz)
            def Jun():
              if(Month<=20):
                yz="Gemini"
                Youre(yz)
              else:
                yz="Cancer"
                Youre(yz)
            def Jul():
             if(Month>=22):
              yz="Cancer" 
              Youre(yz)
             else:
              yz="Leo"
              Youre(yz)
            def Aug():
              if(Month<=22):
                yz="Leo"
                Youre(yz)
              else:
                yz="Virgo"
                Youre(yz)
            def Sep():
              if(Month<=22):
                yz="Virgo"
                Youre(yz)
              else:
                yz="Libra"
                Youre(yz)
            def Oct():
              if(Month<=22):
                yz="Libra"
                Youre(yz)
              else:
                yz="Scorpio"
                Youre(yz)  
            def Nov():
              if(Month<=21):
                yz="Scorpio"
                Youre(yz)
              else:
                yz="Sagittarius"
                Youre(yz)
            def Dec():
              if(Month<=21):
                yz="Sagittarius"
                Youre(yz)
              else:
                yz="Capricorn"
                Youre(yz)                 
            Zs = {
            1:Jan, 2:Feb, 3:Mar,
            4:Apr, 5:May, 6:Jun,
            7:Jul, 8:Aug, 9:Sep,
            10:Oct,11:Nov,12:Dec}
            Zs[Month]()
         print("Mari kita lihat apa yang bisa kita ketahui dari tanggal lahir anda")
         Day= int(input("Masukkan tanggal hari lahir: "))
         Month= int(input("Masukkan angka bulan lahir: "))
         Year= int(input("Masukkan tahun lahir: "))
         print("Anda lahir ",Day," ",Bln[Month]," ",Year,".")
         Age()
         Sign()
         print("") 
         confirm = input("Apakah ingin mengulanginya lagi (y)? Atau kembali ke menu awal(n)?")
    elif(X=="3"):
     confirm="y"
     while(confirm=="y"):
         print("Penghitung usia, kalau anda ingin tahu kapan anda berumur berapa")
         print("1. Untuk tahu kapan anda berusia 18 & 60")
         print("2. Untuk tahu tahun untuk usia tertentu")
         print("3. Untuk tahu usia anda di tahun tertentu")
         class yearCounter:
          def et():
           db = 18-int(now)
           Year = int(ThnIni)+int(db)
           print("Anda berumur 18 tahun saat",Year)
          def st():
           ep = 60-int(now)
           Year = int(ThnIni)+int(ep)
           print("Anda berumur 60 tahun saat",Year)
          def ac():
           age = int(input("Sebutkan Usia yang ingin diketahui: "))
           ps =  age-int(now)  
           Year = int(ThnIni)+int(ps)
           print("Anda berumur",age,"tahun saat",Year)
          def yc():
           Year = input("Masukkan Tahun yang dituju:")
           ps = int(Year)-int(ThnIni)
           age= int(ps)+int(now)
           print("Anda berumur",age,"tahun saat",Year)
         which = input("Pilih salah satu (1,2,3): ")
         now=input("Masukkan usia anda sekarang ini: ")
         if(which=="1"):  
          yearCounter.et()
          yearCounter.st()
         elif(which=="2"):  
          yearCounter.ac()
         else:
          yearCounter.yc()  
         print("") 
         confirm = input("Apakah ingin mengulanginya lagi (y)? Atau kembali ke menu awal(n)?")
           
    else:
     print("Terima Kasih dan semoga beruntung")
     break 