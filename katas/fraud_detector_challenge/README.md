# We have a stilt user who lives in Bakersfield, CA(119.0611119,35.35581513). 

# Design a location based fraud detection system that flags and notifies the user whenever there is a transaction that happens outside of the user's home location.
# The system should work like this:
# * Monitor the transactions as they occur
# * Notify the user when there is a suspicious transaction
# * If the user responds saying, "it's NOT fraud", allow the subsequent transactions in that new location area(probably a travel) and don't ask the user again
#   for that new location
# * If the user responds saying, "it's fraud", add a key-value pair to that transaction that looks like {fraud: true} and also the subsequent ones coming in
#   from that new location

# Eucledien distance: sqrt((x2-x1)^2 + (y2-y1)^2)

# var home = [119.0611119,35.35581513]

## Solution approach
 - 1) is the rquest valid?
    - 1.1 Define what is valid? radius of x distance from home
    - 1.1.1  when out of the radius need customer confirmation
    - 1.1.1.1 process customer answer (y/n)
    - 1.1.1.2. if yes add that location to safe locations


