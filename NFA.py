# DSL

# State functions similar to the DFA conversion.
def state1(step):
    if step == "1":
        return "q4"
    elif step == "0":
        return "q3"
    else:
        return "invalid state"


def state2(step):
    if step == "1":
        return "q1"
    #        return "q1q3"
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
        return "q1"
    elif step == "0":
        return "q2"
    else:
        return "Invalid state"


# Note no q1q3 state function here.


# checks to see if an epsilon transition is possible (in this case we only have one that is # made from q1)
def epsilon1(state):
    if state == "q1":
        return True
    else:
        return False


# Same evaluation function from DFA.  Also note no q1q3 state possibility here.
def stateeval(state, delta):
    if state == "q1":
        return state1(delta)
    elif state == "q2":
        return state2(delta)
    elif state == "q3":
        return state3(delta)
    elif state == "q4":
        return state4(delta)
    else:
        return "Invalid state"


# This function evaluates out a string for acceptance and returns either accept (True) or reject (False) as well as
# the input string and the steps that were taken.
def NFA(stringi, state):
    steps = [state]
    i = 0
    while i < len(str(stringi)):
        steps.append(stateeval(steps[i], str(stringi)[i]))
        i += 1
    if steps[-1] == "q4":
        return True, stringi, steps
    else:
        return False, stringi, steps


# Takes our input
string = str(input("Enter your input string: \n"))

# Trim any spaces and end lines
string = string.replace(" ", "")
string = string.replace("\n", "")

# start state
start = "q1"
# array to capture all possible endings.
possibleendings = []
count = 0

while count < len(str(string)):
    # currentstate is going to figure out the state we are currently in based on the counter count
    currentstate = ["q1"]
    hx = 0
    while hx < count:
        currentstate.append(stateeval(currentstate[hx], str(string)[hx]))
        hx += 1

    # currentstate [-1] is the state we are in after consuming count # of inputs.
    # if epsilon is true, then it generates two possible outcomes.  I don't think it captures all epsilon closures??
    # Given the nature of our NFA, it's impossible to test.  I guess I could have created a new NFA to test this but
    # this was a lot of testing already...
    # This will also add the results (accept/reject), the input string, and the steps taken as well as the inputs
    # consumed.
    if epsilon1(currentstate[-1]):
        possibleendings.append([NFA(string[count:], "q3"), str(count)])
        possibleendings.append([NFA(string[count:], "q1"), str(count)])
        count += 1
    else:
        possibleendings.append([NFA(string[count:], currentstate[-1]), str(count)])
        count += 1

# The below allows for a final epsilon step if you end on q1.  In this case, we know the final state is false, so that's
# why I directly added false for final states of q1 and q3.
if possibleendings[-1][0][2][-1] == "q1":
    possibleendings.append([(False, "epsilon", ["q1"]), "Final Epsilon step"])
    possibleendings.append([(False, "epsilon", ["q3"]), "Final Epsilon step"])

# prints the results of each step consumption
for r in possibleendings:
    print(r)

# Collates all possible accept/reject results
outcomes = [i[0][0] for i in possibleendings]
t = 0

# if a true is found, then your string is accepted and it stops checking, otherwise it will print reject.
while t < len(outcomes):
    if outcomes[t]:
        print("Your string was accepted.")
        break
    else:
        t += 1

if not outcomes[-1]:
    print("Your string was rejected.")
