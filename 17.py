def buildRules(ruleString):
    """

    :param rulesString:
    :return:
    """

    ruleString = ruleString.strip()

    """
    A
    A --> BAB
    B --> +F--FF++F-
    """

    myList = ruleString.split("\n")
    print(myList)