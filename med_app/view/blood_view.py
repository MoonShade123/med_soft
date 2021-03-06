from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from med_app.models import Blood
from med_app.serializers import BloodSerializer


class BloodAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BloodSerializer

    def get(self, request):
        user = request.user
        blood = Blood.objects.filter(user=user)
        serializer = BloodSerializer(blood, many=True).data
        return Response(serializer)

    def post(self, request):
        user = request.user
        blood_results = request.data

        new_blood_results = Blood.objects.create(user=user)

        for key, value in blood_results.items():
            vars(new_blood_results)[key] = value
#        if blood_results['red_blood_cells'] is None:
#            return Response('You must enter red blood cells results', 404)
#
#        if blood_results['hemoglobin'] is None:
#            return Response('You must enter hemoglobin results', 404)
#
#        if blood_results['white_blood_cells'] is None:
#            return Response('You must enter white blood cells results', 404)
#
#        if blood_results['color_index'] is None:
#            return Response('You must enter color index results', 404)
#
#        if blood_results['hematocrit'] is None:
#            return Response('You must enter hematocrit results', 404)
#
#        if blood_results['reticulocytes'] is None:
#            return Response('You must enter your reticulocytes results', 404)
#
#        if blood_results['platelets'] is None:
#            return Response('You must enter platelets results', 404)
#
#        if blood_results['esr'] is None:
#            return Response('You must enter esr results', 404)

#        new_blood_results = Blood.objects.create(user=user, red_blood_cells=blood_results['red_blood_cells'],
#                                                 hemoglobin=blood_results['hemoglobin'],
#                                                 white_blood_cells=blood_results['white_blood_cells'],
#                                                 color_index=blood_results['color_index'],
#                                                 hematocrit=blood_results['hematocrit'],
#                                                 reticulocytes=blood_results['reticulocytes'],
#                                                 platelets=blood_results['platelets'],
#                                                 esr=blood_results['esr']
#                                                 )

        new_blood_results.save()

        serializer = BloodSerializer(new_blood_results).data

        return Response(serializer)

    def put(self, request):
        id = request.query_params["id"]
        user = request.user
        update_blood_results = request.data

        saved_blood_results = get_object_or_404(Blood.objects.all(), user=user, id=id)
#        for key, value in update_blood_results.items():
#            for i in saved_blood_results.__dict__:
#                if saved_blood_results[i][key] == key:
#                    saved_blood_results[i][value] = value
        if len(update_blood_results) is not 0:
            for key, value in update_blood_results.items():
                u = vars(saved_blood_results)
                u[key] = value
#            for key, value in vars(saved_blood_results).items():
#                u = update_blood_results
#                u[key] = value
        else:
            return Response(f"No data provided to update User: {user.username} blood indicators", 400)
#        if len(update_blood_results) is not 0:
#            if update_blood_results != ['red_blood_cells'] is None:
#                saved_blood_results.red_blood_cells = update_blood_results['red_blood_cells']
#            else:
#                saved_blood_results.red_blood_cells = saved_blood_results.red_blood_cells
#            if update_blood_results != ['hemoglobin'] is None:
#                saved_blood_results.hemoglobin = update_blood_results['hemoglobin']
#            else:
#                saved_blood_results.hemoglobin = saved_blood_results.hemoglobin
#            if update_blood_results != ['white_blood_cells'] is None:
#                saved_blood_results.white_blood_cells = update_blood_results['white_blood_cells']
#            else:
#                saved_blood_results.white_blood_cells = saved_blood_results.white_blood_cells
#            if update_blood_results != ['color_index'] is None:
#                saved_blood_results.color_index = update_blood_results['color_index']
#            else:
#                saved_blood_results.color_index = saved_blood_results.color_index
#            if update_blood_results != ['hematocrit'] is None:
#                saved_blood_results.hematocrit = update_blood_results['hematocrit']
#            else:
#                saved_blood_results.hematocrit = saved_blood_results.hematocrit
#            if update_blood_results != ['reticulocytes'] is None:
#                saved_blood_results.reticulocytes = update_blood_results['reticulocytes']
#            else:
#                saved_blood_results.reticulocytes = saved_blood_results.reticulocytes
#            if update_blood_results != ['platelets'] is None:
#                saved_blood_results.platelets = update_blood_results['platelets']
#            else:
#                saved_blood_results.platelets = saved_blood_results.platelets
#            if update_blood_results != ['esr'] is None:
#                saved_blood_results.esr = update_blood_results['esr']
#            else:
#                saved_blood_results.esr = saved_blood_results.esr
#        else:
#            return Response("No data provided", 400)
        saved_blood_results.save()

        serializer = BloodSerializer(saved_blood_results)

        return Response({f"User {user.username} update blood results with Id:{saved_blood_results.id} successfully":
                        serializer.data})

    def delete(self, request):
        id = request.query_params["id"]
        delete_blood_result = get_object_or_404(Blood.objects.all(), id=id)

        delete_blood_result.delete()

        return Response(f"Blood results with Id:{id} deleted successfully")
