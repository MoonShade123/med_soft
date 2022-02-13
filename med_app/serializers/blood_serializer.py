from rest_framework import serializers

from med_app.models import Blood


class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = ('user', 'red_blood_cells', 'hemoglobin', 'white_blood_cells', 'color_index', 'hematocrit',
                  'reticulocytes', 'platelets', 'esr')
