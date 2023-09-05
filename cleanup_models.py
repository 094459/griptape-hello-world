# create a python function that takes in a parameter and then iteratively deletes the first 50 sagemaker models using that parameter as a search string
import boto3
def delete_sagemaker_models(model_name_prefix):
    sagemaker_client = boto3.client('sagemaker')

    # get all models that start with the model_name_prefix
    models = sagemaker_client.list_models(
        NameContains=model_name_prefix,
        SortBy='CreationTime',
        SortOrder='Descending'
    )

    # delete the first 50 models
    for model in models['Models'][:50]:
        sagemaker_client.delete_model(ModelName=model['ModelName'])
        print(f"Deleted model {model['ModelName']}")

delete_sagemaker_models('huggingface-pytorch-tgi-inference')

