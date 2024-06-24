provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0e1d06225679bc1c5"
  instance_type = "t2.micro"

  tags = {
    Name = "DiscountAPI"
  }
}

resource "aws_db_instance" "mysql" {
  allocated_storage    = 20
  engine               = "mysql"
  instance_class       = "db.m5d.large"
  db_name              = "discount_db"
  username             = "mysql_user"
  password             = "mysql_password"
  parameter_group_name = "default.mysql8.0"
}

output "app_server_ip" {
  value = aws_instance.app_server.public_ip
}
