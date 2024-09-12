def numsquaresum(n):
    squaresum=0;
    while(n):
            squaresum+=(n%10)*(n%10);
            n=int(n/10);
            return squaresum;
        
        def isHappynumber(n):
            slow=n;
            fast=n;
            while(True):
                slow=numsquaresum(slow);
                fast=numsquaresum(numsquaresum(fast));
                if(slow!=fast):
                    continue;
                else:
                    break;
                return(slow==1);
            n=2;
            if(isHappynumber(n)):
                print("true"):
                    else:
                        print("false");
