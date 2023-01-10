### Imports:
import assets


### Variables:
accounts = {}
expenseLog = ""

### Functions:
# Account managment functions:
def seeBudget():
	sum = 0
	print("Your budget:")
	for account in accounts.items():
		sum += account[1]
		print(f"    {account[0]}, {account[1]}")
	print("    ==================")
	print(f"    Balance sum: {sum}\n")

def addAccount(accName, accValue):
	accounts.update({accName: accValue})
	seeBudget()

def rmAccount(accName):
	accounts.pop(accName)

# Log functions:
def logExpense(accName, expenseValue):
	accounts[accName] -= expenseValue

def logIncome(accName, incomeValue):
	accounts[accName] += incomeValue

def logTransfer(accToSend, accToGet, transferValue):
	accounts[accToSend] -= transferValue
	accounts[accToGet] += transferValue

### Intro, Main loop and Commands:
assets.logo()
print("Welcome to CLI Budget : Simple Command Line Interface Budget app.\nIf you are unfamiliar with commands in CLI Budget, type 'help'.\nYou can quit the program by typing 'exit'.")

run = True
while run:

	mainCommand = input("Enter command: ").lower()

	# Help.
	if mainCommand == "help":
		assets.help()

	# See budget.
	elif mainCommand == "budget":
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
				logExpense(accName, expenseValue)

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
				logIncome(accName, incomeValue)

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
