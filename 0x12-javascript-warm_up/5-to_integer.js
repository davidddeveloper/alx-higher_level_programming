#!/usr/bin/env node

const argv = process.argv.slice(2);

if (argv[0] === undefined)
{
        console.log("Not a number");
}
else
{
        console.log("My number:", Number(argv[0]));
}
