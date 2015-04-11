__author__ = 'erich_000'


def make_response_codes(output_string):
    # decide response type: True = string; False = int
    if output_string:
        # lists of response codes to use to return
        response_codes = ['Correct-Hit', "Correct-NoResponse", "Incorrect-FA",
                             'Incorrect-NoResponse', 'Incorrect-TooEarly', 'Incorrect-TooLate']
    else:
        response_codes = [1, 2, 3, 4, 5, 6]
    return response_codes


def assess_response(stim_code, rt, user_input=None):
    # assessed_response = assess_response(stim_code, user_input, rt)
    """

    :type user_input: int
    """
    print "assessing response: "
    print "stim_code =", stim_code
    print "user_input =", user_input
    print "rt =", rt
    response_codes = make_response_codes(True)
    #print "response codes =", response_codes
    targets = [52, 10, 11, 12, 62, 110, 111, 112, 72, 210, 211, 212]

    min_rt = 200
    max_rt = 1000
    if rt < min_rt:
        # return early (code 5)
        return response_codes[4]
    elif rt > max_rt:
        # return late (code 6)
        return response_codes[5]

    if user_input == 0 or user_input is None:
        # if inputs no click
        if stim_code in targets:
            # target, no click
            # incorrect-no response (code 4)
            return response_codes[3]
        else:
            # non target, no click
            # correct, no response (code 2)
            return response_codes[1]
    else:
        # user inputs click
        # (L or R doesn't matter; eprime doesn't register incorrect click)
        if stim_code in targets:
            # target, click
            # correct hit (code 1)
            return response_codes[0]
        else:
            # non-target, click
            # incorrect FA (code 3)
            return response_codes[2]


