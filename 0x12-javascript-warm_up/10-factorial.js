#!/usr/bin/node

function factorial (fact, num) {
  if (isNaN(num)) {
    console.log(1);
  } else if (num === 1) {
    console.log(fact);
  } else {
    factorial(fact * num, num - 1);
  }
}

const num = parseInt(process.argv[2]);
factorial(1, num);
