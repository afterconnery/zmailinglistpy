# Python Zcash Memo Mailer
## To be used with Zecwallet Lite CLI on **LINUX**

The python script will open a file in the same directory named "mailinglist.txt" that has a z-address on every line (example provided), and ask the user to input a memo. It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in mailinglist.txt . You will then need to change the mode of the sendletter.sh script so you can execute it. `sudo chmod u+x sendletter.sh`. Also change the mode of the `zmailinglist.sh` so it can be executed as well. 
`sudo chmod u+x zmailinglist.sh`

Make sure to put these files in your zecwallet-cli folder. This way when you run the `zmailinglist.sh` script it will invoke the zecwallet lite client to send out the memos. The `sendletted.sh` file will be overwritten each time you run the python script.

![sending a memo](zmailinglist.png)
