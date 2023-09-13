
SOCIAL_AUTH_GLOBUS_KEY = ""
SOCIAL_AUTH_GLOBUS_SECRET = ""

if not SOCIAL_AUTH_GLOBUS_KEY or not SOCIAL_AUTH_GLOBUS_SECRET:
    print("WARNING: Globus App credentials have not been configured, login will not work. "
          "Please go to the following link and add your credentials in local_settings.py:\n\t"
          "https://app.globus.org/settings/developers/registration/confidential_client/select-project")