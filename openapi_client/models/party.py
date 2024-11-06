# coding: utf-8

"""
    weclapp API

    # Getting Started   API Version: **[v1](v1.html)**   The weclapp REST API lets you integrate weclapp with other applications or services.  The specification for this version can be downloaded here:  | Format                          | Public                                                                           | |---------------------------------|----------------------------------------------------------------------------------| | swagger JSON                    | <a href=\"swagger.json\" download=\"weclapp-swagger.json\">Download</a> | | OpenApi 3 JSON                  | <a href=\"openapi_v1.json\" download=\"weclapp-openapi.json\">Download</a> | | OpenApi 3 YAML (with user docs) | <a href=\"openapi_v1.yaml\" download=\"weclapp-openapi.yaml\">Download</a> |    ## What should I know before starting?  Our API is continuously being developed and improved, but we are still trying to keep it as stable as possible. We try to only have changes that are backwards compatible: usually the changes are only additions, e.g. new resources are implemented or new properties are added to existing resources. Sometimes breaking changes cannot be avoided, e.g. when a new feature requires an incompatible change to the underlying data model, all those changes will be documented in the change log.  ## Security and Authentication  You must be a verified user to make API requests. You can authorize against the API with an API token. The token is configurable in your weclapp account under **My settings > API**. Authentication is possible in multiple ways: If the request contains the session cookies of a logged in weclapp session then the user and permissions of that session are used. This is useful when testing the API in a web browser, because then requests are “automatically” authenticated if weclapp is used in another tab. But generally the API is not used from a browser or with session cookies, instead there is an API token for each user that can be used to authenticate requests. Each user can find his/her token on the \"My Settings page\". The token should be kept secret like a password. A user can also generate a new token at any time, doing that invalidates all previous tokens. Authenticating using a token is possible in two ways:  * the token can be sent using the AuthenticationToken header `AuthenticationToken: {api_token}` * the standard HTTP Basic authentication can be used: the username needs to be `“*”` and the password is the token  ## Using curl  ```bash curl -H \"AuthenticationToken:{api_token} https://<TENANT>.weclapp.com/webapp/api/v1...\" ```  Examples of how to use curl will be shown in each section of this API.  ## Headers  This is a JSON-only API. You must supply a `Content-Type: application/json` header on PUT and POST operations. You must set a `Accept: application/json` header on all requests. You may get a `text/plain` response in case of error, e.g. in case of a bad request, you should treat this as an error you need to take action on.  ## URLs  The base URL for the API is `https://<TENANT>.weclapp.com/webapp/api/v1/` where `<TENANT>.weclapp.com` is the domain of the specific weclapp instance. So each weclapp instance has its own API endpoints which allow accessing data for that particular instance. The API provides access to various resources like customers, sales orders, articles etc.. Each of those resources implements a common set of operations. The URLs and HTTP methods for the different resource operations use the same pattern for all resources:  | Operation                     | HTTP Method | URL pattern                                                           | |-------------------------------|-------------|-----------------------------------------------------------------------| | Query/list instances          | GET         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>`       | | total number of instances     | GET         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/count` | | Get a specific instance by id | GET         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>` | | Create a new instance         | POST        | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>`       | | Update a specific instance    | PUT         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>` | | Delete a specific instance    | DELETE      | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>` |  Not all resources support all of those operations. A general description for each operation can be found in API operations by example, and details for each resource are described on the page for that resource.  ## Additional operations  Some resources allow further operations or actions. Those operations can be executed with a POST request, for some operations that only read data it is also possible to use a GET request (this is documented for each operation). For general operations for a resource the URL pattern is `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/<operation>`. Some operations are instance specific, those use the following URL pattern: `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>/<operation>`.      ## JSON  | Type                 | Representation in JSON                                                                                                                                                                                                                                                                                                                                                                         | |----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | string               | Serialized as JSON string, empty strings (length 0 or only whitespace) are always interpreted as null, it is not possible to have a property with an empty string value.                                                                                                                                                                                                                       | | boolean              | Serialized as `true` / `false`.                                                                                                                                                                                                                                                                                                                                                                | | decimal number       | Most numbers in weclapp are decimal numbers with a fixed precision and scale (e.g. quantities or prices), they are serialized as JSON strings and not as JSON numbers to prevent accidental loss of precision when the JSON is deserialized with a JSON library that uses doubles to represent JSON numbers. The serialized numbers always use a “.” as the decimal mark (if one is required). | | integers             | Integer numbers (that can safely be represented as a double) are serialized as JSON numbers.                                                                                                                                                                                                                                                                                                   | | floats/doubles       | Serialized as JSON numbers.                                                                                                                                                                                                                                                                                                                                                                    | | dates and timestamps | Serialized as the milliseconds since 1970-01-01T00:00:00Z (as a JSON number).                                                                                                                                                                                                                                                                                                                  | | enums                | Sometimes a property value can be one of a fixed number of named options. Those enum properties are serialized as a JSON string with the name of the option.                                                                                                                                                                                                                                   |  The deserialization of data sent to the API is relatively lenient, for example when a string is expected, but a number is given then that number is used as the string and the other way around (if possible). Properties with the value null are not serialized by default and when sending data to the API it is also not necessary to include properties whose value is null: all properties that are missing from the JSON object but are expected are assumed to be `null`. To get all properties including those with the value null the query parameter `serializeNulls` can be added to the request URL, in that case null values are included in the response.    ## Error Responses  Any request on the weclapp API may return an error response, with a structure conforming to [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807). See the [API error reference](#errors) section for details.      ## Change Policy  weclapp may modify the attributes and resources available to the API and our policies related to access and use of the API from time to time without advance notice. weclapp will use commercially reasonable efforts to notify you of any modifications to the API or policies through notifications or posts on the weclapp Developer Website. weclapp also tracks deprecation of attributes of the API on its Changelog. Modification of the API may have an adverse effect on weclapp Applications, including but not limited to changing the manner in which weclapp Applications communicate with the API and display or transmit Your Data. weclapp will not be liable to you or any third party for such modifications or any adverse effects resulting from such modifications    # API newsletter  Sign up here for our [API newsletter](https://340d89eb.sibforms.com/serve/MUIEAEREP3buQMWpwPwuVohmsPBikdVQIilNQeZ2DJBE5NZePFYqyp_62WSheCC5t_Q7eJ6SVpZBauqRY93L8L8Iquik5gaH40Bi0uOtPioS7U7k4JvemqVuSdvEV0A3DgygC5LOAv-kjuN4Ij5MUqzm5DSHYbmKvGucHMXpZMFGGA5Lwi5VUv6ZZbROGqZJCrGfYFxGttzVBqc_). We will inform you regularly about planned API changes.   # API operations sample  As mentioned previously all resources implement common operations in the same way. In the following all the common operations are explained for the `customer` resource. The operations work in the same way for all other resources (some resources don’t support all the operations), the differences between the resources are mostly the data and the properties that are required and used.  ## Querying  The most common operation is querying or listing the existing entity instances. This is possible with a `GET` request to the base URL of a resource:    ### `GET /customer`   ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer\" ```  **Output:**  ```json { \"result\": [ { \"id\": \"4342\", \"version\": \"1\", \"addresses\": [ { \"id\": \"4344\", \"version\": \"0\", \"city\": \"München\", \"countryCode\": \"DE\", \"createdDate\": 1496828973904, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1496828973903, \"primeAddress\": true, \"street1\": \"Mustergasse 7\", \"zipcode\": \"80331 \" } ], \"blocked\": false, \"company\": \"Muster GmbH\", \"contacts\": [ { \"id\": \"4332\", \"version\": \"1\", \"addresses\": [ { \"id\": \"4334\", \"version\": \"0\", \"city\": \"München\", \"countryCode\": \"DE\", \"createdDate\": 1496828882836, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1496828882836, \"primeAddress\": true, \"street1\": \"Fasanenweg 15\", \"zipcode\": \"80331\" } ], \"createdDate\": 1496828882837, \"email\": \"mustermann@beispiel.de\", \"firstName\": \"Max\", \"lastModifiedDate\": 1496828996245, \"lastName\": \"Mustermann\", \"partyType\": \"PERSON\", \"personCompany\": \"Muster GmbH\", \"salutation\": \"MR\" } ], \"createdDate\": 1496828973904, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\" } ], \"customerNumber\": \"C1006\", \"customerTopics\": [], \"deliveryBlock\": false, \"insolvent\": false, \"insured\": false, \"lastModifiedDate\": 1496828996212, \"optIn\": false, \"partyType\": \"ORGANIZATION\", \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"sales@weclapp.com\", \"salesChannel\": \"NET1\", \"useCustomsTariffNumber\": false } ] } ```  In this case there is one sales order with one order item. By default, all null values are omitted, to include them the query parameter serializeNulls can be used:    ### `GET /customer?serializeNulls`    ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?serializeNulls\" ```  **Output:**  ```json { \"result\": [ { \"id\": \"4342\", \"version\": \"1\", \"addresses\": [ { \"id\": \"4344\", \"version\": \"0\", \"city\": \"München\", \"company\": null, \"company2\": null, \"countryCode\": \"DE\", \"createdDate\": 1496828973904, \"deliveryAddress\": false, \"globalLocationNumber\": null, \"invoiceAddress\": false, \"lastModifiedDate\": 1496828973903, \"postOfficeBoxCity\": null, \"postOfficeBoxNumber\": null, \"postOfficeBoxZipCode\": null, \"primeAddress\": true, \"state\": null, \"street1\": \"Mustergasse 7\", \"street2\": null, \"zipcode\": \"80331 \" } ], \"amountInsured\": null, \"annualRevenue\": null, \"birthDate\": null, \"blockNotice\": null, \"blocked\": false, \"commercialLanguageId\": null, \"company\": \"Muster GmbH\", \"company2\": null, \"contacts\": [ { \"id\": \"4332\", \"version\": \"1\", \"addresses\": [ { \"id\": \"4334\", \"version\": \"0\", \"city\": \"München\", \"company\": null, \"company2\": null, \"countryCode\": \"DE\", \"createdDate\": 1496828882836, \"deliveryAddress\": false, \"globalLocationNumber\": null, \"invoiceAddress\": false, \"lastModifiedDate\": 1496828882836, \"postOfficeBoxCity\": null, \"postOfficeBoxNumber\": null, \"postOfficeBoxZipCode\": null, \"primeAddress\": true, \"state\": null, \"street1\": \"Fasanenweg 15\", \"street2\": null, \"zipcode\": \"80331\" } ], \"birthDate\": null, \"company\": null, \"company2\": null, \"createdDate\": 1496828882837, \"customAttributes\": null, \"description\": null, \"email\": \"mustermann@beispiel.de\", \"fax\": null, \"firstName\": \"Max\", \"fixPhone2\": null, \"lastModifiedDate\": 1496828996245, \"lastName\": \"Mustermann\", \"middleName\": null, \"mobilePhone1\": null, \"mobilePhone2\": null, \"partyType\": \"PERSON\", \"personCompany\": \"Muster GmbH\", \"personDepartment\": null, \"personRole\": null, \"phone\": null, \"phoneHome\": null, \"salutation\": \"MR\", \"title\": null, \"website\": null } ], \"createdDate\": 1496828973904, \"creditLimit\": null, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\", \"booleanValue\": null, \"dateValue\": null, \"numberValue\": null, \"selectedValueId\": null, \"selectedValues\": null, \"stringValue\": null } ], \"customerCategoryId\": null, \"customerCategoryName\": null, \"customerNumber\": \"C1006\", \"customerRating\": null, \"customerTopics\": [], \"defaultHeaderDiscount\": null, \"defaultHeaderSurcharge\": null, \"deliveryBlock\": false, \"description\": null, \"email\": null, \"fax\": null, \"firstName\": null, \"insolvent\": false, \"insured\": false, \"invoiceContactId\": null, \"lastModifiedDate\": 1496828996212, \"lastName\": null, \"leadSourceId\": null, \"leadSourceName\": null, \"middleName\": null, \"mobilePhone1\": null, \"oldCustomerNumber\": null, \"optIn\": false, \"parentPartyId\": null, \"partyType\": \"ORGANIZATION\", \"paymentMethodId\": null, \"paymentMethodName\": null, \"personCompany\": null, \"personDepartment\": null, \"personRole\": null, \"phone\": null, \"primaryContactId\": null, \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"sales@weclapp.com\", \"salesChannel\": \"NET1\", \"salutation\": null, \"satisfaction\": null, \"sectorId\": null, \"sectorName\": null, \"shipmentMethodId\": null, \"shipmentMethodName\": null, \"termOfPaymentId\": null, \"termOfPaymentName\": null, \"title\": null, \"useCustomsTariffNumber\": false, \"vatRegistrationNumber\": null, \"website\": null } ] } ```  ## Pagination By default the operation will not return all entity instances but only the first 100, this can be changed by using the `pageSize` query parameter with the number of desired results. But `pageSize` cannot be arbitrarily high it is usually limited 1000 (exceptions to the default limits of 100 and 1000 are noted in the documentation for the specific resources). To get further results it is necessary to skip entity instances, this is done using the `page` query parameter. Examples:    ### `GET /customer?pageSize=10`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?pageSize=10\" ```  returns at most 10 instances  ### `GET /customer?page=2&pageSize=10`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?page=2&pageSize=10\" ```  returns the second page of results (the `page` parameter is one based, so `page=1` is the first page, which is also the default). Using those two parameters it is possible to implement pagination.  ## Sorting  It is also possible to change the order of the returned results using the `sort` parameter:  ### `GET /customer?sort=lastModifiedDate`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?sort=lastModifiedDate\" ```  sort by `lastModifiedDate` (ascending).  ### `GET /customer?sort=-lastModifiedDate`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?sort=-lastModifiedDate\" ```  sort by `lastModifiedDate` descending.  ### `GET /customer?sort=lastModifiedDate,-salesChannel`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?sort=lastModifiedDate,-salesChannel\" ```  sort by `lastModifiedDate` (ascending) and then `salesChannel` descending.   It is generally possible to sort by most of the simple properties of an entity. It is possible to combine multiple sort orders by combining the property names with a comma. To sort in descending order just prepend a minus to the property name. If an unsupported or unknown property is specified then an error response is returned.  ## Filtering  It is often desired to get just a subset of the data, for example just the orders of a specific customer or created after a specific date. This is possible using filtering query parameters:    ### `GET /customer?salesChannel-eq=NET1`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?salesChannel-eq=NET1\" ```  customers for `salesChannel` `NET1`.  ### `GET /customer?createdDate-gt=1398436281262`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?createdDate-gt=1398436281262\" ```  customers created after the specified timestamp.  ### `GET /customer?salesChannel-eq=NET1&createdDate-gt=1398436281262`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?salesChannel-eq=NET1&createdDate-gt=1398436281262\" ```  customers for `salesChannel` `NET1` and created after the specified timestamp.  ### `GET /customer?customAttribute4587-eq=NEW`  ```bash curl -H \"\"\"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?customAttribute4587-eq=NEW\" ```  customers with the value `NEW` for `customAttribute` with id 4587.  ### `GET /customer?customAttribute4587.entityReferences.entityId-eq=1234`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?customAttribute4587.entityReferences.entityId-eq=1234\" ```  customers with an entity reference to an entity with the id 1234 for the `customAttribute` with the id 4587.  ### `GET /customAttributeDefinitions`  All attributeTypes are supported except `MULTISELECT_LIST`. CustomAttributes of attributeType `LIST` could be filtered by `customAttribute{customAttributeId}.id` or `customAttribute{customAttributeId}.value`.  ### `GET /customer?customAttribute3387.value-eq=OPTION1`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?customAttribute3387.value-eq=OPTION1\" ```  customers with value `OPTION1` for `customAttribute` with id 3387.  A filtering query parameter consists of a property name and a filter operator joined together with a minus. If multiple filtering query parameter are specified then they are combined and the returned results match all of them. Filtering query parameters for unknown properties or properties that don’t support filtering are silently ignored.  The following filtering operators are supported (not all of them work for all property types):  | Operator | Meaning                                                                                                                                                                                     | |----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | eq       | equal                                                                                                                                                                                       | | ne       | not equal                                                                                                                                                                                   | | lt       | less than                                                                                                                                                                                   | | gt       | greater than                                                                                                                                                                                | | le       | less equal                                                                                                                                                                                  | | ge       | greater equal                                                                                                                                                                               | | null     | property is null (the query parameter value is ignored and can be omitted)                                                                                                                  | | notnull  | property is not null (the query parameter value is ignored and can be omitted)                                                                                                              | | like     | like expression (supports `%` and `_` as placeholders, similar to SQL LIKE)                                                                                                                 | | notlike  | not like expression                                                                                                                                                                         | | ilike    | like expression, ignoring case                                                                                                                                                              | | notilike | not like expression, ignoring case                                                                                                                                                          | | in       | the property value is in the specified list of values, the query parameter value must be a JSON array with the values in the correct type, for example `?customerNumber-in=[\"1006\",\"1007\"]` | | notin    | the property value is not in the specified list of values                                                                                                                                   |  ## \"Or\" condition filtering  In addition to the default behavior of linking filter expressions via \"and\" you can also link individual filter expressions via \"or\" by prefixing their parameter name with \"or-\":   ### `GET /customer?or-name-eq=charlie&or-name-eq=chaplin`   ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?or-name-eq=charlie&or-name-eq=chaplin\" ```  The above example is the equivalent of the expression `(name equals \"charlie\") or (name equals \"chaplin\")`   For combining `or` and `and` clauses you may also group `or` expressions by using `or<groupname>-` instead of the plain `or-` prefix:   ### `GET /customer?orGroup1-name-eq=charlie&orGroup1-name-eq=chaplin&orGroup2-responsibleUserUsername-eq=mrtest&orGroup2-referenceNumber=4711&commercialLanguageId-eq=12`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?orGroup1-name-eq=charlie&orGroup1-name-eq=chaplin&orGroup2-responsibleUserUsername-eq=mrtest&orGroup2-referenceNumber=4711&commercialLanguageId-eq=12\" ```  The above example is the equivalent of the expression  ``` ((name equals charlie) or (name equals chaplin)) and ((responsibleUserUsername equals \"mrtest\") or (referenceNumber equals \"4711\")) and (commercialLanguageId equals \"12\") ```  Technically, the default \"or-\" variant is just a special case of this, using the empty String as group name.   ## Return only specific properties  Sometimes it is desirable to only fetch a subset of all properties, for example to save bandwidth. This is possible by specifying the desired properties using the `properties` query parameter:  ### `GET /customer?properties=id,customerNumber,salesChannel`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?properties=id,customerNumber,salesChannel\" ```  **Output:**  ```json { \"result\": [ { \"id\": \"3346\", \"customerNumber\": \"C1002\", \"salesChannel\": \"NET1\" } ] } ```  It is also possible to specify property paths:  ### `GET /customer?properties=id,customerNumber,salesChannel,contacts.id,contacts.lastName`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?properties=id,customerNumber,salesChannel,contacts.id,contacts.lastName\" ```  If an unknown property or property path is specified then an error response is returned.  ```json { \"result\": [ { \"id\": \"3346\", \"contacts\": [ { \"id\": \"3731\", \"lastName\": \"Mustermann\" } ], \"customerNumber\": \"C1002\", \"salesChannel\": \"NET1\" } ] } ```   ## Combinations  The query parameters for pagination, sorting, filtering and returning only specific properties can be combined to perform queries.   ## Counting  To determine the total number of entity instances the count operation can be used:  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/count\" ```  It is possible to use the filtering query parameters from the querying operation with the count operation:  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/count?salesChannel-eq=NET1\" ```  returns the number of customers for `salesChannel` `NET1`.   ## Referenced entities  The API offers the possibility to get the referenced entities for a query result in the same request. This way you can save subsequent requests and get all necessary and referenced data in one request. This feature can be used by simply specifying the parameter `includeReferencedEntities` and the primary key references as comma separated list. The API response will contain an additional object `referencedEntities`.   ### `GET /article?includeReferencedEntities=unitId,articleCategoryId`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/article?includeReferencedEntities=unitId,articleCategoryId&properties=id,name,unitId,articleCategoryId\" ```  **Output:**  ```json { \"result\": [ { \"id\": \"3235\", \"name\": \"Testartikel 1\", \"unitId\": \"2770\" }, { \"id\": \"3236\", \"name\": \"Testartikel 2\", \"unitId\": \"2770\" }, { \"id\": \"3237\", \"articleCategoryId\": \"7035\", \"name\": \"Testartikel 3\", \"unitId\": \"2770\" } ], \"referencedEntities\": { \"unit\": [ { \"id\": \"2770\", \"version\": \"0\", \"createdDate\": 1597915605986, \"description\": \"Stück\", \"lastModifiedDate\": 1597915605985, \"name\": \"Stk.\" } ], \"articleCategory\": [ { \"id\": \"7035\", \"version\": \"0\", \"createdDate\": 1619778730348, \"lastModifiedDate\": 1619778730348, \"name\": \"Demo-Gruppe\" } ] } } ```  ## Additional properties  In addition to the common properties, there are additional properties that can be optionally queried. These are calculated or complexly determined and must therefore be explicitly queried.  To use this function, only the parameter `additionalProperties` and the names of the additional properties must be specified as a comma-separated list. The response then contains the additional object `additionalProperties` with the property and an array of values. The index of the value object in this list also represents the reference to the respective entity.   ### `GET /article?additionalProperties=currentSalesPrice`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ \"https://<TENANT>.weclapp.com/webapp/api/v1/article?additionalProperties=currentSalesPrice\" ```  **Output:**  ```json { \"additionalProperties\": { \"currentSalesPrice\": [ { \"articleUnitPrice\": \"39.95\", \"currencyId\": \"255\", \"quantity\": \"1\", \"reductionAdditionItems\": [] }, { \"articleUnitPrice\": \"479.4\", \"currencyId\": \"255\", \"quantity\": \"1\", \"reductionAdditionItems\": [] } ] } } ```   ## Dry-Run  Generic `PUT`, `POST` and `DELETE` endpoints support to perform operations in a \"dry-run-mode\". Where possible, business logic is executed and the data submitted by the requester is validated. To use this functionality the requester can set the optional query parameter \"`dryRun`\" (boolean, default: `false`). The return is as far as possible as with a productive execution, except that 200 \"ok\" is returned in case of success. The meta properties (id, version, createdDate, lastModifiedDate) are not included in \"dry-run-responses\".  ### `POST /salesOrder?dryRun=true`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ -H Content-Type: application/json \\ -X POST \"https://<TENANT>.weclapp.com/webapp/api/v1/salesOrder?dryRun=true\" \\ -d   '{ \"customerNumber\": \"4799\" }' ```  **Error Output:**  ```json { \"detail\": \"customer not found\", \"error\": \"customer not found\", \"status\": 400, \"title\": \"entity validation failed\", \"type\": \"/webapp/view/api/errors.html#!/errors/validation\", \"validationErrors\": [ { \"detail\": \"referenced entity not found\", \"instance\": \"salesOrder\", \"location\": \"customerId\", \"title\": \"referenced entity not found\", \"type\": \"/webapp/view/api/errors.html#!/validation/reference\" } ] } ```  The response status will be 400 (Bad Request).  **Successful Output:**  ```json { \"availability\": \"NOT_CHECKED\", \"availabilityForAllWarehouses\": \"NOT_CHECKED\", \"commissionSalesPartners\": [], \"creatorId\": \"4451\", \"currencyConversionDate\": 1699375721469, \"currencyConversionRate\": \"1\", \"customAttributes\": [], \"customerId\": \"4799\", \"customerNumber\": \"10000\", \"deliveryAddress\": { \"city\": \"Hithausen\", \"company\": \"Beispiel AG\", \"countryCode\": \"DE\", \"street1\": \"Feldstraße 34\", \"zipcode\": \"54321\" }, \"deliveryEmailAddresses\": { \"toAddresses\": \"info@beispielag.de\" }, \"disableEmailTemplate\": false, \"dispatchCountryCode\": \"DE\", \"factoring\": false, \"fulfillmentProviderId\": \"3335\", \"grossAmount\": \"0\", \"grossAmountInCompanyCurrency\": \"0\", \"headerDiscount\": \"0\", \"headerSurcharge\": \"0\", \"invoiceAddress\": { \"city\": \"Hithausen\", \"company\": \"Beispiel AG\", \"countryCode\": \"DE\", \"street1\": \"Feldstraße 34\", \"zipcode\": \"54321\" }, \"invoiced\": false, \"netAmount\": \"0\", \"netAmountInCompanyCurrency\": \"0\", \"nonStandardTaxId\": \"3492\", \"nonStandardTaxName\": \"DE Steuerfrei Drittland (VK)\", \"onlyServices\": false, \"orderDate\": 1699311600000, \"orderItems\": [], \"paid\": false, \"plannedShippingDate\": 1699311600000, \"pricingDate\": 1699311600000, \"projectMembers\": [], \"projectModeActive\": false, \"recordAddress\": { \"city\": \"Hithausen\", \"company\": \"Beispiel AG\", \"countryCode\": \"DE\", \"street1\": \"Feldstraße 34\", \"zipcode\": \"54321\" }, \"recordCurrencyId\": \"255\", \"recordCurrencyName\": \"EUR\", \"recordEmailAddresses\": { \"toAddresses\": \"info@beispielag.de\" }, \"responsibleUserId\": \"4748\", \"responsibleUserUsername\": \"karsten.kunde@example.com\", \"salesChannel\": \"NET1\", \"salesInvoiceEmailAddresses\": { \"toAddresses\": \"info@beispielag.de\" }, \"salesOrderPaymentType\": \"STANDARD\", \"sentToRecipient\": false, \"servicesFinished\": false, \"shipped\": false, \"shippingCostItems\": [], \"shippingLabelsCount\": 1, \"status\": \"ORDER_ENTRY_IN_PROGRESS\", \"statusHistory\": [ { \"status\": \"ORDER_ENTRY_IN_PROGRESS\", \"statusDate\": 1699375721472, \"userId\": \"4451\" } ], \"tags\": [], \"warehouseId\": \"4191\", \"warehouseName\": \"Hauptlager\" } ```  The response status will be 200 (OK).   ## Optimistic locking  For the update operation the resources usually also support optimistic locking using the `version` property: if the `version` property is in the request body and it does not match the current `version`, then the request fails with an optimistic lock error. In that case the caller should again get the latest `version`, apply the changes and try the request again.   ## Basic Operations  The following entries will show you how to use the different basic operations (`GET`, `POST`, `PUT`, `DELETE`) and what an exemplary response they will give whether the operation was successful or not.   The following table will show you the HTTP status codes of the basic operations if the operation was successful:  | Operation | HTTP status code | |-----------|------------------| | GET       | 200 (OK)         | | POST      | 201 (Created)    | | PUT       | 200 (OK)         | | DELETE    | 204 (No Content) |  If you are not currently logged in to weclapp, you are using another browser or the AuthenticationToken was wrong you will get a response of `401 (Unauthorized)`. It is possible to disable the optimistic locking check by just omitting the `version` property, but doing this might accidentally overwrite changes done by another user in the meantime.  ## Get a specific entity instance  Each entity instance has its own URL where it can be retrieved. The URL is based on the entity id.  Performing a GET request on that URL returns the entity instance:  ### `GET /customer/id/3346`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/3346\" ```  **Output:**  ```json { \"result\": [ { \"id\": \"3346\", \"version\": \"2\", \"addresses\": [ { \"id\": \"3348\", \"version\": \"0\", \"countryCode\": \"DE\", \"createdDate\": 1487765943229, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1487765943229, \"primeAddress\": true }, { \"id\": \"3976\", \"version\": \"0\", \"company\": \"11111\", \"company2\": \"22222\", \"countryCode\": \"DE\", \"createdDate\": 1496040807652, \"deliveryAddress\": false, \"globalLocationNumber\": \"gln\", \"invoiceAddress\": false, \"lastModifiedDate\": 1496040807648, \"primeAddress\": false } ], \"blocked\": false, \"company\": \"Musterdaten GmbH\", \"contacts\": [ { \"id\": \"3377\", \"version\": \"0\", \"addresses\": [ { \"id\": \"3379\", \"version\": \"0\", \"countryCode\": \"DE\", \"createdDate\": 1487767121646, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1487767121645, \"primeAddress\": true } ], \"createdDate\": 1487767121649, \"firstName\": \"Max\", \"lastModifiedDate\": 1487767121642, \"lastName\": \"Mustermann\", \"partyType\": \"PERSON\", \"personCompany\": \"Musterdaten GmbH\", \"salutation\": \"MR\" } ], \"createdDate\": 1487765943230, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\" } ], \"customerNumber\": \"C1002\", \"customerTopics\": [], \"deliveryBlock\": false, \"insolvent\": false, \"insured\": false, \"lastModifiedDate\": 1496040807672, \"optIn\": false, \"partyType\": \"ORGANIZATION\", \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"@weclapp.com\", \"salesChannel\": \"NET1\", \"useCustomsTariffNumber\": false } ] } ```  ## Create a new instance  Creating new instances is done by performing a POST request to the base URL of a resource.  The body for that request must have the same structure as the result of the \"get by id\" request, but usually not all properties need to be specified and there are defaults for some properties. Here are some general notes:  * id, version, createdDate and lastModifiedDate can usually not be set by the client, so those values are ignored if they are specified * references to other entities are often represented by two properties (usually id and some other more or less unique property of the referenced entity), for example customer has currencyId and currencyName to reference the currency, when creating a new customer then it is not necessary to specify both properties, one of them is usually enough as long as it specifies the referenced entity uniquely, if both are given then they must not contradict each other * usually some required properties have sensible defaults, so if those are not given or null then the default will be used * boolean properties can be optional (default value would be set) or mandatory   ### `POST /customer`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ -H Content-Type: application/json \\ -X POST \"https://<TENANT>.weclapp.com/webapp/api/v1/customer\" \\ -d   '{ \"customerNumber\": \"C1013\", \"partyType\": \"ORGANIZATION\", \"company\": \"Firma\" }' ```  **Output:**  ```json { \"id\": \"4391\", \"version\": \"0\", \"addresses\": [ { \"id\": \"4393\", \"version\": \"0\", \"countryCode\": \"DE\", \"createdDate\": 1496840784272, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1496840784272, \"primeAddress\": true } ], \"blocked\": false, \"company\": \"Firma\", \"contacts\": [], \"createdDate\": 1496840784273, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\" } ], \"customerNumber\": \"C1013\", \"customerTopics\": [], \"deliveryBlock\": false, \"insolvent\": false, \"insured\": false, \"lastModifiedDate\": 1496840784270, \"optIn\": false, \"partyType\": \"ORGANIZATION\", \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"sales@weclapp.com\", \"salesChannel\": \"NET1\", \"useCustomsTariffNumber\": false } ```  The response status will be 201 (Created) and the response will have a `Location` header pointing to the URL of the created instance.   ## Update a specific instance  Updating an instances is done by performing a `PUT` request to the URL of the instance.  A successful response will have the status 200 (OK) and the response body will contain the updated entity.  Some special aspects must be considered when updating:  * the read-only properties like `createdDate` are ignored anyway, so they do not need to be given * `id` and `version` are processed as follows: if the `id` is given it must match the `id` of the updated instance and if the `version` is given then optimistic locking is enabled (see below) * for the references that use two properties it is again possible to specify only one of them, if both are given then they must not contradict each other * for complete entity updates boolean properties are always mandatory and need to be passed  ### Updating the complete entity  When updating it is generally necessary to specify all properties that are not `null`, all unspecified properties will be interpreted as `null`.  Since sometimes new properties are added to entities, it is strongly recommended that an API client always first gets the latest version using `GET/customer/id/{id}`, then modifies that JSON and finally performs the `PUT` request. Doing this ensures that new properties that the client does not know about are not accidentally overwritten with `null`.  In this example only the property \"company\" will be updated. All other properties are unchanged.  ### `PUT /customer/id/4391`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ -H Content-Type: application/json \\ -X PUT \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/4391\" \\ -d  @- <<JSON { \"id\": \"4391\", \"version\": \"0\", \"addresses\": [ { \"id\": \"4393\", \"version\": \"0\", \"countryCode\": \"DE\", \"createdDate\": 1496840784272, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1496840784272, \"primeAddress\": true } ], \"blocked\": false, \"company\": \"NEUER FIRMENNAME!!!\", \"contacts\": [], \"createdDate\": 1496840784273, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\" } ], \"customerNumber\": \"C1013\", \"customerTopics\": [], \"deliveryBlock\": false, \"insolvent\": false, \"insured\": false, \"lastModifiedDate\": 1496840784270, \"optIn\": false, \"partyType\": \"ORGANIZATION\", \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"sales@weclapp.com\", \"salesChannel\": \"NET1\", \"useCustomsTariffNumber\": false } JSON ```  **Output:**  ```json { \"id\": \"4391\", \"version\": \"1\", \"addresses\": [ { \"id\": \"4393\", \"version\": \"0\", \"countryCode\": \"DE\", \"createdDate\": 1496840784272, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1496840784272, \"primeAddress\": true } ], \"blocked\": false, \"company\": \"NEUER FIRMENNAME!!!\", \"contacts\": [], \"createdDate\": 1496840784273, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\" } ], \"customerNumber\": \"C1013\", \"customerTopics\": [], \"deliveryBlock\": false, \"insolvent\": false, \"insured\": false, \"lastModifiedDate\": 1496842955268, \"optIn\": false, \"partyType\": \"ORGANIZATION\", \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"sales@weclapp.com\", \"salesChannel\": \"NET1\", \"useCustomsTariffNumber\": false } ```  ### Updating only specific properties  It is also possible to update only specific properties. For this you only have to set the parameter `ignoreMissingProperties=true`. We recommend to always include `version` here as well to activate optimistic locking.  If you want to change lists (add, update or delete an item) stored in the entity, it is sufficient to specify the id for existing item entities.  In this example only the property \"company\" will be updated. All other properties are unchanged.  ### `PUT /customer/id/4391`    ```bash curl -H \"AuthenticationToken:<TOKEN>\" \\ -H Content-Type: application/json \\ -X PUT \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/4391?ignoreMissingProperties=true\" \\ -d '{ \"version\": \"0\", \"company\": \"NEUER FIRMENNAME!!!\" }' ```  **Output:**  ```json { \"id\": \"4391\", \"version\": \"1\", \"addresses\": [ { \"id\": \"4393\", \"version\": \"0\", \"countryCode\": \"DE\", \"createdDate\": 1496840784272, \"deliveryAddress\": false, \"invoiceAddress\": false, \"lastModifiedDate\": 1496840784272, \"primeAddress\": true } ], \"blocked\": false, \"company\": \"NEUER FIRMENNAME!!!\", \"contacts\": [], \"createdDate\": 1496840784273, \"currencyId\": \"248\", \"currencyName\": \"EUR\", \"customAttributes\": [ { \"attributeDefinitionId\": \"4048\" } ], \"customerNumber\": \"C1013\", \"customerTopics\": [], \"deliveryBlock\": false, \"insolvent\": false, \"insured\": false, \"lastModifiedDate\": 1496842955268, \"optIn\": false, \"partyType\": \"ORGANIZATION\", \"responsibleUserFixed\": false, \"responsibleUserId\": \"947\", \"responsibleUserUsername\": \"sales@weclapp.com\", \"salesChannel\": \"NET1\", \"useCustomsTariffNumber\": false } ```   ### Optimistic locking   For the update operation the resources usually also support optimistic locking using the version property: if the version property is in the request body and it does not match the current version, then the request fails with an optimistic lock error. In that case the caller should again get the latest version, apply the changes and try the request again. It is possible to disable the optimistic locking check by just omitting the version property, but doing this might accidentally overwrite changes done by another user in the meantime.  ## Delete a specific instance  Deleting an instances is done by performing a `DELETE` request to the URL of the instance.  ### `DELETE /customer/id/{id}`  ```bash curl -H \"AuthenticationToken:<TOKEN>\" -X DELETE \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/4391\" ```  If the deletion is possible it is performed and the response status will be 204 (No Content), otherwise an error response will be returned.  <span id=\"errors\"> </span>  # API error reference  weclapp API errors are basically conformant to [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807), with some notable differences:  * The migration to the RFC 7807 structure is an ongoing process, so some compatibility mechanisms are in place for now: * The responses come with \"`Content-Type: application/json`\" instead of \"`Content-Type: application/problem+json`\" * The \"unstructured\" error responses that have been in use until now are still part of the response JSON, so existing code should work without changes. * Detail information that _should_ be there according to the new structure may be still missing. This applies especially to all kinds of validation errors. * Two custom fields have been added to the response structure: \"location\" and \"validationErrors\". See the general description below and the individual error descriptions for details on these.  ## Error JSON structure  The error JSON is structured as described in [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807), with two additional properties:  | Property         | Datatype         | Description                                                                                                                                                                                                                                       | |------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | type             | string           | (relative) URI reference that identifies the problem type, pointing to the error description in this document. To technically distinguish individual types of errors it is recommended to only evaluate the part after the last '/'.              | | title            | string           | (RFC7807) A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization (e.g., using proactive content negotiation; see RFC7231, Section 3.4).      | | status           | integer          | (RFC7807) The HTTP status code (RFC7231, Section 6) generated by the origin server for this occurrence of the problem.                                                                                                                            | | detail           | string           | (RFC7807) A human-readable explanation specific to this occurrence of the problem. This may be missing when the actual detail information either would be security sensitive (e.g. on unexpected errors) or is contained in the validationErrors. | | instance         | string           | (RFC7807) A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. In weclapp, this typically is the URI to the affected entity.                                      | | validationErrors | array of objects | List of found validation errors, with a structure modeled after RFC 7807 as well (see below).                                                                                                                                                     |  Validation errors have a similar structure:  | Property | Datatype         | Description                                                                                                                                                                                                                                  | |----------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | type     | string           | (relative) URI reference that identifies the problem type, pointing to the error description in this document. To technically distinguish individual types of errors it is recommended to only evaluate the part after the last '/'.         | | title    | string           | (RFC7807) A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization (e.g., using proactive content negotiation; see RFC7231, Section 3.4). | | detail   | string           | (RFC7807) A human-readable explanation specific to this occurrence of the problem.                                                                                                                                                           | | instance | string           | (RFC7807) A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. In weclapp, this is the name of the affected parameter or the URI to the affected entity.     | | location | string           | The JsonPath location of the affected property.                                                                                                                                                                                              | | allowed  | array of strings | List of allowed values, with semantics dependent on the concrete validation error.                                                                                                                                                           |   ## Error reference   <span id=\"!/errors/context\"></span>  ### \"context\": operation not possible in this context  |            |                                       | |------------|---------------------------------------| | description | The operation is not possible in this context or with the current state of the data                  | | type       | [/webapp/view/api/errors.html#!/errors/context](/webapp/view/api/errors.html#!/errors/context)        | | status     | 409 (Conflict)|  <span id=\"!/errors/conversation\"></span>  ### \"conversation\": existing conversation (parameter 'cid') is not allowed  |            |                                       | |------------|---------------------------------------| | description | The request was sent in the context of a running session, which is not allowed for the (stateless) API                  | | type       | [/webapp/view/api/errors.html#!/errors/conversation](/webapp/view/api/errors.html#!/errors/conversation)        | | status     | 400 (Bad Request)| | detail | human readable information on the conversation |  <span id=\"!/errors/entity_not_found\"></span>  ### \"entity_not_found\": (sub)entity not found  |            |                                       | |------------|---------------------------------------| | description | The specified entity or (more likely) a referenced sub-entity could not be found.                  | | type       | [/webapp/view/api/errors.html#!/errors/entity_not_found](/webapp/view/api/errors.html#!/errors/entity_not_found)        | | status     | 400 (Bad Request)|  <span id=\"!/errors/forbidden\"></span>  ### \"forbidden\": insufficient privileges  |            |                                       | |------------|---------------------------------------| | description | The provided credentials are not sufficient to perform the requested operation                  | | type       | [/webapp/view/api/errors.html#!/errors/forbidden](/webapp/view/api/errors.html#!/errors/forbidden)        | | status     | 403 (Forbidden)|  <span id=\"!/errors/invalid_json\"></span>  ### \"invalid_json\": invalid json  |            |                                       | |------------|---------------------------------------| | description | The JSON passed in the request body could not be parsed or the body is not JSON at all.                  | | type       | [/webapp/view/api/errors.html#!/errors/invalid_json](/webapp/view/api/errors.html#!/errors/invalid_json)        | | status     | 400 (Bad Request)|  <span id=\"!/errors/not_found\"></span>  ### \"not_found\": resource not found  |            |                                       | |------------|---------------------------------------| | description | The API endpoint / method / entity could not be found                  | | type       | [/webapp/view/api/errors.html#!/errors/not_found](/webapp/view/api/errors.html#!/errors/not_found)        | | status     | 404 (Not Found)|  <span id=\"!/errors/optimistic_lock\"></span>  ### \"optimistic_lock\": optimistic lock error  |            |                                       | |------------|---------------------------------------| | description | Optimistic Lock error. This appears if an entity you tried to modify has been modified by someone else in the meantime. See 'Optimistic Locking' in the 'API operations sample' section of the docs.                  | | type       | [/webapp/view/api/errors.html#!/errors/optimistic_lock](/webapp/view/api/errors.html#!/errors/optimistic_lock)        | | status     | 409 (Conflict)| | instance | URI to affected entity if available |  <span id=\"!/errors/persistence\"></span>  ### \"persistence\": persistence error  |            |                                       | |------------|---------------------------------------| | description | Catchall for persistence related problems that are not covered by more specific errors. In some cases it is sufficient to try again after a short time, but if the problem persists please contact support.                  | | type       | [/webapp/view/api/errors.html#!/errors/persistence](/webapp/view/api/errors.html#!/errors/persistence)        | | status     | 409 (Conflict)|  <span id=\"!/errors/unauthorized\"></span>  ### \"unauthorized\": missing permission  |            |                                       | |------------|---------------------------------------| | description | Authorization or authentication problem                  | | type       | [/webapp/view/api/errors.html#!/errors/unauthorized](/webapp/view/api/errors.html#!/errors/unauthorized)        | | status     | 401 (Unauthorized)|  <span id=\"!/errors/unexpected\"></span>  ### \"unexpected\": unexpected error  |            |                                       | |------------|---------------------------------------| | description | Catchall error for everything that is not covered by more specific errors. This is typically caused by a bug in weclapp.                  | | type       | [/webapp/view/api/errors.html#!/errors/unexpected](/webapp/view/api/errors.html#!/errors/unexpected)        | | status     | 500 (Internal Server Error)|  <span id=\"!/errors/validation\"></span>  ### \"validation\": validation failed  |            |                                       | |------------|---------------------------------------| | description | The input (entity properties / URL parameters) is malformed or not allowed in this context                  | | type       | [/webapp/view/api/errors.html#!/errors/validation](/webapp/view/api/errors.html#!/errors/validation)        | | status     | 400 (Bad Request)| | validationErrors | validation errors |  ## Validation error reference   <span id=\"!/validation/authorization\"></span>  ### \"authorization\": no authorization to access property or referenced entity  |            |                                       | |------------|---------------------------------------| | description | The client lacks authorization to access the property or referenced entity                  | | type       | [/webapp/view/api/errors.html#!/validation/authorization](/webapp/view/api/errors.html#!/validation/authorization)        |  <span id=\"!/validation/blocked\"></span>  ### \"blocked\": operation was blocked  |            |                                       | |------------|---------------------------------------| | description | The operation was blocked by referenced entities                  | | type       | [/webapp/view/api/errors.html#!/validation/blocked](/webapp/view/api/errors.html#!/validation/blocked)        |  <span id=\"!/validation/consistency\"></span>  ### \"consistency\": values are inconsistent  |            |                                       | |------------|---------------------------------------| | description | The given values are inconsistent (general, unspecific error)                  | | type       | [/webapp/view/api/errors.html#!/validation/consistency](/webapp/view/api/errors.html#!/validation/consistency)        |  <span id=\"!/validation/digits\"></span>  ### \"digits\": maximum number of digits exceeded  |            |                                       | |------------|---------------------------------------| | description | The numerical value given has more than the allowed maximum number of integer and/or fractional digits                  | | type       | [/webapp/view/api/errors.html#!/validation/digits](/webapp/view/api/errors.html#!/validation/digits)        | | allowed | maximum allowed integer digits, maximum allowed fraction digits |  <span id=\"!/validation/duplicate\"></span>  ### \"duplicate\": entity is a duplicate  |            |                                       | |------------|---------------------------------------| | description | The given (sub-)entity is a duplicate                  | | type       | [/webapp/view/api/errors.html#!/validation/duplicate](/webapp/view/api/errors.html#!/validation/duplicate)        |  <span id=\"!/validation/email\"></span>  ### \"email\": not a well-formed email  |            |                                       | |------------|---------------------------------------| | description | The value given is not a well-formed email address                  | | type       | [/webapp/view/api/errors.html#!/validation/email](/webapp/view/api/errors.html#!/validation/email)        |  <span id=\"!/validation/email_or_domain\"></span>  ### \"email_or_domain\": not a well-formed email or domain  |            |                                       | |------------|---------------------------------------| | description | The value given is not a well-formed email address or internet domain name                  | | type       | [/webapp/view/api/errors.html#!/validation/email_or_domain](/webapp/view/api/errors.html#!/validation/email_or_domain)        |  <span id=\"!/validation/empty\"></span>  ### \"empty\": value must be empty  |            |                                       | |------------|---------------------------------------| | description | The value given must be left blank in this context, but is present                  | | type       | [/webapp/view/api/errors.html#!/validation/empty](/webapp/view/api/errors.html#!/validation/empty)        |  <span id=\"!/validation/enum\"></span>  ### \"enum\": unsupported enum value  |            |                                       | |------------|---------------------------------------| | description | The given enum value is unknown or unsupported in this context                  | | type       | [/webapp/view/api/errors.html#!/validation/enum](/webapp/view/api/errors.html#!/validation/enum)        | | allowed | all known / allowed (enum) values |  <span id=\"!/validation/future\"></span>  ### \"future\": timestamp has to be in the future  |            |                                       | |------------|---------------------------------------| | description | The given timestamp should be in the future but is not                  | | type       | [/webapp/view/api/errors.html#!/validation/future](/webapp/view/api/errors.html#!/validation/future)        |  <span id=\"!/validation/greater_than\"></span>  ### \"greater_than\": value has to be above allowed limit  |            |                                       | |------------|---------------------------------------| | description | The numerical value given has to be larger than the allowed limit                  | | type       | [/webapp/view/api/errors.html#!/validation/greater_than](/webapp/view/api/errors.html#!/validation/greater_than)        | | allowed | lower limit (excluded) |  <span id=\"!/validation/less_than\"></span>  ### \"less_than\": value has to be below allowed limit  |            |                                       | |------------|---------------------------------------| | description | The numerical value given has to be smaller than the allowed limit                  | | type       | [/webapp/view/api/errors.html#!/validation/less_than](/webapp/view/api/errors.html#!/validation/less_than)        | | allowed | upper limit (excluded) |  <span id=\"!/validation/max\"></span>  ### \"max\": value is above allowed maximum  |            |                                       | |------------|---------------------------------------| | description | The numerical value given is larger than the allowed maximum                  | | type       | [/webapp/view/api/errors.html#!/validation/max](/webapp/view/api/errors.html#!/validation/max)        | | allowed | maximum allowed value |  <span id=\"!/validation/min\"></span>  ### \"min\": value is below allowed minimum  |            |                                       | |------------|---------------------------------------| | description | The numerical value given is smaller than the allowed minimum                  | | type       | [/webapp/view/api/errors.html#!/validation/min](/webapp/view/api/errors.html#!/validation/min)        | | allowed | minimum allowed value |  <span id=\"!/validation/not_empty\"></span>  ### \"not_empty\": value must not be empty  |            |                                       | |------------|---------------------------------------| | description | The value given is required, but is missing or blank                  | | type       | [/webapp/view/api/errors.html#!/validation/not_empty](/webapp/view/api/errors.html#!/validation/not_empty)        |  <span id=\"!/validation/past\"></span>  ### \"past\": timestamp has to be in the past  |            |                                       | |------------|---------------------------------------| | description | The given timestamp should be in the past but is not                  | | type       | [/webapp/view/api/errors.html#!/validation/past](/webapp/view/api/errors.html#!/validation/past)        |  <span id=\"!/validation/pattern\"></span>  ### \"pattern\": value has to conform to a specific pattern  |            |                                       | |------------|---------------------------------------| | description | The text given does not conform to the allowed pattern                  | | type       | [/webapp/view/api/errors.html#!/validation/pattern](/webapp/view/api/errors.html#!/validation/pattern)        | | allowed | the pattern (regular expression) |  <span id=\"!/validation/reference\"></span>  ### \"reference\": referenced entity not found  |            |                                       | |------------|---------------------------------------| | description | The referenced entity could not be found                  | | type       | [/webapp/view/api/errors.html#!/validation/reference](/webapp/view/api/errors.html#!/validation/reference)        |  <span id=\"!/validation/size\"></span>  ### \"size\": size is outside allowed range  |            |                                       | |------------|---------------------------------------| | description | The text or collection given has not enough or too many characters or elements                  | | type       | [/webapp/view/api/errors.html#!/validation/size](/webapp/view/api/errors.html#!/validation/size)        | | allowed | minimum size, maximum size | 

    The version of the OpenAPI document: 1
    Contact: support@weclapp.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.address import Address
from openapi_client.models.commission_sales_partner import CommissionSalesPartner
from openapi_client.models.commission_type import CommissionType
from openapi_client.models.custom_attribute import CustomAttribute
from openapi_client.models.customer_business_type import CustomerBusinessType
from openapi_client.models.customer_satisfaction import CustomerSatisfaction
from openapi_client.models.distribution_channel import DistributionChannel
from openapi_client.models.entity import Entity
from openapi_client.models.lead_status import LeadStatus
from openapi_client.models.online_account import OnlineAccount
from openapi_client.models.only_id import OnlyId
from openapi_client.models.party_bank_account import PartyBankAccount
from openapi_client.models.party_email_addresses import PartyEmailAddresses
from openapi_client.models.party_habitual_exporter_letter_of_intent import PartyHabitualExporterLetterOfIntent
from openapi_client.models.party_type import PartyType
from openapi_client.models.sales_order_payment_type import SalesOrderPaymentType
from openapi_client.models.sales_stage_history import SalesStageHistory
from openapi_client.models.salutation import Salutation
from typing import Optional, Set
from typing_extensions import Self

class Party(BaseModel):
    """
    Party
    """ # noqa: E501
    id: Optional[StrictStr] = None
    created_date: Optional[StrictInt] = Field(default=None, alias="createdDate")
    last_modified_date: Optional[StrictInt] = Field(default=None, alias="lastModifiedDate")
    version: Optional[StrictStr] = None
    custom_attributes: Optional[List[CustomAttribute]] = Field(default=None, alias="customAttributes")
    addresses: Optional[List[Address]] = None
    birth_date: Optional[StrictInt] = Field(default=None, alias="birthDate")
    company: Optional[StrictStr] = None
    company2: Optional[StrictStr] = None
    delivery_address_id: Optional[StrictStr] = Field(default=None, alias="deliveryAddressId")
    email: Optional[StrictStr] = None
    fax: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    invoice_address_id: Optional[StrictStr] = Field(default=None, alias="invoiceAddressId")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    middle_name: Optional[StrictStr] = Field(default=None, alias="middleName")
    mobile_phone1: Optional[StrictStr] = Field(default=None, alias="mobilePhone1")
    online_accounts: Optional[List[OnlineAccount]] = Field(default=None, alias="onlineAccounts")
    party_type: Optional[PartyType] = Field(default=None, alias="partyType")
    person_company: Optional[StrictStr] = Field(default=None, alias="personCompany")
    person_department_id: Optional[StrictStr] = Field(default=None, alias="personDepartmentId")
    person_role_id: Optional[StrictStr] = Field(default=None, alias="personRoleId")
    phone: Optional[StrictStr] = None
    primary_address_id: Optional[StrictStr] = Field(default=None, alias="primaryAddressId")
    salutation: Optional[Salutation] = None
    tags: Optional[List[StrictStr]] = None
    title: Optional[StrictStr] = None
    title_id: Optional[StrictStr] = Field(default=None, alias="titleId")
    website: Optional[StrictStr] = None
    bank_accounts: Optional[List[PartyBankAccount]] = Field(default=None, alias="bankAccounts")
    commercial_language_id: Optional[StrictStr] = Field(default=None, alias="commercialLanguageId")
    commission_sales_partners: Optional[List[CommissionSalesPartner]] = Field(default=None, alias="commissionSalesPartners")
    company_size_id: Optional[StrictStr] = Field(default=None, alias="companySizeId")
    company_size_name: Optional[StrictStr] = Field(default=None, alias="companySizeName")
    competitor: Optional[StrictBool] = None
    contacts: Optional[List[OnlyId]] = None
    currency_id: Optional[StrictStr] = Field(default=None, alias="currencyId")
    currency_name: Optional[StrictStr] = Field(default=None, alias="currencyName")
    customer: Optional[StrictBool] = None
    customer_amount_insured: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="customerAmountInsured")
    customer_annual_revenue: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="customerAnnualRevenue")
    customer_block_notice: Optional[StrictStr] = Field(default=None, alias="customerBlockNotice")
    customer_blocked: Optional[StrictBool] = Field(default=None, alias="customerBlocked")
    customer_business_type: Optional[CustomerBusinessType] = Field(default=None, alias="customerBusinessType")
    customer_category_id: Optional[StrictStr] = Field(default=None, alias="customerCategoryId")
    customer_category_name: Optional[StrictStr] = Field(default=None, alias="customerCategoryName")
    customer_credit_limit: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="customerCreditLimit")
    customer_current_sales_stage_id: Optional[StrictStr] = Field(default=None, alias="customerCurrentSalesStageId")
    customer_current_sales_stage_name: Optional[StrictStr] = Field(default=None, alias="customerCurrentSalesStageName")
    customer_debtor_account_id: Optional[StrictStr] = Field(default=None, alias="customerDebtorAccountId")
    customer_debtor_account_number: Optional[StrictStr] = Field(default=None, alias="customerDebtorAccountNumber")
    customer_debtor_accounting_code_id: Optional[StrictStr] = Field(default=None, alias="customerDebtorAccountingCodeId")
    customer_default_header_discount: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="customerDefaultHeaderDiscount")
    customer_default_header_surcharge: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="customerDefaultHeaderSurcharge")
    customer_default_shipping_carrier_id: Optional[StrictStr] = Field(default=None, alias="customerDefaultShippingCarrierId")
    customer_delivery_block: Optional[StrictBool] = Field(default=None, alias="customerDeliveryBlock")
    customer_insolvent: Optional[StrictBool] = Field(default=None, alias="customerInsolvent")
    customer_insured: Optional[StrictBool] = Field(default=None, alias="customerInsured")
    customer_internal_note: Optional[StrictStr] = Field(default=None, alias="customerInternalNote")
    customer_loss_description: Optional[StrictStr] = Field(default=None, alias="customerLossDescription")
    customer_loss_reason_id: Optional[StrictStr] = Field(default=None, alias="customerLossReasonId")
    customer_loss_reason_name: Optional[StrictStr] = Field(default=None, alias="customerLossReasonName")
    customer_non_standard_tax_id: Optional[StrictStr] = Field(default=None, alias="customerNonStandardTaxId")
    customer_number: Optional[StrictStr] = Field(default=None, alias="customerNumber")
    customer_number_old: Optional[StrictStr] = Field(default=None, alias="customerNumberOld")
    customer_payment_method_id: Optional[StrictStr] = Field(default=None, alias="customerPaymentMethodId")
    customer_payment_method_name: Optional[StrictStr] = Field(default=None, alias="customerPaymentMethodName")
    customer_sales_channel: Optional[DistributionChannel] = Field(default=None, alias="customerSalesChannel")
    customer_sales_order_payment_type: Optional[SalesOrderPaymentType] = Field(default=None, alias="customerSalesOrderPaymentType")
    customer_sales_probability: Optional[StrictInt] = Field(default=None, alias="customerSalesProbability")
    customer_sales_stage_history: Optional[List[SalesStageHistory]] = Field(default=None, alias="customerSalesStageHistory")
    customer_satisfaction: Optional[CustomerSatisfaction] = Field(default=None, alias="customerSatisfaction")
    customer_shipment_method_id: Optional[StrictStr] = Field(default=None, alias="customerShipmentMethodId")
    customer_shipment_method_name: Optional[StrictStr] = Field(default=None, alias="customerShipmentMethodName")
    customer_supplier_number: Optional[StrictStr] = Field(default=None, alias="customerSupplierNumber")
    customer_term_of_payment_id: Optional[StrictStr] = Field(default=None, alias="customerTermOfPaymentId")
    customer_term_of_payment_name: Optional[StrictStr] = Field(default=None, alias="customerTermOfPaymentName")
    customer_use_customs_tariff_number: Optional[StrictBool] = Field(default=None, alias="customerUseCustomsTariffNumber")
    delivery_email_addresses_id: Optional[StrictStr] = Field(default=None, alias="deliveryEmailAddressesId")
    description: Optional[StrictStr] = None
    dunning_address_id: Optional[StrictStr] = Field(default=None, alias="dunningAddressId")
    dunning_email_addresses_id: Optional[StrictStr] = Field(default=None, alias="dunningEmailAddressesId")
    enable_dropshipping_in_new_supply_sources: Optional[StrictBool] = Field(default=None, alias="enableDropshippingInNewSupplySources")
    eori_number: Optional[StrictStr] = Field(default=None, alias="eoriNumber")
    factoring: Optional[StrictBool] = None
    fix_phone2: Optional[StrictStr] = Field(default=None, alias="fixPhone2")
    fixed_responsible_user: Optional[StrictBool] = Field(default=None, alias="fixedResponsibleUser")
    former_sales_partner: Optional[StrictBool] = Field(default=None, alias="formerSalesPartner")
    habitual_exporter: Optional[StrictBool] = Field(default=None, alias="habitualExporter")
    image_id: Optional[StrictStr] = Field(default=None, alias="imageId")
    invoice_block: Optional[StrictBool] = Field(default=None, alias="invoiceBlock")
    invoice_recipient_id: Optional[StrictStr] = Field(default=None, alias="invoiceRecipientId")
    lead_rating_id: Optional[StrictStr] = Field(default=None, alias="leadRatingId")
    lead_rating_name: Optional[StrictStr] = Field(default=None, alias="leadRatingName")
    lead_source_id: Optional[StrictStr] = Field(default=None, alias="leadSourceId")
    lead_source_name: Optional[StrictStr] = Field(default=None, alias="leadSourceName")
    lead_status: Optional[LeadStatus] = Field(default=None, alias="leadStatus")
    legal_form_id: Optional[StrictStr] = Field(default=None, alias="legalFormId")
    legal_form_name: Optional[StrictStr] = Field(default=None, alias="legalFormName")
    mobile_phone2: Optional[StrictStr] = Field(default=None, alias="mobilePhone2")
    opt_in_email: Optional[StrictBool] = Field(default=None, alias="optInEmail")
    opt_in_letter: Optional[StrictBool] = Field(default=None, alias="optInLetter")
    opt_in_phone: Optional[StrictBool] = Field(default=None, alias="optInPhone")
    opt_in_sms: Optional[StrictBool] = Field(default=None, alias="optInSms")
    parent_party_id: Optional[StrictStr] = Field(default=None, alias="parentPartyId")
    party_email_addresses: Optional[List[PartyEmailAddresses]] = Field(default=None, alias="partyEmailAddresses")
    party_habitual_exporter_letters_of_intent: Optional[List[PartyHabitualExporterLetterOfIntent]] = Field(default=None, alias="partyHabitualExporterLettersOfIntent")
    phone_home: Optional[StrictStr] = Field(default=None, alias="phoneHome")
    primary_contact_id: Optional[StrictStr] = Field(default=None, alias="primaryContactId")
    purchase_email_addresses_id: Optional[StrictStr] = Field(default=None, alias="purchaseEmailAddressesId")
    purchase_via_plafond: Optional[StrictBool] = Field(default=None, alias="purchaseViaPlafond")
    quotation_email_addresses_id: Optional[StrictStr] = Field(default=None, alias="quotationEmailAddressesId")
    rating_id: Optional[StrictStr] = Field(default=None, alias="ratingId")
    rating_name: Optional[StrictStr] = Field(default=None, alias="ratingName")
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    responsible_user_id: Optional[StrictStr] = Field(default=None, alias="responsibleUserId")
    responsible_user_username: Optional[StrictStr] = Field(default=None, alias="responsibleUserUsername")
    sales_invoice_email_addresses_id: Optional[StrictStr] = Field(default=None, alias="salesInvoiceEmailAddressesId")
    sales_order_email_addresses_id: Optional[StrictStr] = Field(default=None, alias="salesOrderEmailAddressesId")
    sales_partner: Optional[StrictBool] = Field(default=None, alias="salesPartner")
    sales_partner_default_commission_fix: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="salesPartnerDefaultCommissionFix")
    sales_partner_default_commission_percentage: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="salesPartnerDefaultCommissionPercentage")
    sales_partner_default_commission_type: Optional[CommissionType] = Field(default=None, alias="salesPartnerDefaultCommissionType")
    sector_id: Optional[StrictStr] = Field(default=None, alias="sectorId")
    sector_name: Optional[StrictStr] = Field(default=None, alias="sectorName")
    supplier: Optional[StrictBool] = None
    supplier_creditor_account_id: Optional[StrictStr] = Field(default=None, alias="supplierCreditorAccountId")
    supplier_creditor_account_number: Optional[StrictStr] = Field(default=None, alias="supplierCreditorAccountNumber")
    supplier_creditor_accounting_code_id: Optional[StrictStr] = Field(default=None, alias="supplierCreditorAccountingCodeId")
    supplier_customer_number_at_supplier: Optional[StrictStr] = Field(default=None, alias="supplierCustomerNumberAtSupplier")
    supplier_default_shipping_carrier_id: Optional[StrictStr] = Field(default=None, alias="supplierDefaultShippingCarrierId")
    supplier_internal_note: Optional[StrictStr] = Field(default=None, alias="supplierInternalNote")
    supplier_minimum_purchase_order_amount: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, alias="supplierMinimumPurchaseOrderAmount")
    supplier_non_standard_tax_id: Optional[StrictStr] = Field(default=None, alias="supplierNonStandardTaxId")
    supplier_number: Optional[StrictStr] = Field(default=None, alias="supplierNumber")
    supplier_number_old: Optional[StrictStr] = Field(default=None, alias="supplierNumberOld")
    supplier_order_block: Optional[StrictBool] = Field(default=None, alias="supplierOrderBlock")
    supplier_payment_method_id: Optional[StrictStr] = Field(default=None, alias="supplierPaymentMethodId")
    supplier_payment_method_name: Optional[StrictStr] = Field(default=None, alias="supplierPaymentMethodName")
    supplier_shipment_method_id: Optional[StrictStr] = Field(default=None, alias="supplierShipmentMethodId")
    supplier_shipment_method_name: Optional[StrictStr] = Field(default=None, alias="supplierShipmentMethodName")
    supplier_term_of_payment_id: Optional[StrictStr] = Field(default=None, alias="supplierTermOfPaymentId")
    supplier_term_of_payment_name: Optional[StrictStr] = Field(default=None, alias="supplierTermOfPaymentName")
    tax_id: Optional[StrictStr] = Field(default=None, alias="taxId")
    topics: Optional[List[Entity]] = None
    vat_identification_number: Optional[StrictStr] = Field(default=None, alias="vatIdentificationNumber")
    x_rechnung_leitweg_id: Optional[StrictStr] = Field(default=None, alias="xRechnungLeitwegId")
    __properties: ClassVar[List[str]] = ["id", "createdDate", "lastModifiedDate", "version", "customAttributes", "addresses", "birthDate", "company", "company2", "deliveryAddressId", "email", "fax", "firstName", "invoiceAddressId", "lastName", "middleName", "mobilePhone1", "onlineAccounts", "partyType", "personCompany", "personDepartmentId", "personRoleId", "phone", "primaryAddressId", "salutation", "tags", "title", "titleId", "website", "bankAccounts", "commercialLanguageId", "commissionSalesPartners", "companySizeId", "companySizeName", "competitor", "contacts", "currencyId", "currencyName", "customer", "customerAmountInsured", "customerAnnualRevenue", "customerBlockNotice", "customerBlocked", "customerBusinessType", "customerCategoryId", "customerCategoryName", "customerCreditLimit", "customerCurrentSalesStageId", "customerCurrentSalesStageName", "customerDebtorAccountId", "customerDebtorAccountNumber", "customerDebtorAccountingCodeId", "customerDefaultHeaderDiscount", "customerDefaultHeaderSurcharge", "customerDefaultShippingCarrierId", "customerDeliveryBlock", "customerInsolvent", "customerInsured", "customerInternalNote", "customerLossDescription", "customerLossReasonId", "customerLossReasonName", "customerNonStandardTaxId", "customerNumber", "customerNumberOld", "customerPaymentMethodId", "customerPaymentMethodName", "customerSalesChannel", "customerSalesOrderPaymentType", "customerSalesProbability", "customerSalesStageHistory", "customerSatisfaction", "customerShipmentMethodId", "customerShipmentMethodName", "customerSupplierNumber", "customerTermOfPaymentId", "customerTermOfPaymentName", "customerUseCustomsTariffNumber", "deliveryEmailAddressesId", "description", "dunningAddressId", "dunningEmailAddressesId", "enableDropshippingInNewSupplySources", "eoriNumber", "factoring", "fixPhone2", "fixedResponsibleUser", "formerSalesPartner", "habitualExporter", "imageId", "invoiceBlock", "invoiceRecipientId", "leadRatingId", "leadRatingName", "leadSourceId", "leadSourceName", "leadStatus", "legalFormId", "legalFormName", "mobilePhone2", "optInEmail", "optInLetter", "optInPhone", "optInSms", "parentPartyId", "partyEmailAddresses", "partyHabitualExporterLettersOfIntent", "phoneHome", "primaryContactId", "purchaseEmailAddressesId", "purchaseViaPlafond", "quotationEmailAddressesId", "ratingId", "ratingName", "referenceNumber", "responsibleUserId", "responsibleUserUsername", "salesInvoiceEmailAddressesId", "salesOrderEmailAddressesId", "salesPartner", "salesPartnerDefaultCommissionFix", "salesPartnerDefaultCommissionPercentage", "salesPartnerDefaultCommissionType", "sectorId", "sectorName", "supplier", "supplierCreditorAccountId", "supplierCreditorAccountNumber", "supplierCreditorAccountingCodeId", "supplierCustomerNumberAtSupplier", "supplierDefaultShippingCarrierId", "supplierInternalNote", "supplierMinimumPurchaseOrderAmount", "supplierNonStandardTaxId", "supplierNumber", "supplierNumberOld", "supplierOrderBlock", "supplierPaymentMethodId", "supplierPaymentMethodName", "supplierShipmentMethodId", "supplierShipmentMethodName", "supplierTermOfPaymentId", "supplierTermOfPaymentName", "taxId", "topics", "vatIdentificationNumber", "xRechnungLeitwegId"]

    @field_validator('customer_amount_insured')
    def customer_amount_insured_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,14})([.][0-9]{1,4})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,14})([.][0-9]{1,4})?$/")
        return value

    @field_validator('customer_annual_revenue')
    def customer_annual_revenue_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,13})([.][0-9]{1,5})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,13})([.][0-9]{1,5})?$/")
        return value

    @field_validator('customer_credit_limit')
    def customer_credit_limit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,14})([.][0-9]{1,4})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,14})([.][0-9]{1,4})?$/")
        return value

    @field_validator('customer_default_header_discount')
    def customer_default_header_discount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,13})([.][0-9]{1,5})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,13})([.][0-9]{1,5})?$/")
        return value

    @field_validator('customer_default_header_surcharge')
    def customer_default_header_surcharge_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,13})([.][0-9]{1,5})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,13})([.][0-9]{1,5})?$/")
        return value

    @field_validator('sales_partner_default_commission_fix')
    def sales_partner_default_commission_fix_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,13})([.][0-9]{1,5})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,13})([.][0-9]{1,5})?$/")
        return value

    @field_validator('sales_partner_default_commission_percentage')
    def sales_partner_default_commission_percentage_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,13})([.][0-9]{1,5})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,13})([.][0-9]{1,5})?$/")
        return value

    @field_validator('supplier_minimum_purchase_order_amount')
    def supplier_minimum_purchase_order_amount_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]{1,13})([.][0-9]{1,5})?$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,13})([.][0-9]{1,5})?$/")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Party from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_date",
            "last_modified_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in custom_attributes (list)
        _items = []
        if self.custom_attributes:
            for _item_custom_attributes in self.custom_attributes:
                if _item_custom_attributes:
                    _items.append(_item_custom_attributes.to_dict())
            _dict['customAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in addresses (list)
        _items = []
        if self.addresses:
            for _item_addresses in self.addresses:
                if _item_addresses:
                    _items.append(_item_addresses.to_dict())
            _dict['addresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in online_accounts (list)
        _items = []
        if self.online_accounts:
            for _item_online_accounts in self.online_accounts:
                if _item_online_accounts:
                    _items.append(_item_online_accounts.to_dict())
            _dict['onlineAccounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in bank_accounts (list)
        _items = []
        if self.bank_accounts:
            for _item_bank_accounts in self.bank_accounts:
                if _item_bank_accounts:
                    _items.append(_item_bank_accounts.to_dict())
            _dict['bankAccounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in commission_sales_partners (list)
        _items = []
        if self.commission_sales_partners:
            for _item_commission_sales_partners in self.commission_sales_partners:
                if _item_commission_sales_partners:
                    _items.append(_item_commission_sales_partners.to_dict())
            _dict['commissionSalesPartners'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in contacts (list)
        _items = []
        if self.contacts:
            for _item_contacts in self.contacts:
                if _item_contacts:
                    _items.append(_item_contacts.to_dict())
            _dict['contacts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in customer_sales_stage_history (list)
        _items = []
        if self.customer_sales_stage_history:
            for _item_customer_sales_stage_history in self.customer_sales_stage_history:
                if _item_customer_sales_stage_history:
                    _items.append(_item_customer_sales_stage_history.to_dict())
            _dict['customerSalesStageHistory'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in party_email_addresses (list)
        _items = []
        if self.party_email_addresses:
            for _item_party_email_addresses in self.party_email_addresses:
                if _item_party_email_addresses:
                    _items.append(_item_party_email_addresses.to_dict())
            _dict['partyEmailAddresses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in party_habitual_exporter_letters_of_intent (list)
        _items = []
        if self.party_habitual_exporter_letters_of_intent:
            for _item_party_habitual_exporter_letters_of_intent in self.party_habitual_exporter_letters_of_intent:
                if _item_party_habitual_exporter_letters_of_intent:
                    _items.append(_item_party_habitual_exporter_letters_of_intent.to_dict())
            _dict['partyHabitualExporterLettersOfIntent'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in topics (list)
        _items = []
        if self.topics:
            for _item_topics in self.topics:
                if _item_topics:
                    _items.append(_item_topics.to_dict())
            _dict['topics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Party from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdDate": obj.get("createdDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "version": obj.get("version"),
            "customAttributes": [CustomAttribute.from_dict(_item) for _item in obj["customAttributes"]] if obj.get("customAttributes") is not None else None,
            "addresses": [Address.from_dict(_item) for _item in obj["addresses"]] if obj.get("addresses") is not None else None,
            "birthDate": obj.get("birthDate"),
            "company": obj.get("company"),
            "company2": obj.get("company2"),
            "deliveryAddressId": obj.get("deliveryAddressId"),
            "email": obj.get("email"),
            "fax": obj.get("fax"),
            "firstName": obj.get("firstName"),
            "invoiceAddressId": obj.get("invoiceAddressId"),
            "lastName": obj.get("lastName"),
            "middleName": obj.get("middleName"),
            "mobilePhone1": obj.get("mobilePhone1"),
            "onlineAccounts": [OnlineAccount.from_dict(_item) for _item in obj["onlineAccounts"]] if obj.get("onlineAccounts") is not None else None,
            "partyType": obj.get("partyType"),
            "personCompany": obj.get("personCompany"),
            "personDepartmentId": obj.get("personDepartmentId"),
            "personRoleId": obj.get("personRoleId"),
            "phone": obj.get("phone"),
            "primaryAddressId": obj.get("primaryAddressId"),
            "salutation": obj.get("salutation"),
            "tags": obj.get("tags"),
            "title": obj.get("title"),
            "titleId": obj.get("titleId"),
            "website": obj.get("website"),
            "bankAccounts": [PartyBankAccount.from_dict(_item) for _item in obj["bankAccounts"]] if obj.get("bankAccounts") is not None else None,
            "commercialLanguageId": obj.get("commercialLanguageId"),
            "commissionSalesPartners": [CommissionSalesPartner.from_dict(_item) for _item in obj["commissionSalesPartners"]] if obj.get("commissionSalesPartners") is not None else None,
            "companySizeId": obj.get("companySizeId"),
            "companySizeName": obj.get("companySizeName"),
            "competitor": obj.get("competitor"),
            "contacts": [OnlyId.from_dict(_item) for _item in obj["contacts"]] if obj.get("contacts") is not None else None,
            "currencyId": obj.get("currencyId"),
            "currencyName": obj.get("currencyName"),
            "customer": obj.get("customer"),
            "customerAmountInsured": obj.get("customerAmountInsured"),
            "customerAnnualRevenue": obj.get("customerAnnualRevenue"),
            "customerBlockNotice": obj.get("customerBlockNotice"),
            "customerBlocked": obj.get("customerBlocked"),
            "customerBusinessType": obj.get("customerBusinessType"),
            "customerCategoryId": obj.get("customerCategoryId"),
            "customerCategoryName": obj.get("customerCategoryName"),
            "customerCreditLimit": obj.get("customerCreditLimit"),
            "customerCurrentSalesStageId": obj.get("customerCurrentSalesStageId"),
            "customerCurrentSalesStageName": obj.get("customerCurrentSalesStageName"),
            "customerDebtorAccountId": obj.get("customerDebtorAccountId"),
            "customerDebtorAccountNumber": obj.get("customerDebtorAccountNumber"),
            "customerDebtorAccountingCodeId": obj.get("customerDebtorAccountingCodeId"),
            "customerDefaultHeaderDiscount": obj.get("customerDefaultHeaderDiscount"),
            "customerDefaultHeaderSurcharge": obj.get("customerDefaultHeaderSurcharge"),
            "customerDefaultShippingCarrierId": obj.get("customerDefaultShippingCarrierId"),
            "customerDeliveryBlock": obj.get("customerDeliveryBlock"),
            "customerInsolvent": obj.get("customerInsolvent"),
            "customerInsured": obj.get("customerInsured"),
            "customerInternalNote": obj.get("customerInternalNote"),
            "customerLossDescription": obj.get("customerLossDescription"),
            "customerLossReasonId": obj.get("customerLossReasonId"),
            "customerLossReasonName": obj.get("customerLossReasonName"),
            "customerNonStandardTaxId": obj.get("customerNonStandardTaxId"),
            "customerNumber": obj.get("customerNumber"),
            "customerNumberOld": obj.get("customerNumberOld"),
            "customerPaymentMethodId": obj.get("customerPaymentMethodId"),
            "customerPaymentMethodName": obj.get("customerPaymentMethodName"),
            "customerSalesChannel": obj.get("customerSalesChannel"),
            "customerSalesOrderPaymentType": obj.get("customerSalesOrderPaymentType"),
            "customerSalesProbability": obj.get("customerSalesProbability"),
            "customerSalesStageHistory": [SalesStageHistory.from_dict(_item) for _item in obj["customerSalesStageHistory"]] if obj.get("customerSalesStageHistory") is not None else None,
            "customerSatisfaction": obj.get("customerSatisfaction"),
            "customerShipmentMethodId": obj.get("customerShipmentMethodId"),
            "customerShipmentMethodName": obj.get("customerShipmentMethodName"),
            "customerSupplierNumber": obj.get("customerSupplierNumber"),
            "customerTermOfPaymentId": obj.get("customerTermOfPaymentId"),
            "customerTermOfPaymentName": obj.get("customerTermOfPaymentName"),
            "customerUseCustomsTariffNumber": obj.get("customerUseCustomsTariffNumber"),
            "deliveryEmailAddressesId": obj.get("deliveryEmailAddressesId"),
            "description": obj.get("description"),
            "dunningAddressId": obj.get("dunningAddressId"),
            "dunningEmailAddressesId": obj.get("dunningEmailAddressesId"),
            "enableDropshippingInNewSupplySources": obj.get("enableDropshippingInNewSupplySources"),
            "eoriNumber": obj.get("eoriNumber"),
            "factoring": obj.get("factoring"),
            "fixPhone2": obj.get("fixPhone2"),
            "fixedResponsibleUser": obj.get("fixedResponsibleUser"),
            "formerSalesPartner": obj.get("formerSalesPartner"),
            "habitualExporter": obj.get("habitualExporter"),
            "imageId": obj.get("imageId"),
            "invoiceBlock": obj.get("invoiceBlock"),
            "invoiceRecipientId": obj.get("invoiceRecipientId"),
            "leadRatingId": obj.get("leadRatingId"),
            "leadRatingName": obj.get("leadRatingName"),
            "leadSourceId": obj.get("leadSourceId"),
            "leadSourceName": obj.get("leadSourceName"),
            "leadStatus": obj.get("leadStatus"),
            "legalFormId": obj.get("legalFormId"),
            "legalFormName": obj.get("legalFormName"),
            "mobilePhone2": obj.get("mobilePhone2"),
            "optInEmail": obj.get("optInEmail"),
            "optInLetter": obj.get("optInLetter"),
            "optInPhone": obj.get("optInPhone"),
            "optInSms": obj.get("optInSms"),
            "parentPartyId": obj.get("parentPartyId"),
            "partyEmailAddresses": [PartyEmailAddresses.from_dict(_item) for _item in obj["partyEmailAddresses"]] if obj.get("partyEmailAddresses") is not None else None,
            "partyHabitualExporterLettersOfIntent": [PartyHabitualExporterLetterOfIntent.from_dict(_item) for _item in obj["partyHabitualExporterLettersOfIntent"]] if obj.get("partyHabitualExporterLettersOfIntent") is not None else None,
            "phoneHome": obj.get("phoneHome"),
            "primaryContactId": obj.get("primaryContactId"),
            "purchaseEmailAddressesId": obj.get("purchaseEmailAddressesId"),
            "purchaseViaPlafond": obj.get("purchaseViaPlafond"),
            "quotationEmailAddressesId": obj.get("quotationEmailAddressesId"),
            "ratingId": obj.get("ratingId"),
            "ratingName": obj.get("ratingName"),
            "referenceNumber": obj.get("referenceNumber"),
            "responsibleUserId": obj.get("responsibleUserId"),
            "responsibleUserUsername": obj.get("responsibleUserUsername"),
            "salesInvoiceEmailAddressesId": obj.get("salesInvoiceEmailAddressesId"),
            "salesOrderEmailAddressesId": obj.get("salesOrderEmailAddressesId"),
            "salesPartner": obj.get("salesPartner"),
            "salesPartnerDefaultCommissionFix": obj.get("salesPartnerDefaultCommissionFix"),
            "salesPartnerDefaultCommissionPercentage": obj.get("salesPartnerDefaultCommissionPercentage"),
            "salesPartnerDefaultCommissionType": obj.get("salesPartnerDefaultCommissionType"),
            "sectorId": obj.get("sectorId"),
            "sectorName": obj.get("sectorName"),
            "supplier": obj.get("supplier"),
            "supplierCreditorAccountId": obj.get("supplierCreditorAccountId"),
            "supplierCreditorAccountNumber": obj.get("supplierCreditorAccountNumber"),
            "supplierCreditorAccountingCodeId": obj.get("supplierCreditorAccountingCodeId"),
            "supplierCustomerNumberAtSupplier": obj.get("supplierCustomerNumberAtSupplier"),
            "supplierDefaultShippingCarrierId": obj.get("supplierDefaultShippingCarrierId"),
            "supplierInternalNote": obj.get("supplierInternalNote"),
            "supplierMinimumPurchaseOrderAmount": obj.get("supplierMinimumPurchaseOrderAmount"),
            "supplierNonStandardTaxId": obj.get("supplierNonStandardTaxId"),
            "supplierNumber": obj.get("supplierNumber"),
            "supplierNumberOld": obj.get("supplierNumberOld"),
            "supplierOrderBlock": obj.get("supplierOrderBlock"),
            "supplierPaymentMethodId": obj.get("supplierPaymentMethodId"),
            "supplierPaymentMethodName": obj.get("supplierPaymentMethodName"),
            "supplierShipmentMethodId": obj.get("supplierShipmentMethodId"),
            "supplierShipmentMethodName": obj.get("supplierShipmentMethodName"),
            "supplierTermOfPaymentId": obj.get("supplierTermOfPaymentId"),
            "supplierTermOfPaymentName": obj.get("supplierTermOfPaymentName"),
            "taxId": obj.get("taxId"),
            "topics": [Entity.from_dict(_item) for _item in obj["topics"]] if obj.get("topics") is not None else None,
            "vatIdentificationNumber": obj.get("vatIdentificationNumber"),
            "xRechnungLeitwegId": obj.get("xRechnungLeitwegId")
        })
        return _obj


