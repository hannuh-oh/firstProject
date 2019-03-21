def applyRules(leftChar):
    """ apply rule transforming leftChar to rightStr """
    rightStr = ""
    if leftChar == 'A':
        rightStr = 'B'   # Rule 1
    elif leftChar == 'B':
        rightStr = 'AB'  # Rule 2
    else:
        rightStr = leftChar    # no rules apply so keep the character
    return rightStr


def processString(oldStr):
    """ given a string oldStr transform it into newStr with rules """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRules(ch)

    return newStr


def executeLSystem(numIters,axiom):
    resultString = axiom
    for i in range(numIters):
        newString = processString(resultString)
        resultString = newString

    return resultString




print(executeLSystem(4, "A"))
