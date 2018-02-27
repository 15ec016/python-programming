print("Enter '0' for exit.");
hk = input("Enter any character: ");
if hk == '0':
    exit();
else:
    if((hk>='a' and hk<='z') or (hk>='A' and hk<='Z')):
    	print(hk, "is an alphabet.");
    else:
    	print(hk, "is not an alphabet.");
