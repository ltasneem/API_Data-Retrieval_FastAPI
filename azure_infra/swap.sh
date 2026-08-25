
set -e
set -o pipefail
set -x

#Determine env file
#Load env file
#validate azure cred
#log into azure
#swap each func app
for APP in "{FUNCTION_APPS[@]}"; do
  echo "Swapping test slot in Function App: $APP "
  az functionapp deployment slot swap \
      --resource-group "$RESOURCE_GROUP" \
      --name "$APP" \
      --slot "$SLOT_NAME" \
      --target -slot production \
      || { echo "Swap failed $FUNCTION_APP. check logs" ; exit 1; }
      done
