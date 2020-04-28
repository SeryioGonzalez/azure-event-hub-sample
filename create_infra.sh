#!/bin/bash

source config.sh

az group create --name $resource_group --location $location

echo "CREATING AZURE MONITOR LOG ANALYTICS"
#MONITOR_LOG_ANALYTICS_NAMESPACE_ID=$(az monitor log-analytics workspace create --resource-group $resource_group --workspace-name $log_analytics_workspace --query "id" -o tsv)

echo "CREATING EVENTHUB NAMESPACE"
#EVENT_HUB_NAMESPACE_ID=$(az eventhubs namespace create --resource-group $resource_group --name $eventhub_namespace_name  --query "id" -o tsv)

echo "CREATING EVENTHUB IN NAMESPACE"
#az eventhubs eventhub create --resource-group $resource_group --namespace-name $eventhub_namespace_name --name $eventhub_name

echo "LINKING EVENT HUB TO LOG ANALYTICS"
#az monitor diagnostic-settings create -n "event-hub-logs" --resource $EVENT_HUB_NAMESPACE_ID --workspace $MONITOR_LOG_ANALYTICS_NAMESPACE_ID \
#--metrics '[
#      {
#        "enabled": true,
#        "retentionPolicy": {
#          "days": 0,
#          "enabled": false
#        },
#        "category": "AllMetrics"
#      }
#    ]'


EVENT_HUB_KEY=$(az eventhubs namespace authorization-rule keys list -g $resource_group --namespace-name $eventhub_namespace_name -n $eventhub_namespace_key_name --query "primaryKey" -o tsv)
EVENT_HUB_URL="amqps://$eventhub_namespace_name.servicebus.windows.net/$eventhub_name"

echo "Exporting key variables for python scripts to work"
echo "export EVENT_HUB_KEY=$EVENT_HUB_KEY"
echo "export EVENT_HUB_URL=$EVENT_HUB_URL"

