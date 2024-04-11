#!/usr/bin/node

const argv = process.argv.slice(2);
let n = argv[0];

if (n === undefined)
{
        console.log("Missing number of occurrences");
}
else
{
        n = Number(n);
        for (let i = 0; i < n; i++)
        {
                console.log("C is fun");
        }
}
