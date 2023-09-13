export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Methode
  cloneCar() {
    // Crée une nouvelle instance de la même classe avec les mêmes valeurs
    return new this.constructor(this._brand, this._motor, this._color);
  }
}
