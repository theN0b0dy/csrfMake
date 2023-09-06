

action_url = input("Enter the action url for your form : ")
form_id = input("Enter Form id (default: form) : ")
if form_id == "":
    form_id = "form"
method = input("Enter the Method (GET,POST,PUT,DELET, ... default:POST ) : ")
if method == "":
    method = "POST"
script = input("Enter your script(defualt:[just submit the form] : ")
if script == "":
    script = f"<script>document.getElementById('{form_id}').submit();</script>"

form_inputs = {}
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
    form_inputs[i] = {
            "name": form_input,
            "value": form_input_value,
            "id": form_input_id,
            "type": form_input_type,
    } 

print("the inputs are : ", form_inputs)
print("the script is : ", script)





