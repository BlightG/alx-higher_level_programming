#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
        let element_count = 0;
        for (let i = 0 ; i < list.length ; i++){
                if (list[i] === searchElement) {
                        element_count += 1;
                } 
        }
        return element_count;
}