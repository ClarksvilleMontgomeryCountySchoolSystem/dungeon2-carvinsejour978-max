good = r"""
            
        .-===-.
        | . . |
        | .'. |
       ()_____()
       ||_____||
   jgs  W     W     
"""

bad = r"""*\o_               _c/*
     /  *             *  \
    <\       *\o/*       />
               )
        c/*   / >    *\o
        <\            />
__o     */\          /\*     c__
* />                        <\ *
 /\*    __o_       _c__     */\
       * /  *     *  \ *
        <\           />
             *\c/*
ejm97        __)__

"""



escaped = True
if escaped:
    outcome = "Legend: finally we are free"
    print(good)
else:
    outcome = "Doom: We need to escape"
    print(bad)
print(outcome)