
def help():
	print("""CLI Budget $_
Simple Command Line Interface Budget monitoring and logging application.
---------------------------------------
Features

Manage accounts:
- See budget with ['ls acc'] to list all of your registered accounts and corresponding amounts with budget sum. 
- Add account with ['add acc'] to add new account, then enter initial value.
- If you wish to remove an account, use ['rm acc'] command.
- More main features to be included.

Funds manipulation:
- You can display your fund records by using ['log'].
- Log income with ['+$'] to an existing account.
- Log expense using ['-$'].
- Log transfer typing ['mv $'] to transfer funds from one account to another.

Additional features to be included.

---------------------------------------
> Python powered

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
