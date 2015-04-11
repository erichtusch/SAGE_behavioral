__author__ = 'erich_000'
from assess_response import assess_response

early_rt = 56
good_rt = 600
late_rt = 1002
def populate_codes():
    # initialize w/practice stim codes
    stimulus_codes = [51, 52, 61, 62, 71, 72]
    start_0 = 7
    start_1 = 107
    start_2 = 207
    i = 0
    # add 0-back stim
    while i < 9:
        stimulus_codes.append(start_0)
        i += 1
        start_0 += 1
    # add 1-back stim
    i = 0
    while i < 12:
        stimulus_codes.append(start_1)
        i += 1
        start_1 += 1
    # add 2-back stim
    i = 0
    while i < 12:
        stimulus_codes.append(start_2)
        i += 1
        start_2 += 1
    user_input = [None, 0, 1, 2]

    print 'stimulus codes =', stimulus_codes
    print 'user_input =', user_input
    return stimulus_codes, user_input
#print assess_response(7, 500, 1)
stimulus_codes, user_input = populate_codes()
rts = [early_rt, good_rt, late_rt]
# make list of lots of inputs and results
testing_list = []
one_test = []
for s in stimulus_codes:
    for r in user_input:
        for t in rts:
            one_test = [s, t, r, assess_response(s, t, r)]
            testing_list.append(one_test)
for t in testing_list:
    print t

print "opening nback_testing_results.csv"
outfile = open('nback_testing_results.csv', 'w')
# write headers
outfile.write('stimulus code,rt,user input,test result\n')
# write tests
for t in testing_list:
    line = str(t)
    line = line.strip('[')
    line = line.rstrip(']')
    line = line.strip("'")
    line = line.replace(" '", " ")
    line = line.replace(" ", "")
    line += '\n'
    # print "writing line =", line
    outfile.write(line)
outfile.close()


