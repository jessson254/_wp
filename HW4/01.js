unction countLetters(str) {
  const map = new Map();

  for (const char of str) {
    if (/[a-zA-Z]/.test(char)) {
      const lowerChar = char.toLowerCase(); // 忽略大小寫
      map.set(lowerChar, (map.get(lowerChar) || 0) + 1);
    }
  }

  return map;
}
const result = countLetters("Hello World!");
console.log(result);
for (const [letter, count] of result) {
  console.log(`${letter}: ${count}`);
}
