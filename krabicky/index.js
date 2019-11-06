const removeFirst = (arr, toRemove) => {
  const newArr = [];
  let removed = false;

  for (let i = 0; i < arr.length; i++) {
    if (removed || arr[i] != toRemove) {
      newArr.push(arr[i]);
    } else {
      removed = true;
    }
  }

  return newArr;
};

const unique = arr => Array.from(new Set(arr));

const run = (options, target, nums, operators, history = []) => {
  unique(operators).forEach(operator => {
    for (let i = 0; i < nums.length; i++) {
      for (let j = i; j < nums.length; j++) {
        const num1 = Math.min(nums[i], nums[j]);
        const num2 = Math.max(nums[i], nums[j]);

        const exp = [num1, num2].join(operator);
        const val = eval(exp);

        const newNums = [...nums, val];
        const newOperators = removeFirst(operators, operator);
        const newHistory = [...history, [exp + ' = ' + val]];

        if (newNums.includes(target)) {
          if (!options.hasOwnProperty(exp)) {
            options[exp] = [];
          }

          options[exp].push(newHistory);
        } else {
          run(options, target, newNums, newOperators, newHistory);
        }
      }
    }
  });

  return options;
};

const options = {};
run(options, 102, [3, 11], ['+', '+', '*', '*']);

Object.entries(options).forEach(([exp, combinations]) => {
  const min = combinations.reduce(
    (min, item) => Math.min(min, item.length),
    Infinity
  );

  // Remove all combinations with an arbitrary operation
  options[exp] = combinations
    .filter(item => item.length == min)
    .map(item => item.join(' | '));
});

console.log(options);
