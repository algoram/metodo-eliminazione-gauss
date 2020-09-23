def check(mat):
	rows = len(mat)
	cols = len(mat[0])

	for i in range(1, rows):
		if len(mat[i]) != cols:
			return (False, 0)

	return (True, cols)

def mcm(a, b):
	return (a * b) // mcd(a, b)

def mcd(a, b):
	while b:
		a, b = b, a % b

	return a

def trova_pivot(riga):
	pivot = 0
	while pivot < len(riga) and riga[pivot] == 0:
		pivot += 1

	return pivot

def aScala(mat):
	last_pivot = -1

	for i in range(len(mat)):
		current_pivot = trova_pivot(mat[i])

		if current_pivot <= last_pivot:
			return False
		else:
			last_pivot = current_pivot

	return True

def miglior_riga(mat):
	posizione_pivot = len(mat[0])
	lista_pivot = []

	for i in range(len(mat)):
		pivot = trova_pivot(mat[i])

		if pivot < posizione_pivot:
			posizione_pivot = pivot
			lista_pivot = []
			lista_pivot.append((pivot, i))
		elif pivot == posizione_pivot:
			lista_pivot.append((pivot, i))

	lista_pivot.sort()

	return lista_pivot[0][1]

def meg(mat):
	if not aScala(mat):
		prima_riga = miglior_riga(mat)

		mat[0], mat[prima_riga] = mat[prima_riga], mat[0]

		i = 0
		while not aScala(mat) and i < len(mat):
			pivot_i = trova_pivot(mat[i])

			for k in range(i+1, len(mat)):
				pivot_k = trova_pivot(mat[k])

				if pivot_i == pivot_k:
					if mat[k][pivot_k] % mat[i][pivot_i] != 0:
						fatt = mcm(mat[k][pivot_k], mat[i][pivot_i]) // mat[k][pivot_k]

						copy = [fatt * num for num in mat[k]]

						mat[k] = copy

					coeff = mat[k][pivot_k] // mat[i][pivot_i]

					temp = [(mat[k][index] - coeff * mat[i][index]) for index in range(len(mat[i]))]

					mat[k] = temp

			i += 1

		if i == len(mat):
			pivots = []
			for j in range(len(mat)):
				pivots.append((trova_pivot(mat[j]), j))

			pivots.sort()

			skip = []

			for j in range(len(mat)):
				if j not in skip:
					mat[j], mat[pivots[j][1]] = mat[pivots[j][1]], mat[j]
					skip.append(pivots[j][1])

def main():
	print("Metodo di eliminazione di Gauss")

	try:
		righe_matrice = int(input("Inserisci il numero di righe della matrice: "))
	except:
		righe_matrice = -1
	while righe_matrice <= 0:
		try:
			righe_matrice = int(input("Inserisci un numero valido di righe: "))
		except:
			righe_matrice = -1

	matrice = []

	for i in range(righe_matrice):
		while len(matrice) == i:
			try:
				matrice.append(list(map(int, input("Inserisci la riga %d: " % i).split(" "))))
			except:
				print("Errore nell'inserimento dei numeri. Riprovare...")

	valida, colonne_matrice = check(matrice)

	if valida:
		meg(matrice)

		print("Matrice ridotta a scala: ")
		for i in range(righe_matrice):
			output = ""
			for j in range(colonne_matrice):
				output += "%4d" % matrice[i][j]

				if j != colonne_matrice - 1:
					output += " "

			print(output)

if __name__ == "__main__":
	main()