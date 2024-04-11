#!/usr/bin/node

let length_of_argv = process.argv.length;
let result;
if (length_of_argv < 3)
{
	result = "No argument";
}
else if (length_of_argv === 3)
{
	result = "Argument found";
}
else
{
	result = "Arguments found";
}
console.log(result);
