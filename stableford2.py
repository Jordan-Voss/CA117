import sys

def main():
	points = {
	-7 : 9,
	-6 : 8,
	-5 : 7,
	-4 : 6,
	-3 : 5,
	-2 : 4,
	-1 : 3,
	 0 : 2,
	 1 : 1,
	 }
	holeindex = {}
	holepar = {}
	lines = sys.stdin.read()
	lines = ''.join(lines)
	lines = lines.split('\n')
	par = lines[0].split()
	index = lines[1].split()
	hole1 = (par[0] + ' ' + index[0]).split()
	hole2 = (par[1] + ' ' + index[1]).split()
	hole3 = (par[2] + ' ' + index[2]).split()
	hole4 = (par[3] + ' ' + index[3]).split()
	hole5 = (par[4] + ' ' + index[4]).split()
	hole6 = (par[5] + ' ' + index[5]).split()
	hole7 = (par[6] + ' ' + index[6]).split()
	hole8 = (par[7] + ' ' + index[7]).split()
	hole9 = (par[8] + ' ' + index[8]).split()
	hole10 = (par[9] + ' ' + index[9]).split()
	hole11 = (par[10] + ' ' + index[10]).split()
	hole12 = (par[11] + ' ' + index[11]).split()
	hole13 = (par[12] + ' ' + index[12]).split()
	hole14 = (par[13] + ' ' + index[13]).split()
	hole15 = (par[14] + ' ' + index[14]).split()
	hole16 = (par[15] + ' ' + index[15]).split()
	hole17 = (par[16] + ' ' + index[16]).split()
	hole18 = (par[17] + ' ' + index[17]).split()
	holeindex[1] = hole1[1]
	holepar[1] = hole1[0]
	holeindex[2] = hole2[1]
	holepar[2] = hole2[0]
	holeindex[3] = hole3[1]
	holepar[3] = hole3[0]
	holeindex[4] = hole4[1]
	holepar[4] = hole4[0]
	holeindex[5] = hole5[1]
	holepar[5] = hole5[0]
	holeindex[6] = hole6[1]
	holepar[6] = hole6[0]
	holeindex[7] = hole7[1]
	holepar[7] = hole7[0]
	holeindex[8] = hole8[1]
	holepar[8] = hole8[0]
	holeindex[9] = hole9[1]
	holepar[9] = hole9[0]
	holeindex[10] = hole10[1]
	holepar[10] = hole10[0]
	holeindex[11] = hole11[1]
	holepar[11] = hole11[0]
	holeindex[12] = hole12[1]
	holepar[12] = hole12[0]
	holeindex[13] = hole13[1]
	holepar[13] = hole13[0]
	holeindex[14] = hole14[1]
	holepar[14] = hole14[0]
	holeindex[15] = hole15[1]
	holepar[15] = hole15[0]
	holeindex[16] = hole16[1]
	holepar[16] = hole16[0]
	holeindex[17] = hole17[1]
	holepar[17] = hole17[0]
	holeindex[18] = hole18[1]
	holepar[18] = hole18[0]
	i = 2
	
	while i < len(lines):
		j = 0
		player_stats = lines[i].split()
		player_name = ' '.join(player_stats[0:-19])
		player_handicap = player_stats[-19]
		player_stats = lines[i].split()[-18:]
		while j < 18:
			par = holepar[j + 1]
			index = holeindex[j + 1]
			strokes = player_stats[j]
			if int(player_handicap) == 14 and int(index) in range(1,14,1):
				net = int(strokes) - 1
			elif int(player_handicap) == 19 and int(index) in range(1,18,1):
				net = int(strokes) - 1
				if int(index) in range(1,1,1):
					net = int(strokes) - 2
			else:
				net = int(strokes)
			
			print(net)
			
				

			
			j += 1
		print(player_name)



		i += 1
	 


if __name__ == '__main__':
	main()