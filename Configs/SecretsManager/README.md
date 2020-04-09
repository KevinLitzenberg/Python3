A simple module for managing certain string secrets, API keys, and passwords.

Current version 0.0.1

Sample useage:
```python
  # Create the manager object
  PasswordManager = configManager("secrets.cfg")

  PasswordManager.get_sections()
  PasswordManager.print_sections()
  PasswordManager.add_section("data")
  PasswordManager.set_config_key("data","secret_data","supersecret")
  PasswordManager.print_sections()
  PasswordManager.print_config_key("data","supersecret")
  PasswordManager.save_config_file()

  # tweepy api
  twitter_keys = {
    'consumer_key':        PasswordManager.get_config_value("keys","consumer_key"),
    'consumer_secret':     PasswordManager.get_config_value("keys","consumer_secret"),
    'access_token_key':    PasswordManager.get_config_value("tokens","access_token"),
    'access_token_secret': PasswordManager.get_config_value("tokens","access_token_secret")
  }

```


Expects a file named "secrets.cfg" with the following format.
Also see the example "secrets.cfg" file in this repo.

```python
[keys]
consumer_key = some_consumer_key
consumer_secret = some_secret_key

[tokens]
access_token = some_access_token
access_token_secret = some_access_secret_token
```

Methods: 
  Arguments:
    config_file: String local file containing the secrets (see above)
    key: String the name of the variable in the local secrets file
    section: String the section of the secrets file i.e. [section]
    value: String that updates/adds the value in [section]


  
    Includes methods for updating key values and adding sections.  If changes are made using these methods ensure the values are persistant by calling "save_config_file."
