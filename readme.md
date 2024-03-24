
# Asset Pulse

This is a very simple corporate asset management system. Here Companies can create account and manage their assets with the employees.


## API Home Page

![App Screenshot](https://i.ibb.co/DGDmTZj/Asset-Pulse-Project-API.png)

## Home Page

![App Screenshot](https://i.ibb.co/wggZw0c/Asset-Pulse.png)

## Asset Category Page

![App Screenshot](https://i.ibb.co/CVcJr8Y/Asset-Pulse-category.png)


## Features

- Sign In & Sign Up Methods
- Create Accounts per Company
- Add Assets
- Add Employees
- Distribute Assets
- CRUD Operations for all section
- Sorting functionality
- Searching Methods by names


## Used Technologies
#### ⏪ Backend
- Python 
- Django
- Django Rest Framework
- Djoser
- Simple JWT
- MySQL

#### ⏩ Frontend 
- Javascript 
- React
- React Router Dom
- Tailwind CSS
- Shadcn



## 🔗 Links
- [Frontend Live Link](https://asset-pulse.netlify.app/)
- [API Live Link](https://corporateasset.pythonanywhere.com/)
- [Frontend Code Link](https://github.com/foysalmia/corporate-asset-management-frontend)
- [Backend Code Link](https://github.com/foysalmia/corporate_asset_management_backend)





## API yaml file 
```
openapi: 3.0.3
info:
  title: Asset Pulse Project API
  version: 1.0.0
  description: This is a corporate asset management system named Asset Pulse api.
    All the assets and employees will be maintain by this api.
paths:
  /api/asset-distribution-history/:
    get:
      operationId: api_asset_distribution_history_retrieve
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          description: No response body
  /api/assets/:
    get:
      operationId: api_assets_list
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/GetAsset'
          description: ''
    post:
      operationId: api_assets_create
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Asset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Asset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Asset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Asset'
          description: ''
  /api/assets/{id}/:
    get:
      operationId: api_assets_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this asset.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetAsset'
          description: ''
    put:
      operationId: api_assets_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this asset.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Asset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Asset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Asset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Asset'
          description: ''
    patch:
      operationId: api_assets_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this asset.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedAsset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedAsset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedAsset'
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Asset'
          description: ''
    delete:
      operationId: api_assets_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this asset.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /api/category/:
    get:
      operationId: api_category_retrieve
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          description: No response body
  /api/dashboard/:
    get:
      operationId: api_dashboard_retrieve
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          description: No response body
  /api/distribute/:
    get:
      operationId: api_distribute_list
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/GetDistribution'
          description: ''
    post:
      operationId: api_distribute_create
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Distribution'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Distribution'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Distribution'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Distribution'
          description: ''
  /api/distribute/{id}/:
    get:
      operationId: api_distribute_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this distribute.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetDistribution'
          description: ''
    put:
      operationId: api_distribute_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this distribute.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Distribution'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Distribution'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Distribution'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Distribution'
          description: ''
    patch:
      operationId: api_distribute_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this distribute.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedDistribution'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedDistribution'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedDistribution'
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Distribution'
          description: ''
    delete:
      operationId: api_distribute_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this distribute.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /api/employee/:
    get:
      operationId: api_employee_list
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/GetEmployee'
          description: ''
    post:
      operationId: api_employee_create
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Employee'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Employee'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Employee'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Employee'
          description: ''
  /api/employee-used-asset-history/:
    get:
      operationId: api_employee_used_asset_history_retrieve
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          description: No response body
  /api/employee/{id}/:
    get:
      operationId: api_employee_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this employee.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetEmployee'
          description: ''
    put:
      operationId: api_employee_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this employee.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Employee'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Employee'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Employee'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Employee'
          description: ''
    patch:
      operationId: api_employee_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this employee.
        required: true
      tags:
      - api
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedEmployee'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedEmployee'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedEmployee'
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Employee'
          description: ''
    delete:
      operationId: api_employee_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this employee.
        required: true
      tags:
      - api
      security:
      - jwtAuth: []
      - {}
      responses:
        '204':
          description: No response body
  /auth/jwt/create/:
    post:
      operationId: auth_jwt_create_create
      description: |-
        Takes a set of user credentials and returns an access and refresh JSON web
        token pair to prove the authentication of those credentials.
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TokenObtainPair'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/TokenObtainPair'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/TokenObtainPair'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenObtainPair'
          description: ''
  /auth/jwt/refresh/:
    post:
      operationId: auth_jwt_refresh_create
      description: |-
        Takes a refresh type JSON web token and returns an access type JSON web
        token if the refresh token is valid.
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TokenRefresh'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/TokenRefresh'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/TokenRefresh'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenRefresh'
          description: ''
  /auth/jwt/verify/:
    post:
      operationId: auth_jwt_verify_create
      description: |-
        Takes a token and indicates if it is valid.  This view provides no
        information about a token's fitness for a particular use.
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TokenVerify'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/TokenVerify'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/TokenVerify'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenVerify'
          description: ''
  /auth/users/:
    get:
      operationId: auth_users_list
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
          description: ''
    post:
      operationId: auth_users_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserCreate'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/UserCreate'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UserCreate'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserCreate'
          description: ''
  /auth/users/{id}/:
    get:
      operationId: auth_users_retrieve
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this company.
        required: true
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    put:
      operationId: auth_users_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this company.
        required: true
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/User'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/User'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    patch:
      operationId: auth_users_partial_update
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this company.
        required: true
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedUser'
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    delete:
      operationId: auth_users_destroy
      parameters:
      - in: path
        name: id
        schema:
          type: integer
        description: A unique integer value identifying this company.
        required: true
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '204':
          description: No response body
  /auth/users/activation/:
    post:
      operationId: auth_users_activation_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Activation'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Activation'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Activation'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Activation'
          description: ''
  /auth/users/me/:
    get:
      operationId: auth_users_me_retrieve
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    put:
      operationId: auth_users_me_update
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/User'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/User'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    patch:
      operationId: auth_users_me_partial_update
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PatchedUser'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PatchedUser'
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
          description: ''
    delete:
      operationId: auth_users_me_destroy
      tags:
      - auth
      security:
      - jwtAuth: []
      responses:
        '204':
          description: No response body
  /auth/users/resend_activation/:
    post:
      operationId: auth_users_resend_activation_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailReset'
          description: ''
  /auth/users/reset_email/:
    post:
      operationId: auth_users_reset_email_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailReset'
          description: ''
  /auth/users/reset_email_confirm/:
    post:
      operationId: auth_users_reset_email_confirm_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UsernameResetConfirm'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/UsernameResetConfirm'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UsernameResetConfirm'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UsernameResetConfirm'
          description: ''
  /auth/users/reset_password/:
    post:
      operationId: auth_users_reset_password_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SendEmailReset'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SendEmailReset'
          description: ''
  /auth/users/reset_password_confirm/:
    post:
      operationId: auth_users_reset_password_confirm_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/PasswordResetConfirm'
        required: true
      security:
      - jwtAuth: []
      - {}
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PasswordResetConfirm'
          description: ''
  /auth/users/set_email/:
    post:
      operationId: auth_users_set_email_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetUsername'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SetUsername'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SetUsername'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SetUsername'
          description: ''
  /auth/users/set_password/:
    post:
      operationId: auth_users_set_password_create
      tags:
      - auth
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SetPassword'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/SetPassword'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/SetPassword'
        required: true
      security:
      - jwtAuth: []
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SetPassword'
          description: ''
components:
  schemas:
    Activation:
      type: object
      properties:
        uid:
          type: string
        token:
          type: string
      required:
      - token
      - uid
    Asset:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        description:
          type: string
        price:
          type: integer
          maximum: 4294967295
          minimum: 0
          format: int64
        buy_date:
          type: string
          format: date
        warranty:
          type: string
          format: date
        category:
          type: integer
        company:
          type: integer
      required:
      - buy_date
      - category
      - company
      - description
      - id
      - name
      - price
      - warranty
    CategoryName:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
      required:
      - id
      - name
    CompanyName:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
      required:
      - id
      - name
    Distribution:
      type: object
      properties:
        asset:
          type: integer
        employee:
          type: integer
        provide_conditions:
          type: string
        return_conditions:
          type: string
        provide_date:
          type: string
          format: date
        return_date:
          type: string
          format: date
        company:
          type: integer
        returned:
          type: boolean
      required:
      - asset
      - employee
      - provide_conditions
      - provide_date
      - return_conditions
      - return_date
    Employee:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        designation:
          type: string
          maxLength: 255
        description:
          type: string
        salary:
          type: integer
          maximum: 4294967295
          minimum: 0
          format: int64
        join_date:
          type: string
          format: date
        company:
          type: integer
      required:
      - description
      - designation
      - id
      - join_date
      - name
      - salary
    GetAsset:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        description:
          type: string
        price:
          type: integer
          maximum: 4294967295
          minimum: 0
          format: int64
        buy_date:
          type: string
          format: date
        warranty:
          type: string
          format: date
        category:
          allOf:
          - $ref: '#/components/schemas/CategoryName'
          readOnly: true
        company:
          allOf:
          - $ref: '#/components/schemas/CompanyName'
          readOnly: true
      required:
      - buy_date
      - category
      - company
      - description
      - id
      - name
      - price
      - warranty
    GetDistribution:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        asset:
          allOf:
          - $ref: '#/components/schemas/SimpleAsset'
          readOnly: true
        employee:
          allOf:
          - $ref: '#/components/schemas/SimpleEmployee'
          readOnly: true
        provide_conditions:
          type: string
        return_conditions:
          type: string
        provide_date:
          type: string
          format: date
        return_date:
          type: string
          format: date
        company:
          allOf:
          - $ref: '#/components/schemas/CompanyName'
          readOnly: true
        status:
          type: string
          readOnly: true
        returned:
          type: boolean
      required:
      - asset
      - company
      - employee
      - id
      - provide_conditions
      - provide_date
      - return_conditions
      - return_date
      - status
    GetEmployee:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        designation:
          type: string
          maxLength: 255
        description:
          type: string
        salary:
          type: integer
          maximum: 4294967295
          minimum: 0
          format: int64
        join_date:
          type: string
          format: date
        company:
          allOf:
          - $ref: '#/components/schemas/CompanyName'
          readOnly: true
      required:
      - company
      - description
      - designation
      - id
      - join_date
      - name
      - salary
    PasswordResetConfirm:
      type: object
      properties:
        uid:
          type: string
        token:
          type: string
        new_password:
          type: string
      required:
      - new_password
      - token
      - uid
    PatchedAsset:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        description:
          type: string
        price:
          type: integer
          maximum: 4294967295
          minimum: 0
          format: int64
        buy_date:
          type: string
          format: date
        warranty:
          type: string
          format: date
        category:
          type: integer
        company:
          type: integer
    PatchedDistribution:
      type: object
      properties:
        asset:
          type: integer
        employee:
          type: integer
        provide_conditions:
          type: string
        return_conditions:
          type: string
        provide_date:
          type: string
          format: date
        return_date:
          type: string
          format: date
        company:
          type: integer
        returned:
          type: boolean
    PatchedEmployee:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
        designation:
          type: string
          maxLength: 255
        description:
          type: string
        salary:
          type: integer
          maximum: 4294967295
          minimum: 0
          format: int64
        join_date:
          type: string
          format: date
        company:
          type: integer
    PatchedUser:
      type: object
      properties:
        name:
          type: string
          maxLength: 255
        description:
          type: string
        id:
          type: integer
          readOnly: true
        email:
          type: string
          format: email
          readOnly: true
    SendEmailReset:
      type: object
      properties:
        email:
          type: string
          format: email
      required:
      - email
    SetPassword:
      type: object
      properties:
        new_password:
          type: string
        current_password:
          type: string
      required:
      - current_password
      - new_password
    SetUsername:
      type: object
      properties:
        current_password:
          type: string
        new_email:
          type: string
          format: email
          title: Email
          maxLength: 254
      required:
      - current_password
      - new_email
    SimpleAsset:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
      required:
      - id
      - name
    SimpleEmployee:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        name:
          type: string
          maxLength: 255
      required:
      - id
      - name
    TokenObtainPair:
      type: object
      properties:
        email:
          type: string
          writeOnly: true
        password:
          type: string
          writeOnly: true
        access:
          type: string
          readOnly: true
        refresh:
          type: string
          readOnly: true
      required:
      - access
      - email
      - password
      - refresh
    TokenRefresh:
      type: object
      properties:
        access:
          type: string
          readOnly: true
        refresh:
          type: string
          writeOnly: true
      required:
      - access
      - refresh
    TokenVerify:
      type: object
      properties:
        token:
          type: string
          writeOnly: true
      required:
      - token
    User:
      type: object
      properties:
        name:
          type: string
          maxLength: 255
        description:
          type: string
        id:
          type: integer
          readOnly: true
        email:
          type: string
          format: email
          readOnly: true
      required:
      - description
      - email
      - id
      - name
    UserCreate:
      type: object
      properties:
        name:
          type: string
          maxLength: 255
        description:
          type: string
        email:
          type: string
          format: email
          maxLength: 254
        password:
          type: string
          writeOnly: true
      required:
      - description
      - email
      - name
      - password
    UsernameResetConfirm:
      type: object
      properties:
        new_email:
          type: string
          format: email
          title: Email
          maxLength: 254
      required:
      - new_email
  securitySchemes:
    jwtAuth:
      type: apiKey
      in: header
      name: Authorization
      description: Token-based authentication with required prefix "JWT"

```

## 🚀 About Me
I'm a React & Django based full stack developer.


![Myself](https://i.ibb.co/6Pwpfz0/myimge.jpg)

