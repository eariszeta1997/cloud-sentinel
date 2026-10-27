terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

# Simulazione di provisioning di un nodo server cloud (EC2)
resource "aws_instance" "sentinel_node" {
  ami           = "ami-0abcdef1234567890" # Identificativo fittizio per il PoC
  instance_type = "t3.micro"

  tags = {
    Name        = "CloudSentinel-Node"
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}