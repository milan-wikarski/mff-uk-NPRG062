const minIndex = arr => {
  let min = arr[0];
  let index = 0;

  for (let i = 1; i < arr.length; i++) {
    if (min > arr[i]) {
      min = arr[i];
      index = i;
    }
  }

  return index;
};

const median = arr => {
  arr = JSON.parse(JSON.stringify(arr));

  const arr1 = arr.slice(0, Math.floor(arr.length / 2) + 1);
  const arr2 = arr.slice(
    Math.floor(arr.length / 2) + 1,
    Math.floor(arr.length)
  );

  while (arr2.length) {
    const element = arr2.pop();
    const i = minIndex(arr1);

    // console.log(element, i, arr1[i]);

    if (arr1[i] < element) {
      arr1[i] = element;
    }
  }

  return arr1[minIndex(arr1)];
};

const SAMPLES = 10;
const SAMPLE_SIZE = 5;
const MAX_VALUE = 10;

const results = [];

const mid = arr => arr.sort((a, b) => a - b)[1];

for (let i = 0; i < SAMPLES; i++) {
  let sample = [];

  for (let j = 0; j < SAMPLE_SIZE; j++) {
    sample.push(Math.floor(Math.random() * (MAX_VALUE - 1)) + 1);
  }

  console.log(sample);

  continue;

  const med = median(sample);
  sample = sample.sort((a, b) => a - b);

  results.push(med == sample[2]);
}

// console.log(results.every(item => Boolean(item)));
