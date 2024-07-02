from random import randint

def repeat(x, y):

    rand_dict = {}
    iteration = 0
    while True:
        iteration += 1
        gen_int = randint(x, y)

        if len(rand_dict) == 0:
            rand_dict[iteration] = gen_int
        else:
            for x in range(len(rand_dict)):
                if gen_int == rand_dict[x + 1]:
                    output_tuple = ([rand_dict[x + 1] for x in range(len(rand_dict))], iteration)
                    return output_tuple
                else:
                    rand_dict[iteration] = gen_int  # same as above

print(repeat(10,100))