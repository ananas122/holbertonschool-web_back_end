import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  // Getter et setter pour `amount`
  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (typeof newAmount === 'number') {
      this._amount = newAmount;
    } else {
      throw new TypeError('amount must be a number');
    }
  }

  // Getter et setter pour `currency`
  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (newCurrency instanceof Currency) {
      this._currency = newCurrency;
    } else {
      throw new TypeError('Currency must be a Currency');
    }
  }

  // Méthode
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Méthode statique
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
