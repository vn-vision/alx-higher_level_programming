#!/usr/bin/node
// returns number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  const l = list.length;
  let nb = 0;

  for (let i = 0; i < l; i++) {
    if (list[i] === searchElement) {
      nb++;
    }
  }
  return nb;
};
