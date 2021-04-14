const clickBtn = {
  input: document.querySelector("[data-input]"),
  input1: document.querySelector("[data-input1]"),
  input2: document.querySelector("[data-input2]"),
  input3: document.querySelector("[data-input3]"),
  input4: document.querySelector("[data-input4]"),
  input5: document.querySelector("[data-input5]"),
  input6: document.querySelector("[data-input6]"),

  clickActive() {
    this.input.value = Number(this.input.value) + 1;
  },
  clickActive1() {
    this.input1.value = Number(this.input1.value) + 1;
  },
  clickActive2() {
    this.input2.value = Number(this.input2.value) + 1;
  },
  clickActive3() {
    this.input3.value = Number(this.input3.value) + 1;
  },
  clickActive4() {
    this.input4.value = Number(this.input4.value) + 1;
  },
  clickActive5() {
    this.input5.value = Number(this.input5.value) + 1;
  },
  clickActive6() {
    this.input5.value = Number(this.input5.value) + 1;
  },
};
