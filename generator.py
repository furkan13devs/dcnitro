''')


		chars = "abcdefghijklmnoprstuvyzqwABCDEFGHIJKLMNOPRSTUVYQW1234567890"

		while 1:
			password_sayi = int(input("Kaç tane oluşturulsun? "))
			for x in range(0,password_sayi):
				password = ""
				for x in range(16):
					password_sayi = random.choice(chars)
					password	= password + password_sayi
				print("discord.gift/"+password)
				''')
