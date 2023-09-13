import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // Call the constructor of the parent class
    this._floors = floors;
  }

  // getter and setter sqft
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }

  // getter and setter floor
  get floors() {
    return this._floors;
  }

  set floors(value) {
    this._floors = value;
  }

  // Override the evacuationWarningMessage method
  evacuationWarningMessage() {
    return `Evacuate slowly ${this._floors} floors`;
  }
}
