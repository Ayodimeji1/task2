from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.serializers import Serializer




class SlackdetailView(APIView):
    slack_details = {"slackUsername": "ayodimejia1", "backend": True, "age": 33, "bio":"a self-taught backend developer"}

    def get(self, request):
        slack_details = {"slackUsername": "Lee", "backend": True, "age": 33, "bio":"a self-taught backend developer"}
        #json_slackdeet = json.dumps(slack_details, safe=False)
        return Response(slack_details)
    def post(self, request):
    
            data = request.data

            operation_type = data['operation_type']
            integer1 = int(data['x'])
            integer2 = int(data['y'])

            if operation_type in ['addition', 'add', 'plus', '+', 'sum']:
                result = integer1+integer2

            elif operation_type in ['subtraction', 'minus','-' ]:
                result = integer1-integer2
            
            elif operation_type in ['multiplication', 'times', 'multiply', '*' ]:
                result = integer1*integer2
             
            else:
                 operation_type = "invalid operation type"
                

            computed_data = {
                "slackUsername":"ayodimejia1",
                "operation_type": operation_type,
                "result": result
                
            }
            return Response(computed_data, status=status.HTTP_200_OK)



        
