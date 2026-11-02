function logAgentActivity(agent, task, status) {

  const sheet =
    SpreadsheetApp
      .openById("YOUR_SPREADSHEET_ID")
      .getSheetByName("SmartBank_Log");

  sheet.appendRow([
    new Date(),
    agent,
    task,
    status
  ]);
}