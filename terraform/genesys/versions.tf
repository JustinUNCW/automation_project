terraform {
  required_version = ">= 1.5.0"

  required_providers {
    genesyscloud = {
      source  = "mypurecloud/genesyscloud"
      version = "1.86.1"
    }
  }
}