provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "datalake" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
  bucket = aws_s3_bucket.datalake.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_object" "nasa_apod_data" {
  bucket = aws_s3_bucket.datalake.id
  key    = var.file_name

  source = var.file_path
  etag   = filemd5(var.file_path)
}
