#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;

  list.forEach(item => {
    if (item === searchElement) {
      occurrences += 1;
    }
  });
  return occurrences;
};
