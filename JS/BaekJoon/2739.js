const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  console.log("input: ", line);
  rl.close();
});

rl.on("close", () => {
  process.exit();
});

let dan = rl;
for (let i = 1; i < 10; i++) {
  console.log(dan, "*", i, "=", dan * i);
}
