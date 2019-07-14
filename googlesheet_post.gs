// Kaggle Experiment Logger
// ------------------------
// Inspired by: https://amalog.hateblo.jp/entry/kaggle-snippets
// ------------------------
// Usage:
//     Please read Usage in googlesheet_post.py


function doPost(e) {
  if (e==null || e.postData == null || e.postData.contents == null) {
    return;
  }
  var ss = SpreadsheetApp.getActive();
  var sheet = ss.getActiveSheet();
  var data = JSON.parse(e.postData.contents);
  var timestamp = new Date();
  data.unshift(timestamp);
  sheet.appendRow(data);
}
