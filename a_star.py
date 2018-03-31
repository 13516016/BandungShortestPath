

def a_star(source,destination,adjacency_matrix, distance_matrix):
	 '''
	 - Source adalah titik awal perjalanan dimulai
	 
	 - Destination adalah titik akhir perjalanan diakhiri
	 
	 - adjacency_matrix berisi status ketetanggaan dua buah simpul
	 	contoh : 	
	 	[0 1 1]
	 	[1 0 0]
	 	[1 0 0]

	 	Matrix di atas berarti simpul-simpul yang bertetangga adalah simpul yang berindeks :
	 		- 0 dan 1
	 		- 0 dan 2

	 - distance_matrix berisi jarak antar simpul pada graf tidak berarah (berarti jarak dari (a -> b) == (b -> a) )
	 	contoh:
	 	[0 20 5]
	 	[20 0 10]
		[5 10 0]

		Matrix di atas berarti:
			- jarak simpul 0 dan 1 adalah 20 
			- jarak simpul 0 dan 2 adalah 5
			- jarak simpul 1 dan 2 adalah 10 
		
	 - Source dan destination adalah indeks matrix pada adjacency_matrix dan distance matrix.
	 	Apabila ingin memeriksa apakah simpul pada  indeks 0 dan indeks 1 bertetangga, 
	 	gunakan ** adjacency_matrix[0][1] ATAU adjacency_matrix[1][0] ** 
	 	(hal ini sama saja karena graph tidak berarah)

	 	Apabila ingin mengetahui jarak simpul pada indeks 0 dan indeks 1 bertetangga, 
	 	gunakan  ** distance_matrix[0][1] ATAU distance_matrix[1][0] ** 
	 	(hal ini sama saja karena graph tidak berarah)

	 - Silahkan implementasi dengan return sebuah array yang menandakan simpul-simpul mana saja yang seharusnya dikunjungi terlebih dahulu
	 	contoh:
	 	[0,2,3,1] 

	 	Array di atas berarti jarak terpendek adalah apabila kita melewati simpul dengan urutan indeks 0 -> 2 -> 3 -> 1
	
	 - Silahkan buat fungsi bantuan apabila perlu
	

	 Thanks and good luck!
	 
	 Dyl
	
	'''

	pass