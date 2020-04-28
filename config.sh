#!/bin/bash


environment_name="demoevhub"
location="westeurope"
resource_group=$environment_name"rg"

eventhub_namespace_name=$environment_name"namespace"
eventhub_name=$environment_name"oneeventhub"
eventhub_namespace_key_name="RootManageSharedAccessKey"

log_analytics_workspace=$environment_name"loganalytics"
