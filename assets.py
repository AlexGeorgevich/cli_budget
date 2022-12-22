
def help():
	print("""

CLI Budget $_
Simple Command Line Interface Budget monitoring and logging application.
---------------------------------------
Features 💻

Manage accounts:
- See budget with ['budget'] to list all of your registered accounts and corresponding amounts with budget sum. 
- Add account with ['add acc'] to add new account, then enter initial value.
- If you wish to remove an account, use ['rm acc'] command.
- More main features to be included.

Funds manipulation:
- Log income with ['+$'] to an existing account.
- Log expense using ['-$'].
- Log transfer typing ['mv $'] to transfer funds from one account to another.

Statistics:
- To be included.

Additional features:
 - To be included.

---------------------------------------
> Python powered
> Edited with nano

""")

def logo():
	print("""
  ______   __        ______        _______                   __                        __               __           
 /      \ /  |      /      |      /       \                 /  |                      /  |            _/  |_         
/$$$$$$  |$$ |      $$$$$$/       $$$$$$$  | __    __   ____$$ |  ______    ______   _$$ |_          / $$   \        
$$ |  $$/ $$ |        $$ |        $$ |__$$ |/  |  /  | /    $$ | /      \  /      \ / $$   |        /$$$$$$  |       
$$ |      $$ |        $$ |        $$    $$< $$ |  $$ |/$$$$$$$ |/$$$$$$  |/$$$$$$  |$$$$$$/         $$ \__$$/        
$$ |   __ $$ |        $$ |        $$$$$$$  |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |  $$ | __       $$      \        
$$ \__/  |$$ |_____  _$$ |_       $$ |__$$ |$$ \__$$ |$$ \__$$ |$$ \__$$ |$$$$$$$$/   $$ |/  |       $$$$$$  |       
$$    $$/ $$       |/ $$   |      $$    $$/ $$    $$/ $$    $$ |$$    $$ |$$       |  $$  $$/       /  \__$$ |______ 
 $$$$$$/  $$$$$$$$/ $$$$$$/       $$$$$$$/   $$$$$$/   $$$$$$$/  $$$$$$$ | $$$$$$$/    $$$$/        $$    $$//      |
                                                                /  \__$$ |                           $$$$$$/ $$$$$$/ 
                                                                $$    $$/                              $$/           
                                                                 $$$$$$/                                             
""")
