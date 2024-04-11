#!/usr/bin/node

const argv = process.argv.slice(2);
let arg_one = Number(argv[1]);

if (argv.length === 1 || argv[0] === undefined)
{
        console.log(0);
}

else
{
        let biggest = Number(argv[0]);
        for (let i = 1; i < argv.length; i++)
        {
                let value = Number(argv[i]);
                if (biggest < value)
                {
                        biggest = value;
                }
        }

        let secondBiggest = Number(argv[0]);
        for (let i = 1; i < argv.length; i++)
        {
                let value = Number(argv[i]);
                if (value < biggest && secondBiggest < value)
                {
                        secondBiggest = value;
                }
        }
        console.log(secondBiggest);
}
~
