import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secrets-management",
    version="0.0.4",
    author="Beauhurst",
    author_email="noreply@beauhurst.com",
    description="Helper library for interacting with AWS Secrets Manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beauhurst/secrets-management",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["aws-secretsmanager-caching", "boto3", "django-environ"],
)
