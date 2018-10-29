"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
var length = function length(value, option) {
  var min = option.min,
      max = option.max;

  return min <= value.length && value.length <= max;
};

var isAlphanumeric = function isAlphanumeric(value) {
  return value.match(/^[a-z0-9]+$/i) !== null;
};

var mustContainUpperCase = function mustContainUpperCase(value) {
  return value.match(/[A-Z]/) !== null;
};

var isEmail = function isEmail(value) {
  var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(value);
};

var isURL = function isURL(value) {
  var re = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([/\w .-]*)*\/?$/;
  return re.test(value);
};

exports.length = length;
exports.isAlphanumeric = isAlphanumeric;
exports.mustContainUpperCase = mustContainUpperCase;
exports.isEmail = isEmail;
exports.isURL = isURL;