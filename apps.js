// Daftar aplikasi di dalam TITANIA. url = alamat aplikasi asli (TITANIA hanya pintasan, tanpa salinan kode). Tambah aplikasi baru cukup menambah satu baris di sini.
var TITANIA_APPS = [
  { id: "loadicator", name: "Loadicator", desc: "Muatan dan stabilitas", icon: "scale", url: "https://sailor-90.github.io/titania-loadicator/" },
  { id: "passage-plan", name: "Passage Plan", desc: "Rencana pelayaran", icon: "route", url: "https://sailor-90.github.io/singapore-passage-plan/" },
  { id: "compass-error", name: "Compass Error", desc: "Salah kompas", icon: "compass", url: "https://sailor-90.github.io/compass-error/" },
  { id: "weekly-report", name: "Weekly Report", desc: "Laporan mingguan", icon: "report", url: "https://sailor-90.github.io/fieldlog/" },
  { id: "pmn", name: "PMN", desc: "Notice pelabuhan", icon: "pin", url: "https://sailor-90.github.io/pmn-plotter-app/" }
];
if (typeof module !== "undefined") module.exports = TITANIA_APPS;
