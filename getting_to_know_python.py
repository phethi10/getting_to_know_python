function_count = 0
function_dict = {}
function_name =[]
start = []
end = []


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
                #path_to_js_file = open
                if "function" in line and "}" in line:
                end.append(counter)              
                f.close()
                equals_index = function_name.index("=")
                if equals_index != -1:
                   function_name.remove("=")
                return [start,function_name,end]
x = list_all_js_function_names("/home/recruit/get_to_know_python/Untitled-123.py")

start = x[0]
names = x[1]

output = {}
output_ls = []

for i, num in enumerate(start):
    output = {"name": names[i], "start": num}
    output_ls.append(output)

print(output_ls)
f.close()
