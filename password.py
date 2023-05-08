password = input('請設定密碼:')
x = 3
while x > 0:
	x = x - 1
	password1 = input('請輸入剛才設定的密碼:')
	if password == password1:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!')
		if x > 0:
			print('還有', x, '次機會')
		else:
		    print('被鎖帳號!')	








