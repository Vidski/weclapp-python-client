# openapi-client
# Getting Started


API Version: **[v1](v1.html)**


The weclapp REST API lets you integrate weclapp with other applications or services.

The specification for this version can be downloaded here:

| Format                          | Public                                                                           |
|---------------------------------|----------------------------------------------------------------------------------|
| swagger JSON                    | <a href=\"swagger.json\" download=\"weclapp-swagger.json\">Download</a> |
| OpenApi 3 JSON                  | <a href=\"openapi_v1.json\" download=\"weclapp-openapi.json\">Download</a> |
| OpenApi 3 YAML (with user docs) | <a href=\"openapi_v1.yaml\" download=\"weclapp-openapi.yaml\">Download</a> |



## What should I know before starting?

Our API is continuously being developed and improved, but we are still
trying to keep it as stable as possible. We try to only have changes
that are backwards compatible: usually the changes are only additions,
e.g. new resources are implemented or new properties are added to
existing resources. Sometimes breaking changes cannot be avoided, e.g.
when a new feature requires an incompatible change to the underlying
data model, all those changes will be documented in the change log.

## Security and Authentication

You must be a verified user to make API requests. You can authorize
against the API with an API token. The token is configurable in your
weclapp account under **My settings > API**. Authentication is
possible in multiple ways: If the request contains the session cookies
of a logged in weclapp session then the user and permissions of that
session are used. This is useful when testing the API in a web browser,
because then requests are “automatically” authenticated if weclapp is
used in another tab. But generally the API is not used from a browser or
with session cookies, instead there is an API token for each user that
can be used to authenticate requests. Each user can find his/her token
on the \"My Settings page\". The token should be kept secret like a
password. A user can also generate a new token at any time, doing that
invalidates all previous tokens. Authenticating using a token is
possible in two ways:

* the token can be sent using the AuthenticationToken header `AuthenticationToken: {api_token}`
* the standard HTTP Basic authentication can be used: the username needs to be `“*”` and the password is the token

## Using curl

```bash
curl -H \"AuthenticationToken:{api_token} https://<TENANT>.weclapp.com/webapp/api/v1...\"
```

Examples of how to use curl will be shown in each section of this API.

## Headers

This is a JSON-only API. You must supply a `Content-Type: application/json`
header on PUT and POST operations. You must set a
`Accept: application/json` header on all requests. You may get a
`text/plain` response in case of error, e.g. in case of a bad request, you
should treat this as an error you need to take action on.

## URLs

The base URL for the API is `https://<TENANT>.weclapp.com/webapp/api/v1/`
where `<TENANT>.weclapp.com` is the domain of the specific
weclapp instance. So each weclapp instance has its own API endpoints
which allow accessing data for that particular instance. The API
provides access to various resources like customers, sales orders,
articles etc.. Each of those resources implements a common set of
operations. The URLs and HTTP methods for the different resource
operations use the same pattern for all resources:

| Operation                     | HTTP Method | URL pattern                                                           |
|-------------------------------|-------------|-----------------------------------------------------------------------|
| Query/list instances          | GET         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>`       |
| total number of instances     | GET         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/count` |
| Get a specific instance by id | GET         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>` |
| Create a new instance         | POST        | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>`       |
| Update a specific instance    | PUT         | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>` |
| Delete a specific instance    | DELETE      | `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>` |

Not all resources support all of those operations. A general description
for each operation can be found in API operations by example, and
details for each resource are described on the page for that resource.

## Additional operations

Some resources allow further operations or actions. Those operations can
be executed with a POST request, for some operations that only read data
it is also possible to use a GET request (this is documented for each
operation). For general operations for a resource the URL pattern is `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/<operation>`.
Some operations are instance specific, those use the following URL
pattern: `https://<TENANT>.weclapp.com/webapp/api/v1/<resource>/id/<id>/<operation>`.





## JSON

| Type                 | Representation in JSON                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| string               | Serialized as JSON string, empty strings (length 0 or only whitespace) are always interpreted as null, it is not possible to have a property with an empty string value.                                                                                                                                                                                                                       |
| boolean              | Serialized as `true` / `false`.                                                                                                                                                                                                                                                                                                                                                                |
| decimal number       | Most numbers in weclapp are decimal numbers with a fixed precision and scale (e.g. quantities or prices), they are serialized as JSON strings and not as JSON numbers to prevent accidental loss of precision when the JSON is deserialized with a JSON library that uses doubles to represent JSON numbers. The serialized numbers always use a “.” as the decimal mark (if one is required). |
| integers             | Integer numbers (that can safely be represented as a double) are serialized as JSON numbers.                                                                                                                                                                                                                                                                                                   |
| floats/doubles       | Serialized as JSON numbers.                                                                                                                                                                                                                                                                                                                                                                    |
| dates and timestamps | Serialized as the milliseconds since 1970-01-01T00:00:00Z (as a JSON number).                                                                                                                                                                                                                                                                                                                  |
| enums                | Sometimes a property value can be one of a fixed number of named options. Those enum properties are serialized as a JSON string with the name of the option.                                                                                                                                                                                                                                   |

The deserialization of data sent to the API is relatively lenient, for
example when a string is expected, but a number is given then that
number is used as the string and the other way around (if possible).
Properties with the value null are not serialized by default and when
sending data to the API it is also not necessary to include properties
whose value is null: all properties that are missing from the JSON
object but are expected are assumed to be `null`. To get all properties
including those with the value null the query parameter `serializeNulls`
can be added to the request URL, in that case null values are included
in the response.



## Error Responses

Any request on the weclapp API may return an error response, with a
structure conforming to [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807).
See the [API error reference](#errors) section for details.





## Change Policy

weclapp may modify the attributes and resources available to the API and
our policies related to access and use of the API from time to time
without advance notice. weclapp will use commercially reasonable efforts
to notify you of any modifications to the API or policies through
notifications or posts on the weclapp Developer Website. weclapp also
tracks deprecation of attributes of the API on its Changelog.
Modification of the API may have an adverse effect on weclapp
Applications, including but not limited to changing the manner in which
weclapp Applications communicate with the API and display or transmit
Your Data. weclapp will not be liable to you or any third party for such
modifications or any adverse effects resulting from such modifications



# API newsletter

Sign up here for our [API newsletter](https://340d89eb.sibforms.com/serve/MUIEAEREP3buQMWpwPwuVohmsPBikdVQIilNQeZ2DJBE5NZePFYqyp_62WSheCC5t_Q7eJ6SVpZBauqRY93L8L8Iquik5gaH40Bi0uOtPioS7U7k4JvemqVuSdvEV0A3DgygC5LOAv-kjuN4Ij5MUqzm5DSHYbmKvGucHMXpZMFGGA5Lwi5VUv6ZZbROGqZJCrGfYFxGttzVBqc_). We will inform you regularly about planned API changes.


# API operations sample

As mentioned previously
all resources implement common operations in the same way. In the
following all the common operations are explained for the `customer`
resource. The operations work in the same way for all other resources
(some resources don’t support all the operations), the differences
between the resources are mostly the data and the properties that are
required and used.

## Querying

The most common operation is querying or listing the existing entity
instances. This is possible with a `GET` request to the base URL of
a resource:



### `GET /customer`


```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer\"
```

**Output:**

```json
{
\"result\": [
{
\"id\": \"4342\",
\"version\": \"1\",
\"addresses\": [
{
\"id\": \"4344\",
\"version\": \"0\",
\"city\": \"München\",
\"countryCode\": \"DE\",
\"createdDate\": 1496828973904,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496828973903,
\"primeAddress\": true,
\"street1\": \"Mustergasse 7\",
\"zipcode\": \"80331 \"
}
],
\"blocked\": false,
\"company\": \"Muster GmbH\",
\"contacts\": [
{
\"id\": \"4332\",
\"version\": \"1\",
\"addresses\": [
{
\"id\": \"4334\",
\"version\": \"0\",
\"city\": \"München\",
\"countryCode\": \"DE\",
\"createdDate\": 1496828882836,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496828882836,
\"primeAddress\": true,
\"street1\": \"Fasanenweg 15\",
\"zipcode\": \"80331\"
}
],
\"createdDate\": 1496828882837,
\"email\": \"mustermann@beispiel.de\",
\"firstName\": \"Max\",
\"lastModifiedDate\": 1496828996245,
\"lastName\": \"Mustermann\",
\"partyType\": \"PERSON\",
\"personCompany\": \"Muster GmbH\",
\"salutation\": \"MR\"
}
],
\"createdDate\": 1496828973904,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\"
}
],
\"customerNumber\": \"C1006\",
\"customerTopics\": [],
\"deliveryBlock\": false,
\"insolvent\": false,
\"insured\": false,
\"lastModifiedDate\": 1496828996212,
\"optIn\": false,
\"partyType\": \"ORGANIZATION\",
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"sales@weclapp.com\",
\"salesChannel\": \"NET1\",
\"useCustomsTariffNumber\": false
}
]
}
```

In this case there is one
sales order with one order item. By default, all null values are
omitted, to include them the query parameter serializeNulls can be
used:



### `GET /customer?serializeNulls`



```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?serializeNulls\"
```

**Output:**

```json
{
\"result\": [
{
\"id\": \"4342\",
\"version\": \"1\",
\"addresses\": [
{
\"id\": \"4344\",
\"version\": \"0\",
\"city\": \"München\",
\"company\": null,
\"company2\": null,
\"countryCode\": \"DE\",
\"createdDate\": 1496828973904,
\"deliveryAddress\": false,
\"globalLocationNumber\": null,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496828973903,
\"postOfficeBoxCity\": null,
\"postOfficeBoxNumber\": null,
\"postOfficeBoxZipCode\": null,
\"primeAddress\": true,
\"state\": null,
\"street1\": \"Mustergasse 7\",
\"street2\": null,
\"zipcode\": \"80331 \"
}
],
\"amountInsured\": null,
\"annualRevenue\": null,
\"birthDate\": null,
\"blockNotice\": null,
\"blocked\": false,
\"commercialLanguageId\": null,
\"company\": \"Muster GmbH\",
\"company2\": null,
\"contacts\": [
{
\"id\": \"4332\",
\"version\": \"1\",
\"addresses\": [
{
\"id\": \"4334\",
\"version\": \"0\",
\"city\": \"München\",
\"company\": null,
\"company2\": null,
\"countryCode\": \"DE\",
\"createdDate\": 1496828882836,
\"deliveryAddress\": false,
\"globalLocationNumber\": null,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496828882836,
\"postOfficeBoxCity\": null,
\"postOfficeBoxNumber\": null,
\"postOfficeBoxZipCode\": null,
\"primeAddress\": true,
\"state\": null,
\"street1\": \"Fasanenweg 15\",
\"street2\": null,
\"zipcode\": \"80331\"
}
],
\"birthDate\": null,
\"company\": null,
\"company2\": null,
\"createdDate\": 1496828882837,
\"customAttributes\": null,
\"description\": null,
\"email\": \"mustermann@beispiel.de\",
\"fax\": null,
\"firstName\": \"Max\",
\"fixPhone2\": null,
\"lastModifiedDate\": 1496828996245,
\"lastName\": \"Mustermann\",
\"middleName\": null,
\"mobilePhone1\": null,
\"mobilePhone2\": null,
\"partyType\": \"PERSON\",
\"personCompany\": \"Muster GmbH\",
\"personDepartment\": null,
\"personRole\": null,
\"phone\": null,
\"phoneHome\": null,
\"salutation\": \"MR\",
\"title\": null,
\"website\": null
}
],
\"createdDate\": 1496828973904,
\"creditLimit\": null,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\",
\"booleanValue\": null,
\"dateValue\": null,
\"numberValue\": null,
\"selectedValueId\": null,
\"selectedValues\": null,
\"stringValue\": null
}
],
\"customerCategoryId\": null,
\"customerCategoryName\": null,
\"customerNumber\": \"C1006\",
\"customerRating\": null,
\"customerTopics\": [],
\"defaultHeaderDiscount\": null,
\"defaultHeaderSurcharge\": null,
\"deliveryBlock\": false,
\"description\": null,
\"email\": null,
\"fax\": null,
\"firstName\": null,
\"insolvent\": false,
\"insured\": false,
\"invoiceContactId\": null,
\"lastModifiedDate\": 1496828996212,
\"lastName\": null,
\"leadSourceId\": null,
\"leadSourceName\": null,
\"middleName\": null,
\"mobilePhone1\": null,
\"oldCustomerNumber\": null,
\"optIn\": false,
\"parentPartyId\": null,
\"partyType\": \"ORGANIZATION\",
\"paymentMethodId\": null,
\"paymentMethodName\": null,
\"personCompany\": null,
\"personDepartment\": null,
\"personRole\": null,
\"phone\": null,
\"primaryContactId\": null,
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"sales@weclapp.com\",
\"salesChannel\": \"NET1\",
\"salutation\": null,
\"satisfaction\": null,
\"sectorId\": null,
\"sectorName\": null,
\"shipmentMethodId\": null,
\"shipmentMethodName\": null,
\"termOfPaymentId\": null,
\"termOfPaymentName\": null,
\"title\": null,
\"useCustomsTariffNumber\": false,
\"vatRegistrationNumber\": null,
\"website\": null
}
]
}
```

## Pagination
By default the operation will not return all entity instances but only
the first 100, this can be changed by using the `pageSize` query parameter
with the number of desired results. But `pageSize` cannot be arbitrarily
high it is usually limited 1000 (exceptions to the default limits of 100
and 1000 are noted in the documentation for the specific resources). To
get further results it is necessary to skip entity instances, this is
done using the `page` query parameter. Examples:



### `GET /customer?pageSize=10`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?pageSize=10\"
```

returns at most 10 instances

### `GET /customer?page=2&pageSize=10`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?page=2&pageSize=10\"
```

returns the second page of results (the `page` parameter is one based, so
`page=1` is the first page, which is also the default). Using those two
parameters it is possible to implement pagination.

## Sorting

It is also possible to change the order of the returned results using
the `sort` parameter:

### `GET /customer?sort=lastModifiedDate`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?sort=lastModifiedDate\"
```

sort by `lastModifiedDate` (ascending).

### `GET /customer?sort=-lastModifiedDate`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?sort=-lastModifiedDate\"
```

sort by `lastModifiedDate` descending.

### `GET /customer?sort=lastModifiedDate,-salesChannel`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?sort=lastModifiedDate,-salesChannel\"
```

sort by `lastModifiedDate` (ascending) and then `salesChannel` descending.


It is generally possible to sort by most of the simple properties of an
entity. It is possible to combine multiple sort orders by combining the
property names with a comma. To sort in descending order just prepend a
minus to the property name. If an unsupported or unknown property is
specified then an error response is returned.

## Filtering

It is often desired to get just a subset of the data, for example just
the orders of a specific customer or created after a specific date. This
is possible using filtering query parameters:



### `GET /customer?salesChannel-eq=NET1`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?salesChannel-eq=NET1\"
```

customers for `salesChannel` `NET1`.

### `GET /customer?createdDate-gt=1398436281262`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer?createdDate-gt=1398436281262\"
```

customers created after the specified timestamp.

### `GET /customer?salesChannel-eq=NET1&createdDate-gt=1398436281262`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?salesChannel-eq=NET1&createdDate-gt=1398436281262\"
```

customers for `salesChannel` `NET1` and created after the specified timestamp.

### `GET /customer?customAttribute4587-eq=NEW`

```bash
curl -H \"\"\"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?customAttribute4587-eq=NEW\"
```

customers with the value `NEW` for `customAttribute` with id 4587.

### `GET /customer?customAttribute4587.entityReferences.entityId-eq=1234`

```bash
curl -H \"AuthenticationToken:<TOKEN>\"
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?customAttribute4587.entityReferences.entityId-eq=1234\"
```

customers with an entity reference to an entity with the id 1234 for the `customAttribute` with the id 4587.

### `GET /customAttributeDefinitions`

All attributeTypes are supported except `MULTISELECT_LIST`. CustomAttributes of attributeType `LIST` could be filtered by `customAttribute{customAttributeId}.id` or `customAttribute{customAttributeId}.value`.

### `GET /customer?customAttribute3387.value-eq=OPTION1`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?customAttribute3387.value-eq=OPTION1\"
```

customers with value `OPTION1` for `customAttribute` with id 3387.

A filtering query parameter consists of a property name and a filter
operator joined together with a minus. If multiple filtering query
parameter are specified then they are combined and the returned results
match all of them. Filtering query parameters for unknown properties or
properties that don’t support filtering are silently ignored.

The following filtering operators are supported (not all of them work
for all property types):

| Operator | Meaning                                                                                                                                                                                     |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eq       | equal                                                                                                                                                                                       |
| ne       | not equal                                                                                                                                                                                   |
| lt       | less than                                                                                                                                                                                   |
| gt       | greater than                                                                                                                                                                                |
| le       | less equal                                                                                                                                                                                  |
| ge       | greater equal                                                                                                                                                                               |
| null     | property is null (the query parameter value is ignored and can be omitted)                                                                                                                  |
| notnull  | property is not null (the query parameter value is ignored and can be omitted)                                                                                                              |
| like     | like expression (supports `%` and `_` as placeholders, similar to SQL LIKE)                                                                                                                 |
| notlike  | not like expression                                                                                                                                                                         |
| ilike    | like expression, ignoring case                                                                                                                                                              |
| notilike | not like expression, ignoring case                                                                                                                                                          |
| in       | the property value is in the specified list of values, the query parameter value must be a JSON array with the values in the correct type, for example `?customerNumber-in=[\"1006\",\"1007\"]` |
| notin    | the property value is not in the specified list of values                                                                                                                                   |

## \"Or\" condition filtering

In addition to the default behavior of linking filter expressions via \"and\" you can also link individual filter expressions via \"or\" by prefixing their parameter name with \"or-\":


### `GET /customer?or-name-eq=charlie&or-name-eq=chaplin`


```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?or-name-eq=charlie&or-name-eq=chaplin\"
```

The above example is the equivalent of the expression `(name equals \"charlie\") or (name equals \"chaplin\")`


For combining `or` and `and` clauses you may also group `or` expressions by using `or<groupname>-` instead of the plain `or-` prefix:


### `GET /customer?orGroup1-name-eq=charlie&orGroup1-name-eq=chaplin&orGroup2-responsibleUserUsername-eq=mrtest&orGroup2-referenceNumber=4711&commercialLanguageId-eq=12`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?orGroup1-name-eq=charlie&orGroup1-name-eq=chaplin&orGroup2-responsibleUserUsername-eq=mrtest&orGroup2-referenceNumber=4711&commercialLanguageId-eq=12\"
```

The above example is the equivalent of the expression

```
((name equals charlie) or (name equals chaplin)) and ((responsibleUserUsername equals \"mrtest\") or (referenceNumber equals \"4711\")) and (commercialLanguageId equals \"12\")
```

Technically, the default \"or-\" variant is just a special case of this, using the empty String as group name.


## Return only specific properties

Sometimes it is desirable to only fetch a subset of all properties, for
example to save bandwidth. This is possible by specifying the desired
properties using the `properties` query parameter:

### `GET /customer?properties=id,customerNumber,salesChannel`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?properties=id,customerNumber,salesChannel\"
```

**Output:**

```json
{
\"result\": [
{
\"id\": \"3346\",
\"customerNumber\": \"C1002\",
\"salesChannel\": \"NET1\"
}
]
}
```

It is also possible to specify property paths:

### `GET /customer?properties=id,customerNumber,salesChannel,contacts.id,contacts.lastName`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer?properties=id,customerNumber,salesChannel,contacts.id,contacts.lastName\"
```

If an unknown property or property path is specified then an error
response is returned.

```json
{
\"result\": [
{
\"id\": \"3346\",
\"contacts\": [
{
\"id\": \"3731\",
\"lastName\": \"Mustermann\"
}
],
\"customerNumber\": \"C1002\",
\"salesChannel\": \"NET1\"
}
]
}
```


## Combinations

The query parameters for pagination, sorting, filtering and returning
only specific properties can be combined to perform queries.


## Counting

To determine the total number of entity instances the count operation
can be used:

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/count\"
```

It is possible to use the filtering query parameters from the querying
operation with the count operation:

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/customer/count?salesChannel-eq=NET1\"
```

returns the number of customers for `salesChannel` `NET1`.


## Referenced entities

The API offers the possibility to get the referenced entities for a query result in the same request. This way you can
save subsequent requests and get all necessary and referenced data in one request. This feature can be used by simply
specifying the parameter `includeReferencedEntities` and the primary key references as comma separated list.
The API response will contain an additional object `referencedEntities`.


### `GET /article?includeReferencedEntities=unitId,articleCategoryId`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/article?includeReferencedEntities=unitId,articleCategoryId&properties=id,name,unitId,articleCategoryId\"
```

**Output:**

```json
{
\"result\": [
{
\"id\": \"3235\",
\"name\": \"Testartikel 1\",
\"unitId\": \"2770\"
},
{
\"id\": \"3236\",
\"name\": \"Testartikel 2\",
\"unitId\": \"2770\"
},
{
\"id\": \"3237\",
\"articleCategoryId\": \"7035\",
\"name\": \"Testartikel 3\",
\"unitId\": \"2770\"
}
],
\"referencedEntities\": {
\"unit\": [
{
\"id\": \"2770\",
\"version\": \"0\",
\"createdDate\": 1597915605986,
\"description\": \"Stück\",
\"lastModifiedDate\": 1597915605985,
\"name\": \"Stk.\"
}
],
\"articleCategory\": [
{
\"id\": \"7035\",
\"version\": \"0\",
\"createdDate\": 1619778730348,
\"lastModifiedDate\": 1619778730348,
\"name\": \"Demo-Gruppe\"
}
]
}
}
```

## Additional properties

In addition to the common properties, there are additional properties that can be optionally queried. These are
calculated or complexly determined and must therefore be explicitly queried.

To use this function, only the parameter `additionalProperties` and the names of the additional properties must be
specified as a comma-separated list. The response then contains the additional object `additionalProperties` with
the property and an array of values. The index of the value object in this list also represents the reference to the
respective entity.


### `GET /article?additionalProperties=currentSalesPrice`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
\"https://<TENANT>.weclapp.com/webapp/api/v1/article?additionalProperties=currentSalesPrice\"
```

**Output:**

```json
{
\"additionalProperties\": {
\"currentSalesPrice\": [
{
\"articleUnitPrice\": \"39.95\",
\"currencyId\": \"255\",
\"quantity\": \"1\",
\"reductionAdditionItems\": []
},
{
\"articleUnitPrice\": \"479.4\",
\"currencyId\": \"255\",
\"quantity\": \"1\",
\"reductionAdditionItems\": []
}
]
}
}
```


## Dry-Run

Generic `PUT`, `POST` and `DELETE` endpoints support to perform operations in a \"dry-run-mode\". Where possible, business logic
is executed and the data submitted by the requester is validated.
To use this functionality the requester can set the optional query parameter \"`dryRun`\" (boolean, default: `false`). The
return is as far as possible as with a productive execution, except that 200 \"ok\" is returned in case of success.
The meta properties (id, version, createdDate, lastModifiedDate) are not included in \"dry-run-responses\".

### `POST /salesOrder?dryRun=true`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
-H Content-Type: application/json \\
-X POST \"https://<TENANT>.weclapp.com/webapp/api/v1/salesOrder?dryRun=true\" \\
-d   '{ \"customerNumber\": \"4799\" }'
```

**Error Output:**

```json
{
\"detail\": \"customer not found\",
\"error\": \"customer not found\",
\"status\": 400,
\"title\": \"entity validation failed\",
\"type\": \"/webapp/view/api/errors.html#!/errors/validation\",
\"validationErrors\": [
{
\"detail\": \"referenced entity not found\",
\"instance\": \"salesOrder\",
\"location\": \"customerId\",
\"title\": \"referenced entity not found\",
\"type\": \"/webapp/view/api/errors.html#!/validation/reference\"
}
]
}
```

The response status will be 400 (Bad Request).

**Successful Output:**

```json
{
\"availability\": \"NOT_CHECKED\",
\"availabilityForAllWarehouses\": \"NOT_CHECKED\",
\"commissionSalesPartners\": [],
\"creatorId\": \"4451\",
\"currencyConversionDate\": 1699375721469,
\"currencyConversionRate\": \"1\",
\"customAttributes\": [],
\"customerId\": \"4799\",
\"customerNumber\": \"10000\",
\"deliveryAddress\": {
\"city\": \"Hithausen\",
\"company\": \"Beispiel AG\",
\"countryCode\": \"DE\",
\"street1\": \"Feldstraße 34\",
\"zipcode\": \"54321\"
},
\"deliveryEmailAddresses\": {
\"toAddresses\": \"info@beispielag.de\"
},
\"disableEmailTemplate\": false,
\"dispatchCountryCode\": \"DE\",
\"factoring\": false,
\"fulfillmentProviderId\": \"3335\",
\"grossAmount\": \"0\",
\"grossAmountInCompanyCurrency\": \"0\",
\"headerDiscount\": \"0\",
\"headerSurcharge\": \"0\",
\"invoiceAddress\": {
\"city\": \"Hithausen\",
\"company\": \"Beispiel AG\",
\"countryCode\": \"DE\",
\"street1\": \"Feldstraße 34\",
\"zipcode\": \"54321\"
},
\"invoiced\": false,
\"netAmount\": \"0\",
\"netAmountInCompanyCurrency\": \"0\",
\"nonStandardTaxId\": \"3492\",
\"nonStandardTaxName\": \"DE Steuerfrei Drittland (VK)\",
\"onlyServices\": false,
\"orderDate\": 1699311600000,
\"orderItems\": [],
\"paid\": false,
\"plannedShippingDate\": 1699311600000,
\"pricingDate\": 1699311600000,
\"projectMembers\": [],
\"projectModeActive\": false,
\"recordAddress\": {
\"city\": \"Hithausen\",
\"company\": \"Beispiel AG\",
\"countryCode\": \"DE\",
\"street1\": \"Feldstraße 34\",
\"zipcode\": \"54321\"
},
\"recordCurrencyId\": \"255\",
\"recordCurrencyName\": \"EUR\",
\"recordEmailAddresses\": {
\"toAddresses\": \"info@beispielag.de\"
},
\"responsibleUserId\": \"4748\",
\"responsibleUserUsername\": \"karsten.kunde@example.com\",
\"salesChannel\": \"NET1\",
\"salesInvoiceEmailAddresses\": {
\"toAddresses\": \"info@beispielag.de\"
},
\"salesOrderPaymentType\": \"STANDARD\",
\"sentToRecipient\": false,
\"servicesFinished\": false,
\"shipped\": false,
\"shippingCostItems\": [],
\"shippingLabelsCount\": 1,
\"status\": \"ORDER_ENTRY_IN_PROGRESS\",
\"statusHistory\": [
{
\"status\": \"ORDER_ENTRY_IN_PROGRESS\",
\"statusDate\": 1699375721472,
\"userId\": \"4451\"
}
],
\"tags\": [],
\"warehouseId\": \"4191\",
\"warehouseName\": \"Hauptlager\"
}
```

The response status will be 200 (OK).


## Optimistic locking

For the update operation the resources usually also support optimistic
locking using the `version` property: if the `version`
property is in the request body and it does not match the current `version`,
then the request fails with an optimistic lock error. In that case the
caller should again get the latest `version`, apply the changes and
try the request again.


## Basic Operations

The following entries will show you how to use the different basic
operations (`GET`, `POST`, `PUT`, `DELETE`) and what an exemplary response they
will give whether the operation was successful or not.


The following table will show you the HTTP status codes of the basic
operations if the operation was successful:

| Operation | HTTP status code |
|-----------|------------------|
| GET       | 200 (OK)         |
| POST      | 201 (Created)    |
| PUT       | 200 (OK)         |
| DELETE    | 204 (No Content) |

If you are not currently logged in to weclapp, you are using another
browser or the AuthenticationToken was wrong you will get a response of
`401 (Unauthorized)`.
It is possible to disable
the optimistic locking check by just omitting the `version` property, but
doing this might accidentally overwrite changes done by another user in the
meantime.

## Get a specific entity instance

Each entity instance has its own URL where it can be retrieved. The URL
is based on the entity id.

Performing a GET request on that URL returns the entity instance:

### `GET /customer/id/3346`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/3346\"
```

**Output:**

```json
{
\"result\": [
{
\"id\": \"3346\",
\"version\": \"2\",
\"addresses\": [
{
\"id\": \"3348\",
\"version\": \"0\",
\"countryCode\": \"DE\",
\"createdDate\": 1487765943229,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1487765943229,
\"primeAddress\": true
},
{
\"id\": \"3976\",
\"version\": \"0\",
\"company\": \"11111\",
\"company2\": \"22222\",
\"countryCode\": \"DE\",
\"createdDate\": 1496040807652,
\"deliveryAddress\": false,
\"globalLocationNumber\": \"gln\",
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496040807648,
\"primeAddress\": false
}
],
\"blocked\": false,
\"company\": \"Musterdaten GmbH\",
\"contacts\": [
{
\"id\": \"3377\",
\"version\": \"0\",
\"addresses\": [
{
\"id\": \"3379\",
\"version\": \"0\",
\"countryCode\": \"DE\",
\"createdDate\": 1487767121646,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1487767121645,
\"primeAddress\": true
}
],
\"createdDate\": 1487767121649,
\"firstName\": \"Max\",
\"lastModifiedDate\": 1487767121642,
\"lastName\": \"Mustermann\",
\"partyType\": \"PERSON\",
\"personCompany\": \"Musterdaten GmbH\",
\"salutation\": \"MR\"
}
],
\"createdDate\": 1487765943230,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\"
}
],
\"customerNumber\": \"C1002\",
\"customerTopics\": [],
\"deliveryBlock\": false,
\"insolvent\": false,
\"insured\": false,
\"lastModifiedDate\": 1496040807672,
\"optIn\": false,
\"partyType\": \"ORGANIZATION\",
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"@weclapp.com\",
\"salesChannel\": \"NET1\",
\"useCustomsTariffNumber\": false
}
]
}
```

## Create a new instance

Creating new instances is done by performing a POST request to the base URL of a resource.

The body for that request must have the same structure as the result of the \"get by id\" request, but usually not all properties need to be specified
and there are defaults for some properties. Here are some general notes:

* id, version, createdDate and lastModifiedDate can usually not be set by the client, so those values are ignored if they are specified
* references to other entities are often represented by two properties (usually id and some other more or less unique property of the referenced entity),
for example customer has currencyId and currencyName to reference the currency, when creating a new customer then it is not necessary
to specify both properties, one of them is usually enough as long as it specifies the referenced entity uniquely, if both are given then they
must not contradict each other
* usually some required properties have sensible defaults, so if those are not given or null then the default will be used
* boolean properties can be optional (default value would be set) or mandatory


### `POST /customer`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
-H Content-Type: application/json \\
-X POST \"https://<TENANT>.weclapp.com/webapp/api/v1/customer\" \\
-d   '{ \"customerNumber\": \"C1013\", \"partyType\": \"ORGANIZATION\", \"company\": \"Firma\" }'
```

**Output:**

```json
{
\"id\": \"4391\",
\"version\": \"0\",
\"addresses\": [
{
\"id\": \"4393\",
\"version\": \"0\",
\"countryCode\": \"DE\",
\"createdDate\": 1496840784272,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496840784272,
\"primeAddress\": true
}
],
\"blocked\": false,
\"company\": \"Firma\",
\"contacts\": [],
\"createdDate\": 1496840784273,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\"
}
],
\"customerNumber\": \"C1013\",
\"customerTopics\": [],
\"deliveryBlock\": false,
\"insolvent\": false,
\"insured\": false,
\"lastModifiedDate\": 1496840784270,
\"optIn\": false,
\"partyType\": \"ORGANIZATION\",
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"sales@weclapp.com\",
\"salesChannel\": \"NET1\",
\"useCustomsTariffNumber\": false
}
```

The response status will be 201 (Created) and the response will have a `Location` header pointing to the URL of the created instance.


## Update a specific instance

Updating an instances is done by performing a `PUT` request to the URL of the instance.

A successful response will have the status 200 (OK) and the response body will contain the updated entity.

Some special aspects must be considered when updating:

* the read-only properties like `createdDate` are ignored anyway, so they do not need to be given
* `id` and `version` are processed as follows: if the `id` is given it must match the `id` of the updated instance and if the `version` is given then optimistic locking is enabled (see below)
* for the references that use two properties it is again possible to specify only one of them, if both are given then they must not contradict each other
* for complete entity updates boolean properties are always mandatory and need to be passed

### Updating the complete entity

When updating it is generally necessary to specify all properties that are not `null`, all unspecified properties will be interpreted as `null`.

Since sometimes new properties are added to entities, it is strongly recommended that an API client always first gets the
latest version using `GET/customer/id/{id}`, then modifies that JSON and finally performs the `PUT` request. Doing this ensures that
new properties that the client does not know about are not accidentally overwritten with `null`.

In this example only the property \"company\" will be updated. All other properties are unchanged.

### `PUT /customer/id/4391`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
-H Content-Type: application/json \\
-X PUT \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/4391\" \\
-d  @- <<JSON
{
\"id\": \"4391\",
\"version\": \"0\",
\"addresses\": [
{
\"id\": \"4393\",
\"version\": \"0\",
\"countryCode\": \"DE\",
\"createdDate\": 1496840784272,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496840784272,
\"primeAddress\": true
}
],
\"blocked\": false,
\"company\": \"NEUER FIRMENNAME!!!\",
\"contacts\": [],
\"createdDate\": 1496840784273,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\"
}
],
\"customerNumber\": \"C1013\",
\"customerTopics\": [],
\"deliveryBlock\": false,
\"insolvent\": false,
\"insured\": false,
\"lastModifiedDate\": 1496840784270,
\"optIn\": false,
\"partyType\": \"ORGANIZATION\",
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"sales@weclapp.com\",
\"salesChannel\": \"NET1\",
\"useCustomsTariffNumber\": false
}
JSON
```

**Output:**

```json
{
\"id\": \"4391\",
\"version\": \"1\",
\"addresses\": [
{
\"id\": \"4393\",
\"version\": \"0\",
\"countryCode\": \"DE\",
\"createdDate\": 1496840784272,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496840784272,
\"primeAddress\": true
}
],
\"blocked\": false,
\"company\": \"NEUER FIRMENNAME!!!\",
\"contacts\": [],
\"createdDate\": 1496840784273,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\"
}
],
\"customerNumber\": \"C1013\",
\"customerTopics\": [],
\"deliveryBlock\": false,
\"insolvent\": false,
\"insured\": false,
\"lastModifiedDate\": 1496842955268,
\"optIn\": false,
\"partyType\": \"ORGANIZATION\",
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"sales@weclapp.com\",
\"salesChannel\": \"NET1\",
\"useCustomsTariffNumber\": false
}
```

### Updating only specific properties

It is also possible to update only specific properties. For this you only have to set the parameter
`ignoreMissingProperties=true`. We recommend to always include `version` here as well to activate optimistic locking.

If you want to change lists (add, update or delete an item) stored in the entity, it is sufficient to specify the id for existing item entities.

In this example only the property \"company\" will be updated. All other properties are unchanged.

### `PUT /customer/id/4391`



```bash
curl -H \"AuthenticationToken:<TOKEN>\" \\
-H Content-Type: application/json \\
-X PUT \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/4391?ignoreMissingProperties=true\" \\
-d '{ \"version\": \"0\", \"company\": \"NEUER FIRMENNAME!!!\" }'
```

**Output:**

```json
{
\"id\": \"4391\",
\"version\": \"1\",
\"addresses\": [
{
\"id\": \"4393\",
\"version\": \"0\",
\"countryCode\": \"DE\",
\"createdDate\": 1496840784272,
\"deliveryAddress\": false,
\"invoiceAddress\": false,
\"lastModifiedDate\": 1496840784272,
\"primeAddress\": true
}
],
\"blocked\": false,
\"company\": \"NEUER FIRMENNAME!!!\",
\"contacts\": [],
\"createdDate\": 1496840784273,
\"currencyId\": \"248\",
\"currencyName\": \"EUR\",
\"customAttributes\": [
{
\"attributeDefinitionId\": \"4048\"
}
],
\"customerNumber\": \"C1013\",
\"customerTopics\": [],
\"deliveryBlock\": false,
\"insolvent\": false,
\"insured\": false,
\"lastModifiedDate\": 1496842955268,
\"optIn\": false,
\"partyType\": \"ORGANIZATION\",
\"responsibleUserFixed\": false,
\"responsibleUserId\": \"947\",
\"responsibleUserUsername\": \"sales@weclapp.com\",
\"salesChannel\": \"NET1\",
\"useCustomsTariffNumber\": false
}
```


### Optimistic locking


For the update operation the resources usually also support optimistic locking using the version property: if the version property is in the request
body and it does not match the current version, then the request fails with an optimistic lock error. In that case the caller should again get the
latest version, apply the changes and try the request again.
It is possible to disable the optimistic locking check by just omitting the version property, but doing this might accidentally overwrite changes
done by another user in the meantime.

## Delete a specific instance

Deleting an instances is done by performing a `DELETE` request to the URL of the instance.

### `DELETE /customer/id/{id}`

```bash
curl -H \"AuthenticationToken:<TOKEN>\" -X DELETE \"https://<TENANT>.weclapp.com/webapp/api/v1/customer/id/4391\"
```

If the deletion is possible it is performed and the response status will be 204 (No Content), otherwise an error response will be returned.

<span id=\"errors\"> </span>

# API error reference

weclapp API errors are basically conformant to [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807),
with some notable differences:

* The migration to the RFC 7807 structure is an ongoing process, so some compatibility mechanisms are in place for now:
* The responses come with \"`Content-Type: application/json`\" instead of \"`Content-Type: application/problem+json`\"
* The \"unstructured\" error responses that have been in use until now are still part of the response JSON, so existing code should work without changes.
* Detail information that _should_ be there according to the new structure may be still missing. This applies especially to all kinds of validation errors.
* Two custom fields have been added to the response structure: \"location\" and \"validationErrors\". See the general description below and the individual error descriptions for details on these.

## Error JSON structure

The error JSON is structured as described in [RFC 7807](https://datatracker.ietf.org/doc/html/rfc7807), with two additional properties:

| Property         | Datatype         | Description                                                                                                                                                                                                                                       |
|------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type             | string           | (relative) URI reference that identifies the problem type, pointing to the error description in this document. To technically distinguish individual types of errors it is recommended to only evaluate the part after the last '/'.              |
| title            | string           | (RFC7807) A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization (e.g., using proactive content negotiation; see RFC7231, Section 3.4).      |
| status           | integer          | (RFC7807) The HTTP status code (RFC7231, Section 6) generated by the origin server for this occurrence of the problem.                                                                                                                            |
| detail           | string           | (RFC7807) A human-readable explanation specific to this occurrence of the problem. This may be missing when the actual detail information either would be security sensitive (e.g. on unexpected errors) or is contained in the validationErrors. |
| instance         | string           | (RFC7807) A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. In weclapp, this typically is the URI to the affected entity.                                      |
| validationErrors | array of objects | List of found validation errors, with a structure modeled after RFC 7807 as well (see below).                                                                                                                                                     |

Validation errors have a similar structure:

| Property | Datatype         | Description                                                                                                                                                                                                                                  |
|----------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| type     | string           | (relative) URI reference that identifies the problem type, pointing to the error description in this document. To technically distinguish individual types of errors it is recommended to only evaluate the part after the last '/'.         |
| title    | string           | (RFC7807) A short, human-readable summary of the problem type. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization (e.g., using proactive content negotiation; see RFC7231, Section 3.4). |
| detail   | string           | (RFC7807) A human-readable explanation specific to this occurrence of the problem.                                                                                                                                                           |
| instance | string           | (RFC7807) A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. In weclapp, this is the name of the affected parameter or the URI to the affected entity.     |
| location | string           | The JsonPath location of the affected property.                                                                                                                                                                                              |
| allowed  | array of strings | List of allowed values, with semantics dependent on the concrete validation error.                                                                                                                                                           |


## Error reference


<span id=\"!/errors/context\"></span>

### \"context\": operation not possible in this context

|            |                                       |
|------------|---------------------------------------|
| description | The operation is not possible in this context or with the current state of the data                  |
| type       | [/webapp/view/api/errors.html#!/errors/context](/webapp/view/api/errors.html#!/errors/context)        |
| status     | 409 (Conflict)|

<span id=\"!/errors/conversation\"></span>

### \"conversation\": existing conversation (parameter 'cid') is not allowed

|            |                                       |
|------------|---------------------------------------|
| description | The request was sent in the context of a running session, which is not allowed for the (stateless) API                  |
| type       | [/webapp/view/api/errors.html#!/errors/conversation](/webapp/view/api/errors.html#!/errors/conversation)        |
| status     | 400 (Bad Request)|
| detail | human readable information on the conversation |

<span id=\"!/errors/entity_not_found\"></span>

### \"entity_not_found\": (sub)entity not found

|            |                                       |
|------------|---------------------------------------|
| description | The specified entity or (more likely) a referenced sub-entity could not be found.                  |
| type       | [/webapp/view/api/errors.html#!/errors/entity_not_found](/webapp/view/api/errors.html#!/errors/entity_not_found)        |
| status     | 400 (Bad Request)|

<span id=\"!/errors/forbidden\"></span>

### \"forbidden\": insufficient privileges

|            |                                       |
|------------|---------------------------------------|
| description | The provided credentials are not sufficient to perform the requested operation                  |
| type       | [/webapp/view/api/errors.html#!/errors/forbidden](/webapp/view/api/errors.html#!/errors/forbidden)        |
| status     | 403 (Forbidden)|

<span id=\"!/errors/invalid_json\"></span>

### \"invalid_json\": invalid json

|            |                                       |
|------------|---------------------------------------|
| description | The JSON passed in the request body could not be parsed or the body is not JSON at all.                  |
| type       | [/webapp/view/api/errors.html#!/errors/invalid_json](/webapp/view/api/errors.html#!/errors/invalid_json)        |
| status     | 400 (Bad Request)|

<span id=\"!/errors/not_found\"></span>

### \"not_found\": resource not found

|            |                                       |
|------------|---------------------------------------|
| description | The API endpoint / method / entity could not be found                  |
| type       | [/webapp/view/api/errors.html#!/errors/not_found](/webapp/view/api/errors.html#!/errors/not_found)        |
| status     | 404 (Not Found)|

<span id=\"!/errors/optimistic_lock\"></span>

### \"optimistic_lock\": optimistic lock error

|            |                                       |
|------------|---------------------------------------|
| description | Optimistic Lock error. This appears if an entity you tried to modify has been modified by someone else in the meantime. See 'Optimistic Locking' in the 'API operations sample' section of the docs.                  |
| type       | [/webapp/view/api/errors.html#!/errors/optimistic_lock](/webapp/view/api/errors.html#!/errors/optimistic_lock)        |
| status     | 409 (Conflict)|
| instance | URI to affected entity if available |

<span id=\"!/errors/persistence\"></span>

### \"persistence\": persistence error

|            |                                       |
|------------|---------------------------------------|
| description | Catchall for persistence related problems that are not covered by more specific errors. In some cases it is sufficient to try again after a short time, but if the problem persists please contact support.                  |
| type       | [/webapp/view/api/errors.html#!/errors/persistence](/webapp/view/api/errors.html#!/errors/persistence)        |
| status     | 409 (Conflict)|

<span id=\"!/errors/unauthorized\"></span>

### \"unauthorized\": missing permission

|            |                                       |
|------------|---------------------------------------|
| description | Authorization or authentication problem                  |
| type       | [/webapp/view/api/errors.html#!/errors/unauthorized](/webapp/view/api/errors.html#!/errors/unauthorized)        |
| status     | 401 (Unauthorized)|

<span id=\"!/errors/unexpected\"></span>

### \"unexpected\": unexpected error

|            |                                       |
|------------|---------------------------------------|
| description | Catchall error for everything that is not covered by more specific errors. This is typically caused by a bug in weclapp.                  |
| type       | [/webapp/view/api/errors.html#!/errors/unexpected](/webapp/view/api/errors.html#!/errors/unexpected)        |
| status     | 500 (Internal Server Error)|

<span id=\"!/errors/validation\"></span>

### \"validation\": validation failed

|            |                                       |
|------------|---------------------------------------|
| description | The input (entity properties / URL parameters) is malformed or not allowed in this context                  |
| type       | [/webapp/view/api/errors.html#!/errors/validation](/webapp/view/api/errors.html#!/errors/validation)        |
| status     | 400 (Bad Request)|
| validationErrors | validation errors |

## Validation error reference


<span id=\"!/validation/authorization\"></span>

### \"authorization\": no authorization to access property or referenced entity

|            |                                       |
|------------|---------------------------------------|
| description | The client lacks authorization to access the property or referenced entity                  |
| type       | [/webapp/view/api/errors.html#!/validation/authorization](/webapp/view/api/errors.html#!/validation/authorization)        |

<span id=\"!/validation/blocked\"></span>

### \"blocked\": operation was blocked

|            |                                       |
|------------|---------------------------------------|
| description | The operation was blocked by referenced entities                  |
| type       | [/webapp/view/api/errors.html#!/validation/blocked](/webapp/view/api/errors.html#!/validation/blocked)        |

<span id=\"!/validation/consistency\"></span>

### \"consistency\": values are inconsistent

|            |                                       |
|------------|---------------------------------------|
| description | The given values are inconsistent (general, unspecific error)                  |
| type       | [/webapp/view/api/errors.html#!/validation/consistency](/webapp/view/api/errors.html#!/validation/consistency)        |

<span id=\"!/validation/digits\"></span>

### \"digits\": maximum number of digits exceeded

|            |                                       |
|------------|---------------------------------------|
| description | The numerical value given has more than the allowed maximum number of integer and/or fractional digits                  |
| type       | [/webapp/view/api/errors.html#!/validation/digits](/webapp/view/api/errors.html#!/validation/digits)        |
| allowed | maximum allowed integer digits, maximum allowed fraction digits |

<span id=\"!/validation/duplicate\"></span>

### \"duplicate\": entity is a duplicate

|            |                                       |
|------------|---------------------------------------|
| description | The given (sub-)entity is a duplicate                  |
| type       | [/webapp/view/api/errors.html#!/validation/duplicate](/webapp/view/api/errors.html#!/validation/duplicate)        |

<span id=\"!/validation/email\"></span>

### \"email\": not a well-formed email

|            |                                       |
|------------|---------------------------------------|
| description | The value given is not a well-formed email address                  |
| type       | [/webapp/view/api/errors.html#!/validation/email](/webapp/view/api/errors.html#!/validation/email)        |

<span id=\"!/validation/email_or_domain\"></span>

### \"email_or_domain\": not a well-formed email or domain

|            |                                       |
|------------|---------------------------------------|
| description | The value given is not a well-formed email address or internet domain name                  |
| type       | [/webapp/view/api/errors.html#!/validation/email_or_domain](/webapp/view/api/errors.html#!/validation/email_or_domain)        |

<span id=\"!/validation/empty\"></span>

### \"empty\": value must be empty

|            |                                       |
|------------|---------------------------------------|
| description | The value given must be left blank in this context, but is present                  |
| type       | [/webapp/view/api/errors.html#!/validation/empty](/webapp/view/api/errors.html#!/validation/empty)        |

<span id=\"!/validation/enum\"></span>

### \"enum\": unsupported enum value

|            |                                       |
|------------|---------------------------------------|
| description | The given enum value is unknown or unsupported in this context                  |
| type       | [/webapp/view/api/errors.html#!/validation/enum](/webapp/view/api/errors.html#!/validation/enum)        |
| allowed | all known / allowed (enum) values |

<span id=\"!/validation/future\"></span>

### \"future\": timestamp has to be in the future

|            |                                       |
|------------|---------------------------------------|
| description | The given timestamp should be in the future but is not                  |
| type       | [/webapp/view/api/errors.html#!/validation/future](/webapp/view/api/errors.html#!/validation/future)        |

<span id=\"!/validation/greater_than\"></span>

### \"greater_than\": value has to be above allowed limit

|            |                                       |
|------------|---------------------------------------|
| description | The numerical value given has to be larger than the allowed limit                  |
| type       | [/webapp/view/api/errors.html#!/validation/greater_than](/webapp/view/api/errors.html#!/validation/greater_than)        |
| allowed | lower limit (excluded) |

<span id=\"!/validation/less_than\"></span>

### \"less_than\": value has to be below allowed limit

|            |                                       |
|------------|---------------------------------------|
| description | The numerical value given has to be smaller than the allowed limit                  |
| type       | [/webapp/view/api/errors.html#!/validation/less_than](/webapp/view/api/errors.html#!/validation/less_than)        |
| allowed | upper limit (excluded) |

<span id=\"!/validation/max\"></span>

### \"max\": value is above allowed maximum

|            |                                       |
|------------|---------------------------------------|
| description | The numerical value given is larger than the allowed maximum                  |
| type       | [/webapp/view/api/errors.html#!/validation/max](/webapp/view/api/errors.html#!/validation/max)        |
| allowed | maximum allowed value |

<span id=\"!/validation/min\"></span>

### \"min\": value is below allowed minimum

|            |                                       |
|------------|---------------------------------------|
| description | The numerical value given is smaller than the allowed minimum                  |
| type       | [/webapp/view/api/errors.html#!/validation/min](/webapp/view/api/errors.html#!/validation/min)        |
| allowed | minimum allowed value |

<span id=\"!/validation/not_empty\"></span>

### \"not_empty\": value must not be empty

|            |                                       |
|------------|---------------------------------------|
| description | The value given is required, but is missing or blank                  |
| type       | [/webapp/view/api/errors.html#!/validation/not_empty](/webapp/view/api/errors.html#!/validation/not_empty)        |

<span id=\"!/validation/past\"></span>

### \"past\": timestamp has to be in the past

|            |                                       |
|------------|---------------------------------------|
| description | The given timestamp should be in the past but is not                  |
| type       | [/webapp/view/api/errors.html#!/validation/past](/webapp/view/api/errors.html#!/validation/past)        |

<span id=\"!/validation/pattern\"></span>

### \"pattern\": value has to conform to a specific pattern

|            |                                       |
|------------|---------------------------------------|
| description | The text given does not conform to the allowed pattern                  |
| type       | [/webapp/view/api/errors.html#!/validation/pattern](/webapp/view/api/errors.html#!/validation/pattern)        |
| allowed | the pattern (regular expression) |

<span id=\"!/validation/reference\"></span>

### \"reference\": referenced entity not found

|            |                                       |
|------------|---------------------------------------|
| description | The referenced entity could not be found                  |
| type       | [/webapp/view/api/errors.html#!/validation/reference](/webapp/view/api/errors.html#!/validation/reference)        |

<span id=\"!/validation/size\"></span>

### \"size\": size is outside allowed range

|            |                                       |
|------------|---------------------------------------|
| description | The text or collection given has not enough or too many characters or elements                  |
| type       | [/webapp/view/api/errors.html#!/validation/size](/webapp/view/api/errors.html#!/validation/size)        |
| allowed | minimum size, maximum size |


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1
- Package version: 1.0.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.weclapp.com](https://www.weclapp.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost:80/webapp/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost:80/webapp/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-token
configuration.api_key['api-token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-token'] = 'Bearer'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountingTransactionApi(api_client)

    try:
        # count accountingTransaction
        api_response = api_instance.accounting_transaction_count_get()
        print("The response of AccountingTransactionApi->accounting_transaction_count_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountingTransactionApi->accounting_transaction_count_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:80/webapp/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountingTransactionApi* | [**accounting_transaction_count_get**](docs/AccountingTransactionApi.md#accounting_transaction_count_get) | **GET** /accountingTransaction/count | count accountingTransaction
*AccountingTransactionApi* | [**accounting_transaction_get**](docs/AccountingTransactionApi.md#accounting_transaction_get) | **GET** /accountingTransaction | query accountingTransaction
*AccountingTransactionApi* | [**accounting_transaction_id_id_get**](docs/AccountingTransactionApi.md#accounting_transaction_id_id_get) | **GET** /accountingTransaction/id/{id} | query a specific accountingTransaction
*ArchivedEmailApi* | [**archived_email_count_get**](docs/ArchivedEmailApi.md#archived_email_count_get) | **GET** /archivedEmail/count | count archivedEmail
*ArchivedEmailApi* | [**archived_email_get**](docs/ArchivedEmailApi.md#archived_email_get) | **GET** /archivedEmail | query archivedEmail
*ArchivedEmailApi* | [**archived_email_id_id_get**](docs/ArchivedEmailApi.md#archived_email_id_id_get) | **GET** /archivedEmail/id/{id} | query a specific archivedEmail
*ArchivedEmailApi* | [**archived_email_id_id_remove_reference_post**](docs/ArchivedEmailApi.md#archived_email_id_id_remove_reference_post) | **POST** /archivedEmail/id/{id}/removeReference | 
*ArticleApi* | [**article_count_get**](docs/ArticleApi.md#article_count_get) | **GET** /article/count | count article
*ArticleApi* | [**article_get**](docs/ArticleApi.md#article_get) | **GET** /article | query article
*ArticleApi* | [**article_id_id_change_unit_post**](docs/ArticleApi.md#article_id_id_change_unit_post) | **POST** /article/id/{id}/changeUnit | 
*ArticleApi* | [**article_id_id_create_datasheet_pdf_post**](docs/ArticleApi.md#article_id_id_create_datasheet_pdf_post) | **POST** /article/id/{id}/createDatasheetPdf | 
*ArticleApi* | [**article_id_id_create_label_pdf_post**](docs/ArticleApi.md#article_id_id_create_label_pdf_post) | **POST** /article/id/{id}/createLabelPdf | 
*ArticleApi* | [**article_id_id_delete**](docs/ArticleApi.md#article_id_id_delete) | **DELETE** /article/id/{id} | delete a article
*ArticleApi* | [**article_id_id_download_article_image_get**](docs/ArticleApi.md#article_id_id_download_article_image_get) | **GET** /article/id/{id}/downloadArticleImage | 
*ArticleApi* | [**article_id_id_download_main_article_image_get**](docs/ArticleApi.md#article_id_id_download_main_article_image_get) | **GET** /article/id/{id}/downloadMainArticleImage | 
*ArticleApi* | [**article_id_id_get**](docs/ArticleApi.md#article_id_id_get) | **GET** /article/id/{id} | query a specific article
*ArticleApi* | [**article_id_id_packaging_unit_structure_get**](docs/ArticleApi.md#article_id_id_packaging_unit_structure_get) | **GET** /article/id/{id}/packagingUnitStructure | 
*ArticleApi* | [**article_id_id_put**](docs/ArticleApi.md#article_id_id_put) | **PUT** /article/id/{id} | update a article
*ArticleApi* | [**article_id_id_upload_article_image_post**](docs/ArticleApi.md#article_id_id_upload_article_image_post) | **POST** /article/id/{id}/uploadArticleImage | 
*ArticleApi* | [**article_post**](docs/ArticleApi.md#article_post) | **POST** /article | create a article
*ArticleAccountingCodeApi* | [**article_accounting_code_count_get**](docs/ArticleAccountingCodeApi.md#article_accounting_code_count_get) | **GET** /articleAccountingCode/count | count articleAccountingCode
*ArticleAccountingCodeApi* | [**article_accounting_code_get**](docs/ArticleAccountingCodeApi.md#article_accounting_code_get) | **GET** /articleAccountingCode | query articleAccountingCode
*ArticleAccountingCodeApi* | [**article_accounting_code_id_id_delete**](docs/ArticleAccountingCodeApi.md#article_accounting_code_id_id_delete) | **DELETE** /articleAccountingCode/id/{id} | delete a articleAccountingCode
*ArticleAccountingCodeApi* | [**article_accounting_code_id_id_get**](docs/ArticleAccountingCodeApi.md#article_accounting_code_id_id_get) | **GET** /articleAccountingCode/id/{id} | query a specific articleAccountingCode
*ArticleAccountingCodeApi* | [**article_accounting_code_id_id_put**](docs/ArticleAccountingCodeApi.md#article_accounting_code_id_id_put) | **PUT** /articleAccountingCode/id/{id} | update a articleAccountingCode
*ArticleAccountingCodeApi* | [**article_accounting_code_post**](docs/ArticleAccountingCodeApi.md#article_accounting_code_post) | **POST** /articleAccountingCode | create a articleAccountingCode
*ArticleCategoryApi* | [**article_category_count_get**](docs/ArticleCategoryApi.md#article_category_count_get) | **GET** /articleCategory/count | count articleCategory
*ArticleCategoryApi* | [**article_category_get**](docs/ArticleCategoryApi.md#article_category_get) | **GET** /articleCategory | query articleCategory
*ArticleCategoryApi* | [**article_category_id_id_delete**](docs/ArticleCategoryApi.md#article_category_id_id_delete) | **DELETE** /articleCategory/id/{id} | delete a articleCategory
*ArticleCategoryApi* | [**article_category_id_id_download_image_get**](docs/ArticleCategoryApi.md#article_category_id_id_download_image_get) | **GET** /articleCategory/id/{id}/downloadImage | 
*ArticleCategoryApi* | [**article_category_id_id_get**](docs/ArticleCategoryApi.md#article_category_id_id_get) | **GET** /articleCategory/id/{id} | query a specific articleCategory
*ArticleCategoryApi* | [**article_category_id_id_put**](docs/ArticleCategoryApi.md#article_category_id_id_put) | **PUT** /articleCategory/id/{id} | update a articleCategory
*ArticleCategoryApi* | [**article_category_id_id_upload_image_post**](docs/ArticleCategoryApi.md#article_category_id_id_upload_image_post) | **POST** /articleCategory/id/{id}/uploadImage | 
*ArticleCategoryApi* | [**article_category_post**](docs/ArticleCategoryApi.md#article_category_post) | **POST** /articleCategory | create a articleCategory
*ArticleItemGroupApi* | [**article_item_group_count_get**](docs/ArticleItemGroupApi.md#article_item_group_count_get) | **GET** /articleItemGroup/count | count articleItemGroup
*ArticleItemGroupApi* | [**article_item_group_get**](docs/ArticleItemGroupApi.md#article_item_group_get) | **GET** /articleItemGroup | query articleItemGroup
*ArticleItemGroupApi* | [**article_item_group_id_id_delete**](docs/ArticleItemGroupApi.md#article_item_group_id_id_delete) | **DELETE** /articleItemGroup/id/{id} | delete a articleItemGroup
*ArticleItemGroupApi* | [**article_item_group_id_id_get**](docs/ArticleItemGroupApi.md#article_item_group_id_id_get) | **GET** /articleItemGroup/id/{id} | query a specific articleItemGroup
*ArticleItemGroupApi* | [**article_item_group_id_id_put**](docs/ArticleItemGroupApi.md#article_item_group_id_id_put) | **PUT** /articleItemGroup/id/{id} | update a articleItemGroup
*ArticleItemGroupApi* | [**article_item_group_post**](docs/ArticleItemGroupApi.md#article_item_group_post) | **POST** /articleItemGroup | create a articleItemGroup
*ArticlePriceApi* | [**article_price_count_get**](docs/ArticlePriceApi.md#article_price_count_get) | **GET** /articlePrice/count | count articlePrice
*ArticlePriceApi* | [**article_price_get**](docs/ArticlePriceApi.md#article_price_get) | **GET** /articlePrice | query articlePrice
*ArticlePriceApi* | [**article_price_id_id_get**](docs/ArticlePriceApi.md#article_price_id_id_get) | **GET** /articlePrice/id/{id} | query a specific articlePrice
*ArticleRatingApi* | [**article_rating_count_get**](docs/ArticleRatingApi.md#article_rating_count_get) | **GET** /articleRating/count | count articleRating
*ArticleRatingApi* | [**article_rating_get**](docs/ArticleRatingApi.md#article_rating_get) | **GET** /articleRating | query articleRating
*ArticleRatingApi* | [**article_rating_id_id_delete**](docs/ArticleRatingApi.md#article_rating_id_id_delete) | **DELETE** /articleRating/id/{id} | delete a articleRating
*ArticleRatingApi* | [**article_rating_id_id_get**](docs/ArticleRatingApi.md#article_rating_id_id_get) | **GET** /articleRating/id/{id} | query a specific articleRating
*ArticleRatingApi* | [**article_rating_id_id_put**](docs/ArticleRatingApi.md#article_rating_id_id_put) | **PUT** /articleRating/id/{id} | update a articleRating
*ArticleRatingApi* | [**article_rating_post**](docs/ArticleRatingApi.md#article_rating_post) | **POST** /articleRating | create a articleRating
*ArticleStatusApi* | [**article_status_count_get**](docs/ArticleStatusApi.md#article_status_count_get) | **GET** /articleStatus/count | count articleStatus
*ArticleStatusApi* | [**article_status_get**](docs/ArticleStatusApi.md#article_status_get) | **GET** /articleStatus | query articleStatus
*ArticleStatusApi* | [**article_status_id_id_delete**](docs/ArticleStatusApi.md#article_status_id_id_delete) | **DELETE** /articleStatus/id/{id} | delete a articleStatus
*ArticleStatusApi* | [**article_status_id_id_get**](docs/ArticleStatusApi.md#article_status_id_id_get) | **GET** /articleStatus/id/{id} | query a specific articleStatus
*ArticleStatusApi* | [**article_status_id_id_put**](docs/ArticleStatusApi.md#article_status_id_id_put) | **PUT** /articleStatus/id/{id} | update a articleStatus
*ArticleStatusApi* | [**article_status_post**](docs/ArticleStatusApi.md#article_status_post) | **POST** /articleStatus | create a articleStatus
*ArticleSupplySourceApi* | [**article_supply_source_count_get**](docs/ArticleSupplySourceApi.md#article_supply_source_count_get) | **GET** /articleSupplySource/count | count articleSupplySource
*ArticleSupplySourceApi* | [**article_supply_source_get**](docs/ArticleSupplySourceApi.md#article_supply_source_get) | **GET** /articleSupplySource | query articleSupplySource
*ArticleSupplySourceApi* | [**article_supply_source_id_id_delete**](docs/ArticleSupplySourceApi.md#article_supply_source_id_id_delete) | **DELETE** /articleSupplySource/id/{id} | delete a articleSupplySource
*ArticleSupplySourceApi* | [**article_supply_source_id_id_get**](docs/ArticleSupplySourceApi.md#article_supply_source_id_id_get) | **GET** /articleSupplySource/id/{id} | query a specific articleSupplySource
*ArticleSupplySourceApi* | [**article_supply_source_id_id_put**](docs/ArticleSupplySourceApi.md#article_supply_source_id_id_put) | **PUT** /articleSupplySource/id/{id} | update a articleSupplySource
*ArticleSupplySourceApi* | [**article_supply_source_post**](docs/ArticleSupplySourceApi.md#article_supply_source_post) | **POST** /articleSupplySource | create a articleSupplySource
*AttendanceApi* | [**attendance_count_get**](docs/AttendanceApi.md#attendance_count_get) | **GET** /attendance/count | count attendance
*AttendanceApi* | [**attendance_current_attendance_get**](docs/AttendanceApi.md#attendance_current_attendance_get) | **GET** /attendance/currentAttendance | 
*AttendanceApi* | [**attendance_get**](docs/AttendanceApi.md#attendance_get) | **GET** /attendance | query attendance
*AttendanceApi* | [**attendance_id_id_delete**](docs/AttendanceApi.md#attendance_id_id_delete) | **DELETE** /attendance/id/{id} | delete a attendance
*AttendanceApi* | [**attendance_id_id_get**](docs/AttendanceApi.md#attendance_id_id_get) | **GET** /attendance/id/{id} | query a specific attendance
*AttendanceApi* | [**attendance_id_id_put**](docs/AttendanceApi.md#attendance_id_id_put) | **PUT** /attendance/id/{id} | update a attendance
*AttendanceApi* | [**attendance_log_off_post**](docs/AttendanceApi.md#attendance_log_off_post) | **POST** /attendance/logOff | 
*AttendanceApi* | [**attendance_log_on_post**](docs/AttendanceApi.md#attendance_log_on_post) | **POST** /attendance/logOn | 
*AttendanceApi* | [**attendance_post**](docs/AttendanceApi.md#attendance_post) | **POST** /attendance | create a attendance
*BankAccountApi* | [**bank_account_count_get**](docs/BankAccountApi.md#bank_account_count_get) | **GET** /bankAccount/count | count bankAccount
*BankAccountApi* | [**bank_account_get**](docs/BankAccountApi.md#bank_account_get) | **GET** /bankAccount | query bankAccount
*BankAccountApi* | [**bank_account_id_id_delete**](docs/BankAccountApi.md#bank_account_id_id_delete) | **DELETE** /bankAccount/id/{id} | delete a bankAccount
*BankAccountApi* | [**bank_account_id_id_get**](docs/BankAccountApi.md#bank_account_id_id_get) | **GET** /bankAccount/id/{id} | query a specific bankAccount
*BankAccountApi* | [**bank_account_id_id_put**](docs/BankAccountApi.md#bank_account_id_id_put) | **PUT** /bankAccount/id/{id} | update a bankAccount
*BankAccountApi* | [**bank_account_post**](docs/BankAccountApi.md#bank_account_post) | **POST** /bankAccount | create a bankAccount
*BatchNumberApi* | [**batch_number_count_get**](docs/BatchNumberApi.md#batch_number_count_get) | **GET** /batchNumber/count | count batchNumber
*BatchNumberApi* | [**batch_number_get**](docs/BatchNumberApi.md#batch_number_get) | **GET** /batchNumber | query batchNumber
*BatchNumberApi* | [**batch_number_id_id_get**](docs/BatchNumberApi.md#batch_number_id_id_get) | **GET** /batchNumber/id/{id} | query a specific batchNumber
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_count_get**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_count_get) | **GET** /blanketPurchaseOrder/count | count blanketPurchaseOrder
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_get**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_get) | **GET** /blanketPurchaseOrder | query blanketPurchaseOrder
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_id_id_delete**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_delete) | **DELETE** /blanketPurchaseOrder/id/{id} | delete a blanketPurchaseOrder
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_download_latest_blanket_purchase_order_pdf_get) | **GET** /blanketPurchaseOrder/id/{id}/downloadLatestBlanketPurchaseOrderPdf | 
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_id_id_generate_releases_post**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_generate_releases_post) | **POST** /blanketPurchaseOrder/id/{id}/generateReleases | 
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_id_id_get**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_get) | **GET** /blanketPurchaseOrder/id/{id} | query a specific blanketPurchaseOrder
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_id_id_put**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_id_id_put) | **PUT** /blanketPurchaseOrder/id/{id} | update a blanketPurchaseOrder
*BlanketPurchaseOrderApi* | [**blanket_purchase_order_post**](docs/BlanketPurchaseOrderApi.md#blanket_purchase_order_post) | **POST** /blanketPurchaseOrder | create a blanketPurchaseOrder
*CalendarApi* | [**calendar_count_get**](docs/CalendarApi.md#calendar_count_get) | **GET** /calendar/count | count calendar
*CalendarApi* | [**calendar_get**](docs/CalendarApi.md#calendar_get) | **GET** /calendar | query calendar
*CalendarApi* | [**calendar_id_id_delete**](docs/CalendarApi.md#calendar_id_id_delete) | **DELETE** /calendar/id/{id} | delete a calendar
*CalendarApi* | [**calendar_id_id_delete_calendar_and_move_events_post**](docs/CalendarApi.md#calendar_id_id_delete_calendar_and_move_events_post) | **POST** /calendar/id/{id}/deleteCalendarAndMoveEvents | 
*CalendarApi* | [**calendar_id_id_get**](docs/CalendarApi.md#calendar_id_id_get) | **GET** /calendar/id/{id} | query a specific calendar
*CalendarApi* | [**calendar_id_id_importi_cal_post**](docs/CalendarApi.md#calendar_id_id_importi_cal_post) | **POST** /calendar/id/{id}/importiCal | 
*CalendarApi* | [**calendar_id_id_put**](docs/CalendarApi.md#calendar_id_id_put) | **PUT** /calendar/id/{id} | update a calendar
*CalendarApi* | [**calendar_post**](docs/CalendarApi.md#calendar_post) | **POST** /calendar | create a calendar
*CalendarEventApi* | [**calendar_event_count_get**](docs/CalendarEventApi.md#calendar_event_count_get) | **GET** /calendarEvent/count | count calendarEvent
*CalendarEventApi* | [**calendar_event_get**](docs/CalendarEventApi.md#calendar_event_get) | **GET** /calendarEvent | query calendarEvent
*CalendarEventApi* | [**calendar_event_id_id_delete**](docs/CalendarEventApi.md#calendar_event_id_id_delete) | **DELETE** /calendarEvent/id/{id} | delete a calendarEvent
*CalendarEventApi* | [**calendar_event_id_id_get**](docs/CalendarEventApi.md#calendar_event_id_id_get) | **GET** /calendarEvent/id/{id} | query a specific calendarEvent
*CalendarEventApi* | [**calendar_event_id_id_put**](docs/CalendarEventApi.md#calendar_event_id_id_put) | **PUT** /calendarEvent/id/{id} | update a calendarEvent
*CalendarEventApi* | [**calendar_event_post**](docs/CalendarEventApi.md#calendar_event_post) | **POST** /calendarEvent | create a calendarEvent
*CampaignApi* | [**campaign_count_get**](docs/CampaignApi.md#campaign_count_get) | **GET** /campaign/count | count campaign
*CampaignApi* | [**campaign_get**](docs/CampaignApi.md#campaign_get) | **GET** /campaign | query campaign
*CampaignApi* | [**campaign_id_id_delete**](docs/CampaignApi.md#campaign_id_id_delete) | **DELETE** /campaign/id/{id} | delete a campaign
*CampaignApi* | [**campaign_id_id_get**](docs/CampaignApi.md#campaign_id_id_get) | **GET** /campaign/id/{id} | query a specific campaign
*CampaignApi* | [**campaign_id_id_put**](docs/CampaignApi.md#campaign_id_id_put) | **PUT** /campaign/id/{id} | update a campaign
*CampaignApi* | [**campaign_post**](docs/CampaignApi.md#campaign_post) | **POST** /campaign | create a campaign
*CampaignParticipantApi* | [**campaign_participant_count_get**](docs/CampaignParticipantApi.md#campaign_participant_count_get) | **GET** /campaignParticipant/count | count campaignParticipant
*CampaignParticipantApi* | [**campaign_participant_get**](docs/CampaignParticipantApi.md#campaign_participant_get) | **GET** /campaignParticipant | query campaignParticipant
*CampaignParticipantApi* | [**campaign_participant_id_id_delete**](docs/CampaignParticipantApi.md#campaign_participant_id_id_delete) | **DELETE** /campaignParticipant/id/{id} | delete a campaignParticipant
*CampaignParticipantApi* | [**campaign_participant_id_id_get**](docs/CampaignParticipantApi.md#campaign_participant_id_id_get) | **GET** /campaignParticipant/id/{id} | query a specific campaignParticipant
*CampaignParticipantApi* | [**campaign_participant_id_id_put**](docs/CampaignParticipantApi.md#campaign_participant_id_id_put) | **PUT** /campaignParticipant/id/{id} | update a campaignParticipant
*CampaignParticipantApi* | [**campaign_participant_post**](docs/CampaignParticipantApi.md#campaign_participant_post) | **POST** /campaignParticipant | create a campaignParticipant
*CashAccountApi* | [**cash_account_count_get**](docs/CashAccountApi.md#cash_account_count_get) | **GET** /cashAccount/count | count cashAccount
*CashAccountApi* | [**cash_account_get**](docs/CashAccountApi.md#cash_account_get) | **GET** /cashAccount | query cashAccount
*CashAccountApi* | [**cash_account_id_id_get**](docs/CashAccountApi.md#cash_account_id_id_get) | **GET** /cashAccount/id/{id} | query a specific cashAccount
*CashAccountApi* | [**cash_account_id_id_put**](docs/CashAccountApi.md#cash_account_id_id_put) | **PUT** /cashAccount/id/{id} | update a cashAccount
*CashAccountApi* | [**cash_account_post**](docs/CashAccountApi.md#cash_account_post) | **POST** /cashAccount | create a cashAccount
*CommentApi* | [**comment_count_get**](docs/CommentApi.md#comment_count_get) | **GET** /comment/count | count comment
*CommentApi* | [**comment_get**](docs/CommentApi.md#comment_get) | **GET** /comment | query comment
*CommentApi* | [**comment_id_id_delete**](docs/CommentApi.md#comment_id_id_delete) | **DELETE** /comment/id/{id} | delete a comment
*CommentApi* | [**comment_id_id_get**](docs/CommentApi.md#comment_id_id_get) | **GET** /comment/id/{id} | query a specific comment
*CommentApi* | [**comment_id_id_put**](docs/CommentApi.md#comment_id_id_put) | **PUT** /comment/id/{id} | update a comment
*CommentApi* | [**comment_post**](docs/CommentApi.md#comment_post) | **POST** /comment | create a comment
*CommercialLanguageApi* | [**commercial_language_count_get**](docs/CommercialLanguageApi.md#commercial_language_count_get) | **GET** /commercialLanguage/count | count commercialLanguage
*CommercialLanguageApi* | [**commercial_language_get**](docs/CommercialLanguageApi.md#commercial_language_get) | **GET** /commercialLanguage | query commercialLanguage
*CommercialLanguageApi* | [**commercial_language_id_id_get**](docs/CommercialLanguageApi.md#commercial_language_id_id_get) | **GET** /commercialLanguage/id/{id} | query a specific commercialLanguage
*CompanySizeApi* | [**company_size_count_get**](docs/CompanySizeApi.md#company_size_count_get) | **GET** /companySize/count | count companySize
*CompanySizeApi* | [**company_size_get**](docs/CompanySizeApi.md#company_size_get) | **GET** /companySize | query companySize
*CompanySizeApi* | [**company_size_id_id_delete**](docs/CompanySizeApi.md#company_size_id_id_delete) | **DELETE** /companySize/id/{id} | delete a companySize
*CompanySizeApi* | [**company_size_id_id_get**](docs/CompanySizeApi.md#company_size_id_id_get) | **GET** /companySize/id/{id} | query a specific companySize
*CompanySizeApi* | [**company_size_id_id_put**](docs/CompanySizeApi.md#company_size_id_id_put) | **PUT** /companySize/id/{id} | update a companySize
*CompanySizeApi* | [**company_size_post**](docs/CompanySizeApi.md#company_size_post) | **POST** /companySize | create a companySize
*ContactApi* | [**contact_count_get**](docs/ContactApi.md#contact_count_get) | **GET** /contact/count | count contact
*ContactApi* | [**contact_get**](docs/ContactApi.md#contact_get) | **GET** /contact | query contact
*ContactApi* | [**contact_id_id_delete**](docs/ContactApi.md#contact_id_id_delete) | **DELETE** /contact/id/{id} | delete a contact
*ContactApi* | [**contact_id_id_download_image_get**](docs/ContactApi.md#contact_id_id_download_image_get) | **GET** /contact/id/{id}/downloadImage | 
*ContactApi* | [**contact_id_id_get**](docs/ContactApi.md#contact_id_id_get) | **GET** /contact/id/{id} | query a specific contact
*ContactApi* | [**contact_id_id_put**](docs/ContactApi.md#contact_id_id_put) | **PUT** /contact/id/{id} | update a contact
*ContactApi* | [**contact_id_id_upload_image_post**](docs/ContactApi.md#contact_id_id_upload_image_post) | **POST** /contact/id/{id}/uploadImage | 
*ContactApi* | [**contact_post**](docs/ContactApi.md#contact_post) | **POST** /contact | create a contact
*ContractApi* | [**contract_count_get**](docs/ContractApi.md#contract_count_get) | **GET** /contract/count | count contract
*ContractApi* | [**contract_get**](docs/ContractApi.md#contract_get) | **GET** /contract | query contract
*ContractApi* | [**contract_id_id_create_contract_document_post**](docs/ContractApi.md#contract_id_id_create_contract_document_post) | **POST** /contract/id/{id}/createContractDocument | 
*ContractApi* | [**contract_id_id_delete**](docs/ContractApi.md#contract_id_id_delete) | **DELETE** /contract/id/{id} | delete a contract
*ContractApi* | [**contract_id_id_download_latest_contract_document_pdf_get**](docs/ContractApi.md#contract_id_id_download_latest_contract_document_pdf_get) | **GET** /contract/id/{id}/downloadLatestContractDocumentPdf | 
*ContractApi* | [**contract_id_id_get**](docs/ContractApi.md#contract_id_id_get) | **GET** /contract/id/{id} | query a specific contract
*ContractApi* | [**contract_id_id_put**](docs/ContractApi.md#contract_id_id_put) | **PUT** /contract/id/{id} | update a contract
*ContractApi* | [**contract_post**](docs/ContractApi.md#contract_post) | **POST** /contract | create a contract
*ContractAuthorizationUnitApi* | [**contract_authorization_unit_count_get**](docs/ContractAuthorizationUnitApi.md#contract_authorization_unit_count_get) | **GET** /contractAuthorizationUnit/count | count contractAuthorizationUnit
*ContractAuthorizationUnitApi* | [**contract_authorization_unit_get**](docs/ContractAuthorizationUnitApi.md#contract_authorization_unit_get) | **GET** /contractAuthorizationUnit | query contractAuthorizationUnit
*ContractAuthorizationUnitApi* | [**contract_authorization_unit_id_id_get**](docs/ContractAuthorizationUnitApi.md#contract_authorization_unit_id_id_get) | **GET** /contractAuthorizationUnit/id/{id} | query a specific contractAuthorizationUnit
*ContractBillingGroupApi* | [**contract_billing_group_count_get**](docs/ContractBillingGroupApi.md#contract_billing_group_count_get) | **GET** /contractBillingGroup/count | count contractBillingGroup
*ContractBillingGroupApi* | [**contract_billing_group_get**](docs/ContractBillingGroupApi.md#contract_billing_group_get) | **GET** /contractBillingGroup | query contractBillingGroup
*ContractBillingGroupApi* | [**contract_billing_group_id_id_delete**](docs/ContractBillingGroupApi.md#contract_billing_group_id_id_delete) | **DELETE** /contractBillingGroup/id/{id} | delete a contractBillingGroup
*ContractBillingGroupApi* | [**contract_billing_group_id_id_get**](docs/ContractBillingGroupApi.md#contract_billing_group_id_id_get) | **GET** /contractBillingGroup/id/{id} | query a specific contractBillingGroup
*ContractBillingGroupApi* | [**contract_billing_group_id_id_put**](docs/ContractBillingGroupApi.md#contract_billing_group_id_id_put) | **PUT** /contractBillingGroup/id/{id} | update a contractBillingGroup
*ContractBillingGroupApi* | [**contract_billing_group_post**](docs/ContractBillingGroupApi.md#contract_billing_group_post) | **POST** /contractBillingGroup | create a contractBillingGroup
*ContractTerminationReasonApi* | [**contract_termination_reason_count_get**](docs/ContractTerminationReasonApi.md#contract_termination_reason_count_get) | **GET** /contractTerminationReason/count | count contractTerminationReason
*ContractTerminationReasonApi* | [**contract_termination_reason_get**](docs/ContractTerminationReasonApi.md#contract_termination_reason_get) | **GET** /contractTerminationReason | query contractTerminationReason
*ContractTerminationReasonApi* | [**contract_termination_reason_id_id_delete**](docs/ContractTerminationReasonApi.md#contract_termination_reason_id_id_delete) | **DELETE** /contractTerminationReason/id/{id} | delete a contractTerminationReason
*ContractTerminationReasonApi* | [**contract_termination_reason_id_id_get**](docs/ContractTerminationReasonApi.md#contract_termination_reason_id_id_get) | **GET** /contractTerminationReason/id/{id} | query a specific contractTerminationReason
*ContractTerminationReasonApi* | [**contract_termination_reason_id_id_put**](docs/ContractTerminationReasonApi.md#contract_termination_reason_id_id_put) | **PUT** /contractTerminationReason/id/{id} | update a contractTerminationReason
*ContractTerminationReasonApi* | [**contract_termination_reason_post**](docs/ContractTerminationReasonApi.md#contract_termination_reason_post) | **POST** /contractTerminationReason | create a contractTerminationReason
*CostCenterApi* | [**cost_center_count_get**](docs/CostCenterApi.md#cost_center_count_get) | **GET** /costCenter/count | count costCenter
*CostCenterApi* | [**cost_center_get**](docs/CostCenterApi.md#cost_center_get) | **GET** /costCenter | query costCenter
*CostCenterApi* | [**cost_center_id_id_delete**](docs/CostCenterApi.md#cost_center_id_id_delete) | **DELETE** /costCenter/id/{id} | delete a costCenter
*CostCenterApi* | [**cost_center_id_id_get**](docs/CostCenterApi.md#cost_center_id_id_get) | **GET** /costCenter/id/{id} | query a specific costCenter
*CostCenterApi* | [**cost_center_id_id_put**](docs/CostCenterApi.md#cost_center_id_id_put) | **PUT** /costCenter/id/{id} | update a costCenter
*CostCenterApi* | [**cost_center_post**](docs/CostCenterApi.md#cost_center_post) | **POST** /costCenter | create a costCenter
*CostCenterGroupApi* | [**cost_center_group_count_get**](docs/CostCenterGroupApi.md#cost_center_group_count_get) | **GET** /costCenterGroup/count | count costCenterGroup
*CostCenterGroupApi* | [**cost_center_group_get**](docs/CostCenterGroupApi.md#cost_center_group_get) | **GET** /costCenterGroup | query costCenterGroup
*CostCenterGroupApi* | [**cost_center_group_id_id_delete**](docs/CostCenterGroupApi.md#cost_center_group_id_id_delete) | **DELETE** /costCenterGroup/id/{id} | delete a costCenterGroup
*CostCenterGroupApi* | [**cost_center_group_id_id_get**](docs/CostCenterGroupApi.md#cost_center_group_id_id_get) | **GET** /costCenterGroup/id/{id} | query a specific costCenterGroup
*CostCenterGroupApi* | [**cost_center_group_id_id_put**](docs/CostCenterGroupApi.md#cost_center_group_id_id_put) | **PUT** /costCenterGroup/id/{id} | update a costCenterGroup
*CostCenterGroupApi* | [**cost_center_group_post**](docs/CostCenterGroupApi.md#cost_center_group_post) | **POST** /costCenterGroup | create a costCenterGroup
*CostTypeApi* | [**cost_type_count_get**](docs/CostTypeApi.md#cost_type_count_get) | **GET** /costType/count | count costType
*CostTypeApi* | [**cost_type_get**](docs/CostTypeApi.md#cost_type_get) | **GET** /costType | query costType
*CostTypeApi* | [**cost_type_id_id_delete**](docs/CostTypeApi.md#cost_type_id_id_delete) | **DELETE** /costType/id/{id} | delete a costType
*CostTypeApi* | [**cost_type_id_id_get**](docs/CostTypeApi.md#cost_type_id_id_get) | **GET** /costType/id/{id} | query a specific costType
*CostTypeApi* | [**cost_type_id_id_put**](docs/CostTypeApi.md#cost_type_id_id_put) | **PUT** /costType/id/{id} | update a costType
*CostTypeApi* | [**cost_type_post**](docs/CostTypeApi.md#cost_type_post) | **POST** /costType | create a costType
*CrmCallCategoryApi* | [**crm_call_category_count_get**](docs/CrmCallCategoryApi.md#crm_call_category_count_get) | **GET** /crmCallCategory/count | count crmCallCategory
*CrmCallCategoryApi* | [**crm_call_category_get**](docs/CrmCallCategoryApi.md#crm_call_category_get) | **GET** /crmCallCategory | query crmCallCategory
*CrmCallCategoryApi* | [**crm_call_category_id_id_delete**](docs/CrmCallCategoryApi.md#crm_call_category_id_id_delete) | **DELETE** /crmCallCategory/id/{id} | delete a crmCallCategory
*CrmCallCategoryApi* | [**crm_call_category_id_id_get**](docs/CrmCallCategoryApi.md#crm_call_category_id_id_get) | **GET** /crmCallCategory/id/{id} | query a specific crmCallCategory
*CrmCallCategoryApi* | [**crm_call_category_id_id_put**](docs/CrmCallCategoryApi.md#crm_call_category_id_id_put) | **PUT** /crmCallCategory/id/{id} | update a crmCallCategory
*CrmCallCategoryApi* | [**crm_call_category_post**](docs/CrmCallCategoryApi.md#crm_call_category_post) | **POST** /crmCallCategory | create a crmCallCategory
*CrmEventApi* | [**crm_event_count_get**](docs/CrmEventApi.md#crm_event_count_get) | **GET** /crmEvent/count | count crmEvent
*CrmEventApi* | [**crm_event_get**](docs/CrmEventApi.md#crm_event_get) | **GET** /crmEvent | query crmEvent
*CrmEventApi* | [**crm_event_id_id_delete**](docs/CrmEventApi.md#crm_event_id_id_delete) | **DELETE** /crmEvent/id/{id} | delete a crmEvent
*CrmEventApi* | [**crm_event_id_id_get**](docs/CrmEventApi.md#crm_event_id_id_get) | **GET** /crmEvent/id/{id} | query a specific crmEvent
*CrmEventApi* | [**crm_event_id_id_put**](docs/CrmEventApi.md#crm_event_id_id_put) | **PUT** /crmEvent/id/{id} | update a crmEvent
*CrmEventApi* | [**crm_event_post**](docs/CrmEventApi.md#crm_event_post) | **POST** /crmEvent | create a crmEvent
*CrmEventCategoryApi* | [**crm_event_category_count_get**](docs/CrmEventCategoryApi.md#crm_event_category_count_get) | **GET** /crmEventCategory/count | count crmEventCategory
*CrmEventCategoryApi* | [**crm_event_category_get**](docs/CrmEventCategoryApi.md#crm_event_category_get) | **GET** /crmEventCategory | query crmEventCategory
*CrmEventCategoryApi* | [**crm_event_category_id_id_delete**](docs/CrmEventCategoryApi.md#crm_event_category_id_id_delete) | **DELETE** /crmEventCategory/id/{id} | delete a crmEventCategory
*CrmEventCategoryApi* | [**crm_event_category_id_id_get**](docs/CrmEventCategoryApi.md#crm_event_category_id_id_get) | **GET** /crmEventCategory/id/{id} | query a specific crmEventCategory
*CrmEventCategoryApi* | [**crm_event_category_id_id_put**](docs/CrmEventCategoryApi.md#crm_event_category_id_id_put) | **PUT** /crmEventCategory/id/{id} | update a crmEventCategory
*CrmEventCategoryApi* | [**crm_event_category_post**](docs/CrmEventCategoryApi.md#crm_event_category_post) | **POST** /crmEventCategory | create a crmEventCategory
*CurrencyApi* | [**currency_company_currency_get**](docs/CurrencyApi.md#currency_company_currency_get) | **GET** /currency/companyCurrency | 
*CurrencyApi* | [**currency_count_get**](docs/CurrencyApi.md#currency_count_get) | **GET** /currency/count | count currency
*CurrencyApi* | [**currency_get**](docs/CurrencyApi.md#currency_get) | **GET** /currency | query currency
*CurrencyApi* | [**currency_id_id_get**](docs/CurrencyApi.md#currency_id_id_get) | **GET** /currency/id/{id} | query a specific currency
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_count_get**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_count_get) | **GET** /customAttributeDefinition/count | count customAttributeDefinition
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_get**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_get) | **GET** /customAttributeDefinition | query customAttributeDefinition
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_id_id_delete**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_id_id_delete) | **DELETE** /customAttributeDefinition/id/{id} | delete a customAttributeDefinition
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_id_id_get**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_id_id_get) | **GET** /customAttributeDefinition/id/{id} | query a specific customAttributeDefinition
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_id_id_put**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_id_id_put) | **PUT** /customAttributeDefinition/id/{id} | update a customAttributeDefinition
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_post**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_post) | **POST** /customAttributeDefinition | create a customAttributeDefinition
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_read_order_get**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_read_order_get) | **GET** /customAttributeDefinition/readOrder | 
*CustomAttributeDefinitionApi* | [**custom_attribute_definition_update_order_post**](docs/CustomAttributeDefinitionApi.md#custom_attribute_definition_update_order_post) | **POST** /customAttributeDefinition/updateOrder | 
*CustomerApi* | [**customer_count_get**](docs/CustomerApi.md#customer_count_get) | **GET** /customer/count | count customer
*CustomerApi* | [**customer_get**](docs/CustomerApi.md#customer_get) | **GET** /customer | query customer
*CustomerApi* | [**customer_id_id_delete**](docs/CustomerApi.md#customer_id_id_delete) | **DELETE** /customer/id/{id} | delete a customer
*CustomerApi* | [**customer_id_id_download_image_get**](docs/CustomerApi.md#customer_id_id_download_image_get) | **GET** /customer/id/{id}/downloadImage | 
*CustomerApi* | [**customer_id_id_get**](docs/CustomerApi.md#customer_id_id_get) | **GET** /customer/id/{id} | query a specific customer
*CustomerApi* | [**customer_id_id_put**](docs/CustomerApi.md#customer_id_id_put) | **PUT** /customer/id/{id} | update a customer
*CustomerApi* | [**customer_id_id_upload_image_post**](docs/CustomerApi.md#customer_id_id_upload_image_post) | **POST** /customer/id/{id}/uploadImage | 
*CustomerApi* | [**customer_post**](docs/CustomerApi.md#customer_post) | **POST** /customer | create a customer
*CustomerCategoryApi* | [**customer_category_count_get**](docs/CustomerCategoryApi.md#customer_category_count_get) | **GET** /customerCategory/count | count customerCategory
*CustomerCategoryApi* | [**customer_category_get**](docs/CustomerCategoryApi.md#customer_category_get) | **GET** /customerCategory | query customerCategory
*CustomerCategoryApi* | [**customer_category_id_id_delete**](docs/CustomerCategoryApi.md#customer_category_id_id_delete) | **DELETE** /customerCategory/id/{id} | delete a customerCategory
*CustomerCategoryApi* | [**customer_category_id_id_get**](docs/CustomerCategoryApi.md#customer_category_id_id_get) | **GET** /customerCategory/id/{id} | query a specific customerCategory
*CustomerCategoryApi* | [**customer_category_id_id_put**](docs/CustomerCategoryApi.md#customer_category_id_id_put) | **PUT** /customerCategory/id/{id} | update a customerCategory
*CustomerCategoryApi* | [**customer_category_post**](docs/CustomerCategoryApi.md#customer_category_post) | **POST** /customerCategory | create a customerCategory
*CustomerLeadLossReasonApi* | [**customer_lead_loss_reason_count_get**](docs/CustomerLeadLossReasonApi.md#customer_lead_loss_reason_count_get) | **GET** /customerLeadLossReason/count | count customerLeadLossReason
*CustomerLeadLossReasonApi* | [**customer_lead_loss_reason_get**](docs/CustomerLeadLossReasonApi.md#customer_lead_loss_reason_get) | **GET** /customerLeadLossReason | query customerLeadLossReason
*CustomerLeadLossReasonApi* | [**customer_lead_loss_reason_id_id_delete**](docs/CustomerLeadLossReasonApi.md#customer_lead_loss_reason_id_id_delete) | **DELETE** /customerLeadLossReason/id/{id} | delete a customerLeadLossReason
*CustomerLeadLossReasonApi* | [**customer_lead_loss_reason_id_id_get**](docs/CustomerLeadLossReasonApi.md#customer_lead_loss_reason_id_id_get) | **GET** /customerLeadLossReason/id/{id} | query a specific customerLeadLossReason
*CustomerLeadLossReasonApi* | [**customer_lead_loss_reason_id_id_put**](docs/CustomerLeadLossReasonApi.md#customer_lead_loss_reason_id_id_put) | **PUT** /customerLeadLossReason/id/{id} | update a customerLeadLossReason
*CustomerLeadLossReasonApi* | [**customer_lead_loss_reason_post**](docs/CustomerLeadLossReasonApi.md#customer_lead_loss_reason_post) | **POST** /customerLeadLossReason | create a customerLeadLossReason
*CustomerTopicApi* | [**customer_topic_count_get**](docs/CustomerTopicApi.md#customer_topic_count_get) | **GET** /customerTopic/count | count customerTopic
*CustomerTopicApi* | [**customer_topic_get**](docs/CustomerTopicApi.md#customer_topic_get) | **GET** /customerTopic | query customerTopic
*CustomerTopicApi* | [**customer_topic_id_id_delete**](docs/CustomerTopicApi.md#customer_topic_id_id_delete) | **DELETE** /customerTopic/id/{id} | delete a customerTopic
*CustomerTopicApi* | [**customer_topic_id_id_get**](docs/CustomerTopicApi.md#customer_topic_id_id_get) | **GET** /customerTopic/id/{id} | query a specific customerTopic
*CustomerTopicApi* | [**customer_topic_id_id_put**](docs/CustomerTopicApi.md#customer_topic_id_id_put) | **PUT** /customerTopic/id/{id} | update a customerTopic
*CustomerTopicApi* | [**customer_topic_post**](docs/CustomerTopicApi.md#customer_topic_post) | **POST** /customerTopic | create a customerTopic
*CustomsTariffNumberApi* | [**customs_tariff_number_count_get**](docs/CustomsTariffNumberApi.md#customs_tariff_number_count_get) | **GET** /customsTariffNumber/count | count customsTariffNumber
*CustomsTariffNumberApi* | [**customs_tariff_number_get**](docs/CustomsTariffNumberApi.md#customs_tariff_number_get) | **GET** /customsTariffNumber | query customsTariffNumber
*CustomsTariffNumberApi* | [**customs_tariff_number_id_id_delete**](docs/CustomsTariffNumberApi.md#customs_tariff_number_id_id_delete) | **DELETE** /customsTariffNumber/id/{id} | delete a customsTariffNumber
*CustomsTariffNumberApi* | [**customs_tariff_number_id_id_get**](docs/CustomsTariffNumberApi.md#customs_tariff_number_id_id_get) | **GET** /customsTariffNumber/id/{id} | query a specific customsTariffNumber
*CustomsTariffNumberApi* | [**customs_tariff_number_id_id_put**](docs/CustomsTariffNumberApi.md#customs_tariff_number_id_id_put) | **PUT** /customsTariffNumber/id/{id} | update a customsTariffNumber
*CustomsTariffNumberApi* | [**customs_tariff_number_post**](docs/CustomsTariffNumberApi.md#customs_tariff_number_post) | **POST** /customsTariffNumber | create a customsTariffNumber
*DocumentApi* | [**document_copy_post**](docs/DocumentApi.md#document_copy_post) | **POST** /document/copy | 
*DocumentApi* | [**document_count_get**](docs/DocumentApi.md#document_count_get) | **GET** /document/count | count document
*DocumentApi* | [**document_get**](docs/DocumentApi.md#document_get) | **GET** /document | query document
*DocumentApi* | [**document_id_id_copy_post**](docs/DocumentApi.md#document_id_id_copy_post) | **POST** /document/id/{id}/copy | 
*DocumentApi* | [**document_id_id_delete**](docs/DocumentApi.md#document_id_id_delete) | **DELETE** /document/id/{id} | delete a document
*DocumentApi* | [**document_id_id_download_document_version_get**](docs/DocumentApi.md#document_id_id_download_document_version_get) | **GET** /document/id/{id}/downloadDocumentVersion | 
*DocumentApi* | [**document_id_id_download_document_versions_zipped_get**](docs/DocumentApi.md#document_id_id_download_document_versions_zipped_get) | **GET** /document/id/{id}/downloadDocumentVersionsZipped | 
*DocumentApi* | [**document_id_id_download_get**](docs/DocumentApi.md#document_id_id_download_get) | **GET** /document/id/{id}/download | 
*DocumentApi* | [**document_id_id_get**](docs/DocumentApi.md#document_id_id_get) | **GET** /document/id/{id} | query a specific document
*DocumentApi* | [**document_id_id_put**](docs/DocumentApi.md#document_id_id_put) | **PUT** /document/id/{id} | update a document
*DocumentApi* | [**document_id_id_upload_post**](docs/DocumentApi.md#document_id_id_upload_post) | **POST** /document/id/{id}/upload | 
*DocumentApi* | [**document_upload_post**](docs/DocumentApi.md#document_upload_post) | **POST** /document/upload | 
*ExternalConnectionApi* | [**external_connection_count_get**](docs/ExternalConnectionApi.md#external_connection_count_get) | **GET** /externalConnection/count | count externalConnection
*ExternalConnectionApi* | [**external_connection_get**](docs/ExternalConnectionApi.md#external_connection_get) | **GET** /externalConnection | query externalConnection
*ExternalConnectionApi* | [**external_connection_id_id_get**](docs/ExternalConnectionApi.md#external_connection_id_id_get) | **GET** /externalConnection/id/{id} | query a specific externalConnection
*FinancialYearApi* | [**financial_year_count_get**](docs/FinancialYearApi.md#financial_year_count_get) | **GET** /financialYear/count | count financialYear
*FinancialYearApi* | [**financial_year_get**](docs/FinancialYearApi.md#financial_year_get) | **GET** /financialYear | query financialYear
*FinancialYearApi* | [**financial_year_id_id_delete**](docs/FinancialYearApi.md#financial_year_id_id_delete) | **DELETE** /financialYear/id/{id} | delete a financialYear
*FinancialYearApi* | [**financial_year_id_id_generate_periods_post**](docs/FinancialYearApi.md#financial_year_id_id_generate_periods_post) | **POST** /financialYear/id/{id}/generatePeriods | 
*FinancialYearApi* | [**financial_year_id_id_get**](docs/FinancialYearApi.md#financial_year_id_id_get) | **GET** /financialYear/id/{id} | query a specific financialYear
*FinancialYearApi* | [**financial_year_id_id_put**](docs/FinancialYearApi.md#financial_year_id_id_put) | **PUT** /financialYear/id/{id} | update a financialYear
*FinancialYearApi* | [**financial_year_post**](docs/FinancialYearApi.md#financial_year_post) | **POST** /financialYear | create a financialYear
*FulfillmentProviderApi* | [**fulfillment_provider_count_get**](docs/FulfillmentProviderApi.md#fulfillment_provider_count_get) | **GET** /fulfillmentProvider/count | count fulfillmentProvider
*FulfillmentProviderApi* | [**fulfillment_provider_get**](docs/FulfillmentProviderApi.md#fulfillment_provider_get) | **GET** /fulfillmentProvider | query fulfillmentProvider
*FulfillmentProviderApi* | [**fulfillment_provider_id_id_get**](docs/FulfillmentProviderApi.md#fulfillment_provider_id_id_get) | **GET** /fulfillmentProvider/id/{id} | query a specific fulfillmentProvider
*IncomingGoodsApi* | [**incoming_goods_count_get**](docs/IncomingGoodsApi.md#incoming_goods_count_get) | **GET** /incomingGoods/count | count incomingGoods
*IncomingGoodsApi* | [**incoming_goods_get**](docs/IncomingGoodsApi.md#incoming_goods_get) | **GET** /incomingGoods | query incomingGoods
*IncomingGoodsApi* | [**incoming_goods_id_id_add_purchase_orders_post**](docs/IncomingGoodsApi.md#incoming_goods_id_id_add_purchase_orders_post) | **POST** /incomingGoods/id/{id}/addPurchaseOrders | 
*IncomingGoodsApi* | [**incoming_goods_id_id_create_compensation_shipment_post**](docs/IncomingGoodsApi.md#incoming_goods_id_id_create_compensation_shipment_post) | **POST** /incomingGoods/id/{id}/createCompensationShipment | 
*IncomingGoodsApi* | [**incoming_goods_id_id_create_credit_note_post**](docs/IncomingGoodsApi.md#incoming_goods_id_id_create_credit_note_post) | **POST** /incomingGoods/id/{id}/createCreditNote | 
*IncomingGoodsApi* | [**incoming_goods_id_id_create_return_labels_post**](docs/IncomingGoodsApi.md#incoming_goods_id_id_create_return_labels_post) | **POST** /incomingGoods/id/{id}/createReturnLabels | 
*IncomingGoodsApi* | [**incoming_goods_id_id_create_supplier_return_post**](docs/IncomingGoodsApi.md#incoming_goods_id_id_create_supplier_return_post) | **POST** /incomingGoods/id/{id}/createSupplierReturn | 
*IncomingGoodsApi* | [**incoming_goods_id_id_delete**](docs/IncomingGoodsApi.md#incoming_goods_id_id_delete) | **DELETE** /incomingGoods/id/{id} | delete a incomingGoods
*IncomingGoodsApi* | [**incoming_goods_id_id_get**](docs/IncomingGoodsApi.md#incoming_goods_id_id_get) | **GET** /incomingGoods/id/{id} | query a specific incomingGoods
*IncomingGoodsApi* | [**incoming_goods_id_id_incoming_bookings_get**](docs/IncomingGoodsApi.md#incoming_goods_id_id_incoming_bookings_get) | **GET** /incomingGoods/id/{id}/incomingBookings | 
*IncomingGoodsApi* | [**incoming_goods_id_id_put**](docs/IncomingGoodsApi.md#incoming_goods_id_id_put) | **PUT** /incomingGoods/id/{id} | update a incomingGoods
*IncomingGoodsApi* | [**incoming_goods_id_id_update_incoming_bookings_post**](docs/IncomingGoodsApi.md#incoming_goods_id_id_update_incoming_bookings_post) | **POST** /incomingGoods/id/{id}/updateIncomingBookings | 
*IncomingGoodsApi* | [**incoming_goods_post**](docs/IncomingGoodsApi.md#incoming_goods_post) | **POST** /incomingGoods | create a incomingGoods
*InternalTransportReferenceApi* | [**internal_transport_reference_count_get**](docs/InternalTransportReferenceApi.md#internal_transport_reference_count_get) | **GET** /internalTransportReference/count | count internalTransportReference
*InternalTransportReferenceApi* | [**internal_transport_reference_get**](docs/InternalTransportReferenceApi.md#internal_transport_reference_get) | **GET** /internalTransportReference | query internalTransportReference
*InternalTransportReferenceApi* | [**internal_transport_reference_id_id_create_label_post**](docs/InternalTransportReferenceApi.md#internal_transport_reference_id_id_create_label_post) | **POST** /internalTransportReference/id/{id}/createLabel | 
*InternalTransportReferenceApi* | [**internal_transport_reference_id_id_delete**](docs/InternalTransportReferenceApi.md#internal_transport_reference_id_id_delete) | **DELETE** /internalTransportReference/id/{id} | delete a internalTransportReference
*InternalTransportReferenceApi* | [**internal_transport_reference_id_id_download_latest_label_get**](docs/InternalTransportReferenceApi.md#internal_transport_reference_id_id_download_latest_label_get) | **GET** /internalTransportReference/id/{id}/downloadLatestLabel | 
*InternalTransportReferenceApi* | [**internal_transport_reference_id_id_get**](docs/InternalTransportReferenceApi.md#internal_transport_reference_id_id_get) | **GET** /internalTransportReference/id/{id} | query a specific internalTransportReference
*InternalTransportReferenceApi* | [**internal_transport_reference_id_id_put**](docs/InternalTransportReferenceApi.md#internal_transport_reference_id_id_put) | **PUT** /internalTransportReference/id/{id} | update a internalTransportReference
*InternalTransportReferenceApi* | [**internal_transport_reference_post**](docs/InternalTransportReferenceApi.md#internal_transport_reference_post) | **POST** /internalTransportReference | create a internalTransportReference
*JobApi* | [**job_abort_get**](docs/JobApi.md#job_abort_get) | **GET** /job/abort | 
*JobApi* | [**job_status_get**](docs/JobApi.md#job_status_get) | **GET** /job/status | 
*LeadApi* | [**lead_count_get**](docs/LeadApi.md#lead_count_get) | **GET** /lead/count | count lead
*LeadApi* | [**lead_get**](docs/LeadApi.md#lead_get) | **GET** /lead | query lead
*LeadApi* | [**lead_id_id_convert_lead_to_customer_get**](docs/LeadApi.md#lead_id_id_convert_lead_to_customer_get) | **GET** /lead/id/{id}/convertLeadToCustomer | 
*LeadApi* | [**lead_id_id_delete**](docs/LeadApi.md#lead_id_id_delete) | **DELETE** /lead/id/{id} | delete a lead
*LeadApi* | [**lead_id_id_download_image_get**](docs/LeadApi.md#lead_id_id_download_image_get) | **GET** /lead/id/{id}/downloadImage | 
*LeadApi* | [**lead_id_id_get**](docs/LeadApi.md#lead_id_id_get) | **GET** /lead/id/{id} | query a specific lead
*LeadApi* | [**lead_id_id_put**](docs/LeadApi.md#lead_id_id_put) | **PUT** /lead/id/{id} | update a lead
*LeadApi* | [**lead_id_id_upload_image_post**](docs/LeadApi.md#lead_id_id_upload_image_post) | **POST** /lead/id/{id}/uploadImage | 
*LeadApi* | [**lead_post**](docs/LeadApi.md#lead_post) | **POST** /lead | create a lead
*LeadRatingApi* | [**lead_rating_count_get**](docs/LeadRatingApi.md#lead_rating_count_get) | **GET** /leadRating/count | count leadRating
*LeadRatingApi* | [**lead_rating_get**](docs/LeadRatingApi.md#lead_rating_get) | **GET** /leadRating | query leadRating
*LeadRatingApi* | [**lead_rating_id_id_delete**](docs/LeadRatingApi.md#lead_rating_id_id_delete) | **DELETE** /leadRating/id/{id} | delete a leadRating
*LeadRatingApi* | [**lead_rating_id_id_get**](docs/LeadRatingApi.md#lead_rating_id_id_get) | **GET** /leadRating/id/{id} | query a specific leadRating
*LeadRatingApi* | [**lead_rating_id_id_put**](docs/LeadRatingApi.md#lead_rating_id_id_put) | **PUT** /leadRating/id/{id} | update a leadRating
*LeadRatingApi* | [**lead_rating_post**](docs/LeadRatingApi.md#lead_rating_post) | **POST** /leadRating | create a leadRating
*LeadSourceApi* | [**lead_source_count_get**](docs/LeadSourceApi.md#lead_source_count_get) | **GET** /leadSource/count | count leadSource
*LeadSourceApi* | [**lead_source_get**](docs/LeadSourceApi.md#lead_source_get) | **GET** /leadSource | query leadSource
*LeadSourceApi* | [**lead_source_id_id_delete**](docs/LeadSourceApi.md#lead_source_id_id_delete) | **DELETE** /leadSource/id/{id} | delete a leadSource
*LeadSourceApi* | [**lead_source_id_id_get**](docs/LeadSourceApi.md#lead_source_id_id_get) | **GET** /leadSource/id/{id} | query a specific leadSource
*LeadSourceApi* | [**lead_source_id_id_put**](docs/LeadSourceApi.md#lead_source_id_id_put) | **PUT** /leadSource/id/{id} | update a leadSource
*LeadSourceApi* | [**lead_source_post**](docs/LeadSourceApi.md#lead_source_post) | **POST** /leadSource | create a leadSource
*LedgerAccountApi* | [**ledger_account_count_get**](docs/LedgerAccountApi.md#ledger_account_count_get) | **GET** /ledgerAccount/count | count ledgerAccount
*LedgerAccountApi* | [**ledger_account_get**](docs/LedgerAccountApi.md#ledger_account_get) | **GET** /ledgerAccount | query ledgerAccount
*LedgerAccountApi* | [**ledger_account_id_id_delete**](docs/LedgerAccountApi.md#ledger_account_id_id_delete) | **DELETE** /ledgerAccount/id/{id} | delete a ledgerAccount
*LedgerAccountApi* | [**ledger_account_id_id_get**](docs/LedgerAccountApi.md#ledger_account_id_id_get) | **GET** /ledgerAccount/id/{id} | query a specific ledgerAccount
*LedgerAccountApi* | [**ledger_account_id_id_put**](docs/LedgerAccountApi.md#ledger_account_id_id_put) | **PUT** /ledgerAccount/id/{id} | update a ledgerAccount
*LedgerAccountApi* | [**ledger_account_post**](docs/LedgerAccountApi.md#ledger_account_post) | **POST** /ledgerAccount | create a ledgerAccount
*LegalFormApi* | [**legal_form_count_get**](docs/LegalFormApi.md#legal_form_count_get) | **GET** /legalForm/count | count legalForm
*LegalFormApi* | [**legal_form_get**](docs/LegalFormApi.md#legal_form_get) | **GET** /legalForm | query legalForm
*LegalFormApi* | [**legal_form_id_id_delete**](docs/LegalFormApi.md#legal_form_id_id_delete) | **DELETE** /legalForm/id/{id} | delete a legalForm
*LegalFormApi* | [**legal_form_id_id_get**](docs/LegalFormApi.md#legal_form_id_id_get) | **GET** /legalForm/id/{id} | query a specific legalForm
*LegalFormApi* | [**legal_form_id_id_put**](docs/LegalFormApi.md#legal_form_id_id_put) | **PUT** /legalForm/id/{id} | update a legalForm
*LegalFormApi* | [**legal_form_post**](docs/LegalFormApi.md#legal_form_post) | **POST** /legalForm | create a legalForm
*LoadingEquipmentIdentifierApi* | [**loading_equipment_identifier_count_get**](docs/LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_count_get) | **GET** /loadingEquipmentIdentifier/count | count loadingEquipmentIdentifier
*LoadingEquipmentIdentifierApi* | [**loading_equipment_identifier_get**](docs/LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_get) | **GET** /loadingEquipmentIdentifier | query loadingEquipmentIdentifier
*LoadingEquipmentIdentifierApi* | [**loading_equipment_identifier_id_id_delete**](docs/LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_id_id_delete) | **DELETE** /loadingEquipmentIdentifier/id/{id} | delete a loadingEquipmentIdentifier
*LoadingEquipmentIdentifierApi* | [**loading_equipment_identifier_id_id_get**](docs/LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_id_id_get) | **GET** /loadingEquipmentIdentifier/id/{id} | query a specific loadingEquipmentIdentifier
*LoadingEquipmentIdentifierApi* | [**loading_equipment_identifier_id_id_put**](docs/LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_id_id_put) | **PUT** /loadingEquipmentIdentifier/id/{id} | update a loadingEquipmentIdentifier
*LoadingEquipmentIdentifierApi* | [**loading_equipment_identifier_post**](docs/LoadingEquipmentIdentifierApi.md#loading_equipment_identifier_post) | **POST** /loadingEquipmentIdentifier | create a loadingEquipmentIdentifier
*MailTemplateApi* | [**mail_template_count_get**](docs/MailTemplateApi.md#mail_template_count_get) | **GET** /mailTemplate/count | count mailTemplate
*MailTemplateApi* | [**mail_template_get**](docs/MailTemplateApi.md#mail_template_get) | **GET** /mailTemplate | query mailTemplate
*MailTemplateApi* | [**mail_template_id_id_delete**](docs/MailTemplateApi.md#mail_template_id_id_delete) | **DELETE** /mailTemplate/id/{id} | delete a mailTemplate
*MailTemplateApi* | [**mail_template_id_id_get**](docs/MailTemplateApi.md#mail_template_id_id_get) | **GET** /mailTemplate/id/{id} | query a specific mailTemplate
*MailTemplateApi* | [**mail_template_id_id_put**](docs/MailTemplateApi.md#mail_template_id_id_put) | **PUT** /mailTemplate/id/{id} | update a mailTemplate
*MailTemplateApi* | [**mail_template_post**](docs/MailTemplateApi.md#mail_template_post) | **POST** /mailTemplate | create a mailTemplate
*ManufacturerApi* | [**manufacturer_count_get**](docs/ManufacturerApi.md#manufacturer_count_get) | **GET** /manufacturer/count | count manufacturer
*ManufacturerApi* | [**manufacturer_get**](docs/ManufacturerApi.md#manufacturer_get) | **GET** /manufacturer | query manufacturer
*ManufacturerApi* | [**manufacturer_id_id_delete**](docs/ManufacturerApi.md#manufacturer_id_id_delete) | **DELETE** /manufacturer/id/{id} | delete a manufacturer
*ManufacturerApi* | [**manufacturer_id_id_get**](docs/ManufacturerApi.md#manufacturer_id_id_get) | **GET** /manufacturer/id/{id} | query a specific manufacturer
*ManufacturerApi* | [**manufacturer_id_id_put**](docs/ManufacturerApi.md#manufacturer_id_id_put) | **PUT** /manufacturer/id/{id} | update a manufacturer
*ManufacturerApi* | [**manufacturer_post**](docs/ManufacturerApi.md#manufacturer_post) | **POST** /manufacturer | create a manufacturer
*MetaApi* | [**meta_query_filter_properties_get**](docs/MetaApi.md#meta_query_filter_properties_get) | **GET** /meta/queryFilterProperties | 
*MetaApi* | [**meta_query_sort_properties_get**](docs/MetaApi.md#meta_query_sort_properties_get) | **GET** /meta/querySortProperties | 
*MetaApi* | [**meta_resources_get**](docs/MetaApi.md#meta_resources_get) | **GET** /meta/resources | 
*NotificationApi* | [**notification_count_get**](docs/NotificationApi.md#notification_count_get) | **GET** /notification/count | count notification
*NotificationApi* | [**notification_get**](docs/NotificationApi.md#notification_get) | **GET** /notification | query notification
*NotificationApi* | [**notification_id_id_get**](docs/NotificationApi.md#notification_id_id_get) | **GET** /notification/id/{id} | query a specific notification
*NotificationApi* | [**notification_id_id_mark_read_post**](docs/NotificationApi.md#notification_id_id_mark_read_post) | **POST** /notification/id/{id}/markRead | 
*OpportunityApi* | [**opportunity_count_get**](docs/OpportunityApi.md#opportunity_count_get) | **GET** /opportunity/count | count opportunity
*OpportunityApi* | [**opportunity_get**](docs/OpportunityApi.md#opportunity_get) | **GET** /opportunity | query opportunity
*OpportunityApi* | [**opportunity_id_id_delete**](docs/OpportunityApi.md#opportunity_id_id_delete) | **DELETE** /opportunity/id/{id} | delete a opportunity
*OpportunityApi* | [**opportunity_id_id_get**](docs/OpportunityApi.md#opportunity_id_id_get) | **GET** /opportunity/id/{id} | query a specific opportunity
*OpportunityApi* | [**opportunity_id_id_link_quotation_post**](docs/OpportunityApi.md#opportunity_id_id_link_quotation_post) | **POST** /opportunity/id/{id}/linkQuotation | 
*OpportunityApi* | [**opportunity_id_id_put**](docs/OpportunityApi.md#opportunity_id_id_put) | **PUT** /opportunity/id/{id} | update a opportunity
*OpportunityApi* | [**opportunity_post**](docs/OpportunityApi.md#opportunity_post) | **POST** /opportunity | create a opportunity
*OpportunityTopicApi* | [**opportunity_topic_count_get**](docs/OpportunityTopicApi.md#opportunity_topic_count_get) | **GET** /opportunityTopic/count | count opportunityTopic
*OpportunityTopicApi* | [**opportunity_topic_get**](docs/OpportunityTopicApi.md#opportunity_topic_get) | **GET** /opportunityTopic | query opportunityTopic
*OpportunityTopicApi* | [**opportunity_topic_id_id_delete**](docs/OpportunityTopicApi.md#opportunity_topic_id_id_delete) | **DELETE** /opportunityTopic/id/{id} | delete a opportunityTopic
*OpportunityTopicApi* | [**opportunity_topic_id_id_get**](docs/OpportunityTopicApi.md#opportunity_topic_id_id_get) | **GET** /opportunityTopic/id/{id} | query a specific opportunityTopic
*OpportunityTopicApi* | [**opportunity_topic_id_id_put**](docs/OpportunityTopicApi.md#opportunity_topic_id_id_put) | **PUT** /opportunityTopic/id/{id} | update a opportunityTopic
*OpportunityTopicApi* | [**opportunity_topic_post**](docs/OpportunityTopicApi.md#opportunity_topic_post) | **POST** /opportunityTopic | create a opportunityTopic
*OpportunityWinLossReasonApi* | [**opportunity_win_loss_reason_count_get**](docs/OpportunityWinLossReasonApi.md#opportunity_win_loss_reason_count_get) | **GET** /opportunityWinLossReason/count | count opportunityWinLossReason
*OpportunityWinLossReasonApi* | [**opportunity_win_loss_reason_get**](docs/OpportunityWinLossReasonApi.md#opportunity_win_loss_reason_get) | **GET** /opportunityWinLossReason | query opportunityWinLossReason
*OpportunityWinLossReasonApi* | [**opportunity_win_loss_reason_id_id_delete**](docs/OpportunityWinLossReasonApi.md#opportunity_win_loss_reason_id_id_delete) | **DELETE** /opportunityWinLossReason/id/{id} | delete a opportunityWinLossReason
*OpportunityWinLossReasonApi* | [**opportunity_win_loss_reason_id_id_get**](docs/OpportunityWinLossReasonApi.md#opportunity_win_loss_reason_id_id_get) | **GET** /opportunityWinLossReason/id/{id} | query a specific opportunityWinLossReason
*OpportunityWinLossReasonApi* | [**opportunity_win_loss_reason_id_id_put**](docs/OpportunityWinLossReasonApi.md#opportunity_win_loss_reason_id_id_put) | **PUT** /opportunityWinLossReason/id/{id} | update a opportunityWinLossReason
*OpportunityWinLossReasonApi* | [**opportunity_win_loss_reason_post**](docs/OpportunityWinLossReasonApi.md#opportunity_win_loss_reason_post) | **POST** /opportunityWinLossReason | create a opportunityWinLossReason
*PartyApi* | [**party_count_get**](docs/PartyApi.md#party_count_get) | **GET** /party/count | count party
*PartyApi* | [**party_get**](docs/PartyApi.md#party_get) | **GET** /party | query party
*PartyApi* | [**party_id_id_delete**](docs/PartyApi.md#party_id_id_delete) | **DELETE** /party/id/{id} | delete a party
*PartyApi* | [**party_id_id_download_image_get**](docs/PartyApi.md#party_id_id_download_image_get) | **GET** /party/id/{id}/downloadImage | 
*PartyApi* | [**party_id_id_get**](docs/PartyApi.md#party_id_id_get) | **GET** /party/id/{id} | query a specific party
*PartyApi* | [**party_id_id_put**](docs/PartyApi.md#party_id_id_put) | **PUT** /party/id/{id} | update a party
*PartyApi* | [**party_id_id_upload_image_post**](docs/PartyApi.md#party_id_id_upload_image_post) | **POST** /party/id/{id}/uploadImage | 
*PartyApi* | [**party_post**](docs/PartyApi.md#party_post) | **POST** /party | create a party
*PartyRatingApi* | [**party_rating_count_get**](docs/PartyRatingApi.md#party_rating_count_get) | **GET** /partyRating/count | count partyRating
*PartyRatingApi* | [**party_rating_get**](docs/PartyRatingApi.md#party_rating_get) | **GET** /partyRating | query partyRating
*PartyRatingApi* | [**party_rating_id_id_delete**](docs/PartyRatingApi.md#party_rating_id_id_delete) | **DELETE** /partyRating/id/{id} | delete a partyRating
*PartyRatingApi* | [**party_rating_id_id_get**](docs/PartyRatingApi.md#party_rating_id_id_get) | **GET** /partyRating/id/{id} | query a specific partyRating
*PartyRatingApi* | [**party_rating_id_id_put**](docs/PartyRatingApi.md#party_rating_id_id_put) | **PUT** /partyRating/id/{id} | update a partyRating
*PartyRatingApi* | [**party_rating_post**](docs/PartyRatingApi.md#party_rating_post) | **POST** /partyRating | create a partyRating
*PaymentMethodApi* | [**payment_method_count_get**](docs/PaymentMethodApi.md#payment_method_count_get) | **GET** /paymentMethod/count | count paymentMethod
*PaymentMethodApi* | [**payment_method_get**](docs/PaymentMethodApi.md#payment_method_get) | **GET** /paymentMethod | query paymentMethod
*PaymentMethodApi* | [**payment_method_id_id_delete**](docs/PaymentMethodApi.md#payment_method_id_id_delete) | **DELETE** /paymentMethod/id/{id} | delete a paymentMethod
*PaymentMethodApi* | [**payment_method_id_id_get**](docs/PaymentMethodApi.md#payment_method_id_id_get) | **GET** /paymentMethod/id/{id} | query a specific paymentMethod
*PaymentMethodApi* | [**payment_method_id_id_put**](docs/PaymentMethodApi.md#payment_method_id_id_put) | **PUT** /paymentMethod/id/{id} | update a paymentMethod
*PaymentMethodApi* | [**payment_method_post**](docs/PaymentMethodApi.md#payment_method_post) | **POST** /paymentMethod | create a paymentMethod
*PaymentRunApi* | [**payment_run_count_get**](docs/PaymentRunApi.md#payment_run_count_get) | **GET** /paymentRun/count | count paymentRun
*PaymentRunApi* | [**payment_run_get**](docs/PaymentRunApi.md#payment_run_get) | **GET** /paymentRun | query paymentRun
*PaymentRunApi* | [**payment_run_id_id_delete**](docs/PaymentRunApi.md#payment_run_id_id_delete) | **DELETE** /paymentRun/id/{id} | delete a paymentRun
*PaymentRunApi* | [**payment_run_id_id_get**](docs/PaymentRunApi.md#payment_run_id_id_get) | **GET** /paymentRun/id/{id} | query a specific paymentRun
*PaymentRunApi* | [**payment_run_id_id_put**](docs/PaymentRunApi.md#payment_run_id_id_put) | **PUT** /paymentRun/id/{id} | update a paymentRun
*PaymentRunItemApi* | [**payment_run_item_count_get**](docs/PaymentRunItemApi.md#payment_run_item_count_get) | **GET** /paymentRunItem/count | count paymentRunItem
*PaymentRunItemApi* | [**payment_run_item_get**](docs/PaymentRunItemApi.md#payment_run_item_get) | **GET** /paymentRunItem | query paymentRunItem
*PaymentRunItemApi* | [**payment_run_item_id_id_get**](docs/PaymentRunItemApi.md#payment_run_item_id_id_get) | **GET** /paymentRunItem/id/{id} | query a specific paymentRunItem
*PersonDepartmentApi* | [**person_department_count_get**](docs/PersonDepartmentApi.md#person_department_count_get) | **GET** /personDepartment/count | count personDepartment
*PersonDepartmentApi* | [**person_department_get**](docs/PersonDepartmentApi.md#person_department_get) | **GET** /personDepartment | query personDepartment
*PersonDepartmentApi* | [**person_department_id_id_delete**](docs/PersonDepartmentApi.md#person_department_id_id_delete) | **DELETE** /personDepartment/id/{id} | delete a personDepartment
*PersonDepartmentApi* | [**person_department_id_id_get**](docs/PersonDepartmentApi.md#person_department_id_id_get) | **GET** /personDepartment/id/{id} | query a specific personDepartment
*PersonDepartmentApi* | [**person_department_id_id_put**](docs/PersonDepartmentApi.md#person_department_id_id_put) | **PUT** /personDepartment/id/{id} | update a personDepartment
*PersonDepartmentApi* | [**person_department_post**](docs/PersonDepartmentApi.md#person_department_post) | **POST** /personDepartment | create a personDepartment
*PersonRoleApi* | [**person_role_count_get**](docs/PersonRoleApi.md#person_role_count_get) | **GET** /personRole/count | count personRole
*PersonRoleApi* | [**person_role_get**](docs/PersonRoleApi.md#person_role_get) | **GET** /personRole | query personRole
*PersonRoleApi* | [**person_role_id_id_delete**](docs/PersonRoleApi.md#person_role_id_id_delete) | **DELETE** /personRole/id/{id} | delete a personRole
*PersonRoleApi* | [**person_role_id_id_get**](docs/PersonRoleApi.md#person_role_id_id_get) | **GET** /personRole/id/{id} | query a specific personRole
*PersonRoleApi* | [**person_role_id_id_put**](docs/PersonRoleApi.md#person_role_id_id_put) | **PUT** /personRole/id/{id} | update a personRole
*PersonRoleApi* | [**person_role_post**](docs/PersonRoleApi.md#person_role_post) | **POST** /personRole | create a personRole
*PersonalAccountingCodeApi* | [**personal_accounting_code_count_get**](docs/PersonalAccountingCodeApi.md#personal_accounting_code_count_get) | **GET** /personalAccountingCode/count | count personalAccountingCode
*PersonalAccountingCodeApi* | [**personal_accounting_code_get**](docs/PersonalAccountingCodeApi.md#personal_accounting_code_get) | **GET** /personalAccountingCode | query personalAccountingCode
*PersonalAccountingCodeApi* | [**personal_accounting_code_id_id_delete**](docs/PersonalAccountingCodeApi.md#personal_accounting_code_id_id_delete) | **DELETE** /personalAccountingCode/id/{id} | delete a personalAccountingCode
*PersonalAccountingCodeApi* | [**personal_accounting_code_id_id_get**](docs/PersonalAccountingCodeApi.md#personal_accounting_code_id_id_get) | **GET** /personalAccountingCode/id/{id} | query a specific personalAccountingCode
*PersonalAccountingCodeApi* | [**personal_accounting_code_id_id_put**](docs/PersonalAccountingCodeApi.md#personal_accounting_code_id_id_put) | **PUT** /personalAccountingCode/id/{id} | update a personalAccountingCode
*PersonalAccountingCodeApi* | [**personal_accounting_code_post**](docs/PersonalAccountingCodeApi.md#personal_accounting_code_post) | **POST** /personalAccountingCode | create a personalAccountingCode
*PickApi* | [**pick_count_get**](docs/PickApi.md#pick_count_get) | **GET** /pick/count | count pick
*PickApi* | [**pick_get**](docs/PickApi.md#pick_get) | **GET** /pick | query pick
*PickApi* | [**pick_id_id_get**](docs/PickApi.md#pick_id_id_get) | **GET** /pick/id/{id} | query a specific pick
*PickCheckReasonApi* | [**pick_check_reason_count_get**](docs/PickCheckReasonApi.md#pick_check_reason_count_get) | **GET** /pickCheckReason/count | count pickCheckReason
*PickCheckReasonApi* | [**pick_check_reason_get**](docs/PickCheckReasonApi.md#pick_check_reason_get) | **GET** /pickCheckReason | query pickCheckReason
*PickCheckReasonApi* | [**pick_check_reason_id_id_delete**](docs/PickCheckReasonApi.md#pick_check_reason_id_id_delete) | **DELETE** /pickCheckReason/id/{id} | delete a pickCheckReason
*PickCheckReasonApi* | [**pick_check_reason_id_id_get**](docs/PickCheckReasonApi.md#pick_check_reason_id_id_get) | **GET** /pickCheckReason/id/{id} | query a specific pickCheckReason
*PickCheckReasonApi* | [**pick_check_reason_id_id_put**](docs/PickCheckReasonApi.md#pick_check_reason_id_id_put) | **PUT** /pickCheckReason/id/{id} | update a pickCheckReason
*PickCheckReasonApi* | [**pick_check_reason_post**](docs/PickCheckReasonApi.md#pick_check_reason_post) | **POST** /pickCheckReason | create a pickCheckReason
*PlaceOfServiceApi* | [**place_of_service_count_get**](docs/PlaceOfServiceApi.md#place_of_service_count_get) | **GET** /placeOfService/count | count placeOfService
*PlaceOfServiceApi* | [**place_of_service_get**](docs/PlaceOfServiceApi.md#place_of_service_get) | **GET** /placeOfService | query placeOfService
*PlaceOfServiceApi* | [**place_of_service_id_id_delete**](docs/PlaceOfServiceApi.md#place_of_service_id_id_delete) | **DELETE** /placeOfService/id/{id} | delete a placeOfService
*PlaceOfServiceApi* | [**place_of_service_id_id_get**](docs/PlaceOfServiceApi.md#place_of_service_id_id_get) | **GET** /placeOfService/id/{id} | query a specific placeOfService
*PlaceOfServiceApi* | [**place_of_service_id_id_put**](docs/PlaceOfServiceApi.md#place_of_service_id_id_put) | **PUT** /placeOfService/id/{id} | update a placeOfService
*PlaceOfServiceApi* | [**place_of_service_post**](docs/PlaceOfServiceApi.md#place_of_service_post) | **POST** /placeOfService | create a placeOfService
*ProductionOrderApi* | [**production_order_count_get**](docs/ProductionOrderApi.md#production_order_count_get) | **GET** /productionOrder/count | count productionOrder
*ProductionOrderApi* | [**production_order_fast_production_booking_post**](docs/ProductionOrderApi.md#production_order_fast_production_booking_post) | **POST** /productionOrder/fastProductionBooking | 
*ProductionOrderApi* | [**production_order_get**](docs/ProductionOrderApi.md#production_order_get) | **GET** /productionOrder | query productionOrder
*ProductionOrderApi* | [**production_order_id_id_create_picking_list_post**](docs/ProductionOrderApi.md#production_order_id_id_create_picking_list_post) | **POST** /productionOrder/id/{id}/createPickingList | 
*ProductionOrderApi* | [**production_order_id_id_delete**](docs/ProductionOrderApi.md#production_order_id_id_delete) | **DELETE** /productionOrder/id/{id} | delete a productionOrder
*ProductionOrderApi* | [**production_order_id_id_download_latest_production_order_pdf_get**](docs/ProductionOrderApi.md#production_order_id_id_download_latest_production_order_pdf_get) | **GET** /productionOrder/id/{id}/downloadLatestProductionOrderPdf | 
*ProductionOrderApi* | [**production_order_id_id_get**](docs/ProductionOrderApi.md#production_order_id_id_get) | **GET** /productionOrder/id/{id} | query a specific productionOrder
*ProductionOrderApi* | [**production_order_id_id_put**](docs/ProductionOrderApi.md#production_order_id_id_put) | **PUT** /productionOrder/id/{id} | update a productionOrder
*ProductionOrderApi* | [**production_order_post**](docs/ProductionOrderApi.md#production_order_post) | **POST** /productionOrder | create a productionOrder
*ProductionWorkScheduleApi* | [**production_work_schedule_count_get**](docs/ProductionWorkScheduleApi.md#production_work_schedule_count_get) | **GET** /productionWorkSchedule/count | count productionWorkSchedule
*ProductionWorkScheduleApi* | [**production_work_schedule_get**](docs/ProductionWorkScheduleApi.md#production_work_schedule_get) | **GET** /productionWorkSchedule | query productionWorkSchedule
*ProductionWorkScheduleApi* | [**production_work_schedule_id_id_delete**](docs/ProductionWorkScheduleApi.md#production_work_schedule_id_id_delete) | **DELETE** /productionWorkSchedule/id/{id} | delete a productionWorkSchedule
*ProductionWorkScheduleApi* | [**production_work_schedule_id_id_get**](docs/ProductionWorkScheduleApi.md#production_work_schedule_id_id_get) | **GET** /productionWorkSchedule/id/{id} | query a specific productionWorkSchedule
*ProductionWorkScheduleApi* | [**production_work_schedule_id_id_put**](docs/ProductionWorkScheduleApi.md#production_work_schedule_id_id_put) | **PUT** /productionWorkSchedule/id/{id} | update a productionWorkSchedule
*ProductionWorkScheduleApi* | [**production_work_schedule_post**](docs/ProductionWorkScheduleApi.md#production_work_schedule_post) | **POST** /productionWorkSchedule | create a productionWorkSchedule
*ProductionWorkScheduleAssignmentApi* | [**production_work_schedule_assignment_count_get**](docs/ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_count_get) | **GET** /productionWorkScheduleAssignment/count | count productionWorkScheduleAssignment
*ProductionWorkScheduleAssignmentApi* | [**production_work_schedule_assignment_get**](docs/ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_get) | **GET** /productionWorkScheduleAssignment | query productionWorkScheduleAssignment
*ProductionWorkScheduleAssignmentApi* | [**production_work_schedule_assignment_id_id_delete**](docs/ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_id_id_delete) | **DELETE** /productionWorkScheduleAssignment/id/{id} | delete a productionWorkScheduleAssignment
*ProductionWorkScheduleAssignmentApi* | [**production_work_schedule_assignment_id_id_get**](docs/ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_id_id_get) | **GET** /productionWorkScheduleAssignment/id/{id} | query a specific productionWorkScheduleAssignment
*ProductionWorkScheduleAssignmentApi* | [**production_work_schedule_assignment_id_id_put**](docs/ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_id_id_put) | **PUT** /productionWorkScheduleAssignment/id/{id} | update a productionWorkScheduleAssignment
*ProductionWorkScheduleAssignmentApi* | [**production_work_schedule_assignment_post**](docs/ProductionWorkScheduleAssignmentApi.md#production_work_schedule_assignment_post) | **POST** /productionWorkScheduleAssignment | create a productionWorkScheduleAssignment
*PropertyTranslationApi* | [**property_translation_read_property_translations_get**](docs/PropertyTranslationApi.md#property_translation_read_property_translations_get) | **GET** /propertyTranslation/readPropertyTranslations | 
*PropertyTranslationApi* | [**property_translation_update_property_translations_post**](docs/PropertyTranslationApi.md#property_translation_update_property_translations_post) | **POST** /propertyTranslation/updatePropertyTranslations | 
*PurchaseInvoiceApi* | [**purchase_invoice_count_get**](docs/PurchaseInvoiceApi.md#purchase_invoice_count_get) | **GET** /purchaseInvoice/count | count purchaseInvoice
*PurchaseInvoiceApi* | [**purchase_invoice_get**](docs/PurchaseInvoiceApi.md#purchase_invoice_get) | **GET** /purchaseInvoice | query purchaseInvoice
*PurchaseInvoiceApi* | [**purchase_invoice_id_id_create_credit_note_post**](docs/PurchaseInvoiceApi.md#purchase_invoice_id_id_create_credit_note_post) | **POST** /purchaseInvoice/id/{id}/createCreditNote | 
*PurchaseInvoiceApi* | [**purchase_invoice_id_id_delete**](docs/PurchaseInvoiceApi.md#purchase_invoice_id_id_delete) | **DELETE** /purchaseInvoice/id/{id} | delete a purchaseInvoice
*PurchaseInvoiceApi* | [**purchase_invoice_id_id_download_latest_purchase_invoice_document_get**](docs/PurchaseInvoiceApi.md#purchase_invoice_id_id_download_latest_purchase_invoice_document_get) | **GET** /purchaseInvoice/id/{id}/downloadLatestPurchaseInvoiceDocument | 
*PurchaseInvoiceApi* | [**purchase_invoice_id_id_get**](docs/PurchaseInvoiceApi.md#purchase_invoice_id_id_get) | **GET** /purchaseInvoice/id/{id} | query a specific purchaseInvoice
*PurchaseInvoiceApi* | [**purchase_invoice_id_id_put**](docs/PurchaseInvoiceApi.md#purchase_invoice_id_id_put) | **PUT** /purchaseInvoice/id/{id} | update a purchaseInvoice
*PurchaseInvoiceApi* | [**purchase_invoice_post**](docs/PurchaseInvoiceApi.md#purchase_invoice_post) | **POST** /purchaseInvoice | create a purchaseInvoice
*PurchaseOpenItemApi* | [**purchase_open_item_count_get**](docs/PurchaseOpenItemApi.md#purchase_open_item_count_get) | **GET** /purchaseOpenItem/count | count purchaseOpenItem
*PurchaseOpenItemApi* | [**purchase_open_item_get**](docs/PurchaseOpenItemApi.md#purchase_open_item_get) | **GET** /purchaseOpenItem | query purchaseOpenItem
*PurchaseOpenItemApi* | [**purchase_open_item_id_id_create_payment_application_post**](docs/PurchaseOpenItemApi.md#purchase_open_item_id_id_create_payment_application_post) | **POST** /purchaseOpenItem/id/{id}/createPaymentApplication | 
*PurchaseOpenItemApi* | [**purchase_open_item_id_id_get**](docs/PurchaseOpenItemApi.md#purchase_open_item_id_id_get) | **GET** /purchaseOpenItem/id/{id} | query a specific purchaseOpenItem
*PurchaseOrderApi* | [**purchase_order_count_get**](docs/PurchaseOrderApi.md#purchase_order_count_get) | **GET** /purchaseOrder/count | count purchaseOrder
*PurchaseOrderApi* | [**purchase_order_get**](docs/PurchaseOrderApi.md#purchase_order_get) | **GET** /purchaseOrder | query purchaseOrder
*PurchaseOrderApi* | [**purchase_order_id_id_create_dropshipping_delivery_note_pdf_post**](docs/PurchaseOrderApi.md#purchase_order_id_id_create_dropshipping_delivery_note_pdf_post) | **POST** /purchaseOrder/id/{id}/createDropshippingDeliveryNotePdf | 
*PurchaseOrderApi* | [**purchase_order_id_id_create_incoming_goods_post**](docs/PurchaseOrderApi.md#purchase_order_id_id_create_incoming_goods_post) | **POST** /purchaseOrder/id/{id}/createIncomingGoods | 
*PurchaseOrderApi* | [**purchase_order_id_id_create_purchase_invoice_post**](docs/PurchaseOrderApi.md#purchase_order_id_id_create_purchase_invoice_post) | **POST** /purchaseOrder/id/{id}/createPurchaseInvoice | 
*PurchaseOrderApi* | [**purchase_order_id_id_create_supplier_return_post**](docs/PurchaseOrderApi.md#purchase_order_id_id_create_supplier_return_post) | **POST** /purchaseOrder/id/{id}/createSupplierReturn | 
*PurchaseOrderApi* | [**purchase_order_id_id_delete**](docs/PurchaseOrderApi.md#purchase_order_id_id_delete) | **DELETE** /purchaseOrder/id/{id} | delete a purchaseOrder
*PurchaseOrderApi* | [**purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get**](docs/PurchaseOrderApi.md#purchase_order_id_id_download_latest_dropshipping_delivery_note_pdf_get) | **GET** /purchaseOrder/id/{id}/downloadLatestDropshippingDeliveryNotePdf | 
*PurchaseOrderApi* | [**purchase_order_id_id_download_latest_purchase_order_pdf_get**](docs/PurchaseOrderApi.md#purchase_order_id_id_download_latest_purchase_order_pdf_get) | **GET** /purchaseOrder/id/{id}/downloadLatestPurchaseOrderPdf | 
*PurchaseOrderApi* | [**purchase_order_id_id_get**](docs/PurchaseOrderApi.md#purchase_order_id_id_get) | **GET** /purchaseOrder/id/{id} | query a specific purchaseOrder
*PurchaseOrderApi* | [**purchase_order_id_id_process_dropshipping_post**](docs/PurchaseOrderApi.md#purchase_order_id_id_process_dropshipping_post) | **POST** /purchaseOrder/id/{id}/processDropshipping | 
*PurchaseOrderApi* | [**purchase_order_id_id_put**](docs/PurchaseOrderApi.md#purchase_order_id_id_put) | **PUT** /purchaseOrder/id/{id} | update a purchaseOrder
*PurchaseOrderApi* | [**purchase_order_post**](docs/PurchaseOrderApi.md#purchase_order_post) | **POST** /purchaseOrder | create a purchaseOrder
*PurchaseOrderRequestApi* | [**purchase_order_request_count_get**](docs/PurchaseOrderRequestApi.md#purchase_order_request_count_get) | **GET** /purchaseOrderRequest/count | count purchaseOrderRequest
*PurchaseOrderRequestApi* | [**purchase_order_request_get**](docs/PurchaseOrderRequestApi.md#purchase_order_request_get) | **GET** /purchaseOrderRequest | query purchaseOrderRequest
*PurchaseOrderRequestApi* | [**purchase_order_request_id_id_create_blanket_purchase_order_post**](docs/PurchaseOrderRequestApi.md#purchase_order_request_id_id_create_blanket_purchase_order_post) | **POST** /purchaseOrderRequest/id/{id}/createBlanketPurchaseOrder | 
*PurchaseOrderRequestApi* | [**purchase_order_request_id_id_create_purchase_order_post**](docs/PurchaseOrderRequestApi.md#purchase_order_request_id_id_create_purchase_order_post) | **POST** /purchaseOrderRequest/id/{id}/createPurchaseOrder | 
*PurchaseOrderRequestApi* | [**purchase_order_request_id_id_delete**](docs/PurchaseOrderRequestApi.md#purchase_order_request_id_id_delete) | **DELETE** /purchaseOrderRequest/id/{id} | delete a purchaseOrderRequest
*PurchaseOrderRequestApi* | [**purchase_order_request_id_id_get**](docs/PurchaseOrderRequestApi.md#purchase_order_request_id_id_get) | **GET** /purchaseOrderRequest/id/{id} | query a specific purchaseOrderRequest
*PurchaseOrderRequestApi* | [**purchase_order_request_id_id_put**](docs/PurchaseOrderRequestApi.md#purchase_order_request_id_id_put) | **PUT** /purchaseOrderRequest/id/{id} | update a purchaseOrderRequest
*PurchaseOrderRequestApi* | [**purchase_order_request_post**](docs/PurchaseOrderRequestApi.md#purchase_order_request_post) | **POST** /purchaseOrderRequest | create a purchaseOrderRequest
*PurchaseRequisitionApi* | [**purchase_requisition_count_get**](docs/PurchaseRequisitionApi.md#purchase_requisition_count_get) | **GET** /purchaseRequisition/count | count purchaseRequisition
*PurchaseRequisitionApi* | [**purchase_requisition_delete_all_requisitions_post**](docs/PurchaseRequisitionApi.md#purchase_requisition_delete_all_requisitions_post) | **POST** /purchaseRequisition/deleteAllRequisitions | 
*PurchaseRequisitionApi* | [**purchase_requisition_get**](docs/PurchaseRequisitionApi.md#purchase_requisition_get) | **GET** /purchaseRequisition | query purchaseRequisition
*PurchaseRequisitionApi* | [**purchase_requisition_id_id_get**](docs/PurchaseRequisitionApi.md#purchase_requisition_id_id_get) | **GET** /purchaseRequisition/id/{id} | query a specific purchaseRequisition
*PurchaseRequisitionApi* | [**purchase_requisition_id_id_put**](docs/PurchaseRequisitionApi.md#purchase_requisition_id_id_put) | **PUT** /purchaseRequisition/id/{id} | update a purchaseRequisition
*PurchaseRequisitionApi* | [**purchase_requisition_start_material_planning_run_post**](docs/PurchaseRequisitionApi.md#purchase_requisition_start_material_planning_run_post) | **POST** /purchaseRequisition/startMaterialPlanningRun | 
*QuotationApi* | [**quotation_count_get**](docs/QuotationApi.md#quotation_count_get) | **GET** /quotation/count | count quotation
*QuotationApi* | [**quotation_get**](docs/QuotationApi.md#quotation_get) | **GET** /quotation | query quotation
*QuotationApi* | [**quotation_id_id_accept_post**](docs/QuotationApi.md#quotation_id_id_accept_post) | **POST** /quotation/id/{id}/accept | 
*QuotationApi* | [**quotation_id_id_create_new_version_post**](docs/QuotationApi.md#quotation_id_id_create_new_version_post) | **POST** /quotation/id/{id}/createNewVersion | 
*QuotationApi* | [**quotation_id_id_create_quotation_pdf_post**](docs/QuotationApi.md#quotation_id_id_create_quotation_pdf_post) | **POST** /quotation/id/{id}/createQuotationPdf | 
*QuotationApi* | [**quotation_id_id_delete**](docs/QuotationApi.md#quotation_id_id_delete) | **DELETE** /quotation/id/{id} | delete a quotation
*QuotationApi* | [**quotation_id_id_download_latest_quotation_pdf_get**](docs/QuotationApi.md#quotation_id_id_download_latest_quotation_pdf_get) | **GET** /quotation/id/{id}/downloadLatestQuotationPdf | 
*QuotationApi* | [**quotation_id_id_get**](docs/QuotationApi.md#quotation_id_id_get) | **GET** /quotation/id/{id} | query a specific quotation
*QuotationApi* | [**quotation_id_id_inquire_post**](docs/QuotationApi.md#quotation_id_id_inquire_post) | **POST** /quotation/id/{id}/inquire | 
*QuotationApi* | [**quotation_id_id_put**](docs/QuotationApi.md#quotation_id_id_put) | **PUT** /quotation/id/{id} | update a quotation
*QuotationApi* | [**quotation_post**](docs/QuotationApi.md#quotation_post) | **POST** /quotation | create a quotation
*RecordEmailingRuleApi* | [**record_emailing_rule_count_get**](docs/RecordEmailingRuleApi.md#record_emailing_rule_count_get) | **GET** /recordEmailingRule/count | count recordEmailingRule
*RecordEmailingRuleApi* | [**record_emailing_rule_get**](docs/RecordEmailingRuleApi.md#record_emailing_rule_get) | **GET** /recordEmailingRule | query recordEmailingRule
*RecordEmailingRuleApi* | [**record_emailing_rule_id_id_delete**](docs/RecordEmailingRuleApi.md#record_emailing_rule_id_id_delete) | **DELETE** /recordEmailingRule/id/{id} | delete a recordEmailingRule
*RecordEmailingRuleApi* | [**record_emailing_rule_id_id_get**](docs/RecordEmailingRuleApi.md#record_emailing_rule_id_id_get) | **GET** /recordEmailingRule/id/{id} | query a specific recordEmailingRule
*RecordEmailingRuleApi* | [**record_emailing_rule_id_id_put**](docs/RecordEmailingRuleApi.md#record_emailing_rule_id_id_put) | **PUT** /recordEmailingRule/id/{id} | update a recordEmailingRule
*RecordEmailingRuleApi* | [**record_emailing_rule_post**](docs/RecordEmailingRuleApi.md#record_emailing_rule_post) | **POST** /recordEmailingRule | create a recordEmailingRule
*RemotePrintJobApi* | [**remote_print_job_count_get**](docs/RemotePrintJobApi.md#remote_print_job_count_get) | **GET** /remotePrintJob/count | count remotePrintJob
*RemotePrintJobApi* | [**remote_print_job_create_print_job_with_document_post**](docs/RemotePrintJobApi.md#remote_print_job_create_print_job_with_document_post) | **POST** /remotePrintJob/createPrintJobWithDocument | 
*RemotePrintJobApi* | [**remote_print_job_get**](docs/RemotePrintJobApi.md#remote_print_job_get) | **GET** /remotePrintJob | query remotePrintJob
*RemotePrintJobApi* | [**remote_print_job_id_id_delete**](docs/RemotePrintJobApi.md#remote_print_job_id_id_delete) | **DELETE** /remotePrintJob/id/{id} | delete a remotePrintJob
*RemotePrintJobApi* | [**remote_print_job_id_id_get**](docs/RemotePrintJobApi.md#remote_print_job_id_id_get) | **GET** /remotePrintJob/id/{id} | query a specific remotePrintJob
*RemotePrintJobApi* | [**remote_print_job_id_id_put**](docs/RemotePrintJobApi.md#remote_print_job_id_id_put) | **PUT** /remotePrintJob/id/{id} | update a remotePrintJob
*RemotePrintJobApi* | [**remote_print_job_post**](docs/RemotePrintJobApi.md#remote_print_job_post) | **POST** /remotePrintJob | create a remotePrintJob
*SalesChannelApi* | [**sales_channel_active_sales_channels_get**](docs/SalesChannelApi.md#sales_channel_active_sales_channels_get) | **GET** /salesChannel/activeSalesChannels | 
*SalesInvoiceApi* | [**sales_invoice_count_get**](docs/SalesInvoiceApi.md#sales_invoice_count_get) | **GET** /salesInvoice/count | count salesInvoice
*SalesInvoiceApi* | [**sales_invoice_get**](docs/SalesInvoiceApi.md#sales_invoice_get) | **GET** /salesInvoice | query salesInvoice
*SalesInvoiceApi* | [**sales_invoice_id_id_add_sales_orders_post**](docs/SalesInvoiceApi.md#sales_invoice_id_id_add_sales_orders_post) | **POST** /salesInvoice/id/{id}/addSalesOrders | 
*SalesInvoiceApi* | [**sales_invoice_id_id_create_credit_note_post**](docs/SalesInvoiceApi.md#sales_invoice_id_id_create_credit_note_post) | **POST** /salesInvoice/id/{id}/createCreditNote | 
*SalesInvoiceApi* | [**sales_invoice_id_id_delete**](docs/SalesInvoiceApi.md#sales_invoice_id_id_delete) | **DELETE** /salesInvoice/id/{id} | delete a salesInvoice
*SalesInvoiceApi* | [**sales_invoice_id_id_download_latest_sales_invoice_pdf_get**](docs/SalesInvoiceApi.md#sales_invoice_id_id_download_latest_sales_invoice_pdf_get) | **GET** /salesInvoice/id/{id}/downloadLatestSalesInvoicePdf | 
*SalesInvoiceApi* | [**sales_invoice_id_id_get**](docs/SalesInvoiceApi.md#sales_invoice_id_id_get) | **GET** /salesInvoice/id/{id} | query a specific salesInvoice
*SalesInvoiceApi* | [**sales_invoice_id_id_put**](docs/SalesInvoiceApi.md#sales_invoice_id_id_put) | **PUT** /salesInvoice/id/{id} | update a salesInvoice
*SalesInvoiceApi* | [**sales_invoice_post**](docs/SalesInvoiceApi.md#sales_invoice_post) | **POST** /salesInvoice | create a salesInvoice
*SalesOpenItemApi* | [**sales_open_item_count_get**](docs/SalesOpenItemApi.md#sales_open_item_count_get) | **GET** /salesOpenItem/count | count salesOpenItem
*SalesOpenItemApi* | [**sales_open_item_get**](docs/SalesOpenItemApi.md#sales_open_item_get) | **GET** /salesOpenItem | query salesOpenItem
*SalesOpenItemApi* | [**sales_open_item_id_id_create_payment_application_post**](docs/SalesOpenItemApi.md#sales_open_item_id_id_create_payment_application_post) | **POST** /salesOpenItem/id/{id}/createPaymentApplication | 
*SalesOpenItemApi* | [**sales_open_item_id_id_get**](docs/SalesOpenItemApi.md#sales_open_item_id_id_get) | **GET** /salesOpenItem/id/{id} | query a specific salesOpenItem
*SalesOrderApi* | [**sales_order_count_get**](docs/SalesOrderApi.md#sales_order_count_get) | **GET** /salesOrder/count | count salesOrder
*SalesOrderApi* | [**sales_order_default_values_for_create_get**](docs/SalesOrderApi.md#sales_order_default_values_for_create_get) | **GET** /salesOrder/defaultValuesForCreate | 
*SalesOrderApi* | [**sales_order_get**](docs/SalesOrderApi.md#sales_order_get) | **GET** /salesOrder | query salesOrder
*SalesOrderApi* | [**sales_order_id_id_cancel_or_manually_close_post**](docs/SalesOrderApi.md#sales_order_id_id_cancel_or_manually_close_post) | **POST** /salesOrder/id/{id}/cancelOrManuallyClose | 
*SalesOrderApi* | [**sales_order_id_id_create_advance_payment_request_post**](docs/SalesOrderApi.md#sales_order_id_id_create_advance_payment_request_post) | **POST** /salesOrder/id/{id}/createAdvancePaymentRequest | 
*SalesOrderApi* | [**sales_order_id_id_create_customer_return_post**](docs/SalesOrderApi.md#sales_order_id_id_create_customer_return_post) | **POST** /salesOrder/id/{id}/createCustomerReturn | 
*SalesOrderApi* | [**sales_order_id_id_create_dropshipping_post**](docs/SalesOrderApi.md#sales_order_id_id_create_dropshipping_post) | **POST** /salesOrder/id/{id}/createDropshipping | 
*SalesOrderApi* | [**sales_order_id_id_create_part_payment_invoice_post**](docs/SalesOrderApi.md#sales_order_id_id_create_part_payment_invoice_post) | **POST** /salesOrder/id/{id}/createPartPaymentInvoice | 
*SalesOrderApi* | [**sales_order_id_id_create_prepayment_final_invoice_post**](docs/SalesOrderApi.md#sales_order_id_id_create_prepayment_final_invoice_post) | **POST** /salesOrder/id/{id}/createPrepaymentFinalInvoice | 
*SalesOrderApi* | [**sales_order_id_id_create_purchase_order_post**](docs/SalesOrderApi.md#sales_order_id_id_create_purchase_order_post) | **POST** /salesOrder/id/{id}/createPurchaseOrder | 
*SalesOrderApi* | [**sales_order_id_id_create_return_labels_post**](docs/SalesOrderApi.md#sales_order_id_id_create_return_labels_post) | **POST** /salesOrder/id/{id}/createReturnLabels | 
*SalesOrderApi* | [**sales_order_id_id_create_sales_invoice_post**](docs/SalesOrderApi.md#sales_order_id_id_create_sales_invoice_post) | **POST** /salesOrder/id/{id}/createSalesInvoice | 
*SalesOrderApi* | [**sales_order_id_id_create_shipment_post**](docs/SalesOrderApi.md#sales_order_id_id_create_shipment_post) | **POST** /salesOrder/id/{id}/createShipment | 
*SalesOrderApi* | [**sales_order_id_id_create_shipping_labels_post**](docs/SalesOrderApi.md#sales_order_id_id_create_shipping_labels_post) | **POST** /salesOrder/id/{id}/createShippingLabels | 
*SalesOrderApi* | [**sales_order_id_id_delete**](docs/SalesOrderApi.md#sales_order_id_id_delete) | **DELETE** /salesOrder/id/{id} | delete a salesOrder
*SalesOrderApi* | [**sales_order_id_id_download_latest_order_confirmation_pdf_get**](docs/SalesOrderApi.md#sales_order_id_id_download_latest_order_confirmation_pdf_get) | **GET** /salesOrder/id/{id}/downloadLatestOrderConfirmationPdf | 
*SalesOrderApi* | [**sales_order_id_id_get**](docs/SalesOrderApi.md#sales_order_id_id_get) | **GET** /salesOrder/id/{id} | query a specific salesOrder
*SalesOrderApi* | [**sales_order_id_id_manually_close_post**](docs/SalesOrderApi.md#sales_order_id_id_manually_close_post) | **POST** /salesOrder/id/{id}/manuallyClose | 
*SalesOrderApi* | [**sales_order_id_id_put**](docs/SalesOrderApi.md#sales_order_id_id_put) | **PUT** /salesOrder/id/{id} | update a salesOrder
*SalesOrderApi* | [**sales_order_id_id_ship_order_for_external_fulfillment_post**](docs/SalesOrderApi.md#sales_order_id_id_ship_order_for_external_fulfillment_post) | **POST** /salesOrder/id/{id}/shipOrderForExternalFulfillment | 
*SalesOrderApi* | [**sales_order_id_id_toggle_project_team_post**](docs/SalesOrderApi.md#sales_order_id_id_toggle_project_team_post) | **POST** /salesOrder/id/{id}/toggleProjectTeam | 
*SalesOrderApi* | [**sales_order_id_id_toggle_services_finished_post**](docs/SalesOrderApi.md#sales_order_id_id_toggle_services_finished_post) | **POST** /salesOrder/id/{id}/toggleServicesFinished | 
*SalesOrderApi* | [**sales_order_post**](docs/SalesOrderApi.md#sales_order_post) | **POST** /salesOrder | create a salesOrder
*SalesStageApi* | [**sales_stage_count_get**](docs/SalesStageApi.md#sales_stage_count_get) | **GET** /salesStage/count | count salesStage
*SalesStageApi* | [**sales_stage_get**](docs/SalesStageApi.md#sales_stage_get) | **GET** /salesStage | query salesStage
*SalesStageApi* | [**sales_stage_id_id_delete**](docs/SalesStageApi.md#sales_stage_id_id_delete) | **DELETE** /salesStage/id/{id} | delete a salesStage
*SalesStageApi* | [**sales_stage_id_id_get**](docs/SalesStageApi.md#sales_stage_id_id_get) | **GET** /salesStage/id/{id} | query a specific salesStage
*SalesStageApi* | [**sales_stage_id_id_put**](docs/SalesStageApi.md#sales_stage_id_id_put) | **PUT** /salesStage/id/{id} | update a salesStage
*SalesStageApi* | [**sales_stage_post**](docs/SalesStageApi.md#sales_stage_post) | **POST** /salesStage | create a salesStage
*SectorApi* | [**sector_count_get**](docs/SectorApi.md#sector_count_get) | **GET** /sector/count | count sector
*SectorApi* | [**sector_get**](docs/SectorApi.md#sector_get) | **GET** /sector | query sector
*SectorApi* | [**sector_id_id_delete**](docs/SectorApi.md#sector_id_id_delete) | **DELETE** /sector/id/{id} | delete a sector
*SectorApi* | [**sector_id_id_get**](docs/SectorApi.md#sector_id_id_get) | **GET** /sector/id/{id} | query a specific sector
*SectorApi* | [**sector_id_id_put**](docs/SectorApi.md#sector_id_id_put) | **PUT** /sector/id/{id} | update a sector
*SectorApi* | [**sector_post**](docs/SectorApi.md#sector_post) | **POST** /sector | create a sector
*SepaDirectDebitMandateApi* | [**sepa_direct_debit_mandate_count_get**](docs/SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_count_get) | **GET** /sepaDirectDebitMandate/count | count sepaDirectDebitMandate
*SepaDirectDebitMandateApi* | [**sepa_direct_debit_mandate_get**](docs/SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_get) | **GET** /sepaDirectDebitMandate | query sepaDirectDebitMandate
*SepaDirectDebitMandateApi* | [**sepa_direct_debit_mandate_id_id_delete**](docs/SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_id_id_delete) | **DELETE** /sepaDirectDebitMandate/id/{id} | delete a sepaDirectDebitMandate
*SepaDirectDebitMandateApi* | [**sepa_direct_debit_mandate_id_id_get**](docs/SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_id_id_get) | **GET** /sepaDirectDebitMandate/id/{id} | query a specific sepaDirectDebitMandate
*SepaDirectDebitMandateApi* | [**sepa_direct_debit_mandate_id_id_put**](docs/SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_id_id_put) | **PUT** /sepaDirectDebitMandate/id/{id} | update a sepaDirectDebitMandate
*SepaDirectDebitMandateApi* | [**sepa_direct_debit_mandate_post**](docs/SepaDirectDebitMandateApi.md#sepa_direct_debit_mandate_post) | **POST** /sepaDirectDebitMandate | create a sepaDirectDebitMandate
*SerialNumberApi* | [**serial_number_count_get**](docs/SerialNumberApi.md#serial_number_count_get) | **GET** /serialNumber/count | count serialNumber
*SerialNumberApi* | [**serial_number_get**](docs/SerialNumberApi.md#serial_number_get) | **GET** /serialNumber | query serialNumber
*SerialNumberApi* | [**serial_number_id_id_get**](docs/SerialNumberApi.md#serial_number_id_id_get) | **GET** /serialNumber/id/{id} | query a specific serialNumber
*SerialNumberApi* | [**serial_number_id_id_put**](docs/SerialNumberApi.md#serial_number_id_id_put) | **PUT** /serialNumber/id/{id} | update a serialNumber
*ShelfApi* | [**shelf_count_get**](docs/ShelfApi.md#shelf_count_get) | **GET** /shelf/count | count shelf
*ShelfApi* | [**shelf_get**](docs/ShelfApi.md#shelf_get) | **GET** /shelf | query shelf
*ShelfApi* | [**shelf_id_id_activate_post**](docs/ShelfApi.md#shelf_id_id_activate_post) | **POST** /shelf/id/{id}/activate | 
*ShelfApi* | [**shelf_id_id_deactivate_post**](docs/ShelfApi.md#shelf_id_id_deactivate_post) | **POST** /shelf/id/{id}/deactivate | 
*ShelfApi* | [**shelf_id_id_delete**](docs/ShelfApi.md#shelf_id_id_delete) | **DELETE** /shelf/id/{id} | delete a shelf
*ShelfApi* | [**shelf_id_id_get**](docs/ShelfApi.md#shelf_id_id_get) | **GET** /shelf/id/{id} | query a specific shelf
*ShelfApi* | [**shelf_id_id_put**](docs/ShelfApi.md#shelf_id_id_put) | **PUT** /shelf/id/{id} | update a shelf
*ShelfApi* | [**shelf_post**](docs/ShelfApi.md#shelf_post) | **POST** /shelf | create a shelf
*ShipmentApi* | [**shipment_count_get**](docs/ShipmentApi.md#shipment_count_get) | **GET** /shipment/count | count shipment
*ShipmentApi* | [**shipment_get**](docs/ShipmentApi.md#shipment_get) | **GET** /shipment | query shipment
*ShipmentApi* | [**shipment_id_id_create_picking_list_post**](docs/ShipmentApi.md#shipment_id_id_create_picking_list_post) | **POST** /shipment/id/{id}/createPickingList | 
*ShipmentApi* | [**shipment_id_id_create_return_labels_post**](docs/ShipmentApi.md#shipment_id_id_create_return_labels_post) | **POST** /shipment/id/{id}/createReturnLabels | 
*ShipmentApi* | [**shipment_id_id_create_sales_invoice_post**](docs/ShipmentApi.md#shipment_id_id_create_sales_invoice_post) | **POST** /shipment/id/{id}/createSalesInvoice | 
*ShipmentApi* | [**shipment_id_id_create_shipping_label_pdf_post**](docs/ShipmentApi.md#shipment_id_id_create_shipping_label_pdf_post) | **POST** /shipment/id/{id}/createShippingLabelPdf | 
*ShipmentApi* | [**shipment_id_id_create_shipping_labels_post**](docs/ShipmentApi.md#shipment_id_id_create_shipping_labels_post) | **POST** /shipment/id/{id}/createShippingLabels | 
*ShipmentApi* | [**shipment_id_id_delete**](docs/ShipmentApi.md#shipment_id_id_delete) | **DELETE** /shipment/id/{id} | delete a shipment
*ShipmentApi* | [**shipment_id_id_download_latest_delivery_note_pdf_get**](docs/ShipmentApi.md#shipment_id_id_download_latest_delivery_note_pdf_get) | **GET** /shipment/id/{id}/downloadLatestDeliveryNotePdf | 
*ShipmentApi* | [**shipment_id_id_download_latest_picking_list_pdf_get**](docs/ShipmentApi.md#shipment_id_id_download_latest_picking_list_pdf_get) | **GET** /shipment/id/{id}/downloadLatestPickingListPdf | 
*ShipmentApi* | [**shipment_id_id_download_latest_shipping_label_pdf_get**](docs/ShipmentApi.md#shipment_id_id_download_latest_shipping_label_pdf_get) | **GET** /shipment/id/{id}/downloadLatestShippingLabelPdf | 
*ShipmentApi* | [**shipment_id_id_get**](docs/ShipmentApi.md#shipment_id_id_get) | **GET** /shipment/id/{id} | query a specific shipment
*ShipmentApi* | [**shipment_id_id_put**](docs/ShipmentApi.md#shipment_id_id_put) | **PUT** /shipment/id/{id} | update a shipment
*ShipmentApi* | [**shipment_post**](docs/ShipmentApi.md#shipment_post) | **POST** /shipment | create a shipment
*ShipmentMethodApi* | [**shipment_method_count_get**](docs/ShipmentMethodApi.md#shipment_method_count_get) | **GET** /shipmentMethod/count | count shipmentMethod
*ShipmentMethodApi* | [**shipment_method_get**](docs/ShipmentMethodApi.md#shipment_method_get) | **GET** /shipmentMethod | query shipmentMethod
*ShipmentMethodApi* | [**shipment_method_id_id_delete**](docs/ShipmentMethodApi.md#shipment_method_id_id_delete) | **DELETE** /shipmentMethod/id/{id} | delete a shipmentMethod
*ShipmentMethodApi* | [**shipment_method_id_id_get**](docs/ShipmentMethodApi.md#shipment_method_id_id_get) | **GET** /shipmentMethod/id/{id} | query a specific shipmentMethod
*ShipmentMethodApi* | [**shipment_method_id_id_put**](docs/ShipmentMethodApi.md#shipment_method_id_id_put) | **PUT** /shipmentMethod/id/{id} | update a shipmentMethod
*ShipmentMethodApi* | [**shipment_method_post**](docs/ShipmentMethodApi.md#shipment_method_post) | **POST** /shipmentMethod | create a shipmentMethod
*ShipmentReturnAssessmentApi* | [**shipment_return_assessment_count_get**](docs/ShipmentReturnAssessmentApi.md#shipment_return_assessment_count_get) | **GET** /shipmentReturnAssessment/count | count shipmentReturnAssessment
*ShipmentReturnAssessmentApi* | [**shipment_return_assessment_get**](docs/ShipmentReturnAssessmentApi.md#shipment_return_assessment_get) | **GET** /shipmentReturnAssessment | query shipmentReturnAssessment
*ShipmentReturnAssessmentApi* | [**shipment_return_assessment_id_id_delete**](docs/ShipmentReturnAssessmentApi.md#shipment_return_assessment_id_id_delete) | **DELETE** /shipmentReturnAssessment/id/{id} | delete a shipmentReturnAssessment
*ShipmentReturnAssessmentApi* | [**shipment_return_assessment_id_id_get**](docs/ShipmentReturnAssessmentApi.md#shipment_return_assessment_id_id_get) | **GET** /shipmentReturnAssessment/id/{id} | query a specific shipmentReturnAssessment
*ShipmentReturnAssessmentApi* | [**shipment_return_assessment_id_id_put**](docs/ShipmentReturnAssessmentApi.md#shipment_return_assessment_id_id_put) | **PUT** /shipmentReturnAssessment/id/{id} | update a shipmentReturnAssessment
*ShipmentReturnAssessmentApi* | [**shipment_return_assessment_post**](docs/ShipmentReturnAssessmentApi.md#shipment_return_assessment_post) | **POST** /shipmentReturnAssessment | create a shipmentReturnAssessment
*ShipmentReturnErrorApi* | [**shipment_return_error_count_get**](docs/ShipmentReturnErrorApi.md#shipment_return_error_count_get) | **GET** /shipmentReturnError/count | count shipmentReturnError
*ShipmentReturnErrorApi* | [**shipment_return_error_get**](docs/ShipmentReturnErrorApi.md#shipment_return_error_get) | **GET** /shipmentReturnError | query shipmentReturnError
*ShipmentReturnErrorApi* | [**shipment_return_error_id_id_delete**](docs/ShipmentReturnErrorApi.md#shipment_return_error_id_id_delete) | **DELETE** /shipmentReturnError/id/{id} | delete a shipmentReturnError
*ShipmentReturnErrorApi* | [**shipment_return_error_id_id_get**](docs/ShipmentReturnErrorApi.md#shipment_return_error_id_id_get) | **GET** /shipmentReturnError/id/{id} | query a specific shipmentReturnError
*ShipmentReturnErrorApi* | [**shipment_return_error_id_id_put**](docs/ShipmentReturnErrorApi.md#shipment_return_error_id_id_put) | **PUT** /shipmentReturnError/id/{id} | update a shipmentReturnError
*ShipmentReturnErrorApi* | [**shipment_return_error_post**](docs/ShipmentReturnErrorApi.md#shipment_return_error_post) | **POST** /shipmentReturnError | create a shipmentReturnError
*ShipmentReturnReasonApi* | [**shipment_return_reason_count_get**](docs/ShipmentReturnReasonApi.md#shipment_return_reason_count_get) | **GET** /shipmentReturnReason/count | count shipmentReturnReason
*ShipmentReturnReasonApi* | [**shipment_return_reason_get**](docs/ShipmentReturnReasonApi.md#shipment_return_reason_get) | **GET** /shipmentReturnReason | query shipmentReturnReason
*ShipmentReturnReasonApi* | [**shipment_return_reason_id_id_delete**](docs/ShipmentReturnReasonApi.md#shipment_return_reason_id_id_delete) | **DELETE** /shipmentReturnReason/id/{id} | delete a shipmentReturnReason
*ShipmentReturnReasonApi* | [**shipment_return_reason_id_id_get**](docs/ShipmentReturnReasonApi.md#shipment_return_reason_id_id_get) | **GET** /shipmentReturnReason/id/{id} | query a specific shipmentReturnReason
*ShipmentReturnReasonApi* | [**shipment_return_reason_id_id_put**](docs/ShipmentReturnReasonApi.md#shipment_return_reason_id_id_put) | **PUT** /shipmentReturnReason/id/{id} | update a shipmentReturnReason
*ShipmentReturnReasonApi* | [**shipment_return_reason_post**](docs/ShipmentReturnReasonApi.md#shipment_return_reason_post) | **POST** /shipmentReturnReason | create a shipmentReturnReason
*ShipmentReturnRectificationApi* | [**shipment_return_rectification_count_get**](docs/ShipmentReturnRectificationApi.md#shipment_return_rectification_count_get) | **GET** /shipmentReturnRectification/count | count shipmentReturnRectification
*ShipmentReturnRectificationApi* | [**shipment_return_rectification_get**](docs/ShipmentReturnRectificationApi.md#shipment_return_rectification_get) | **GET** /shipmentReturnRectification | query shipmentReturnRectification
*ShipmentReturnRectificationApi* | [**shipment_return_rectification_id_id_delete**](docs/ShipmentReturnRectificationApi.md#shipment_return_rectification_id_id_delete) | **DELETE** /shipmentReturnRectification/id/{id} | delete a shipmentReturnRectification
*ShipmentReturnRectificationApi* | [**shipment_return_rectification_id_id_get**](docs/ShipmentReturnRectificationApi.md#shipment_return_rectification_id_id_get) | **GET** /shipmentReturnRectification/id/{id} | query a specific shipmentReturnRectification
*ShipmentReturnRectificationApi* | [**shipment_return_rectification_id_id_put**](docs/ShipmentReturnRectificationApi.md#shipment_return_rectification_id_id_put) | **PUT** /shipmentReturnRectification/id/{id} | update a shipmentReturnRectification
*ShipmentReturnRectificationApi* | [**shipment_return_rectification_post**](docs/ShipmentReturnRectificationApi.md#shipment_return_rectification_post) | **POST** /shipmentReturnRectification | create a shipmentReturnRectification
*ShippingCarrierApi* | [**shipping_carrier_count_get**](docs/ShippingCarrierApi.md#shipping_carrier_count_get) | **GET** /shippingCarrier/count | count shippingCarrier
*ShippingCarrierApi* | [**shipping_carrier_get**](docs/ShippingCarrierApi.md#shipping_carrier_get) | **GET** /shippingCarrier | query shippingCarrier
*ShippingCarrierApi* | [**shipping_carrier_id_id_delete**](docs/ShippingCarrierApi.md#shipping_carrier_id_id_delete) | **DELETE** /shippingCarrier/id/{id} | delete a shippingCarrier
*ShippingCarrierApi* | [**shipping_carrier_id_id_get**](docs/ShippingCarrierApi.md#shipping_carrier_id_id_get) | **GET** /shippingCarrier/id/{id} | query a specific shippingCarrier
*ShippingCarrierApi* | [**shipping_carrier_id_id_put**](docs/ShippingCarrierApi.md#shipping_carrier_id_id_put) | **PUT** /shippingCarrier/id/{id} | update a shippingCarrier
*ShippingCarrierApi* | [**shipping_carrier_post**](docs/ShippingCarrierApi.md#shipping_carrier_post) | **POST** /shippingCarrier | create a shippingCarrier
*StorageLocationApi* | [**storage_location_count_get**](docs/StorageLocationApi.md#storage_location_count_get) | **GET** /storageLocation/count | count storageLocation
*StorageLocationApi* | [**storage_location_get**](docs/StorageLocationApi.md#storage_location_get) | **GET** /storageLocation | query storageLocation
*StorageLocationApi* | [**storage_location_id_id_activate_post**](docs/StorageLocationApi.md#storage_location_id_id_activate_post) | **POST** /storageLocation/id/{id}/activate | 
*StorageLocationApi* | [**storage_location_id_id_deactivate_post**](docs/StorageLocationApi.md#storage_location_id_id_deactivate_post) | **POST** /storageLocation/id/{id}/deactivate | 
*StorageLocationApi* | [**storage_location_id_id_delete**](docs/StorageLocationApi.md#storage_location_id_id_delete) | **DELETE** /storageLocation/id/{id} | delete a storageLocation
*StorageLocationApi* | [**storage_location_id_id_get**](docs/StorageLocationApi.md#storage_location_id_id_get) | **GET** /storageLocation/id/{id} | query a specific storageLocation
*StorageLocationApi* | [**storage_location_id_id_put**](docs/StorageLocationApi.md#storage_location_id_id_put) | **PUT** /storageLocation/id/{id} | update a storageLocation
*StorageLocationApi* | [**storage_location_post**](docs/StorageLocationApi.md#storage_location_post) | **POST** /storageLocation | create a storageLocation
*StoragePlaceApi* | [**storage_place_count_get**](docs/StoragePlaceApi.md#storage_place_count_get) | **GET** /storagePlace/count | count storagePlace
*StoragePlaceApi* | [**storage_place_get**](docs/StoragePlaceApi.md#storage_place_get) | **GET** /storagePlace | query storagePlace
*StoragePlaceApi* | [**storage_place_id_id_get**](docs/StoragePlaceApi.md#storage_place_id_id_get) | **GET** /storagePlace/id/{id} | query a specific storagePlace
*StoragePlaceBlockingReasonApi* | [**storage_place_blocking_reason_count_get**](docs/StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_count_get) | **GET** /storagePlaceBlockingReason/count | count storagePlaceBlockingReason
*StoragePlaceBlockingReasonApi* | [**storage_place_blocking_reason_get**](docs/StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_get) | **GET** /storagePlaceBlockingReason | query storagePlaceBlockingReason
*StoragePlaceBlockingReasonApi* | [**storage_place_blocking_reason_id_id_delete**](docs/StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_id_id_delete) | **DELETE** /storagePlaceBlockingReason/id/{id} | delete a storagePlaceBlockingReason
*StoragePlaceBlockingReasonApi* | [**storage_place_blocking_reason_id_id_get**](docs/StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_id_id_get) | **GET** /storagePlaceBlockingReason/id/{id} | query a specific storagePlaceBlockingReason
*StoragePlaceBlockingReasonApi* | [**storage_place_blocking_reason_id_id_put**](docs/StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_id_id_put) | **PUT** /storagePlaceBlockingReason/id/{id} | update a storagePlaceBlockingReason
*StoragePlaceBlockingReasonApi* | [**storage_place_blocking_reason_post**](docs/StoragePlaceBlockingReasonApi.md#storage_place_blocking_reason_post) | **POST** /storagePlaceBlockingReason | create a storagePlaceBlockingReason
*StoragePlaceSizeApi* | [**storage_place_size_count_get**](docs/StoragePlaceSizeApi.md#storage_place_size_count_get) | **GET** /storagePlaceSize/count | count storagePlaceSize
*StoragePlaceSizeApi* | [**storage_place_size_get**](docs/StoragePlaceSizeApi.md#storage_place_size_get) | **GET** /storagePlaceSize | query storagePlaceSize
*StoragePlaceSizeApi* | [**storage_place_size_id_id_delete**](docs/StoragePlaceSizeApi.md#storage_place_size_id_id_delete) | **DELETE** /storagePlaceSize/id/{id} | delete a storagePlaceSize
*StoragePlaceSizeApi* | [**storage_place_size_id_id_get**](docs/StoragePlaceSizeApi.md#storage_place_size_id_id_get) | **GET** /storagePlaceSize/id/{id} | query a specific storagePlaceSize
*StoragePlaceSizeApi* | [**storage_place_size_id_id_put**](docs/StoragePlaceSizeApi.md#storage_place_size_id_id_put) | **PUT** /storagePlaceSize/id/{id} | update a storagePlaceSize
*StoragePlaceSizeApi* | [**storage_place_size_post**](docs/StoragePlaceSizeApi.md#storage_place_size_post) | **POST** /storagePlaceSize | create a storagePlaceSize
*SupplierApi* | [**supplier_count_get**](docs/SupplierApi.md#supplier_count_get) | **GET** /supplier/count | count supplier
*SupplierApi* | [**supplier_get**](docs/SupplierApi.md#supplier_get) | **GET** /supplier | query supplier
*SupplierApi* | [**supplier_id_id_delete**](docs/SupplierApi.md#supplier_id_id_delete) | **DELETE** /supplier/id/{id} | delete a supplier
*SupplierApi* | [**supplier_id_id_download_image_get**](docs/SupplierApi.md#supplier_id_id_download_image_get) | **GET** /supplier/id/{id}/downloadImage | 
*SupplierApi* | [**supplier_id_id_get**](docs/SupplierApi.md#supplier_id_id_get) | **GET** /supplier/id/{id} | query a specific supplier
*SupplierApi* | [**supplier_id_id_put**](docs/SupplierApi.md#supplier_id_id_put) | **PUT** /supplier/id/{id} | update a supplier
*SupplierApi* | [**supplier_id_id_upload_image_post**](docs/SupplierApi.md#supplier_id_id_upload_image_post) | **POST** /supplier/id/{id}/uploadImage | 
*SupplierApi* | [**supplier_post**](docs/SupplierApi.md#supplier_post) | **POST** /supplier | create a supplier
*SystemApi* | [**system_create_demo_test_system_post**](docs/SystemApi.md#system_create_demo_test_system_post) | **POST** /system/createDemoTestSystem | 
*SystemApi* | [**system_demo_test_system_info_get**](docs/SystemApi.md#system_demo_test_system_info_get) | **GET** /system/demoTestSystemInfo | 
*SystemApi* | [**system_licenses_get**](docs/SystemApi.md#system_licenses_get) | **GET** /system/licenses | 
*TagApi* | [**tag_count_get**](docs/TagApi.md#tag_count_get) | **GET** /tag/count | count tag
*TagApi* | [**tag_get**](docs/TagApi.md#tag_get) | **GET** /tag | query tag
*TagApi* | [**tag_id_id_delete**](docs/TagApi.md#tag_id_id_delete) | **DELETE** /tag/id/{id} | delete a tag
*TagApi* | [**tag_id_id_get**](docs/TagApi.md#tag_id_id_get) | **GET** /tag/id/{id} | query a specific tag
*TagApi* | [**tag_id_id_put**](docs/TagApi.md#tag_id_id_put) | **PUT** /tag/id/{id} | update a tag
*TagApi* | [**tag_post**](docs/TagApi.md#tag_post) | **POST** /tag | create a tag
*TaxApi* | [**tax_configure_purchase_taxes_post**](docs/TaxApi.md#tax_configure_purchase_taxes_post) | **POST** /tax/configurePurchaseTaxes | 
*TaxApi* | [**tax_configure_sales_taxes_post**](docs/TaxApi.md#tax_configure_sales_taxes_post) | **POST** /tax/configureSalesTaxes | 
*TaxApi* | [**tax_count_get**](docs/TaxApi.md#tax_count_get) | **GET** /tax/count | count tax
*TaxApi* | [**tax_find_purchase_tax_get**](docs/TaxApi.md#tax_find_purchase_tax_get) | **GET** /tax/findPurchaseTax | 
*TaxApi* | [**tax_find_sales_tax_get**](docs/TaxApi.md#tax_find_sales_tax_get) | **GET** /tax/findSalesTax | 
*TaxApi* | [**tax_get**](docs/TaxApi.md#tax_get) | **GET** /tax | query tax
*TaxApi* | [**tax_id_id_delete**](docs/TaxApi.md#tax_id_id_delete) | **DELETE** /tax/id/{id} | delete a tax
*TaxApi* | [**tax_id_id_get**](docs/TaxApi.md#tax_id_id_get) | **GET** /tax/id/{id} | query a specific tax
*TaxApi* | [**tax_id_id_put**](docs/TaxApi.md#tax_id_id_put) | **PUT** /tax/id/{id} | update a tax
*TaxApi* | [**tax_post**](docs/TaxApi.md#tax_post) | **POST** /tax | create a tax
*TaxApi* | [**tax_reset_system_taxes_post**](docs/TaxApi.md#tax_reset_system_taxes_post) | **POST** /tax/resetSystemTaxes | 
*TaxDeterminationRuleApi* | [**tax_determination_rule_count_get**](docs/TaxDeterminationRuleApi.md#tax_determination_rule_count_get) | **GET** /taxDeterminationRule/count | count taxDeterminationRule
*TaxDeterminationRuleApi* | [**tax_determination_rule_get**](docs/TaxDeterminationRuleApi.md#tax_determination_rule_get) | **GET** /taxDeterminationRule | query taxDeterminationRule
*TaxDeterminationRuleApi* | [**tax_determination_rule_id_id_delete**](docs/TaxDeterminationRuleApi.md#tax_determination_rule_id_id_delete) | **DELETE** /taxDeterminationRule/id/{id} | delete a taxDeterminationRule
*TaxDeterminationRuleApi* | [**tax_determination_rule_id_id_get**](docs/TaxDeterminationRuleApi.md#tax_determination_rule_id_id_get) | **GET** /taxDeterminationRule/id/{id} | query a specific taxDeterminationRule
*TaxDeterminationRuleApi* | [**tax_determination_rule_id_id_put**](docs/TaxDeterminationRuleApi.md#tax_determination_rule_id_id_put) | **PUT** /taxDeterminationRule/id/{id} | update a taxDeterminationRule
*TaxDeterminationRuleApi* | [**tax_determination_rule_post**](docs/TaxDeterminationRuleApi.md#tax_determination_rule_post) | **POST** /taxDeterminationRule | create a taxDeterminationRule
*TermOfPaymentApi* | [**term_of_payment_count_get**](docs/TermOfPaymentApi.md#term_of_payment_count_get) | **GET** /termOfPayment/count | count termOfPayment
*TermOfPaymentApi* | [**term_of_payment_get**](docs/TermOfPaymentApi.md#term_of_payment_get) | **GET** /termOfPayment | query termOfPayment
*TermOfPaymentApi* | [**term_of_payment_id_id_delete**](docs/TermOfPaymentApi.md#term_of_payment_id_id_delete) | **DELETE** /termOfPayment/id/{id} | delete a termOfPayment
*TermOfPaymentApi* | [**term_of_payment_id_id_get**](docs/TermOfPaymentApi.md#term_of_payment_id_id_get) | **GET** /termOfPayment/id/{id} | query a specific termOfPayment
*TermOfPaymentApi* | [**term_of_payment_id_id_put**](docs/TermOfPaymentApi.md#term_of_payment_id_id_put) | **PUT** /termOfPayment/id/{id} | update a termOfPayment
*TermOfPaymentApi* | [**term_of_payment_post**](docs/TermOfPaymentApi.md#term_of_payment_post) | **POST** /termOfPayment | create a termOfPayment
*TicketApi* | [**ticket_count_get**](docs/TicketApi.md#ticket_count_get) | **GET** /ticket/count | count ticket
*TicketApi* | [**ticket_get**](docs/TicketApi.md#ticket_get) | **GET** /ticket | query ticket
*TicketApi* | [**ticket_id_id_create_public_page_post**](docs/TicketApi.md#ticket_id_id_create_public_page_post) | **POST** /ticket/id/{id}/createPublicPage | 
*TicketApi* | [**ticket_id_id_delete**](docs/TicketApi.md#ticket_id_id_delete) | **DELETE** /ticket/id/{id} | delete a ticket
*TicketApi* | [**ticket_id_id_disable_public_page_post**](docs/TicketApi.md#ticket_id_id_disable_public_page_post) | **POST** /ticket/id/{id}/disablePublicPage | 
*TicketApi* | [**ticket_id_id_get**](docs/TicketApi.md#ticket_id_id_get) | **GET** /ticket/id/{id} | query a specific ticket
*TicketApi* | [**ticket_id_id_link_sales_order_post**](docs/TicketApi.md#ticket_id_id_link_sales_order_post) | **POST** /ticket/id/{id}/linkSalesOrder | 
*TicketApi* | [**ticket_id_id_put**](docs/TicketApi.md#ticket_id_id_put) | **PUT** /ticket/id/{id} | update a ticket
*TicketApi* | [**ticket_id_id_unlink_sales_order_post**](docs/TicketApi.md#ticket_id_id_unlink_sales_order_post) | **POST** /ticket/id/{id}/unlinkSalesOrder | 
*TicketApi* | [**ticket_post**](docs/TicketApi.md#ticket_post) | **POST** /ticket | create a ticket
*TicketAssignmentRuleApi* | [**ticket_assignment_rule_count_get**](docs/TicketAssignmentRuleApi.md#ticket_assignment_rule_count_get) | **GET** /ticketAssignmentRule/count | count ticketAssignmentRule
*TicketAssignmentRuleApi* | [**ticket_assignment_rule_get**](docs/TicketAssignmentRuleApi.md#ticket_assignment_rule_get) | **GET** /ticketAssignmentRule | query ticketAssignmentRule
*TicketAssignmentRuleApi* | [**ticket_assignment_rule_id_id_delete**](docs/TicketAssignmentRuleApi.md#ticket_assignment_rule_id_id_delete) | **DELETE** /ticketAssignmentRule/id/{id} | delete a ticketAssignmentRule
*TicketAssignmentRuleApi* | [**ticket_assignment_rule_id_id_get**](docs/TicketAssignmentRuleApi.md#ticket_assignment_rule_id_id_get) | **GET** /ticketAssignmentRule/id/{id} | query a specific ticketAssignmentRule
*TicketAssignmentRuleApi* | [**ticket_assignment_rule_id_id_put**](docs/TicketAssignmentRuleApi.md#ticket_assignment_rule_id_id_put) | **PUT** /ticketAssignmentRule/id/{id} | update a ticketAssignmentRule
*TicketAssignmentRuleApi* | [**ticket_assignment_rule_post**](docs/TicketAssignmentRuleApi.md#ticket_assignment_rule_post) | **POST** /ticketAssignmentRule | create a ticketAssignmentRule
*TicketCategoryApi* | [**ticket_category_count_get**](docs/TicketCategoryApi.md#ticket_category_count_get) | **GET** /ticketCategory/count | count ticketCategory
*TicketCategoryApi* | [**ticket_category_get**](docs/TicketCategoryApi.md#ticket_category_get) | **GET** /ticketCategory | query ticketCategory
*TicketCategoryApi* | [**ticket_category_id_id_get**](docs/TicketCategoryApi.md#ticket_category_id_id_get) | **GET** /ticketCategory/id/{id} | query a specific ticketCategory
*TicketChannelApi* | [**ticket_channel_count_get**](docs/TicketChannelApi.md#ticket_channel_count_get) | **GET** /ticketChannel/count | count ticketChannel
*TicketChannelApi* | [**ticket_channel_get**](docs/TicketChannelApi.md#ticket_channel_get) | **GET** /ticketChannel | query ticketChannel
*TicketChannelApi* | [**ticket_channel_id_id_delete**](docs/TicketChannelApi.md#ticket_channel_id_id_delete) | **DELETE** /ticketChannel/id/{id} | delete a ticketChannel
*TicketChannelApi* | [**ticket_channel_id_id_get**](docs/TicketChannelApi.md#ticket_channel_id_id_get) | **GET** /ticketChannel/id/{id} | query a specific ticketChannel
*TicketChannelApi* | [**ticket_channel_id_id_put**](docs/TicketChannelApi.md#ticket_channel_id_id_put) | **PUT** /ticketChannel/id/{id} | update a ticketChannel
*TicketChannelApi* | [**ticket_channel_post**](docs/TicketChannelApi.md#ticket_channel_post) | **POST** /ticketChannel | create a ticketChannel
*TicketFaqApi* | [**ticket_faq_count_get**](docs/TicketFaqApi.md#ticket_faq_count_get) | **GET** /ticketFaq/count | count ticketFaq
*TicketFaqApi* | [**ticket_faq_get**](docs/TicketFaqApi.md#ticket_faq_get) | **GET** /ticketFaq | query ticketFaq
*TicketFaqApi* | [**ticket_faq_id_id_delete**](docs/TicketFaqApi.md#ticket_faq_id_id_delete) | **DELETE** /ticketFaq/id/{id} | delete a ticketFaq
*TicketFaqApi* | [**ticket_faq_id_id_get**](docs/TicketFaqApi.md#ticket_faq_id_id_get) | **GET** /ticketFaq/id/{id} | query a specific ticketFaq
*TicketFaqApi* | [**ticket_faq_id_id_put**](docs/TicketFaqApi.md#ticket_faq_id_id_put) | **PUT** /ticketFaq/id/{id} | update a ticketFaq
*TicketFaqApi* | [**ticket_faq_post**](docs/TicketFaqApi.md#ticket_faq_post) | **POST** /ticketFaq | create a ticketFaq
*TicketPoolingGroupApi* | [**ticket_pooling_group_count_get**](docs/TicketPoolingGroupApi.md#ticket_pooling_group_count_get) | **GET** /ticketPoolingGroup/count | count ticketPoolingGroup
*TicketPoolingGroupApi* | [**ticket_pooling_group_get**](docs/TicketPoolingGroupApi.md#ticket_pooling_group_get) | **GET** /ticketPoolingGroup | query ticketPoolingGroup
*TicketPoolingGroupApi* | [**ticket_pooling_group_id_id_get**](docs/TicketPoolingGroupApi.md#ticket_pooling_group_id_id_get) | **GET** /ticketPoolingGroup/id/{id} | query a specific ticketPoolingGroup
*TicketServiceLevelAgreementApi* | [**ticket_service_level_agreement_count_get**](docs/TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_count_get) | **GET** /ticketServiceLevelAgreement/count | count ticketServiceLevelAgreement
*TicketServiceLevelAgreementApi* | [**ticket_service_level_agreement_get**](docs/TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_get) | **GET** /ticketServiceLevelAgreement | query ticketServiceLevelAgreement
*TicketServiceLevelAgreementApi* | [**ticket_service_level_agreement_id_id_delete**](docs/TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_id_id_delete) | **DELETE** /ticketServiceLevelAgreement/id/{id} | delete a ticketServiceLevelAgreement
*TicketServiceLevelAgreementApi* | [**ticket_service_level_agreement_id_id_get**](docs/TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_id_id_get) | **GET** /ticketServiceLevelAgreement/id/{id} | query a specific ticketServiceLevelAgreement
*TicketServiceLevelAgreementApi* | [**ticket_service_level_agreement_id_id_put**](docs/TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_id_id_put) | **PUT** /ticketServiceLevelAgreement/id/{id} | update a ticketServiceLevelAgreement
*TicketServiceLevelAgreementApi* | [**ticket_service_level_agreement_post**](docs/TicketServiceLevelAgreementApi.md#ticket_service_level_agreement_post) | **POST** /ticketServiceLevelAgreement | create a ticketServiceLevelAgreement
*TicketStatusApi* | [**ticket_status_count_get**](docs/TicketStatusApi.md#ticket_status_count_get) | **GET** /ticketStatus/count | count ticketStatus
*TicketStatusApi* | [**ticket_status_get**](docs/TicketStatusApi.md#ticket_status_get) | **GET** /ticketStatus | query ticketStatus
*TicketStatusApi* | [**ticket_status_id_id_delete**](docs/TicketStatusApi.md#ticket_status_id_id_delete) | **DELETE** /ticketStatus/id/{id} | delete a ticketStatus
*TicketStatusApi* | [**ticket_status_id_id_get**](docs/TicketStatusApi.md#ticket_status_id_id_get) | **GET** /ticketStatus/id/{id} | query a specific ticketStatus
*TicketStatusApi* | [**ticket_status_id_id_put**](docs/TicketStatusApi.md#ticket_status_id_id_put) | **PUT** /ticketStatus/id/{id} | update a ticketStatus
*TicketStatusApi* | [**ticket_status_post**](docs/TicketStatusApi.md#ticket_status_post) | **POST** /ticketStatus | create a ticketStatus
*TicketTypeApi* | [**ticket_type_count_get**](docs/TicketTypeApi.md#ticket_type_count_get) | **GET** /ticketType/count | count ticketType
*TicketTypeApi* | [**ticket_type_get**](docs/TicketTypeApi.md#ticket_type_get) | **GET** /ticketType | query ticketType
*TicketTypeApi* | [**ticket_type_id_id_delete**](docs/TicketTypeApi.md#ticket_type_id_id_delete) | **DELETE** /ticketType/id/{id} | delete a ticketType
*TicketTypeApi* | [**ticket_type_id_id_get**](docs/TicketTypeApi.md#ticket_type_id_id_get) | **GET** /ticketType/id/{id} | query a specific ticketType
*TicketTypeApi* | [**ticket_type_id_id_put**](docs/TicketTypeApi.md#ticket_type_id_id_put) | **PUT** /ticketType/id/{id} | update a ticketType
*TicketTypeApi* | [**ticket_type_post**](docs/TicketTypeApi.md#ticket_type_post) | **POST** /ticketType | create a ticketType
*TitleApi* | [**title_count_get**](docs/TitleApi.md#title_count_get) | **GET** /title/count | count title
*TitleApi* | [**title_get**](docs/TitleApi.md#title_get) | **GET** /title | query title
*TitleApi* | [**title_id_id_delete**](docs/TitleApi.md#title_id_id_delete) | **DELETE** /title/id/{id} | delete a title
*TitleApi* | [**title_id_id_get**](docs/TitleApi.md#title_id_id_get) | **GET** /title/id/{id} | query a specific title
*TitleApi* | [**title_id_id_put**](docs/TitleApi.md#title_id_id_put) | **PUT** /title/id/{id} | update a title
*TitleApi* | [**title_post**](docs/TitleApi.md#title_post) | **POST** /title | create a title
*TranslationApi* | [**translation_count_get**](docs/TranslationApi.md#translation_count_get) | **GET** /translation/count | count translation
*TranslationApi* | [**translation_get**](docs/TranslationApi.md#translation_get) | **GET** /translation | query translation
*TranslationApi* | [**translation_id_id_delete**](docs/TranslationApi.md#translation_id_id_delete) | **DELETE** /translation/id/{id} | delete a translation
*TranslationApi* | [**translation_id_id_get**](docs/TranslationApi.md#translation_id_id_get) | **GET** /translation/id/{id} | query a specific translation
*TranslationApi* | [**translation_id_id_put**](docs/TranslationApi.md#translation_id_id_put) | **PUT** /translation/id/{id} | update a translation
*TranslationApi* | [**translation_post**](docs/TranslationApi.md#translation_post) | **POST** /translation | create a translation
*TransportationOrderApi* | [**transportation_order_count_get**](docs/TransportationOrderApi.md#transportation_order_count_get) | **GET** /transportationOrder/count | count transportationOrder
*TransportationOrderApi* | [**transportation_order_get**](docs/TransportationOrderApi.md#transportation_order_get) | **GET** /transportationOrder | query transportationOrder
*TransportationOrderApi* | [**transportation_order_id_id_create_pick_post**](docs/TransportationOrderApi.md#transportation_order_id_id_create_pick_post) | **POST** /transportationOrder/id/{id}/createPick | 
*TransportationOrderApi* | [**transportation_order_id_id_create_picking_list_post**](docs/TransportationOrderApi.md#transportation_order_id_id_create_picking_list_post) | **POST** /transportationOrder/id/{id}/createPickingList | 
*TransportationOrderApi* | [**transportation_order_id_id_create_transportation_order_from_unpicked_records_post**](docs/TransportationOrderApi.md#transportation_order_id_id_create_transportation_order_from_unpicked_records_post) | **POST** /transportationOrder/id/{id}/createTransportationOrderFromUnpickedRecords | 
*TransportationOrderApi* | [**transportation_order_id_id_delete**](docs/TransportationOrderApi.md#transportation_order_id_id_delete) | **DELETE** /transportationOrder/id/{id} | delete a transportationOrder
*TransportationOrderApi* | [**transportation_order_id_id_get**](docs/TransportationOrderApi.md#transportation_order_id_id_get) | **GET** /transportationOrder/id/{id} | query a specific transportationOrder
*TransportationOrderApi* | [**transportation_order_id_id_internal_transport_references_for_pick_up_get**](docs/TransportationOrderApi.md#transportation_order_id_id_internal_transport_references_for_pick_up_get) | **GET** /transportationOrder/id/{id}/internalTransportReferencesForPickUp | 
*TransportationOrderApi* | [**transportation_order_id_id_pick_pick_post**](docs/TransportationOrderApi.md#transportation_order_id_id_pick_pick_post) | **POST** /transportationOrder/id/{id}/pickPick | 
*TransportationOrderApi* | [**transportation_order_id_id_put**](docs/TransportationOrderApi.md#transportation_order_id_id_put) | **PUT** /transportationOrder/id/{id} | update a transportationOrder
*TransportationOrderApi* | [**transportation_order_id_id_put_down_internal_transport_reference_post**](docs/TransportationOrderApi.md#transportation_order_id_id_put_down_internal_transport_reference_post) | **POST** /transportationOrder/id/{id}/putDownInternalTransportReference | 
*TransportationOrderApi* | [**transportation_order_post**](docs/TransportationOrderApi.md#transportation_order_post) | **POST** /transportationOrder | create a transportationOrder
*UnitApi* | [**unit_count_get**](docs/UnitApi.md#unit_count_get) | **GET** /unit/count | count unit
*UnitApi* | [**unit_get**](docs/UnitApi.md#unit_get) | **GET** /unit | query unit
*UnitApi* | [**unit_id_id_delete**](docs/UnitApi.md#unit_id_id_delete) | **DELETE** /unit/id/{id} | delete a unit
*UnitApi* | [**unit_id_id_get**](docs/UnitApi.md#unit_id_id_get) | **GET** /unit/id/{id} | query a specific unit
*UnitApi* | [**unit_id_id_put**](docs/UnitApi.md#unit_id_id_put) | **PUT** /unit/id/{id} | update a unit
*UnitApi* | [**unit_post**](docs/UnitApi.md#unit_post) | **POST** /unit | create a unit
*UserApi* | [**user_count_get**](docs/UserApi.md#user_count_get) | **GET** /user/count | count user
*UserApi* | [**user_current_user_get**](docs/UserApi.md#user_current_user_get) | **GET** /user/currentUser | 
*UserApi* | [**user_get**](docs/UserApi.md#user_get) | **GET** /user | query user
*UserApi* | [**user_id_id_delete**](docs/UserApi.md#user_id_id_delete) | **DELETE** /user/id/{id} | delete a user
*UserApi* | [**user_id_id_get**](docs/UserApi.md#user_id_id_get) | **GET** /user/id/{id} | query a specific user
*UserApi* | [**user_id_id_invite_post**](docs/UserApi.md#user_id_id_invite_post) | **POST** /user/id/{id}/invite | 
*UserApi* | [**user_id_id_put**](docs/UserApi.md#user_id_id_put) | **PUT** /user/id/{id} | update a user
*UserApi* | [**user_id_id_user_image_get**](docs/UserApi.md#user_id_id_user_image_get) | **GET** /user/id/{id}/userImage | 
*UserApi* | [**user_id_id_user_image_thumbnail_get**](docs/UserApi.md#user_id_id_user_image_thumbnail_get) | **GET** /user/id/{id}/userImageThumbnail | 
*UserApi* | [**user_post**](docs/UserApi.md#user_post) | **POST** /user | create a user
*UserRoleApi* | [**user_role_count_get**](docs/UserRoleApi.md#user_role_count_get) | **GET** /userRole/count | count userRole
*UserRoleApi* | [**user_role_disable_user_roles_during_trial_post**](docs/UserRoleApi.md#user_role_disable_user_roles_during_trial_post) | **POST** /userRole/disableUserRolesDuringTrial | 
*UserRoleApi* | [**user_role_enable_user_roles_during_trial_post**](docs/UserRoleApi.md#user_role_enable_user_roles_during_trial_post) | **POST** /userRole/enableUserRolesDuringTrial | 
*UserRoleApi* | [**user_role_get**](docs/UserRoleApi.md#user_role_get) | **GET** /userRole | query userRole
*UserRoleApi* | [**user_role_id_id_delete**](docs/UserRoleApi.md#user_role_id_id_delete) | **DELETE** /userRole/id/{id} | delete a userRole
*UserRoleApi* | [**user_role_id_id_get**](docs/UserRoleApi.md#user_role_id_id_get) | **GET** /userRole/id/{id} | query a specific userRole
*UserRoleApi* | [**user_role_id_id_put**](docs/UserRoleApi.md#user_role_id_id_put) | **PUT** /userRole/id/{id} | update a userRole
*UserRoleApi* | [**user_role_post**](docs/UserRoleApi.md#user_role_post) | **POST** /userRole | create a userRole
*VariantArticleApi* | [**variant_article_count_get**](docs/VariantArticleApi.md#variant_article_count_get) | **GET** /variantArticle/count | count variantArticle
*VariantArticleApi* | [**variant_article_get**](docs/VariantArticleApi.md#variant_article_get) | **GET** /variantArticle | query variantArticle
*VariantArticleApi* | [**variant_article_id_id_delete**](docs/VariantArticleApi.md#variant_article_id_id_delete) | **DELETE** /variantArticle/id/{id} | delete a variantArticle
*VariantArticleApi* | [**variant_article_id_id_get**](docs/VariantArticleApi.md#variant_article_id_id_get) | **GET** /variantArticle/id/{id} | query a specific variantArticle
*VariantArticleApi* | [**variant_article_id_id_put**](docs/VariantArticleApi.md#variant_article_id_id_put) | **PUT** /variantArticle/id/{id} | update a variantArticle
*VariantArticleApi* | [**variant_article_post**](docs/VariantArticleApi.md#variant_article_post) | **POST** /variantArticle | create a variantArticle
*VariantArticleAttributeApi* | [**variant_article_attribute_count_get**](docs/VariantArticleAttributeApi.md#variant_article_attribute_count_get) | **GET** /variantArticleAttribute/count | count variantArticleAttribute
*VariantArticleAttributeApi* | [**variant_article_attribute_get**](docs/VariantArticleAttributeApi.md#variant_article_attribute_get) | **GET** /variantArticleAttribute | query variantArticleAttribute
*VariantArticleAttributeApi* | [**variant_article_attribute_id_id_delete**](docs/VariantArticleAttributeApi.md#variant_article_attribute_id_id_delete) | **DELETE** /variantArticleAttribute/id/{id} | delete a variantArticleAttribute
*VariantArticleAttributeApi* | [**variant_article_attribute_id_id_get**](docs/VariantArticleAttributeApi.md#variant_article_attribute_id_id_get) | **GET** /variantArticleAttribute/id/{id} | query a specific variantArticleAttribute
*VariantArticleAttributeApi* | [**variant_article_attribute_id_id_put**](docs/VariantArticleAttributeApi.md#variant_article_attribute_id_id_put) | **PUT** /variantArticleAttribute/id/{id} | update a variantArticleAttribute
*VariantArticleAttributeApi* | [**variant_article_attribute_post**](docs/VariantArticleAttributeApi.md#variant_article_attribute_post) | **POST** /variantArticleAttribute | create a variantArticleAttribute
*VariantArticleVariantApi* | [**variant_article_variant_count_get**](docs/VariantArticleVariantApi.md#variant_article_variant_count_get) | **GET** /variantArticleVariant/count | count variantArticleVariant
*VariantArticleVariantApi* | [**variant_article_variant_get**](docs/VariantArticleVariantApi.md#variant_article_variant_get) | **GET** /variantArticleVariant | query variantArticleVariant
*VariantArticleVariantApi* | [**variant_article_variant_id_id_get**](docs/VariantArticleVariantApi.md#variant_article_variant_id_id_get) | **GET** /variantArticleVariant/id/{id} | query a specific variantArticleVariant
*WarehouseApi* | [**warehouse_count_get**](docs/WarehouseApi.md#warehouse_count_get) | **GET** /warehouse/count | count warehouse
*WarehouseApi* | [**warehouse_get**](docs/WarehouseApi.md#warehouse_get) | **GET** /warehouse | query warehouse
*WarehouseApi* | [**warehouse_id_id_activate_post**](docs/WarehouseApi.md#warehouse_id_id_activate_post) | **POST** /warehouse/id/{id}/activate | 
*WarehouseApi* | [**warehouse_id_id_deactivate_post**](docs/WarehouseApi.md#warehouse_id_id_deactivate_post) | **POST** /warehouse/id/{id}/deactivate | 
*WarehouseApi* | [**warehouse_id_id_delete**](docs/WarehouseApi.md#warehouse_id_id_delete) | **DELETE** /warehouse/id/{id} | delete a warehouse
*WarehouseApi* | [**warehouse_id_id_get**](docs/WarehouseApi.md#warehouse_id_id_get) | **GET** /warehouse/id/{id} | query a specific warehouse
*WarehouseApi* | [**warehouse_id_id_put**](docs/WarehouseApi.md#warehouse_id_id_put) | **PUT** /warehouse/id/{id} | update a warehouse
*WarehouseApi* | [**warehouse_post**](docs/WarehouseApi.md#warehouse_post) | **POST** /warehouse | create a warehouse
*WarehouseStockApi* | [**warehouse_stock_count_get**](docs/WarehouseStockApi.md#warehouse_stock_count_get) | **GET** /warehouseStock/count | count warehouseStock
*WarehouseStockApi* | [**warehouse_stock_get**](docs/WarehouseStockApi.md#warehouse_stock_get) | **GET** /warehouseStock | query warehouseStock
*WarehouseStockApi* | [**warehouse_stock_id_id_get**](docs/WarehouseStockApi.md#warehouse_stock_id_id_get) | **GET** /warehouseStock/id/{id} | query a specific warehouseStock
*WarehouseStockMovementApi* | [**warehouse_stock_movement_book_direct_stock_transfer_post**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_book_direct_stock_transfer_post) | **POST** /warehouseStockMovement/bookDirectStockTransfer | 
*WarehouseStockMovementApi* | [**warehouse_stock_movement_book_from_loading_equipment_place_post**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_book_from_loading_equipment_place_post) | **POST** /warehouseStockMovement/bookFromLoadingEquipmentPlace | 
*WarehouseStockMovementApi* | [**warehouse_stock_movement_book_incoming_movement_post**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_book_incoming_movement_post) | **POST** /warehouseStockMovement/bookIncomingMovement | 
*WarehouseStockMovementApi* | [**warehouse_stock_movement_book_onto_internal_transport_reference_post**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_book_onto_internal_transport_reference_post) | **POST** /warehouseStockMovement/bookOntoInternalTransportReference | 
*WarehouseStockMovementApi* | [**warehouse_stock_movement_book_outgoing_movement_post**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_book_outgoing_movement_post) | **POST** /warehouseStockMovement/bookOutgoingMovement | 
*WarehouseStockMovementApi* | [**warehouse_stock_movement_book_to_loading_equipment_place_post**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_book_to_loading_equipment_place_post) | **POST** /warehouseStockMovement/bookToLoadingEquipmentPlace | 
*WarehouseStockMovementApi* | [**warehouse_stock_movement_count_get**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_count_get) | **GET** /warehouseStockMovement/count | count warehouseStockMovement
*WarehouseStockMovementApi* | [**warehouse_stock_movement_get**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_get) | **GET** /warehouseStockMovement | query warehouseStockMovement
*WarehouseStockMovementApi* | [**warehouse_stock_movement_id_id_get**](docs/WarehouseStockMovementApi.md#warehouse_stock_movement_id_id_get) | **GET** /warehouseStockMovement/id/{id} | query a specific warehouseStockMovement
*WebhookApi* | [**webhook_count_get**](docs/WebhookApi.md#webhook_count_get) | **GET** /webhook/count | count webhook
*WebhookApi* | [**webhook_get**](docs/WebhookApi.md#webhook_get) | **GET** /webhook | query webhook
*WebhookApi* | [**webhook_id_id_delete**](docs/WebhookApi.md#webhook_id_id_delete) | **DELETE** /webhook/id/{id} | delete a webhook
*WebhookApi* | [**webhook_id_id_get**](docs/WebhookApi.md#webhook_id_id_get) | **GET** /webhook/id/{id} | query a specific webhook
*WebhookApi* | [**webhook_id_id_put**](docs/WebhookApi.md#webhook_id_id_put) | **PUT** /webhook/id/{id} | update a webhook
*WebhookApi* | [**webhook_post**](docs/WebhookApi.md#webhook_post) | **POST** /webhook | create a webhook
*WeclappOsApi* | [**weclapp_os_count_get**](docs/WeclappOsApi.md#weclapp_os_count_get) | **GET** /weclappOs/count | count weclappOs
*WeclappOsApi* | [**weclapp_os_get**](docs/WeclappOsApi.md#weclapp_os_get) | **GET** /weclappOs | query weclappOs
*WeclappOsApi* | [**weclapp_os_id_id_delete**](docs/WeclappOsApi.md#weclapp_os_id_id_delete) | **DELETE** /weclappOs/id/{id} | delete a weclappOs
*WeclappOsApi* | [**weclapp_os_id_id_get**](docs/WeclappOsApi.md#weclapp_os_id_id_get) | **GET** /weclappOs/id/{id} | query a specific weclappOs
*WeclappOsApi* | [**weclapp_os_id_id_put**](docs/WeclappOsApi.md#weclapp_os_id_id_put) | **PUT** /weclappOs/id/{id} | update a weclappOs
*WeclappOsApi* | [**weclapp_os_post**](docs/WeclappOsApi.md#weclapp_os_post) | **POST** /weclappOs | create a weclappOs


## Documentation For Models

 - [AbstractBillOfMaterial](docs/AbstractBillOfMaterial.md)
 - [AbstractBookRecord](docs/AbstractBookRecord.md)
 - [AbstractEntity](docs/AbstractEntity.md)
 - [AbstractEntityWithCustomAttributes](docs/AbstractEntityWithCustomAttributes.md)
 - [AbstractParty](docs/AbstractParty.md)
 - [AccountingTransaction](docs/AccountingTransaction.md)
 - [AccountingTransactionCountGet200Response](docs/AccountingTransactionCountGet200Response.md)
 - [AccountingTransactionDetail](docs/AccountingTransactionDetail.md)
 - [AccountingTransactionGet200Response](docs/AccountingTransactionGet200Response.md)
 - [AccountingTransactionStatus](docs/AccountingTransactionStatus.md)
 - [Address](docs/Address.md)
 - [AdvancePaymentStatus](docs/AdvancePaymentStatus.md)
 - [Amount](docs/Amount.md)
 - [ApiProblem](docs/ApiProblem.md)
 - [ApiProblemType](docs/ApiProblemType.md)
 - [ArchivedEmail](docs/ArchivedEmail.md)
 - [ArchivedEmailGet200Response](docs/ArchivedEmailGet200Response.md)
 - [ArchivedEmailIdIdRemoveReferencePost200Response](docs/ArchivedEmailIdIdRemoveReferencePost200Response.md)
 - [ArchivedEmailIdIdRemoveReferencePostRequest](docs/ArchivedEmailIdIdRemoveReferencePostRequest.md)
 - [Article](docs/Article.md)
 - [ArticleAccountingCodeGet200Response](docs/ArticleAccountingCodeGet200Response.md)
 - [ArticleAlternativeQuantity](docs/ArticleAlternativeQuantity.md)
 - [ArticleCalculationPrice](docs/ArticleCalculationPrice.md)
 - [ArticleCalculationPriceType](docs/ArticleCalculationPriceType.md)
 - [ArticleCategory](docs/ArticleCategory.md)
 - [ArticleCategoryGet200Response](docs/ArticleCategoryGet200Response.md)
 - [ArticleGet200Response](docs/ArticleGet200Response.md)
 - [ArticleGet200ResponseAdditionalProperties](docs/ArticleGet200ResponseAdditionalProperties.md)
 - [ArticleIdIdChangeUnitPostRequest](docs/ArticleIdIdChangeUnitPostRequest.md)
 - [ArticleIdIdCreateDatasheetPdfPostRequest](docs/ArticleIdIdCreateDatasheetPdfPostRequest.md)
 - [ArticleIdIdCreateLabelPdfPostRequest](docs/ArticleIdIdCreateLabelPdfPostRequest.md)
 - [ArticleIdIdPackagingUnitStructureGet200Response](docs/ArticleIdIdPackagingUnitStructureGet200Response.md)
 - [ArticleImage](docs/ArticleImage.md)
 - [ArticleItemGroup](docs/ArticleItemGroup.md)
 - [ArticleItemGroupGet200Response](docs/ArticleItemGroupGet200Response.md)
 - [ArticleItemGroupItem](docs/ArticleItemGroupItem.md)
 - [ArticlePrice](docs/ArticlePrice.md)
 - [ArticlePriceGet200Response](docs/ArticlePriceGet200Response.md)
 - [ArticlePriceWithoutArticleReference](docs/ArticlePriceWithoutArticleReference.md)
 - [ArticlePriceWithoutSalesChannel](docs/ArticlePriceWithoutSalesChannel.md)
 - [ArticleSupplySource](docs/ArticleSupplySource.md)
 - [ArticleSupplySourceGet200Response](docs/ArticleSupplySourceGet200Response.md)
 - [ArticleType](docs/ArticleType.md)
 - [Attendance](docs/Attendance.md)
 - [AttendanceCurrentAttendanceGet200Response](docs/AttendanceCurrentAttendanceGet200Response.md)
 - [AttendanceGet200Response](docs/AttendanceGet200Response.md)
 - [BalanceSheetItem](docs/BalanceSheetItem.md)
 - [BankAccount](docs/BankAccount.md)
 - [BankAccountGet200Response](docs/BankAccountGet200Response.md)
 - [BaossUserStatus](docs/BaossUserStatus.md)
 - [BaseArticle](docs/BaseArticle.md)
 - [BaseMinimalRecordItem](docs/BaseMinimalRecordItem.md)
 - [BasePickingBookRecord](docs/BasePickingBookRecord.md)
 - [BasePurchaseRecord](docs/BasePurchaseRecord.md)
 - [BaseRecord](docs/BaseRecord.md)
 - [BaseRecordItem](docs/BaseRecordItem.md)
 - [BaseRecordItemWithMoney](docs/BaseRecordItemWithMoney.md)
 - [BaseRecordItemWithPrintSettings](docs/BaseRecordItemWithPrintSettings.md)
 - [BaseRecordWithMoney](docs/BaseRecordWithMoney.md)
 - [BaseSalesRecord](docs/BaseSalesRecord.md)
 - [BaseSalesRecordItemWithCost](docs/BaseSalesRecordItemWithCost.md)
 - [BaseSalesRecordItemWithService](docs/BaseSalesRecordItemWithService.md)
 - [BaseSalesRecordWithAddresses](docs/BaseSalesRecordWithAddresses.md)
 - [BaseShipment](docs/BaseShipment.md)
 - [BaseShippingCostItem](docs/BaseShippingCostItem.md)
 - [BatchNumber](docs/BatchNumber.md)
 - [BatchNumberGet200Response](docs/BatchNumberGet200Response.md)
 - [BatchSerialNumber](docs/BatchSerialNumber.md)
 - [BillOfMaterial](docs/BillOfMaterial.md)
 - [BillUntil](docs/BillUntil.md)
 - [BillableInvoiceStatus](docs/BillableInvoiceStatus.md)
 - [BlanketPurchaseOrder](docs/BlanketPurchaseOrder.md)
 - [BlanketPurchaseOrderGet200Response](docs/BlanketPurchaseOrderGet200Response.md)
 - [BlanketPurchaseOrderIdIdGenerateReleasesPost200Response](docs/BlanketPurchaseOrderIdIdGenerateReleasesPost200Response.md)
 - [BlanketPurchaseOrderIdIdGenerateReleasesPostRequest](docs/BlanketPurchaseOrderIdIdGenerateReleasesPostRequest.md)
 - [BlanketPurchaseOrderStatusHistory](docs/BlanketPurchaseOrderStatusHistory.md)
 - [BlanketPurchaseOrderStatusType](docs/BlanketPurchaseOrderStatusType.md)
 - [BookingType](docs/BookingType.md)
 - [CDBReminderType](docs/CDBReminderType.md)
 - [CalculationType](docs/CalculationType.md)
 - [Calendar](docs/Calendar.md)
 - [CalendarEvent](docs/CalendarEvent.md)
 - [CalendarEventAttendee](docs/CalendarEventAttendee.md)
 - [CalendarEventGet200Response](docs/CalendarEventGet200Response.md)
 - [CalendarGet200Response](docs/CalendarGet200Response.md)
 - [CalendarIdIdDeleteCalendarAndMoveEventsPostRequest](docs/CalendarIdIdDeleteCalendarAndMoveEventsPostRequest.md)
 - [CalendarSharingPermissionType](docs/CalendarSharingPermissionType.md)
 - [CalendarSharingPermissions](docs/CalendarSharingPermissions.md)
 - [Campaign](docs/Campaign.md)
 - [CampaignGet200Response](docs/CampaignGet200Response.md)
 - [CampaignParticipant](docs/CampaignParticipant.md)
 - [CampaignParticipantGet200Response](docs/CampaignParticipantGet200Response.md)
 - [CampaignType](docs/CampaignType.md)
 - [CashAccount](docs/CashAccount.md)
 - [CashAccountGet200Response](docs/CashAccountGet200Response.md)
 - [CollectiveInvoicePositionPrintType](docs/CollectiveInvoicePositionPrintType.md)
 - [Comment](docs/Comment.md)
 - [CommentGet200Response](docs/CommentGet200Response.md)
 - [CommercialLanguage](docs/CommercialLanguage.md)
 - [CommercialLanguageGet200Response](docs/CommercialLanguageGet200Response.md)
 - [CommissionSalesPartner](docs/CommissionSalesPartner.md)
 - [CommissionType](docs/CommissionType.md)
 - [ConditionsForEntityType](docs/ConditionsForEntityType.md)
 - [Contact](docs/Contact.md)
 - [ContactGet200Response](docs/ContactGet200Response.md)
 - [Contract](docs/Contract.md)
 - [ContractAdditionalAddress](docs/ContractAdditionalAddress.md)
 - [ContractAuthorizationUnit](docs/ContractAuthorizationUnit.md)
 - [ContractAuthorizationUnitGet200Response](docs/ContractAuthorizationUnitGet200Response.md)
 - [ContractBillingType](docs/ContractBillingType.md)
 - [ContractChargeInterval](docs/ContractChargeInterval.md)
 - [ContractChargeIntervalType](docs/ContractChargeIntervalType.md)
 - [ContractChargeType](docs/ContractChargeType.md)
 - [ContractCostItem](docs/ContractCostItem.md)
 - [ContractGet200Response](docs/ContractGet200Response.md)
 - [ContractItem](docs/ContractItem.md)
 - [ContractSoftframe](docs/ContractSoftframe.md)
 - [ContractStatus](docs/ContractStatus.md)
 - [ContractUnitType](docs/ContractUnitType.md)
 - [CostCenter](docs/CostCenter.md)
 - [CostCenterGet200Response](docs/CostCenterGet200Response.md)
 - [CostCenterWithDistributionPercentage](docs/CostCenterWithDistributionPercentage.md)
 - [CostType](docs/CostType.md)
 - [CostTypeGet200Response](docs/CostTypeGet200Response.md)
 - [CrmEvent](docs/CrmEvent.md)
 - [CrmEventGet200Response](docs/CrmEventGet200Response.md)
 - [CrmEventType](docs/CrmEventType.md)
 - [Currency](docs/Currency.md)
 - [CurrencyCompanyCurrencyGet200Response](docs/CurrencyCompanyCurrencyGet200Response.md)
 - [CurrencyGet200Response](docs/CurrencyGet200Response.md)
 - [CustomAttribute](docs/CustomAttribute.md)
 - [CustomAttributeDefinition](docs/CustomAttributeDefinition.md)
 - [CustomAttributeDefinitionConditionOperator](docs/CustomAttributeDefinitionConditionOperator.md)
 - [CustomAttributeDefinitionConditionType](docs/CustomAttributeDefinitionConditionType.md)
 - [CustomAttributeDefinitionConditions](docs/CustomAttributeDefinitionConditions.md)
 - [CustomAttributeDefinitionGet200Response](docs/CustomAttributeDefinitionGet200Response.md)
 - [CustomAttributeDefinitionListValue](docs/CustomAttributeDefinitionListValue.md)
 - [CustomAttributeDefinitionOrder](docs/CustomAttributeDefinitionOrder.md)
 - [CustomAttributeDefinitionPermission](docs/CustomAttributeDefinitionPermission.md)
 - [CustomAttributeDefinitionPermissionType](docs/CustomAttributeDefinitionPermissionType.md)
 - [CustomAttributeDefinitionPropertyCondition](docs/CustomAttributeDefinitionPropertyCondition.md)
 - [CustomAttributeDefinitionReadOrderGet200Response](docs/CustomAttributeDefinitionReadOrderGet200Response.md)
 - [CustomAttributeDefinitionTranslation](docs/CustomAttributeDefinitionTranslation.md)
 - [CustomAttributeDefinitionUpdateOrderPostRequest](docs/CustomAttributeDefinitionUpdateOrderPostRequest.md)
 - [CustomAttributeDefinitionUpdateOrderPostRequestOrderInner](docs/CustomAttributeDefinitionUpdateOrderPostRequestOrderInner.md)
 - [CustomAttributeEntityType](docs/CustomAttributeEntityType.md)
 - [CustomAttributeExtendableEntity](docs/CustomAttributeExtendableEntity.md)
 - [CustomAttributePublicPageType](docs/CustomAttributePublicPageType.md)
 - [CustomAttributeType](docs/CustomAttributeType.md)
 - [CustomValue](docs/CustomValue.md)
 - [Customer](docs/Customer.md)
 - [CustomerBusinessType](docs/CustomerBusinessType.md)
 - [CustomerGet200Response](docs/CustomerGet200Response.md)
 - [CustomerOrLead](docs/CustomerOrLead.md)
 - [CustomerSatisfaction](docs/CustomerSatisfaction.md)
 - [CustomerSpecificArticleAttributes](docs/CustomerSpecificArticleAttributes.md)
 - [DebitCreditIndicator](docs/DebitCreditIndicator.md)
 - [DemoTestSystemInfo](docs/DemoTestSystemInfo.md)
 - [DesiredInvoiceStatusType](docs/DesiredInvoiceStatusType.md)
 - [DispositionInfoAvailabilityType](docs/DispositionInfoAvailabilityType.md)
 - [DistributionChannel](docs/DistributionChannel.md)
 - [Document](docs/Document.md)
 - [DocumentCopyPost200Response](docs/DocumentCopyPost200Response.md)
 - [DocumentCopyPostRequest](docs/DocumentCopyPostRequest.md)
 - [DocumentGet200Response](docs/DocumentGet200Response.md)
 - [DocumentIdIdCopyPostRequest](docs/DocumentIdIdCopyPostRequest.md)
 - [DocumentType](docs/DocumentType.md)
 - [DocumentVersion](docs/DocumentVersion.md)
 - [DueDateOption](docs/DueDateOption.md)
 - [DunningBlockState](docs/DunningBlockState.md)
 - [Duration](docs/Duration.md)
 - [EcommerceOrder](docs/EcommerceOrder.md)
 - [EmailAddresses](docs/EmailAddresses.md)
 - [Entity](docs/Entity.md)
 - [EntityReference](docs/EntityReference.md)
 - [EventInvitationStatus](docs/EventInvitationStatus.md)
 - [EventRight](docs/EventRight.md)
 - [ExternalConnection](docs/ExternalConnection.md)
 - [ExternalConnectionGet200Response](docs/ExternalConnectionGet200Response.md)
 - [ExternalConnectionType](docs/ExternalConnectionType.md)
 - [FastProductionBookingResult](docs/FastProductionBookingResult.md)
 - [FastProductionBookingResultMessage](docs/FastProductionBookingResultMessage.md)
 - [FinancialYear](docs/FinancialYear.md)
 - [FinancialYearGet200Response](docs/FinancialYearGet200Response.md)
 - [FinancialYearIdIdGeneratePeriodsPost200Response](docs/FinancialYearIdIdGeneratePeriodsPost200Response.md)
 - [FinancialYearStatus](docs/FinancialYearStatus.md)
 - [FollowupBusyState](docs/FollowupBusyState.md)
 - [FulfillmentProvider](docs/FulfillmentProvider.md)
 - [FulfillmentProviderGet200Response](docs/FulfillmentProviderGet200Response.md)
 - [FulfillmentProviderType](docs/FulfillmentProviderType.md)
 - [IncomingBooking](docs/IncomingBooking.md)
 - [IncomingGoods](docs/IncomingGoods.md)
 - [IncomingGoodsGet200Response](docs/IncomingGoodsGet200Response.md)
 - [IncomingGoodsIdIdAddPurchaseOrdersPost200Response](docs/IncomingGoodsIdIdAddPurchaseOrdersPost200Response.md)
 - [IncomingGoodsIdIdAddPurchaseOrdersPostRequest](docs/IncomingGoodsIdIdAddPurchaseOrdersPostRequest.md)
 - [IncomingGoodsIdIdCreateCompensationShipmentPost200Response](docs/IncomingGoodsIdIdCreateCompensationShipmentPost200Response.md)
 - [IncomingGoodsIdIdCreateCreditNotePost200Response](docs/IncomingGoodsIdIdCreateCreditNotePost200Response.md)
 - [IncomingGoodsIdIdCreateSupplierReturnPostRequest](docs/IncomingGoodsIdIdCreateSupplierReturnPostRequest.md)
 - [IncomingGoodsIdIdIncomingBookingsGet200Response](docs/IncomingGoodsIdIdIncomingBookingsGet200Response.md)
 - [IncomingGoodsIdIdUpdateIncomingBookingsPostRequest](docs/IncomingGoodsIdIdUpdateIncomingBookingsPostRequest.md)
 - [IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner](docs/IncomingGoodsIdIdUpdateIncomingBookingsPostRequestIncomingBookingsInner.md)
 - [IncomingGoodsItem](docs/IncomingGoodsItem.md)
 - [InternalShippingCarrier](docs/InternalShippingCarrier.md)
 - [InternalTicketStatus](docs/InternalTicketStatus.md)
 - [InternalTransportReference](docs/InternalTransportReference.md)
 - [InternalTransportReferenceGet200Response](docs/InternalTransportReferenceGet200Response.md)
 - [InvoicingType](docs/InvoicingType.md)
 - [JobAbortGet200Response](docs/JobAbortGet200Response.md)
 - [JobStatus](docs/JobStatus.md)
 - [Lead](docs/Lead.md)
 - [LeadGet200Response](docs/LeadGet200Response.md)
 - [LeadIdIdConvertLeadToCustomerGet200Response](docs/LeadIdIdConvertLeadToCustomerGet200Response.md)
 - [LeadStatus](docs/LeadStatus.md)
 - [LedgerAccount](docs/LedgerAccount.md)
 - [LedgerAccountGet200Response](docs/LedgerAccountGet200Response.md)
 - [LedgerAccountType](docs/LedgerAccountType.md)
 - [License](docs/License.md)
 - [LoadingEquipmentIdentifier](docs/LoadingEquipmentIdentifier.md)
 - [LoadingEquipmentIdentifierGet200Response](docs/LoadingEquipmentIdentifierGet200Response.md)
 - [MailTemplate](docs/MailTemplate.md)
 - [MailTemplateGet200Response](docs/MailTemplateGet200Response.md)
 - [MarginCalculationPriceType](docs/MarginCalculationPriceType.md)
 - [MetaQueryFilterPropertiesGet200Response](docs/MetaQueryFilterPropertiesGet200Response.md)
 - [MetaResourcesGet200Response](docs/MetaResourcesGet200Response.md)
 - [MinimalStoragePlace](docs/MinimalStoragePlace.md)
 - [MoneyTransaction](docs/MoneyTransaction.md)
 - [MoneyTransactionProcessingStrategy](docs/MoneyTransactionProcessingStrategy.md)
 - [MoneyTransactionSource](docs/MoneyTransactionSource.md)
 - [NestedStoragePlace](docs/NestedStoragePlace.md)
 - [Notification](docs/Notification.md)
 - [NotificationGet200Response](docs/NotificationGet200Response.md)
 - [NotificationIdIdMarkReadPost200Response](docs/NotificationIdIdMarkReadPost200Response.md)
 - [NotificationPriority](docs/NotificationPriority.md)
 - [OfferOutType](docs/OfferOutType.md)
 - [OfferStatusType](docs/OfferStatusType.md)
 - [OnlineAccount](docs/OnlineAccount.md)
 - [OnlineAccountType](docs/OnlineAccountType.md)
 - [OnlyId](docs/OnlyId.md)
 - [OpenItem](docs/OpenItem.md)
 - [OpenItemType](docs/OpenItemType.md)
 - [Opportunity](docs/Opportunity.md)
 - [OpportunityGet200Response](docs/OpportunityGet200Response.md)
 - [OpportunityIdIdLinkQuotationPost200Response](docs/OpportunityIdIdLinkQuotationPost200Response.md)
 - [OpportunityIdIdLinkQuotationPostRequest](docs/OpportunityIdIdLinkQuotationPostRequest.md)
 - [OrderStatusType](docs/OrderStatusType.md)
 - [PackagingUnit](docs/PackagingUnit.md)
 - [Party](docs/Party.md)
 - [PartyBankAccount](docs/PartyBankAccount.md)
 - [PartyButNotContact](docs/PartyButNotContact.md)
 - [PartyEmailAddresses](docs/PartyEmailAddresses.md)
 - [PartyGet200Response](docs/PartyGet200Response.md)
 - [PartyHabitualExporterLetterOfIntent](docs/PartyHabitualExporterLetterOfIntent.md)
 - [PartyHabitualExporterLetterOfIntentType](docs/PartyHabitualExporterLetterOfIntentType.md)
 - [PartyType](docs/PartyType.md)
 - [PaymentApplication](docs/PaymentApplication.md)
 - [PaymentMethod](docs/PaymentMethod.md)
 - [PaymentMethodGet200Response](docs/PaymentMethodGet200Response.md)
 - [PaymentMethodTypeKey](docs/PaymentMethodTypeKey.md)
 - [PaymentRun](docs/PaymentRun.md)
 - [PaymentRunGet200Response](docs/PaymentRunGet200Response.md)
 - [PaymentRunItem](docs/PaymentRunItem.md)
 - [PaymentRunItemGet200Response](docs/PaymentRunItemGet200Response.md)
 - [PaymentRunPaymentType](docs/PaymentRunPaymentType.md)
 - [PaymentStatus](docs/PaymentStatus.md)
 - [PaymentType](docs/PaymentType.md)
 - [PerformanceRecordedStatus](docs/PerformanceRecordedStatus.md)
 - [Period](docs/Period.md)
 - [PermissionString](docs/PermissionString.md)
 - [Pick](docs/Pick.md)
 - [PickGet200Response](docs/PickGet200Response.md)
 - [PriceCalculationParameter](docs/PriceCalculationParameter.md)
 - [PriceConditionType](docs/PriceConditionType.md)
 - [PriceData](docs/PriceData.md)
 - [PriceDataReductionAdditionItem](docs/PriceDataReductionAdditionItem.md)
 - [PriceScaleType](docs/PriceScaleType.md)
 - [ProductionCostCenterType](docs/ProductionCostCenterType.md)
 - [ProductionOrder](docs/ProductionOrder.md)
 - [ProductionOrderFastProductionBookingPost200Response](docs/ProductionOrderFastProductionBookingPost200Response.md)
 - [ProductionOrderFastProductionBookingPostRequest](docs/ProductionOrderFastProductionBookingPostRequest.md)
 - [ProductionOrderGet200Response](docs/ProductionOrderGet200Response.md)
 - [ProductionOrderItem](docs/ProductionOrderItem.md)
 - [ProductionOrderItemStatus](docs/ProductionOrderItemStatus.md)
 - [ProductionOrderStatusHistory](docs/ProductionOrderStatusHistory.md)
 - [ProductionOrderStatusType](docs/ProductionOrderStatusType.md)
 - [ProductionOrderWorkItem](docs/ProductionOrderWorkItem.md)
 - [ProductionWorkSchedule](docs/ProductionWorkSchedule.md)
 - [ProductionWorkScheduleAssignment](docs/ProductionWorkScheduleAssignment.md)
 - [ProductionWorkScheduleAssignmentGet200Response](docs/ProductionWorkScheduleAssignmentGet200Response.md)
 - [ProductionWorkScheduleGet200Response](docs/ProductionWorkScheduleGet200Response.md)
 - [ProductionWorkScheduleItem](docs/ProductionWorkScheduleItem.md)
 - [ProductionWorkScheduleItemTimeType](docs/ProductionWorkScheduleItemTimeType.md)
 - [ProductionWorkScheduleStatus](docs/ProductionWorkScheduleStatus.md)
 - [ProjectMembers](docs/ProjectMembers.md)
 - [PropertyTranslation](docs/PropertyTranslation.md)
 - [PropertyTranslationReadPropertyTranslationsGet200Response](docs/PropertyTranslationReadPropertyTranslationsGet200Response.md)
 - [PropertyTranslationUpdatePropertyTranslationsPostRequest](docs/PropertyTranslationUpdatePropertyTranslationsPostRequest.md)
 - [PropertyTranslationUpdatePropertyTranslationsPostRequestPropertyTranslationsInner](docs/PropertyTranslationUpdatePropertyTranslationsPostRequestPropertyTranslationsInner.md)
 - [PropertyTranslationValue](docs/PropertyTranslationValue.md)
 - [PurchaseInvoice](docs/PurchaseInvoice.md)
 - [PurchaseInvoiceGet200Response](docs/PurchaseInvoiceGet200Response.md)
 - [PurchaseInvoiceIdIdCreateCreditNotePost200Response](docs/PurchaseInvoiceIdIdCreateCreditNotePost200Response.md)
 - [PurchaseInvoiceIdIdCreateCreditNotePostRequest](docs/PurchaseInvoiceIdIdCreateCreditNotePostRequest.md)
 - [PurchaseInvoiceItem](docs/PurchaseInvoiceItem.md)
 - [PurchaseInvoiceItemRelationship](docs/PurchaseInvoiceItemRelationship.md)
 - [PurchaseInvoiceStatusHistory](docs/PurchaseInvoiceStatusHistory.md)
 - [PurchaseInvoiceStatusType](docs/PurchaseInvoiceStatusType.md)
 - [PurchaseInvoiceType](docs/PurchaseInvoiceType.md)
 - [PurchaseOpenItem](docs/PurchaseOpenItem.md)
 - [PurchaseOpenItemGet200Response](docs/PurchaseOpenItemGet200Response.md)
 - [PurchaseOpenItemIdIdCreatePaymentApplicationPost200Response](docs/PurchaseOpenItemIdIdCreatePaymentApplicationPost200Response.md)
 - [PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest](docs/PurchaseOpenItemIdIdCreatePaymentApplicationPostRequest.md)
 - [PurchaseOrder](docs/PurchaseOrder.md)
 - [PurchaseOrderGet200Response](docs/PurchaseOrderGet200Response.md)
 - [PurchaseOrderIdIdCreateIncomingGoodsPostRequest](docs/PurchaseOrderIdIdCreateIncomingGoodsPostRequest.md)
 - [PurchaseOrderIdIdCreatePurchaseInvoicePostRequest](docs/PurchaseOrderIdIdCreatePurchaseInvoicePostRequest.md)
 - [PurchaseOrderIdIdProcessDropshippingPost200Response](docs/PurchaseOrderIdIdProcessDropshippingPost200Response.md)
 - [PurchaseOrderItem](docs/PurchaseOrderItem.md)
 - [PurchaseOrderRequest](docs/PurchaseOrderRequest.md)
 - [PurchaseOrderRequestGet200Response](docs/PurchaseOrderRequestGet200Response.md)
 - [PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPost200Response](docs/PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPost200Response.md)
 - [PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest](docs/PurchaseOrderRequestIdIdCreateBlanketPurchaseOrderPostRequest.md)
 - [PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest](docs/PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequest.md)
 - [PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner](docs/PurchaseOrderRequestIdIdCreatePurchaseOrderPostRequestOfferItemToUpdateSupplierInformationInner.md)
 - [PurchaseOrderRequestItem](docs/PurchaseOrderRequestItem.md)
 - [PurchaseOrderRequestOffer](docs/PurchaseOrderRequestOffer.md)
 - [PurchaseOrderRequestOfferItem](docs/PurchaseOrderRequestOfferItem.md)
 - [PurchaseOrderRequestOfferItemScaleValue](docs/PurchaseOrderRequestOfferItemScaleValue.md)
 - [PurchaseOrderRequestPurchasePriceUpdateMode](docs/PurchaseOrderRequestPurchasePriceUpdateMode.md)
 - [PurchaseOrderRequestStatusHistory](docs/PurchaseOrderRequestStatusHistory.md)
 - [PurchaseOrderRequestStatusType](docs/PurchaseOrderRequestStatusType.md)
 - [PurchaseOrderRequestSupplierStatusType](docs/PurchaseOrderRequestSupplierStatusType.md)
 - [PurchaseOrderRequestType](docs/PurchaseOrderRequestType.md)
 - [PurchaseOrderStatusHistory](docs/PurchaseOrderStatusHistory.md)
 - [PurchaseRequisition](docs/PurchaseRequisition.md)
 - [PurchaseRequisitionGet200Response](docs/PurchaseRequisitionGet200Response.md)
 - [PurchaseRequisitionStartMaterialPlanningRunPostRequest](docs/PurchaseRequisitionStartMaterialPlanningRunPostRequest.md)
 - [PurchaseRequisitionStatusHistory](docs/PurchaseRequisitionStatusHistory.md)
 - [PurchaseRequisitionStatusType](docs/PurchaseRequisitionStatusType.md)
 - [PurchaseShippingCostItem](docs/PurchaseShippingCostItem.md)
 - [QuantityConversion](docs/QuantityConversion.md)
 - [Quotation](docs/Quotation.md)
 - [QuotationGet200Response](docs/QuotationGet200Response.md)
 - [QuotationIdIdAcceptPostRequest](docs/QuotationIdIdAcceptPostRequest.md)
 - [QuotationIdIdAcceptPostRequestAcceptQuotationItemsInner](docs/QuotationIdIdAcceptPostRequestAcceptQuotationItemsInner.md)
 - [QuotationIdIdCreateNewVersionPost200Response](docs/QuotationIdIdCreateNewVersionPost200Response.md)
 - [QuotationIdIdInquirePostRequest](docs/QuotationIdIdInquirePostRequest.md)
 - [QuotationItem](docs/QuotationItem.md)
 - [QuotationStatusHistory](docs/QuotationStatusHistory.md)
 - [Rating](docs/Rating.md)
 - [RecordAddress](docs/RecordAddress.md)
 - [RecordEmailingRule](docs/RecordEmailingRule.md)
 - [RecordEmailingRuleEventType](docs/RecordEmailingRuleEventType.md)
 - [RecordEmailingRuleGet200Response](docs/RecordEmailingRuleGet200Response.md)
 - [RecordEmailingRuleRecipientType](docs/RecordEmailingRuleRecipientType.md)
 - [RecordItemReductionAdditionSource](docs/RecordItemReductionAdditionSource.md)
 - [RecordItemReductionAdditionType](docs/RecordItemReductionAdditionType.md)
 - [RecurringEvent](docs/RecurringEvent.md)
 - [RecurringEventType](docs/RecurringEventType.md)
 - [ReductionAddition](docs/ReductionAddition.md)
 - [ReductionAdditionItem](docs/ReductionAdditionItem.md)
 - [Releases](docs/Releases.md)
 - [ReminderSendType](docs/ReminderSendType.md)
 - [RemotePrintJob](docs/RemotePrintJob.md)
 - [RemotePrintJobCreatePrintJobWithDocumentPost200Response](docs/RemotePrintJobCreatePrintJobWithDocumentPost200Response.md)
 - [RemotePrintJobGet200Response](docs/RemotePrintJobGet200Response.md)
 - [RemotePrintJobStatus](docs/RemotePrintJobStatus.md)
 - [SalesBillOfMaterialArticleItem](docs/SalesBillOfMaterialArticleItem.md)
 - [SalesChannel](docs/SalesChannel.md)
 - [SalesChannelActiveSalesChannelsGet200Response](docs/SalesChannelActiveSalesChannelsGet200Response.md)
 - [SalesInvoice](docs/SalesInvoice.md)
 - [SalesInvoiceGet200Response](docs/SalesInvoiceGet200Response.md)
 - [SalesInvoiceIdIdAddSalesOrdersPostRequest](docs/SalesInvoiceIdIdAddSalesOrdersPostRequest.md)
 - [SalesInvoiceItem](docs/SalesInvoiceItem.md)
 - [SalesInvoiceItemRelationship](docs/SalesInvoiceItemRelationship.md)
 - [SalesInvoiceOrigin](docs/SalesInvoiceOrigin.md)
 - [SalesInvoiceStatusHistory](docs/SalesInvoiceStatusHistory.md)
 - [SalesInvoiceStatusType](docs/SalesInvoiceStatusType.md)
 - [SalesInvoiceType](docs/SalesInvoiceType.md)
 - [SalesOpenItem](docs/SalesOpenItem.md)
 - [SalesOpenItemGet200Response](docs/SalesOpenItemGet200Response.md)
 - [SalesOpenItemIdIdCreatePaymentApplicationPost200Response](docs/SalesOpenItemIdIdCreatePaymentApplicationPost200Response.md)
 - [SalesOrder](docs/SalesOrder.md)
 - [SalesOrderDefaultValuesForCreateGet200Response](docs/SalesOrderDefaultValuesForCreateGet200Response.md)
 - [SalesOrderGet200Response](docs/SalesOrderGet200Response.md)
 - [SalesOrderGet200ResponseAdditionalProperties](docs/SalesOrderGet200ResponseAdditionalProperties.md)
 - [SalesOrderIdIdCreateDropshippingPostRequest](docs/SalesOrderIdIdCreateDropshippingPostRequest.md)
 - [SalesOrderIdIdCreatePurchaseOrderPostRequest](docs/SalesOrderIdIdCreatePurchaseOrderPostRequest.md)
 - [SalesOrderIdIdCreateSalesInvoicePostRequest](docs/SalesOrderIdIdCreateSalesInvoicePostRequest.md)
 - [SalesOrderItem](docs/SalesOrderItem.md)
 - [SalesOrderPayment](docs/SalesOrderPayment.md)
 - [SalesOrderPaymentType](docs/SalesOrderPaymentType.md)
 - [SalesOrderStatusHistory](docs/SalesOrderStatusHistory.md)
 - [SalesShippingCostItem](docs/SalesShippingCostItem.md)
 - [SalesStage](docs/SalesStage.md)
 - [SalesStageGet200Response](docs/SalesStageGet200Response.md)
 - [SalesStageHistory](docs/SalesStageHistory.md)
 - [Salutation](docs/Salutation.md)
 - [SepaDirectDebitMandate](docs/SepaDirectDebitMandate.md)
 - [SepaDirectDebitMandateGet200Response](docs/SepaDirectDebitMandateGet200Response.md)
 - [SepaDirectDebitRuntime](docs/SepaDirectDebitRuntime.md)
 - [SepaDirectDebitType](docs/SepaDirectDebitType.md)
 - [SerialNumber](docs/SerialNumber.md)
 - [SerialNumberGet200Response](docs/SerialNumberGet200Response.md)
 - [Shelf](docs/Shelf.md)
 - [ShelfGet200Response](docs/ShelfGet200Response.md)
 - [ShelfIdIdActivatePost200Response](docs/ShelfIdIdActivatePost200Response.md)
 - [Shipment](docs/Shipment.md)
 - [ShipmentGet200Response](docs/ShipmentGet200Response.md)
 - [ShipmentInType](docs/ShipmentInType.md)
 - [ShipmentItem](docs/ShipmentItem.md)
 - [ShipmentMethod](docs/ShipmentMethod.md)
 - [ShipmentMethodGet200Response](docs/ShipmentMethodGet200Response.md)
 - [ShipmentOutType](docs/ShipmentOutType.md)
 - [ShipmentReturnAssessmentGet200Response](docs/ShipmentReturnAssessmentGet200Response.md)
 - [ShipmentReturnDescription](docs/ShipmentReturnDescription.md)
 - [ShipmentStatus](docs/ShipmentStatus.md)
 - [ShipmentStatusType](docs/ShipmentStatusType.md)
 - [ShippingCarrier](docs/ShippingCarrier.md)
 - [ShippingCarrierGet200Response](docs/ShippingCarrierGet200Response.md)
 - [SpecialCalculationMode](docs/SpecialCalculationMode.md)
 - [StockMovementType](docs/StockMovementType.md)
 - [StorageLocation](docs/StorageLocation.md)
 - [StorageLocationGet200Response](docs/StorageLocationGet200Response.md)
 - [StorageLocationIdIdActivatePost200Response](docs/StorageLocationIdIdActivatePost200Response.md)
 - [StoragePlace](docs/StoragePlace.md)
 - [StoragePlaceGet200Response](docs/StoragePlaceGet200Response.md)
 - [StoragePlaceSize](docs/StoragePlaceSize.md)
 - [StoragePlaceSizeGet200Response](docs/StoragePlaceSizeGet200Response.md)
 - [StoragePlaceType](docs/StoragePlaceType.md)
 - [StoragePlaceTypeSettings](docs/StoragePlaceTypeSettings.md)
 - [StoreType](docs/StoreType.md)
 - [SuccessResponse](docs/SuccessResponse.md)
 - [Supplier](docs/Supplier.md)
 - [SupplierGet200Response](docs/SupplierGet200Response.md)
 - [SupplierOrderStatusType](docs/SupplierOrderStatusType.md)
 - [SupplierOrderType](docs/SupplierOrderType.md)
 - [SupplySource](docs/SupplySource.md)
 - [SystemCreateDemoTestSystemPostRequest](docs/SystemCreateDemoTestSystemPostRequest.md)
 - [SystemDemoTestSystemInfoGet200Response](docs/SystemDemoTestSystemInfoGet200Response.md)
 - [SystemLicensesGet200Response](docs/SystemLicensesGet200Response.md)
 - [Tag](docs/Tag.md)
 - [TagGet200Response](docs/TagGet200Response.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [Tax](docs/Tax.md)
 - [TaxConfigurePurchaseTaxesPostRequest](docs/TaxConfigurePurchaseTaxesPostRequest.md)
 - [TaxConfigureSalesTaxesPostRequest](docs/TaxConfigureSalesTaxesPostRequest.md)
 - [TaxDeterminationRule](docs/TaxDeterminationRule.md)
 - [TaxDeterminationRuleGet200Response](docs/TaxDeterminationRuleGet200Response.md)
 - [TaxFindPurchaseTaxGet200Response](docs/TaxFindPurchaseTaxGet200Response.md)
 - [TaxGet200Response](docs/TaxGet200Response.md)
 - [TaxKey](docs/TaxKey.md)
 - [TaxRateType](docs/TaxRateType.md)
 - [TaxResetSystemTaxesPostRequest](docs/TaxResetSystemTaxesPostRequest.md)
 - [TaxType](docs/TaxType.md)
 - [TeamRole](docs/TeamRole.md)
 - [TemplateType](docs/TemplateType.md)
 - [TermOfPayment](docs/TermOfPayment.md)
 - [TermOfPaymentCondition](docs/TermOfPaymentCondition.md)
 - [TermOfPaymentGet200Response](docs/TermOfPaymentGet200Response.md)
 - [Ticket](docs/Ticket.md)
 - [TicketAssigneeType](docs/TicketAssigneeType.md)
 - [TicketAssignmentRule](docs/TicketAssignmentRule.md)
 - [TicketAssignmentRuleGet200Response](docs/TicketAssignmentRuleGet200Response.md)
 - [TicketCategory](docs/TicketCategory.md)
 - [TicketCategoryGet200Response](docs/TicketCategoryGet200Response.md)
 - [TicketFaq](docs/TicketFaq.md)
 - [TicketFaqGet200Response](docs/TicketFaqGet200Response.md)
 - [TicketFaqVisibility](docs/TicketFaqVisibility.md)
 - [TicketGet200Response](docs/TicketGet200Response.md)
 - [TicketGet200ResponseAdditionalProperties](docs/TicketGet200ResponseAdditionalProperties.md)
 - [TicketIdIdCreatePublicPagePost200Response](docs/TicketIdIdCreatePublicPagePost200Response.md)
 - [TicketIdIdLinkSalesOrderPostRequest](docs/TicketIdIdLinkSalesOrderPostRequest.md)
 - [TicketPoolingGroup](docs/TicketPoolingGroup.md)
 - [TicketPoolingGroupGet200Response](docs/TicketPoolingGroupGet200Response.md)
 - [TicketPoolingGroupMember](docs/TicketPoolingGroupMember.md)
 - [TicketServiceLevelAgreement](docs/TicketServiceLevelAgreement.md)
 - [TicketServiceLevelAgreementGet200Response](docs/TicketServiceLevelAgreementGet200Response.md)
 - [TicketServiceLevelAgreementTarget](docs/TicketServiceLevelAgreementTarget.md)
 - [TicketServiceLevelAgreementUnit](docs/TicketServiceLevelAgreementUnit.md)
 - [TicketStatus](docs/TicketStatus.md)
 - [TicketStatusColor](docs/TicketStatusColor.md)
 - [TicketStatusGet200Response](docs/TicketStatusGet200Response.md)
 - [TicketType](docs/TicketType.md)
 - [TicketTypeGet200Response](docs/TicketTypeGet200Response.md)
 - [TimeUnit](docs/TimeUnit.md)
 - [Translation](docs/Translation.md)
 - [TranslationGet200Response](docs/TranslationGet200Response.md)
 - [TranslationValue](docs/TranslationValue.md)
 - [TransportationOrder](docs/TransportationOrder.md)
 - [TransportationOrderGet200Response](docs/TransportationOrderGet200Response.md)
 - [TransportationOrderIdIdCreatePickPost200Response](docs/TransportationOrderIdIdCreatePickPost200Response.md)
 - [TransportationOrderIdIdCreatePickPostRequest](docs/TransportationOrderIdIdCreatePickPostRequest.md)
 - [TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner](docs/TransportationOrderIdIdCreatePickPostRequestExistingReservationsInner.md)
 - [TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest](docs/TransportationOrderIdIdCreateTransportationOrderFromUnpickedRecordsPostRequest.md)
 - [TransportationOrderIdIdPickPickPostRequest](docs/TransportationOrderIdIdPickPickPostRequest.md)
 - [TransportationOrderIdIdPutDownInternalTransportReferencePostRequest](docs/TransportationOrderIdIdPutDownInternalTransportReferencePostRequest.md)
 - [TransportationOrderStatusHistory](docs/TransportationOrderStatusHistory.md)
 - [TransportationOrderStatusType](docs/TransportationOrderStatusType.md)
 - [TransportationOrderType](docs/TransportationOrderType.md)
 - [Unit](docs/Unit.md)
 - [UnitGet200Response](docs/UnitGet200Response.md)
 - [User](docs/User.md)
 - [UserCurrentUserGet200Response](docs/UserCurrentUserGet200Response.md)
 - [UserGet200Response](docs/UserGet200Response.md)
 - [UserRole](docs/UserRole.md)
 - [UserRoleGet200Response](docs/UserRoleGet200Response.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorType](docs/ValidationErrorType.md)
 - [VariantArticle](docs/VariantArticle.md)
 - [VariantArticleAttribute](docs/VariantArticleAttribute.md)
 - [VariantArticleAttributeGet200Response](docs/VariantArticleAttributeGet200Response.md)
 - [VariantArticleAttributeOption](docs/VariantArticleAttributeOption.md)
 - [VariantArticleGet200Response](docs/VariantArticleGet200Response.md)
 - [VariantArticleVariant](docs/VariantArticleVariant.md)
 - [VariantArticleVariantGet200Response](docs/VariantArticleVariantGet200Response.md)
 - [VariantArticleVariantWithoutReference](docs/VariantArticleVariantWithoutReference.md)
 - [Warehouse](docs/Warehouse.md)
 - [WarehouseGet200Response](docs/WarehouseGet200Response.md)
 - [WarehouseIdIdActivatePost200Response](docs/WarehouseIdIdActivatePost200Response.md)
 - [WarehouseQuantity](docs/WarehouseQuantity.md)
 - [WarehouseStock](docs/WarehouseStock.md)
 - [WarehouseStockGet200Response](docs/WarehouseStockGet200Response.md)
 - [WarehouseStockMovement](docs/WarehouseStockMovement.md)
 - [WarehouseStockMovementBookDirectStockTransferPostRequest](docs/WarehouseStockMovementBookDirectStockTransferPostRequest.md)
 - [WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner](docs/WarehouseStockMovementBookDirectStockTransferPostRequestCustomAttributesInner.md)
 - [WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest](docs/WarehouseStockMovementBookFromLoadingEquipmentPlacePostRequest.md)
 - [WarehouseStockMovementBookIncomingMovementPostRequest](docs/WarehouseStockMovementBookIncomingMovementPostRequest.md)
 - [WarehouseStockMovementBookOntoInternalTransportReferencePostRequest](docs/WarehouseStockMovementBookOntoInternalTransportReferencePostRequest.md)
 - [WarehouseStockMovementBookOutgoingMovementPostRequest](docs/WarehouseStockMovementBookOutgoingMovementPostRequest.md)
 - [WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest](docs/WarehouseStockMovementBookToLoadingEquipmentPlacePostRequest.md)
 - [WarehouseStockMovementGet200Response](docs/WarehouseStockMovementGet200Response.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookGet200Response](docs/WebhookGet200Response.md)
 - [WebhookRequestMethod](docs/WebhookRequestMethod.md)
 - [WeclappOs](docs/WeclappOs.md)
 - [WeclappOsGet200Response](docs/WeclappOsGet200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api-token"></a>
### api-token

- **Type**: API key
- **API key parameter name**: AuthenticationToken
- **Location**: HTTP header


## Author

support@weclapp.com


