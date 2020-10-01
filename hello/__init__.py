import azure.functions as func

def main(request):
    return func.HttpResponse("Hello!")
