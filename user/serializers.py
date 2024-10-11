from rest_framework import serializers


class UserTransactionSerializer(serializers.Serializer):
    start_date = serializers.CharField()
    end_date = serializers.CharField()


    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if start_date > end_date:
            raise serializers.ValidationError('Start date needs to be earlier than end date.')
        return {'start_date': start_date, 'end_date': end_date}
