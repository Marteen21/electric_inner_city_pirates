def print_sudoku(third_list):
	print
	for row in third_list:
		row_str=''
		for char in row:
			row_str+=char
		print row_str
	print
def check_row(third_list,row_index,col_index, results):
	row=third_list[row_index]
	for char in row:
		if char in results:
			results.remove(char)
	return results

def check_col(third_list,row_index,col_index, results):
	for i, row in enumerate (third_list):
		for j, char in enumerate (row):
				if j==col_index and char in results:
						results.remove(char)
	return results

def is_in_same_matrix(i,j,ci,cj):
	if (i/6 == ci/6) and (j/6 == cj/6):
		return True
	else:
		return False

def check_matrix(third_list,row_index,col_index, results):
	for i, row in enumerate (third_list):
		for j, char in enumerate (row):
			if is_in_same_matrix(row_index,col_index,i,j):
				if char in results:
					results.remove(char)		
	return results

def calc_obvious (third_list):
	worth_looping=True
	while worth_looping:
		worth_looping=False
		for i, row in enumerate (third_list):
			for j, char in enumerate (row):
				possible_chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
				if (third_list[i][j]=='_'):
					possible_chars=check_row(third_list,i,j,possible_chars)
					possible_chars=check_col(third_list,i,j,possible_chars)
					possible_chars=check_matrix(third_list,i,j,possible_chars)
					if len(possible_chars)==0:
						print 'lo'
						return False, third_list
					if len(possible_chars)==1:
						third_list[i][j]=possible_chars[0]
						worth_looping=True
					
	return True, third_list

def populate_sudokus (sudokus):
	new_sudokus=[]
	for sudoku in sudokus:
		for i, row in enumerate (sudoku):
			for j, char in enumerate (row):
				if (sudoku[i][j]=='_'):
					possible_chars=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
					possible_chars=check_row(sudoku,i,j,possible_chars)
					possible_chars=check_col(sudoku,i,j,possible_chars)
					possible_chars=check_matrix(sudoku,i,j,possible_chars)
					for char in possible_chars:
						new_sudoku=sudoku
						print_sudoku(new_sudoku)
						new_sudoku[i][j]=char
						valid, new_sudoku = calc_obvious(new_sudoku)
						if valid:
							print 'sia'
							check_if_done(new_sudoku)
							new_sudokus.append(new_sudoku)
						else:
							print i*36+j
	
	if (len(new_sudokus)==0):
		print 'Szar'
		raw_input()
	return new_sudokus

def check_if_done (sudoku):
	for i, row in enumerate (sudoku):
		for j, char in enumerate (row):
			if char == '_':
				return False
	print_sudoku(sudoku)
	print 'DONNE!'
	raw_input()
	return True	

def calc_sum (sudoku):
	total = 0
	for i, row in enumerate (sudoku):
		for j, char in enumerate (row):
			if (i==j):
				total+=	
			
original='___3OAHEWUP___DNTZ_YC7_BM_GL_F6_195_5FDS__MJ___I0___WC_UQ1Z_NP_R83B7__K_T_H1ZK0D9_G7______MJNI_R_CA4___F3UV_B_M_Y_5_6_FCA___1__0_WX_Z_Q7_E_N_PJT_PGCV_Q1O__LF_75_2SD___E__6W0__I8X_RXU___72K_N__RJ_L4M_OGPF_S_9__5C__H_0U7_A_4__B_3Z__IJHT8R_LM___1___20QF6V_E__0__X_OY__P____Q5_4___LTIF_AK_8C7PISLN__7MC_29F_8_4_Z_X_____K_Q_3HJ_BG_Y9QRL6___ES__Z_____CN____B4_U____1_TF____R__QP1A0CD3W_IJBG5Z__27__LE_YD1_8_M____I_VQ__R__EY9___0CG_6_ZSN4_A_P_G_____Z___6F___Q720_83J9__HTO_D__Z_5_NG__26_O_STUY_K_F__IX_HQ_R_____CDUO_XV4KWH9281E3_5G_YIZ_7___N_P___6V4Q__I____EOD___CP_M_NHL_BZ5_Y71___XS30619PQ7__BHWJX__D_VOE_UG___KF_Z_IN__R_K_YM__0___Q_N7X_6_3__D_V_4E5__UAO6__RWS_4_1__V_B_FI8_0___5__J9_C_T__KC_G_PN___LU_5Z0_J__DBAXY__E6OQ49S2M9___F8X_0ZW_T1G_P_NH___UC4____Y__VOL0___L_O___9_3MY_QH_CW51PFN7ZGSJ_UBRK_____Z_F5_CY__O_9_GLKV_M_2H__P8_7_1__B_I2Y__QTVJ_KN4L___S3___R_____H_D_Z_NBHD_R_PI8___T7F__1__C2_Y____5_M_WS7_WJ__39__S1UC5D_ILNRKVFGM__H____Z0_Z____0_WN____R4_____5__A7___CLIU61_OI_LUM_K_T_____P_A_Z_X_D4J_5N9__BY7FQ6RV_C1_5LY7___H_ZG____W__QO_P__E__N_2X9EA5___6___LK_Y07BMQ__4S_8__T_C_3PY_7__DJ__5_H_TVU0_CAB_RW__L_1G3___ZE1_XM9__LER__5___ID3_JG_0W__YNZ_8B2T_L26_3_4_G9_T_EW_B__S___IXH_Q_V_R_M_J_HNT4___2PO_Z_M6G1______0A_J7UKVI5_F_J__SGD0F_XA_9RH7_Y4___5B___3M__WCQU_5KV_U7_I1_3L_FQJ_6PHZ___9SCTD0XG___'
first_list = []
c=0
for k in range(0,36):
	first_list.append(original[c:c+36])
	c=c+36
second_list=[]
sudoku=[]
for row in first_list:
	for char in row:
		second_list.append(char)
	sudoku.append(second_list)
	second_list=[]

tries = []
print_sudoku(sudoku)
valid, sudoku = calc_obvious(sudoku)
print valid
print_sudoku(sudoku)
sudokus=[sudoku]
while True:
	sudokus = populate_sudokus(sudokus)

