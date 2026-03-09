good = r"""

       (_. /)
        ..) -
       (V  -i
        `- `-----.
        `.        )   .-
        _-\ `--( /``-''`'
       (.' )/ _7)7 `''
          --   --  BP"""
bad = r"""

   _,,
  (/..\
   \ -/
  _\`.|_
 /`H  I'\
( (H  I- )
 \/==O=\/
 >    , \
/    /   \
    /\    \
   /  \   / _
 ,"    `-.`'/
--.       \P Ojo.
`""
"""





has_key = False
if has_key:
    outcome = "Click: I can open the door"
    print(good)
else:
    outcome = "Doom: I need the key"
    print(bad)
print(outcome)