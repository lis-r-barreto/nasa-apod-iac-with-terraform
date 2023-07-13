# APOD Data Pipeline 

This project showcases a simple data pipeline for extracting, transforming, and loading data from the NASA APOD (Astronomy Picture of the Day) API using PySpark and AWS S3.

## Description

The APOD Data Pipeline project demonstrates the process of collecting daily data from the NASA APOD API, performing data transformations using PySpark, and storing the processed data in AWS S3 for further analysis or consumption.

The pipeline consists of the following steps:
1. Data extraction: Daily data is collected from the NASA APOD API using the provided PySpark code.
2. Data transformation: The extracted data is transformed using PySpark to a desired format or structure.
3. Data loading: The transformed data is stored in AWS S3 for future access and analysis.

The project also includes the necessary setup and configuration files for deploying the data pipeline using Terraform and automating the workflow using GitHub Actions.

## Prerequisites

Before running the data pipeline, ensure that you have the following prerequisites in place:
- Python installed
- Poetry installed (to manage project dependencies)
- AWS account and access credentials
- Terraform installed (for infrastructure provisioning)
- Configured `.env` file or environment variables with required credentials

## Getting Started

To get started with the APOD Data Pipeline, follow these steps:

1. Clone this repository: `git clone <repository-url>`
2. Install project dependencies using Poetry: `poetry install`
3. Configure the necessary environment variables or `.env` file with your AWS credentials and API key for the NASA APOD API.
4. Modify the configuration files (`terraform.tfvars` and `main.tf`) to customize the AWS resources and settings, if needed.
5. Provision the required AWS resources using Terraform: `terraform init` and `terraform apply`
6. Execute the data pipeline by running the PySpark script: `poetry run python extract.py` (for data extraction) and `poetry run python transform.py` (for data transformation).
7. Check the output and verify that the data has been successfully loaded into AWS S3.

## Contributing

Contributions to the APOD Data Pipeline project are welcome! If you encounter any issues, have suggestions, or want to contribute improvements, please create an issue or submit a pull request.

## License

The APOD Data Pipeline project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

## Acknowledgments

This project was created as a sample project to showcase the capabilities of PySpark and AWS S3 for building data pipelines. Special thanks to the contributors and the open-source community for their valuable contributions and support.

## Resources

- [NASA APOD API Documentation](https://api.nasa.gov/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/index.html)
- [Terraform Documentation](https://www.terraform.io/docs/)
- [Poetry Documentation](https://python-poetry.org/docs/)

Feel free to update the README with more detailed information, project-specific instructions, or additional sections as needed.