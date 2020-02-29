# This python script will open a file named "mailinglist.txt" that has a z-address on every line, and ask the user
# to input a memo. It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in
# mailinglist.txt . Finally, while zecwallet light cli is running, run sendletter.sh in the same folder as zecwallet-cli to send.

 
file = open("mailinglist.txt")
memotext=input("Input Memo (IN QUOTES): ")
outstring=""
output = open("sendletter.sh","w")
outstring += './zecwallet-cli send '
outstring += '"['
 
for a in file:
    outstring += '{\\"address\\": \\"'+a.replace(',','')+'\\",\\"amount\\": 1, \\"memo\\":\\"'+memotext+'\\"},'
   
 
outstring=outstring[:-1]
outstring+= ']"'
outstring = outstring.replace('\n', '')
output.write(outstring)
