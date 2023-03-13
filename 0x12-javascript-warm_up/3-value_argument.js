#!/usr/bin/node
let i = 2;
if (!process.argv[i])
    console.log('No argument');

while (process.argv[i])
{
    console.log(process.argv[i]);
    i++;
}
