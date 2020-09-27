# DSL

# Goal is to create a FSM but more easily readable and adaptable to reconfiguration.

# So the hard part was actually the set theory to convert the NDA to a DFA.  Because of the way q1 and q3 are
# defined, the epsilon transition doesn't actually do anything (i.e. regular expression of accepted values does not
# change), but I thought it useful to work through the programming anyways so there is a state q1q3 function that
# ends up having the same output states as both q1 and q3.

# Create state functions.  This way if you want to change them it's more obvious where to change it.
def state1(step):
    if step == "1":
        return "q4"
    elif step == "0":
        return "q3"
    else:
        return "invalid state"


def state2(step):
    if step == "1":
        return "q1q3"
    elif step == "0":
        return "q2"
    else:
        return "Invalid state"


def state3(step):
    if step == "1":
        return "q4"
    elif step == "0":
        return "q3"
    else:
        return "Invalid state"


def state4(step):
    if step == "1":
        return "q1q3"
    elif step == "0":
        return "q2"
    else:
        return "Invalid state"


def stateq1q3(step):
    if step == "1":
        return "q4"
    elif step == "0":
        return "q3"
    else:
        return "Invalid state"


# Create function that evaluates what state you're in and makes the "move."  This also means if you have a new
# state, you can just make a new function like above and add it with a few lines.

def stateeval(state, delta):
    if state == "q1":
        return state1(delta)
    elif state == "q2":
        return state2(delta)
    elif state == "q3":
        return state3(delta)
    elif state == "q4":
        return state4(delta)
    elif state == "q1q3":
        return stateq1q3(delta)
    else:
        return "Invalid state"


string = str(input("Enter your input string: \n"))

# trim any spaces and end line
string = string.replace(" ", "")
string = string.replace("\n", "")

# print(string)

# define start state
# token = "q1"
i = 0
steps = ["q1"]

# use while loop to make the steps. each step is appended to the list meaning you can map out the moves.
while i < len(str(string)):
    #    I initially used the commented code below but found I could consolidate it to one line.
    #    token = stateeval(token, step)
    #    steps.append(str(token))
    steps.append(stateeval(steps[i], str(string)[i]))
    # I had to play around with variable types but need str(string)[i] else it will read 1 or 0 as integers and
    # be unable to compare.
    i += 1

print("The moves are as follows:")
print(steps)

# Checks the final state you're in, if not in the accepting state (q4) then rejects.
if steps[-1] == "q4":
    print("Your string was accepted.")
else:
    print("Your string was rejected.")
