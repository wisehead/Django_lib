#1.BookingDetailAPIView

```
BookingDetailAPIView.update
--instance = self.get_object()
----GenericAPIView.get_object
--serializer = self.get_serializer(instance, data=request.data, partial=partial)
--serializer.is_valid(raise_exception=True)
--self.perform_update(serializer)
----BookingSerializer.save
```