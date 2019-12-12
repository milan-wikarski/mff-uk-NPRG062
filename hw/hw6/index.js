Object.defineProperty(Array.prototype, "swap", {
  value: function(a, b) {
    const temp = this[a];
    this[a] = this[b];
    this[b] = temp;

    return this;
  }
});

class State {
  constructor(items, size, gap, moves, parent = null) {
    this.items = items;
    this.size = size;
    this.gap = gap;
    this.moves = moves;

    this.parent = parent;

    this.key = this.items.join("_");
  }

  print() {
    for (let i = 0; i < this.size; i++) {
      const row = [];

      for (let j = 0; j < this.size; j++) {
        row.push(this.items[i * this.size + j]);
      }

      console.log(row.join(" "));
    }

    console.log();
  }

  printHistory(maxRowLength = 40) {
    const rows = Array.from({ length: this.size }, () => []);
    let rowLength = 0;
    let rowOffset = 0;

    let state = this;
    while (state != null) {
      for (let i = 0; i < state.size; i++) {
        for (let j = 0; j < state.size; j++) {
          rows[i + rowOffset].push(state.items[i * state.size + j]);
        }

        rows[i + rowOffset].push(" ");
      }

      rowLength += state.size * 2 + 1;
      if (rowLength > maxRowLength) {
        rowLength = 0;
        rowOffset += state.size + 1;

        for (let i = 0; i < state.size + 1; i++) {
          rows.push([]);
        }
      }

      state = state.parent;
    }

    return rows.map(row => row.join(" ")).join("\n");
  }

  static mutate(state) {
    const states = [];

    // Top
    if (state.gap >= state.size) {
      states.push(
        new State(
          [...state.items].swap(state.gap, state.gap - state.size),
          state.size,
          state.gap - state.size,
          state.moves + 1,
          state
        )
      );
    }

    // Bottom
    if (state.gap + state.size < state.size ** 2) {
      states.push(
        new State(
          [...state.items].swap(state.gap, state.gap + state.size),
          state.size,
          state.gap + state.size,
          state.moves + 1,
          state
        )
      );
    }

    // Left
    if (state.gap % state.size != 0) {
      states.push(
        new State(
          [...state.items].swap(state.gap, state.gap - 1),
          state.size,
          state.gap - 1,
          state.moves + 1,
          state
        )
      );
    }

    // Right
    if (state.gap % state.size != state.size - 1) {
      states.push(
        new State(
          [...state.items].swap(state.gap, state.gap + 1),
          state.size,
          state.gap + 1,
          state.moves + 1,
          state
        )
      );
    }

    return states;
  }
}

class Game {
  constructor(size) {
    this.size = size;

    this.initial = new State(
      [...Array.from({ length: this.size ** 2 - 1 }, (a, i) => i + 1), 0],
      size,
      size ** 2 - 1,
      0
    );

    this.states = new Map();
    this.states.set(this.initial.key, this.initial);

    this.moves = new Map();
    this.moves.set(0, new Set([this.initial]));
  }

  explore() {
    let states = [this.initial];

    while (states.length) {
      const new_states = [];

      for (let i in states) {
        State.mutate(states[i])
          .filter(state => !this.states.has(state.key))
          .forEach(state => {
            this.states.set(state.key, state);

            if (!this.moves.has(state.moves)) {
              this.moves.set(state.moves, new Set());
            }

            this.moves.get(state.moves).add(state);

            new_states.push(state);
          });
      }

      states = new_states;
    }
  }
}

const game = new Game(3);

game.explore();

console.log("#############################################");
console.log("##    Read left to right, top to bottom    ##");
console.log("#############################################\n");

console.log(
  Array.from(game.moves.get(game.moves.size - 1))
    .map(
      (solution, index) =>
        `                 SOLUTION ${index +
          1}\n\n${solution.printHistory()}\n\nSolved in ${solution.moves} moves`
    )
    .join("\n\n---------------------------------------------\n\n")
);
