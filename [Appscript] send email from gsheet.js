function send_report_email(spreadsheetId) {
 
  var yesterday = new Date(new Date().getTime() - 24*60*60*1000);  // yesterday date
  var year = yesterday.getFullYear();
  var month = yesterday.getMonth()+1;
  var day = yesterday.getDate();
   
  while (month.toString().length < 2) month = "0" + month ;
  while (day.toString().length < 2) day = "0" + day ;
  var report_date = year + "-" + month + "-" + day ;
 
  var spreadsheet   = SpreadsheetApp.getActiveSpreadsheet();
  var spreadsheetId = spreadsheet.getId(); 
  var file          = DriveApp.getFileById(spreadsheetId);
  var url           = 'https://docs.google.com/spreadsheets/d/'+spreadsheetId+'/export?format=xlsx';
  var token         = ScriptApp.getOAuthToken();
  var response      = UrlFetchApp.fetch(url, {
    headers: {
      'Authorization': 'Bearer ' +  token
    }
  });
 
 var fileName = (spreadsheet.getName()) + '_' +report_date + '.xlsx';         // edit file name here
 var blobs   = [response.getBlob().setName(fileName)];
 
///////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 
 var receipient = "email1@seamoney.com,email2@seamoney.com";    // separate with comma (,) .... don't put space before or after email!
 var subject = "TEST" + '_' + report_date;           // edit email subject here
 var emailbody = "TEST  \n\ " + report_date;             // edit email body here .... can use \n\ to start new line
 var cc_list = "email3@seamoney.com";
 MailApp.sendEmail(receipient, subject, emailbody, {attachments: blobs, cc : cc_list});
  }
