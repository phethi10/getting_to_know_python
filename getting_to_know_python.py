function_count = 0
function_dict = {}
function_name =[]

f = open("information.js")
for line in f:

    if "function" in line:
        function = line.split(" ")
        print(function)

        if 'function' in function[0]:
            name = function[1].split("(")
            function_dict['name'] = function_name
            print(function_dict)

            if 'function' in function[2]:
                function_call = function[0]
                function_dict['name'] = function_call
                print(function_dict)
f.close()
