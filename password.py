password = input('請設定密碼:')
x = 2
while x >= 0:
	password1 = input('請輸入剛才設定的密碼:')
	if password == password1:
		print('登入成功!')
		break
	else:
		if x == 0:
			break
		print('密碼錯誤! 還有', x, '次機會')
		x = x - 1







