bids = input("Enter All Bid : ").split(" ")
for i in range(0,len(bids)):
    bids[i] = int(bids[i])
if len(bids)==1:
    print("not enough bidder")
else:
    bids.sort()
    if bids[-2] == bids[-1]:
        print("error : have more than one highest bid")
    else :
        print("winner bid is",bids[-1],"need to pay",bids[-2])
