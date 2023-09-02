# Generic views

1. ListAPIView\
   Widok używany jedynie do `odczytu kolekcji instancji` modelu\
   Obsługiwane metody: **GET**
2. CreateAPIView\
   Widok używany jedynie do `tworzenia instancji` modelu\
   Obsługiwane metody: **POST**
3. RetrieveAPIView\
   Widok używany jedynie do `odczytu pojedynczej instancji` modelu\
   Obsługiwane metody: **GET**
4. DestroyAPIView\
   Widok używany jedynie do `usuwania pojedynczej instancji` modelu\
   Obsługiwane metody: **DELETE**
5. UpdateAPIView\
   Widok używany jedynie do `aktualizacji pojedynczej instancji` modelu\
   Obsługiwane metody: **PUT**, **PATCH**
6. ListCreateAPIView\
   Widok używany do `tworzenia lub odczytu kolekcji instancji` modelu\
   Obsługiwane metody: **POST**, **GET**
7. RetrieveUpdateAPIView\
   Widok używany do `odczytu lub aktualizacji pojedynczej instancji` modelu\
   Obsługiwane metody: **GET**, **PUT**, **PATCH**
8. RetrieveDestroyAPIView\
   Widok używany do `odczytu lub usunięcia pojedynczej instancji` modelu\
   Obsługiwane metody: **GET**, **DELETE**
9. RetrieveUpdateDestroyAPIView\
   Widok używany do `odczytu lub aktualizacji lub usunięcia pojedynczej instancji` modelu\
   Obsługiwane metody: **GET**, **PUT**, **PATCH**, **DELETE**