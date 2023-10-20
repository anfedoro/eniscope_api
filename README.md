## Eniscope API

Best.Enegry Eniscope Analytic API access framework, which defines EniscopeAPIClient class with such functions as
 - API Authenticaton. Uses keyrings package to store sensitive authentication/authorization information as such as 
   encryption_key = b"XXXXXXXXXXXXXXXXXX"
   api_key = "xxxxxxxxxxxxxxxx"
   encrypted username:MD5_password for HTTP Basic authorization.
 - base GET and OPTION requests
 - API user details request
 - get organizations list
 - get list of data channels belong to organization or multiple organizations
 - get channel historical data (aka readings) for specific channel, date range, list fo metering parameters and resolution
 - get multiple channels and data ranges fo historical data simultaniously. Rely on ThreadPoolExecutor and http pooling for better performance.
 - get list of alarms related to arganization and their settings (rules and periods)
 - get alarm event list for requested organizations and data ranges


