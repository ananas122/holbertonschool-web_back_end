export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Define a method to return the size when cast into a Number.
  valueOf() {
    return this._size;
  }

  // Define a method to return the location when cast into a String.
  toString() {
    return this._location;
  }
}
