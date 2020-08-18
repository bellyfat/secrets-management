# Secrets Management Utility

This project can be pip installed into other projects as a Python package to have access to the secrets management classes and helpers for integrating AWS Secrets Manager.

## Adding into a project

### Requirements

The project assumes that the parent repo already has access to the following Python packages:
- [aws-secretsmanager-caching](https://pypi.org/project/aws-secretsmanager-caching/)
- [boto3](https://pypi.org/project/boto3/)
- [django-environ](https://pypi.org/project/django-environ/)

### Steps

You can `pip` install it manually via `pip install git+https://github.com/Beauhurst/secrets-management.git`

Or add `git+https://github.com/Beauhurst/secrets-management.git` to your `requirements.txt` file.

## Usage

Simple example:

```python
from secrets_management import SecretsManager

secrets_manager = SecretsManager(region_name="eu-west-2")
secret = secrets_manager.retrieve_secret("name/of/secret")

SOME_API_KEY = secret.get("SOME_API_KEY")
ANOTHER_API_KEY = secret.get("ANOTHER_API_KEY", default="a-sensible-default")
```

If you want to enable falling back on a local `.env` file:

```python
env = environ.Env()
secrets_manager = SecretsManager(region_name="eu-west-2")
secret = secrets_manager.retrieve_secret("name/of/secret")
secret.set_fallback_env(env)

# will try and access `SOME_API_KEY` from environment file if not found in secret
SOME_API_KEY = secret.get("SOME_API_KEY", allow_env_fallback=True)

# will try and access `ANOTHER_API_KEY` from environment file if not found in secret
# if not in the environment file, then use the `default` value
ANOTHER_API_KEY = secret.get("ANOTHER_API_KEY", allow_env_fallback=True, default="a-sensible-default")
```

Ideally, you should combine both approaches and read the secret name and the corresponding region from an env file to avoid hardcoding this in your settings.

