// Uji daftar aplikasi: node test_apps.js
var apps = require("./apps.js"), assert = require("assert");
var ids = {};
assert.ok(apps.length >= 5, "minimal 5 aplikasi");
apps.forEach(function (a) {
  ["id", "name", "desc", "icon", "url"].forEach(function (k) { assert.ok(a[k], a.id + " tanpa " + k); });
  assert.ok(/^https:\/\/sailor-90\.github\.io\/[a-z0-9-]+\/$/.test(a.url), "URL tidak valid: " + a.url);
  assert.ok(!ids[a.id], "id kembar: " + a.id); ids[a.id] = 1;
});
console.log("OK: " + apps.length + " aplikasi");
