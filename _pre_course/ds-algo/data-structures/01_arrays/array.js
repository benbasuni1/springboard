class DynamicArray {

  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  set(index, value) {
    this.data[index] = value;
  }

  insertAt(item, index) {
    for (let i = this.length; i >= index; i--) {
      this.data[i] = this.data[i - 1];
    }

    this.data[index] = item;
    this.length++;
    return this.data;
  }

  delete() {
    for(let i = index; i < this.length - 1; i++){
      this.data[i]=this.data[i+1];
    }

    delete this.data[this.length-1];
    this.length--;
    return this.data; 
  }

  isEmpty() {
    return this.length === 0;
  }

  contains(value) {
    for (let i = 0; i <= this.length - 1; i++) {
      let current = this.data[i];
      if (current === value) return true;

      return false;
    }
  }
}

