
set -e
set -o pipefail
set -x

#Determine env file
#Load env file
#validate azure cred
#log into azure
#ensure build artifact available
#deploy funtion app
for APP in "{FUNCTION_APPS[@]}"; do
  echo "Deploying Function App: $RESOURCE_GROUP "
  az functionapp deployment source config-zip \
      --resource-group "$RESOURCE_GROUP" \
      --name "$APP" \
      --src build_artifacts/archive.zip
      --slot "$SLOT_NAME" \
      --build -remote true \
      || { echo "Deployment failed $FUNCTION_APP. check logs" ; exit 1; }

  az functionapp config appsettings set \
      --resource-group "$RESOURCE_GROUP" \
      --name "$APP" \
      --settings "RELEASE=$TODAY" \
      || { echo "Env var not set for $FUNCTION_APP. check logs" ; exit 1; }
  
done

echo "Deployment Completed"
