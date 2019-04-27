
output = open("output.txt")
output_try = open("output_try.txt")


output_lines = output.readlines()
output_try_lines = output_try.readlines()


line = 0

amount = 0

test = 0
begin = True
success = True

for line in range(len(output_lines)):
    if amount == 0:
        if begin:
            begin = False
        else:
            print("Success on test ", test)
        test += 1
        #print("line ", line)
        #print(output_lines[line])

        amount = int(output_lines[line][:-1]) * 2

        print("Running test ", test)
    else:
        #print(output_lines[line][:-1] , output_try_lines[line][:-1])
        v1 = float(output_lines[line][:-1])
        v2 = float(output_try_lines[line][:-1])
        if abs(v1-v2) > 1:
            print("Error on test case ", test)
            print("Expected: ", v1)
            print("Received: ", v2)
            success = False
            break

        amount -= 1

if success:
    print("Success on test ",test)
    print("Sucess on all tests")



