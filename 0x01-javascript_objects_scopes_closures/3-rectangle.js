#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== 0 && h !== 0) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let hei = 0; hei < this.height; hei++) {
      let result = '';
      for (let wid = 0; wid < this.width; wid++) {
        result += 'X';
      }
      console.log(result);
    }
  }
};