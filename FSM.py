# DSL

# Goal is to create a FSM but more easily readable and adaptable to reconfiguration

# create state functions.  This way if you want to change them it's more obvious where to change it.
def state1(step):
    if step == "1":
        return "q4"
    elif step == "0":
        return "q3"
    # epsilon allows any input and just moves to q3
    else:
        return "q3"


def state2(step):
    if step == "1":
        return "q1"
    elif step == "0":
        return "q2"
    # Our alphabet only allows 1 and 0s (and epsilon, but only for q1) so this will break the loop to return a
    # rejection.
    else:
        return "invalid"


def state3(step):
    if step == "1":
        return "q4"
    elif step == "0":
        return "q3"
    else:
        return "invalid"

def state4(step):
    if step == "1":
        return "q1"
    elif step == "0":
        return "q2"
    else:
        return "invalid"


# Create function that evaluates what state you're in and makes the "move"
def stateeval(state, delta):
    if state == "q1":
        return state1(delta)
    elif state == "q2":
        return state2(delta)
    elif state == "q3":
        return state3(delta)
    elif state == "q4":
        return state4(delta)
    elif state == "invalid":
        print("Invalid state")



import sys

string = str(input("Enter your input string: \n"))

# trim any spaces and end line
string = string.replace(" ", "")
string = string.replace("\n", "")

#print(string)

# define start state
#token = "q1"
i = 0
steps = ["q1"]

# check your alphabet:
while i < len(str(string)):
    step = str(string)[i]
#    token = stateeval(token, step)
#    steps.append(str(token))
    steps.append(stateeval(steps[i], step))
    i += 1

print("The moves are as follows:")
print(steps)

if steps[-1] == "q4":
    print("Your string was accepted.")
else:
    print("Your string was rejected.")

#if token == "q4":
#    print("Your string was accepted.")
#else:
#    print("Your string was rejected.")
