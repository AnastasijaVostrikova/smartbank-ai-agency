function sendDailyReport() {

  const recipient =
    "vos.anastasija@gmail.com";

  const subject =
    "SmartBank AI Agency Daily Report";

  const body =
`
Daily Banking Operations Summary

Completed Tasks: 42

Onboarding:
12 customers assisted

Product Recommendations:
19 offers created

Fraud Monitoring:
3 alerts reviewed

Loan Services:
8 applications checked

Customer Support:
15 tickets processed

Customer Retention:
5 churn-risk customers identified

Generated automatically by Project Manager AI
`;

  GmailApp.sendEmail(
    recipient,
    subject,
    body
  );
}