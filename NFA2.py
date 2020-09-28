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
def nfa(stringi, state):
    steps = [state]
    i = 0
    while i < len(str(stringi)):
        steps.append(stateeval(steps[i], str(stringi)[i]))
        i += 1
    if steps[-1] == "q4":
        return True, stringi, steps
    else:
        return False, stringi, steps


if __name__ == "__main__":
    # Takes our input
    string = str(input("Enter your input string: \n"))

    # Trim any spaces and end lines
    string = string.replace(" ", "")
    string = string.replace("\n", "")

    # start state
    start = "q1"
    r = 0

    # array to capture all possible endings.
    possibleendings = [[nfa(string, start), r]]

    # checks to see if your first step can be an epsilon step.  I think this could be worked into the next part somehow.
    if epsilon1(start):
        possibleendings.append([nfa(string, "q3"), r])

    # this essentially looks for any other instances of states that can can an epsilon step then adds two possibilities:
    # one where it takes the step "q3" and one where it does not and remains at "q1".
    try:
        while r < len(possibleendings):
            if possibleendings[r][0][2][1:].index("q1") >= 0:
                possibleendings.append([nfa(possibleendings[r][0][1][possibleendings[r][0][2][1:].index("q1") + 1:], "q3"),
                                        str(possibleendings[r][1])])
                possibleendings.append([nfa(possibleendings[r][0][1][possibleendings[r][0][2][1:].index("q1") + 1:], "q1"),
                                        str(possibleendings[r][1])])
                r += 1
            else:
                r += 1
    except ValueError:  # at some point you will come across a string that does not have q1 in it.
        pass

    # prints the results of each branch
    for r in possibleendings:
        print(r)

    # Collates all possible accept/reject results
    outcomes = [i[0][0] for i in possibleendings]
    t = 0

    # if a true is found, then your string is accepted and it stops checking, otherwise it will print reject.  There's
    # probably a better way to do this.
    while t < len(outcomes):
        if outcomes[t]:
            print("Your string was accepted.")
            break
        else:
            t += 1

    if not outcomes[-1]:
        print("Your string was rejected.")

