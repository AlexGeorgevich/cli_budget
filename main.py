### Imports:
import assets, json, os

# Loading local JSON file "userAccounts.json" containing user data (or empty JSON object for first time users).
with open("userAccounts.json", "r") as readAccounts:
	accounts = json.load(readAccounts)
# Loading local JSON file "userRecords.json" containing user data (or empty JSON object for first time users).
with open("userRecords.json", "r") as readRecords:
	records = json.load(readRecords)

### Functions:
# Account managment functions:
def seeBudget():
	sum = 0
	print("Your budget:")
	for account in accounts.items():
		sum += account[1]
		print(f"    ({account[0]}) {account[1]}")
	print("    ==================")
	print(f"    Balance sum: {sum}\n")

def addAccount(accName, accValue):
	accounts.update({accName: accValue})
	seeBudget()

def rmAccount(accName):
	accounts.pop(accName)

# Log functions:
def seeLog():
	print("Your records:")
	for record in records:
		print(f"    ({record[0]}) {record[1]}{record[2]} | {record[3]}")
	print("    ==================")

def logExpense(accName, expenseValue, expenseMessage):
	accounts[accName] -= expenseValue
	records.append([accName, "-", int(expenseValue), expenseMessage])

def logIncome(accName, incomeValue, incomeMessage):
	accounts[accName] += incomeValue
	records.append([accName, "+", int(incomeValue), incomeMessage])

def logTransfer(accToSend, accToGet, transferValue):
	accounts[accToSend] -= transferValue
	accounts[accToGet] += transferValue
	records.append([accToSend, int(transferValue), " >>> " + accToGet, "Transfer"])

def clear():
	os.system('clear')

### Intro, Main loop and Commands:
clear()
assets.logo()
print("Welcome to CLI Budget: Simple Command Line Interface Budget app.\nIf you are unfamiliar with commands in CLI Budget, type 'help'.\nYou can quit the program by typing 'exit'.")

run = True
while run:
	
	mainCommand = input("Enter command: ").lower()
	clear()
	assets.logo()

	# Help.
	if mainCommand == "help":
		assets.help()

	# See budget.
	elif mainCommand == "ls acc":
		if accounts == {}:
			print("You don't have any registered accounts. Try adding one with the 'add acc' command.")
		else:
			seeBudget()

  	# Add account.
	elif mainCommand == "add acc":
		accName = input("Enter account name: ")
		# Check if name is already in the budget list.
		if accName in accounts.keys():
			print(f"Account with name '{accName}' already exists.")
			continue
    		# Check if name is not one of the keywords.
		if accName.lower() in ["cancel", "exit"]:
			print("You can't use that account name, try another.")
			continue
		try:
			accValue = int(input("Enter starting value (positive numbers only, without spaces): "))
		except ValueError:
			print("You must enter positive digits only, try again.")
			continue
		if int(accValue) < 0:
			print("You can't assign negative starting value.")
			continue
		else:
			addAccount(accName, accValue)

	# Remove account.
	elif mainCommand == 'rm acc':
		if accounts == {}:
			print("You don't have any registered accounts. Try adding one with the 'add acc' command.")
		else:
			accName = input("WARNING! You are about to delete an account.\nType 'cancel' if you wish to cancel, or enter name of the account you wish to remove: ")
			if accName.lower() == 'cancel':
				continue
			elif accName not in accounts.keys():
				print(f"Account with name '{accName}' doesn't exist.")
			else:
				rmAccount(accName)

	# See records log.
	elif mainCommand.lower() == "log":
		if records == []:
			print("You don't have any fund records logged.")
		else:
			seeLog()

	# Log expense.
	elif mainCommand == "-$":
		if accounts == {}:
			print("You don't have any registered accounts. Try adding one with the 'add acc' command.")
		else:
			accName = input("Log EXPENSE on account: ")
			if accName not in accounts.keys():
				print(f"Account with name '{accName}' doesn't exist.")
				continue
			else:
				expenseValue = int(input("EXPENSE amount: "))
				expenseMessage = input("Log EXPENSE message [press 'Enter' to skip]: ")
				logExpense(accName, expenseValue, expenseMessage)

	# Log income.
	elif mainCommand == "+$":
		if accounts == {}:
			print("You don't have any registered accounts. Try adding one with the 'add acc' command.")
		else:
			accName = input("Log INCOME on account: ")
			if accName not in accounts.keys():
				print(f"Account with name '{accName}' doesn't exist.")
				continue
			else:
				incomeValue = int(input("INCOME amount: "))
				incomeMessage = input("Log INCOME message [press 'Enter' to skip]: ")
				logIncome(accName, incomeValue, incomeMessage)

	# Log transfer.
	elif mainCommand == "mv $":
		if accounts == {}:
			print("You don't have any registered accounts. Try adding one with the 'add acc' command.")
		else:
			accToSend = input("Log TRANSFER from account: ")
			if accToSend not in accounts.keys():
				print(f"Account with name '{accToSend}' doesn't exist.")
				continue
			else:
				accToGet = input("To account: ")
				if accToGet not in accounts.keys():
					print(f"Account with name '{accToGet}' doesn't exist.")
					continue
				else:
					transferValue = int(input("TRANSFER amount: "))
					logTransfer(accToSend, accToGet, transferValue)

  	# Exit program (last elif statement).
	elif mainCommand.lower() == "exit":
		run = False

  	# Handle unknown inputs.
	else:
		print("Unknown command, try again or type 'help' to see avaliable commands.")

# Saving user data to local JSON file "userAccounts.json" for future usage.
with open("userAccounts.json", "w") as writeAccounts:
	json.dump(accounts, writeAccounts)
# Saving user data to local JSON file "userRecords.json" for future usage.
with open("userRecords.json", "w") as writeRecords:
	json.dump(records, writeRecords)
