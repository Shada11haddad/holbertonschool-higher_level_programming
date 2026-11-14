#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const nums = args.map(Number).sort((a, b) => b - a);
  console.log(nums[1]);
}
