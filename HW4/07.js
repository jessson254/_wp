class Vector {
  constructor(components) {
    this.components = components;
  }

  add(other) {
    this.#validateSameDimension(other);
    const result = this.components.map((val, i) => val + other.components[i]);
    return new Vector(result);
  }

  subtract(other) {
    this.#validateSameDimension(other);
    const result = this.components.map((val, i) => val - other.components[i]);
    return new Vector(result);
  }

  dot(other) {
    this.#validateSameDimension(other);
    return this.components.reduce((sum, val, i) => sum + val * other.components[i], 0);
  }

  toString() {
    return `Vector(${this.components.join(', ')})`;
  }
